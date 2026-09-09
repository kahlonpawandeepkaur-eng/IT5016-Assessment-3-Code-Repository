# Author : Pawan Kaur
# Class : Software Development Fundamentals
# Date : 2026-09-14

"""
Student Registration Process
"""
# This file handles Student Registration 

# ====================================
# Step 1: Student Registration Process 
# ====================================

# This global variable generates a  unique registration ID for each student 
# Initialize the registration counter
registration_counter = 50000

# This function collects student details and generates a unique registration ID
def student_registration():
    global registration_counter 

    # SOFTWARE DESIGN PRINCIPLE: SINGLE RESPONSIBILITY
    # This function collects the student details and creates a registration ID

    # SOFTWARE DESIGN PRINCIPLE: KISS
    # Simple input statements are used to collect student details

    
    # Collect student registration details
    registration_date = input("Enter registration date (YYYY-MM-DD): ")
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    course_name = input("Enter course name: ")

    # Generate a unique registration ID by incrementing the counter
    registration_counter += 1
    registration_id = registration_counter

    # SOFTWARE DESIGN PRINCIPLE: CLEAN CODE OVER CLEVER CODE
    # Clear names and simple code make the program easy to understand

    # SOFTWARE DESIGN PRINCIPLE: DRY
    # Using variables helps avoid repeating the same values in the code

    # This returns the collected student details and registration ID
    # Return the  registration details as a tuple
    return registration_date, student_id, student_name, course_name, registration_id

# ==================================================
# Step 2 : Testing the Student Registration Function
#===================================================

# Call the function and unpack the returned values
registration_date, student_id, student_name, course_name, registration_id = student_registration()

# SOFTWARE DESIGN PRINCIPLE: SEPARATION OF CONCERNS 
# The function collects the details and the code below displays them


# Display the registered student details
print("=" * 40)
print("\nPrinting Student Registration Details:")
print("=" * 40)
print(f"Date: {registration_date}")
print(f"Student ID: {student_id}")
print(f"Student Name: {student_name}")
print(f"Course Name: {course_name}")
print(f"Registration ID: {registration_id}")
print("=" * 40)


     
    
