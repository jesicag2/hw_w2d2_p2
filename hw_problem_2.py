# HW2_P2: Quick Decisions: The Event Planner 🎉

# Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
print(venue)


# Task 2: Venue Selection
'''
Based on the corrected code from Task 1, further enhance the program to 
recommend additional facilities like "audio system" or "projector" based 
on the number of attendees.
'''

attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
print(venue)

add_facilities = "audio system" if attendees > 75 else "projector"
print(add_facilities)


# Task 3: Catering Choices
'''
Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" 
if yes, otherwise recommend "Gourmet Meals Caterers".
'''

attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
print(venue)

add_facilities = "audio system" if attendees > 75 else "projector"
print(add_facilities)

catering_choice = input("Do you want vegetarian food? (yes/no) ")

catering_rec = "Veggie Delight Caterers" if catering_choice == "yes" else "Gourmet Meals Caterers"
print(catering_rec)
