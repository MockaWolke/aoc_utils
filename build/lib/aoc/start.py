import datetime
from .utils import validate_date
from typing import Optional
import os
from .open_webpage import open_website

def create_file_and_open(day: Optional[int] = None, year: Optional[int] = None, path: Optional[str] = None):
    date: datetime.date = validate_date(day=day, year=year)

    if path is None:
        path = os.path.join(os.getcwd(), f"aoc_{date.day}_{date.year}.py")
    
    if not path.endswith('.py'):
        path += '.py'

    if os.path.dirname(path) and not os.path.isdir(os.path.dirname(path)):
        raise ValueError(f"The directory does not exist: {os.path.dirname(path)}")

    if os.path.exists(path):
        raise FileExistsError(f"The file already exists: {path}")

    code = f"""from aoc import get_aoc_input

data = get_aoc_input(day={date.day}, year={date.year})
# Your solution starts here
"""

    try:
        with open(path, "w") as f:
            f.write(code)
    except OSError as e:
        raise OSError(f"Error writing to file: {path}, {e}")

    print(f"File created successfully at: {path}")

    open_website(day=date.day, year=date.year)

    try:
        if os.name == 'posix':  # For Linux/macOS
            os.system(f'xdg-open {path}')
        elif os.name == 'nt':   # For Windows
            os.startfile(path)
        else:
            print("What are you operating on??")
    except Exception as e:
        print(f"Failed to open the file in the editor: {e}")
