# IT5016 Assessment 3 Programming Principles and Concepts
## Overview
This repository contains two Python programs created for IT5016 Assessment 3. While developing these programs I focused on applying basic software design principles.

## Programs Included  
### 1. Parking Meter System
The Parking Meter System calculates the parking cost based on the parking time and generates a unique ticket ID. The program uses simple variables, IF/ELSE statement and a function to complete the parking process.

### 2. Student Registration System 
The Student Registration System collects student registration details and generates a unique registration ID. The program uses a function to handle the registration process and return the required information.

## Software Design Principles

### KISS - Keep It Simple
The KISS principle shows the programs are written in a simple way using basic Python concepts. The code is easy to read, understand and follow without unnecessary complexity.

### DRY - Don't Repeat Yourself 
The DRY principle shows that the functions are used to keep the main task in one place. The Parking Meter System uses the `parking_meter()` function,  while the Student Registration System uses the `student_registration()` function. This helps avoid writing the same code again and makes the programs easier to manage.

### Single Responsibility 
Each function has a clear purpose. The `parking_meter()` function handles the parking calculations and ticket ID, while the `student_registration()` function handles student registration details and the registration ID.

### Separation of Concerns
The various parts of the programs are kept organised. The main processing, testing and displaying of results are handled separately where possible.

### Clean Code Over Clever Code
The programs use meaningful variable names such as `park_time`, `cost`, `ticket_id`, `student_name` and `registration_id`. Comments have been added to explain important parts of the code. Clear headings and spacing also make the code easier to read.

## Conclusion 
Overall, the two programs demonstrate basic software design principles through simple structure, meaningful names, comments, functions and clear organisation. The analysis also identifies areas where the code could be improved in the future. 
