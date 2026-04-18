from fastapi import HTTPException, status

from app.models.habit import Habit
from app.schemas.habit import HabitCreate

async def create_new_habit(habit_in: HabitCreate, owner_id: int) -> Habit:
    habit_data = habit_in.model_dump(exclude_unset = True, exclude_none = True)
    habit_data.update({"owner_id": owner_id})
    
    new_habit = Habit(
        **habit_data
    )

    return await new_habit.insert()