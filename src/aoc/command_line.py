import argparse
from .open_webpage import open_website
from .get_data import get_aoc_input
from .start import create_file_and_open

def add_date_args(sub_parser):
    sub_parser.add_argument('day', type=int, nargs='?', help='Day of the challenge (1-25)')  
    sub_parser.add_argument('year', type=int, nargs='?', help='Year of the challenge')       
    sub_parser.add_argument('--day', type=int, help='Day of the challenge (1-25)')  
    sub_parser.add_argument('--year', type=int, help='Year of the challenge')       
    

def main():
    parser = argparse.ArgumentParser(description="Advent of Code CLI")

    subparsers = parser.add_subparsers(dest='command', help='Sub-command to run')

    open_parser = subparsers.add_parser('open', help='Open the Advent of Code website for a specific day and year')
    add_date_args(sub_parser=open_parser)
    
    read_parser = subparsers.add_parser('read', help='Read the input for a specific day and year')
    add_date_args(sub_parser=read_parser)
    
    start_parser = subparsers.add_parser('start', help='Create a new Python file for the specified day and year, and open the Advent of Code website.')
    add_date_args(sub_parser=start_parser)
    start_parser.add_argument('path', type=str, nargs='?', help='Optional path where the Python file should be created. Defaults to the current directory.')
    start_parser.add_argument('--path', type=str, help='Optional path where the Python file should be created. Defaults to the current directory.')

    args = parser.parse_args()

    if args.command == 'open':
        # Call open_website with the provided day and year
        open_website(day=args.day, year=args.year)
    elif args.command == 'read':
        # Call get_aoc_input and print the result
        result = get_aoc_input(day=args.day, year=args.year)
        print(result)
    elif args.command == "start":
        create_file_and_open(day=args.day, year=args.year, path = args.path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
