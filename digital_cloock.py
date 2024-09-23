# Importing necessary libraries
from tkinter import Label, Tk
import time

# Setting up the main window for the clock
window = Tk()
window.title("Digital Clock")  # Title of the window
window.geometry("350x150")     # Window size
window.resizable(False, False) # Preventing window resizing
window.configure(bg='black')   # Background color

# Label for displaying the time
clock_label = Label(window, font=('Arial', 24), bg='black', fg='white')
clock_label.grid(row=0, column=1)

# Function to update the time
def update_time():
    current_time = time.strftime('%H:%M:%S %p')  # Time format
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Update every 1 second

# Call the function to display the time initially
update_time()

# Run the application
window.mainloop()
