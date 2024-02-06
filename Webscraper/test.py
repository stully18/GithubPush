import tkinter as tk
import tkinter.ttk as ttk

# Create a Tkinter window
window = tk.Tk()

# Create a style object
style = ttk.Style()

# Set the theme to 'alt'
style.theme_use('kroc')

# Now, when you create ttk widgets, they will use the 'alt' theme
# For instance, creating a Button widget
button = ttk.Button(window, text="Click Me")
button.pack()

# Run the Tkinter event loop
window.mainloop()
