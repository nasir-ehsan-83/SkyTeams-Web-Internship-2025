from fastapi import APIRouter

from app.models.habit import Habit
from app.schemas.habit import HabitCreate, HabitOut
from app.services.habit_service import create_new_habit#, get_habit_by_id

router = APIRouter(
    prefix = '/habits',
    tags = ["habits"]
)

@router.post('/', response_model = HabitOut)
async def create_habit(habit: HabitCreate, owner_id: int) -> Habit:
    print(habit)
    return await create_new_habit(habit, owner_id)

""" router.get('/{id}', response_model = HabitOut)
async def get_habit(id: int, owner_id: int) -> Habit:

    return await get_habit_by_id(id, owner_id) """