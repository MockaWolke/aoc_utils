import webbrowser
from typing import Optional
from .utils import validate_date

def open_website(day: Optional[int] = None, year: Optional[int] = None):
    date = validate_date(day, year)
    
    url = f"https://adventofcode.com/{date.year}/day/{date.day}"
    
    webbrowser.open(url)
