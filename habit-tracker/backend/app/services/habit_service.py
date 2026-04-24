from typing import List, Optional
from fastapi import HTTPException, Response, status
from pymongo.errors import DuplicateKeyError

from app.models.habit import Habit
from app.schemas.habit import HabitCreate, HabitUpdate

async def create_new_habit(habit_in: HabitCreate, current_user: int) -> Habit:
    # get habit from database by specific owner
    existing_habit = await Habit.find_one({
        "name": habit_in.name.strip(),
        "owner_id": int(current_user.id)
    })
    
    # if user already has habit
    if existing_habit:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"You already have a habit named '{habit_in.name}'"
        )

    try:
        habit_data = habit_in.model_dump(exclude_unset=True, exclude_none=True)
        
        if "remind_time" in habit_data and hasattr(habit_data["remind_time"], "strftime"):
            habit_data["remind_time"] = habit_data["remind_time"].strftime("%H:%M")
            
        habit_data.update({"owner_id": int(current_user.id), "name": habit_in.name.strip()})
        
        new_habit = Habit(**habit_data)
        return await new_habit.insert()

    except DuplicateKeyError:
       
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Conflict: A habit with this name already exists for this user."
        )

async def get_all_habits_owner(current_user: int) -> List[Habit]:
    # get all habits of users
    habits = await Habit.find_all({"owner_id": int(current_user.id)})
    
    return habits

async def get_all_habits_admin(owner_id: Optional[int] = None) -> List[Habit]:
    # get all habits of specific user
    if owner_id is not None:
        habits = await Habit.find_all({"owner_id": owner_id})

        return habits

    # else get all habits of all users 
    habits = await Habit.find_all()

    return habits

async def get_habit_by_name(name: str, current_user: int) -> Habit:
    # get habit by specific owner
    existance_habit = await Habit.find_one({"name": name, "owner_id": int(current_user.id)})

    # if habit does not exist
    if not existance_habit:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"habit with name: {name} does not exists"
        )
    
    # if habit exists then return 
    return existance_habit

async def udpdate_habit_by_name(name: str, update_habit: HabitUpdate, current_user: int) -> Habit:
    # get specific habit form database
    existance_habit = await Habit.find_one({"name": name, "owner_id": int(current_user.id)})

    # if habit does not exist
    if not existance_habit:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"habit with name: {name} does not exist"
        )
    
    # delete undefined or null values
    update_data = update_habit.model_dump(exclude_unset = True, exclude_none = True)
    update_data.update({"owner_id": int(current_user.id)})

    # update habit and  store in database
    await existance_habit.update({"$set": update_data})
    habit = await Habit.get(existance_habit.id)
    
    # return habit
    return habit

async def delete_habit_by_name(name: str, current_user: int):
    # get specific habit from database
    existance_habit = await Habit.find_one({"name": name, "owner_id": int(current_user.id)})
    
    # if specific habit does not exist
    if not existance_habit:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"user with id: {current_user.id} does not have any habit with name: {name}"
        )
    
    # if exists delete
    await existance_habit.delete()

    # return nothing
    return Response(status_code = status.HTTP_204_NO_CONTENT)