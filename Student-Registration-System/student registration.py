# Author : Pawan Kaur
# Class : Software Development Fundamentals
# Date : 2026-09-14

"""
Student Registration Process
"""

# ====================================
# Step 1: Student Registration Process 
# ====================================

#  Initialize the registration counter
registration_counter = 50000

def student_registration():
    global registration_counter 

    # Collect student registration details
    registration_date = input("Enter registration date (YYYY-MM-DD): ")
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    course_name = input("Enter course name: ")

    # Generate a unique registration ID by incrementing the counter
    registration_counter += 1
    registration_id = registration_counter

    # Return the  registration details as a tuple
    return registration_date, student_id, student_name, course_name, registration_id

# ==================================================
# Step 2 : Testing the Student Registration Function
#===================================================

# Call the function and unpack the returned values
registration_date, student_id, student_name, course_name, registration_id = student_registration()


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


     
    