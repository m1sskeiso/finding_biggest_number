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
root = tk.Tk()
root.title("Largest Number Finder")

# Create a frame for the layout
frame = ttk.Frame(root, padding="30")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Entry fields for the numbers
entry_num1 = ttk.Entry(frame, width=15, font=("Georgia", 16))
entry_num1.grid(row=0, column=1, padx=10, pady=10)

entry_num2 = ttk.Entry(frame, width=15, font=("Georgia", 16))
entry_num2.grid(row=1, column=1, padx=10, pady=10)

entry_num3 = ttk.Entry(frame, width=15, font=("Georgia", 16))
entry_num3.grid(row=2, column=1, padx=10, pady=10)

# Labels for the entry fields
label_num1 = ttk.Label(frame, text="Enter first number:", font=("Georgia", 16))
label_num1.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

label_num2 = ttk.Label(frame, text="Enter second number:", font=("Georgia", 16))
label_num2.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

label_num3 = ttk.Label(frame, text="Enter third number:", font=("Georgia", 16))
label_num3.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)

# Button to find the largest number
find_button = ttk.Button(frame, text="Find Largest Number", command=find_largest, style="W.TButton")
find_button.grid(row=3, column=0, columnspan=2, pady=20)

# Label to display the result
result_label = ttk.Label(frame, text="", font=("Georgia", 16))
result_label.grid(row=4, column=0, columnspan=2)

# Styling the button
style = ttk.Style()
style.configure("W.TButton", font=("Arial", 16), padding=10)

# Run the application
root.mainloop()

