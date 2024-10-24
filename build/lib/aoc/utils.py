from typing import Optional
from datetime import date, datetime

def validate_date(day: Optional[int] = None, year: Optional[int] = None) -> date:
    now = datetime.now()

    if day is None:
        if now.month != 12:
            raise ValueError("You can only leave out the day in December")
        day = now.day  

    if day > 25:
        raise ValueError("There are sadly only 25 goodies per year ):")

    if year is None:
        year = now.year if now.month == 12 else now.year - 1

    if year < 2015:
        raise ValueError("Year must be >= 2015")

    validated_date = date(year=year, month=12, day=day) 
    if now.date() < validated_date:
        raise ValueError("You are in the future my friend")

    return validated_date 