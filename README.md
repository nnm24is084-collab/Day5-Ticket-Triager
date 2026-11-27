# Day 5 - Equipment Complaint Triager

A Python-based equipment complaint triager using structured JSON and Pydantic.

## Features
- Equipment identification
- Urgency classification
- Hospital extraction
- Next action recommendation
- Structured output using Pydantic
- Evaluation using 20 synthetic complaints

## Technologies
Python, Pydantic, CSV, Regex

## Run
```bash
python triager.py
``` 

## Evaluation
20 synthetic test cases. Equipment: 100%, Urgency: 100%, Hospital: 100%, Overall: 100%.

## Note
Rule-based prototype. Prompts are not connected to a live LLM. Not clinically validated.


## Project Status
Completed as part of AI Studio Internship Day 5. Includes structured complaint output and evaluation on 20 synthetic test cases.
