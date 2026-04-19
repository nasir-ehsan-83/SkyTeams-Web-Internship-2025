from fastapi import HTTPException, status
from pymongo.errors import DuplicateKeyError

from app.models.habit import Habit
from app.schemas.habit import HabitCreate

async def create_new_habit(habit_in: HabitCreate, owner_id: int) -> Habit:
    existance_habit = await Habit.find_one({"name": habit_in.name})

    if existance_habit:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = f"habit with name: {habit_in.name} already exists"
        )
    
    try:
        habit_data = habit_in.model_dump(exclude_unset = True, exclude_none = True)
        habit_data.update({"owner_id": owner_id})
        
        new_habit = Habit(
            **habit_data
        )

        return await new_habit.insert()
    
    except DuplicateKeyError:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Data Conflict: The provided habit already exists"
        )