# Author : Pawan Kaur
# Class : Software Development Fundamentals
# Date : 2026-06-10

"""
Parking Meter System
"""

# ==========================================
# PART 1: Parking Meter Process
# ==========================================

# Initialize a global ticket counter
ticket_counter = 10000

def parking_meter():
    global ticket_counter


    # 1. Display a message with standard decorations to indicate the start of the parking meter process
    print("_" * 30)
    print("Kia Ora! This is parking meter")
    print("_" * 30)

    # 2. Creates and sets the value for variable ParkTime = 4 hours
    park_time = 4

    # 3. Creates and sets value for variables: rate and cost
    rate = 4
    cost = 0

    # 4. Calculates the parking charges for parktime using an IF statement
    if park_time > 3:
        cost = rate * 3

        # Drop the rate by $2
        rate -= 2

        remaining_time = park_time - 3

        # Add to the current cost
        cost += rate * remaining_time 
    else:
        cost = rate * park_time

    # Generate a unique ticket ID by incrementing the counter
    ticket_counter += 1
    ticket_id = ticket_counter    

    # Return the parking variables and ticket ID as a tuple
    return park_time, cost, ticket_id

# ==================================================
# PART 2: Testing the Parking Meter Function
#===================================================

# Call the function to process parking and unpack the returned values
park_time, cost, ticket_id = parking_meter()

# 5. Display appropriate message showing the calculated parking charges 
print()
print("_" * 30)
print("\nPrinting Parking Meter Details:")
print()
print(f"Parking Time: {park_time} hours")
print(f"The Cost of the parking is ${cost}")
print(f"Ticket ID: {ticket_id}")
print("_" * 30)