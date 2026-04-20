from fastapi import APIRouter

from app.models.habit import Habit
from app.schemas.habit import HabitCreate, HabitOut, HabitUpdate
from app.services.habit_service import(
    create_new_habit, 
    get_habit_by_name,
    udpdate_habit_by_name,
    delete_habit_by_name
)

router = APIRouter(
    prefix = '/habits',
    tags = ["Habits"]
)

@router.post('/', response_model = HabitOut)
async def create_habit(habit: HabitCreate, owner_id: int) -> Habit:
    print(habit)
    return await create_new_habit(habit, owner_id)

@router.get('/name/{name}', response_model = HabitOut)
async def get_habit(name: str, owner_id: int) -> Habit:

    return await get_habit_by_name(name, owner_id)

@router.patch('/name/{name}', response_model = HabitOut)
async def update_habit(name: str, update_habit: HabitUpdate, owner_id: int) -> Habit:
    
    return await udpdate_habit_by_name(name, update_habit, owner_id)

@router.delete('/name/{name}')
async def delete_habit(name: str, owner_id: int) :

    return await delete_habit_by_name(name, owner_id)