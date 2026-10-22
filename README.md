
# Bug Fixing Using Cursor AI

## Project Objective
Demonstrate how to identify and fix a common Python runtime error.

## Files
- `buggy_code.py` — original code that fails for an empty list.
- `fixed_code.py` — corrected code with input validation.

## Bug Identified
The original function divides by the length of the list. If the list is empty, its length is zero, causing a `ZeroDivisionError`.

## Solution
The corrected function checks whether the list is empty and raises a clear `ValueError` before performing the division.

## Requirements
Python 3.

## Run
python buggy_code.py
python fixed_code.py

## Expected Output
Average: 20.0

## Learning Outcome
Practice debugging, exception handling, input validation, and writing more reliable Python functions.
