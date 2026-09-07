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


    # Display a message  to show the start of the parking meter process
    print("_" * 30)
    print("Kia Ora! This is the Parking meter")
    print("_" * 30)

    # Sets the parking time to 4 hours
    park_time = 4

    # set the initial rate and cost
    rate = 4
    cost = 0

    # Calculate the parking cost using an IF statement
    if park_time > 3:
        cost = rate * 3

        # Reduce the rate by $2
        rate -= 2

        remaining_time = park_time - 3

        # Add the remaining time cost
        cost += rate * remaining_time 
    else:
        cost = rate * park_time

    # Create a unique ticket ID by incrementing the counter
    ticket_counter += 1
    ticket_id = ticket_counter    

    # Return the parking Details and ticket ID as a tuple
    return park_time, cost, ticket_id

# ==================================================
# PART 2: Testing the Parking Meter Function
#===================================================

# Call the function and unpack the returned values
park_time, cost, ticket_id = parking_meter()

# 5. Display the calculated parking charges 
print()
print("_" * 30)
print("\nPrinting Parking Meter Details:")
print()
print(f"Parking Time: {park_time} hours")
print(f"The Cost of the parking is ${cost}")
print(f"Ticket ID: {ticket_id}")
print("_" * 30)