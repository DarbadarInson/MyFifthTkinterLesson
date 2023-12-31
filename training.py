import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("@imdevana")
window.geometry("300x200")

label = tk.Label(window, text="Enter your input")
label.pack()

# Create an Entry widget
entry = tk.Entry(window, bg="gray40")
entry.pack()

# Run the application
window.mainloop()