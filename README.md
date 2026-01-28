# Password Strength Regex Tester

## Project Title & Goal
A Python-based utility that validates password strength using regex-based security rules.

## Setup Instructions
1. Make sure Python is installed
2. Run the script using:
   python main.py

## The Logic (How I thought)
I used regular expressions because they are efficient and widely used for password validation.
Each password is checked for minimum length, presence of numeric characters, and special characters.
To ensure correctness, I added assertions to validate expected outcomes, simulating basic test cases.
The main challenge was designing clear validation rules without overcomplicating the logic.

## Output Screenshots

<img width="1915" height="1015" alt="Screenshot 2026-01-28 103039" src="https://github.com/user-attachments/assets/5251704b-f44c-43b4-9561-24dada326528" />

## Future Improvements
If I had two more days, I would:
- Add uppercase and lowercase validation rules
- Read passwords dynamically from a file
- Convert assertions into proper unit tests using PyTest
