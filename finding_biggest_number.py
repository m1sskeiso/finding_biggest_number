import tkinter as tk
from tkinter import ttk

# Function to find and display the largest number
def find_largest():
    try:

# Retrieve numbers from the entry fields
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        num3 = float(entry_num3.get())

# Find the largest number using if-else statements
        if num1 >= num2 and num1 >= num3:
            largest = num1
        elif num2 >= num1 and num2 >= num3:
            largest = num2
        else:
            largest = num3
            
# Display the result
result_label.config(text=f"The largest number is: {largest}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")


# Create the main window
# Create a frame for the layout
# Entry fields for the numbers
# Labels for the entry fields
# Button to find the largest number
# Label to display the result
# Styling the button
# Run the application
