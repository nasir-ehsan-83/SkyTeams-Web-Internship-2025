from typing import List, Optional
from fastapi import HTTPException, Response, status
from pymongo.errors import DuplicateKeyError
from datetime import datetime, timezone

from app.models.habit import Habit
from app.schemas.habit import HabitCreate, HabitUpdate
from app.schemas.token import TokenData

async def create_new_habit(habit_in: HabitCreate, current_user: TokenData) -> Habit:
    # get habit from database by specific owner
    existing_habit = await Habit.find_one(
        Habit.name == habit_in.name,
        Habit.owner_id == int(current_user.id),
        Habit.status != "deleted"
    )
    
    # if user already has habit
    if existing_habit:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Habit already exists"
        )

    try:
        new_habit = Habit(
            **habit_in.model_dump(),
            owner_id = int(current_user.id)
        )

        return await new_habit.insert()

    except DuplicateKeyError:
       
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Conflict: A habit with this name already exists for this user."
        )


async def get_all_habits_owner(current_user: TokenData) -> List[Habit]:
    # get all habits of users
    return  await Habit.find_all(Habit.owner_id == int(current_user.id), Habit.status != "deleted").to_list()


async def get_all_habits_admin(current_user: TokenData, owner_id: Optional[int] = None) -> List[Habit]:
    # get all habits of specific user
    if current_user.role is not "admin":
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid credential"
        )
    
    if owner_id is not None:
        return await Habit.find_all(Habit.owner_id == owner_id).to_list()

    # else get all habits of all users 
    return await Habit.find_all().to_list()


async def get_habit_by_name(name: str, current_user: int) -> Habit:
    # get habit by specific owner
    existing_habit = await Habit.find_one(
        Habit.name == name,
        Habit.owner_id == int(current_user.id),
        Habit.status != "deleted"   
    )

    # if habit does not exist
    if not existing_habit:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Habit not found"
        )
    
    # if habit exists then return 
    return existing_habit

async def udpdate_habit_by_name(name: str, update_habit: HabitUpdate, current_user: TokenData) -> Habit:
    # get specific habit form database
    existing_habit = await Habit.find_one(
        Habit.name == name,
        Habit.owner_id == int(current_user.id),
        Habit.status != "deleted"
    )

    # if habit does not exist
    if not existing_habit:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Habit not found"
        )
    
    # delete undefined or null values
    update_data = update_habit.model_dump(
        exclude_unset = True, 
        exclude_none = True
    )

    update_data.update({
        "updated_at": datetime.now(timezone.utc)
    })
    
    # update habit and  store in database
    await existing_habit.update({
        "$set": update_data
    })
    
    return await Habit.get(existing_habit.id)
    

async def delete_habit_by_name(name: str, current_user: TokenData):
    # get specific habit from database
    existing_habit = await Habit.find_one(
        Habit.name == name,
        Habit.owner_id == int(current_user.id),
        Habit.status != "deleted"
    )
    
    # if specific habit does not exist
    if not existing_habit:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Habit not found"
        )
    
    # if exists delete
    await existing_habit.update({
        "$set": {
            "status": "deleted"
        }
    })

    # return nothing
    return Response(status_code = status.HTTP_204_NO_CONTENT)