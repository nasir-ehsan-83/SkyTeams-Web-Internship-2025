from typing import List, Optional
from fastapi import APIRouter

from app.models.habit import Habit
from app.schemas.habit import HabitCreate, HabitPrivateOut, HabitAdminOut, HabitUpdate
from app.services.habit_service import(
    create_new_habit,
    get_all_habits_admin, 
    get_habit_by_name,
    udpdate_habit_by_name,
    delete_habit_by_name
)

router = APIRouter(
    prefix = '/habits',
    tags = ["Habits"]
)

@router.post('/', response_model = HabitPrivateOut)
async def create_habit(habit: HabitCreate, owner_id: int) -> Habit:
    print(habit)
    return await create_new_habit(habit, owner_id)

# get all habits of specific user by  owner access
@router.get('/', response_model = List[HabitAdminOut])
async def get_habits_owner(owner_id: int) -> List[Habit]:
    
    return await get_habits_owner(owner_id)

# get all habits of all usres by admin access
@router.get('/all', response_model = List[HabitPrivateOut])
async def get_habits_admin(owner_id: Optional[int] = None) -> List[Habit]:
    
    return await get_all_habits_admin(owner_id)

@router.get('/name', response_model = HabitPrivateOut)
async def get_habit(name: str, owner_id: int) -> Habit:

    return await get_habit_by_name(name, owner_id)

@router.put('/name', response_model = HabitPrivateOut)
async def update_habit(name: str, update_habit: HabitUpdate, owner_id: int) -> Habit:
    
    return await udpdate_habit_by_name(name, update_habit, owner_id)

@router.delete('/name')
async def delete_habit(name: str, owner_id: int) :

    return await delete_habit_by_name(name, owner_id)