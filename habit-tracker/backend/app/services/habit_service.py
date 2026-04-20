from fastapi import HTTPException, Response, status
from pymongo.errors import DuplicateKeyError

from app.models.habit import Habit
from app.schemas.habit import HabitCreate, HabitUpdate

async def create_new_habit(habit_in: HabitCreate, owner_id: int) -> Habit:
    # ۱. چک کردن دستی برای تجربه کاربری بهتر (قبل از خطای دیتابیس)
    existing_habit = await Habit.find_one({
        "name": habit_in.name.strip(), # پاک کردن فاصله‌های اضافی
        "owner_id": owner_id
    })
    
    if existing_habit:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"You already have a habit named '{habit_in.name}'"
        )

    try:
        habit_data = habit_in.model_dump(exclude_unset=True, exclude_none=True)
        # تبدیل زمان به رشته برای جلوگیری از خطای Beanie
        if "remind_time" in habit_data and hasattr(habit_data["remind_time"], "strftime"):
            habit_data["remind_time"] = habit_data["remind_time"].strftime("%H:%M")
            
        habit_data.update({"owner_id": owner_id, "name": habit_in.name.strip()})
        
        new_habit = Habit(**habit_data)
        return await new_habit.insert()

    except DuplicateKeyError:
        # این بخش اگر دو درخواست همزمان برسند، امنیت دیتابیس را تضمین می‌کند
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Conflict: A habit with this name already exists for this user."
        )

    
async def get_habit_by_name(name: str, owner_id: int) -> Habit:
    existance_habit = await Habit.find_one({"name": name})

    if not existance_habit:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"habit with name: {name} does not exists"
        )
    
    return existance_habit

async def udpdate_habit_by_name(name: str, update_habit: HabitUpdate, owener_id: int) -> Habit:
    existance_habit = await Habit.find_one({"name": name})

    if not existance_habit:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"habit with name: {name} does not exist"
        )
    
    update_data = update_habit.model_dump(exclude_unset = True, exclude_none = True)
    update_data.update({"owner_id": owener_id})

    await existance_habit.update({"$set": update_data})
    habit = await Habit.get(existance_habit.id)
    
    return habit

async def delete_habit_by_name(name: str, owner_id: int):

    existance_habit = await Habit.find_one({"name": name, "owner_id": owner_id})
    
    if not existance_habit:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"user with id: {owner_id} does not have any habit with name: {name}"
        )
    
    await existance_habit.delete()

    return Response(status_code = status.HTTP_204_NO_CONTENT)