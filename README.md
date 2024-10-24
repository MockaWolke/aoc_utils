# aoc-utils

**aoc-utils** is a standalone Python command-line tool that simplifies interactions with [Advent of Code](https://adventofcode.com). It allows you to open specific challenge pages, retrieve input data, and automatically create Python templates to get started with your Advent of Code solutions.

## Features

- **Open Advent of Code challenge**: Open a specific challenge day directly in your browser.
- **Get Advent of Code input data**: Fetch input data for a specific challenge day and year.
- **Create a Python template**: Automatically create a Python script with boilerplate code for a specific day.
- **Export input data to a file**: Easily fetch and save input data to a file using the `read` command and redirection.

## Usage

`aoc-utils` provides the following commands:

### 1. **Open Advent of Code Website**

```bash
aoc open 10 2023
```

This command opens the Advent of Code website for day 10 of the year 2023 in your default web browser.

You can also specify the day and year using flags:

```bash
aoc open --day 10 --year 2023
```

### 2. Fetch Advent of Code Input

```bash
aoc read 10 2023 > inputs.txt

```

### 3. Create a Python File for Advent of Code
```bash
aoc start 10 2023 /path/to/myfile.py
```
This creates a Python file for day 10 of 2023 at the specified path, pre-filled with the basic template to fetch input data, and opens it with your default editor. If no path is provided, it defaults to the current directory:

```bash
aoc start 10 2023
```
The resulting file will be named aoc_10_2023.py.

## Installation
aoc-utils has no external dependencies or requirements and is completely standalone. To use it, clone the repository and install the package:

```bash
git clone https://github.com/your-username/aoc-utils.git
cd aoc-utils
pip install .
```

### Setting up your session token
To fetch your personalized inputs, you need to set your Advent of Code session token as an environment variable. You can find your session token by going to any Advent of Code input page, opening your browser's developer tools, and inspecting the cookies. Look for a cookie called session.

Once you have the session token, set it as an environment variable:

```bash 
export AOC_SESSION=your-session-token
```

As you can tell this readme is clearly chatgpt generated (:

