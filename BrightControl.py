import tkinter as tk
from tkinter import messagebox
import subprocess

# Configuration file path
config_file = "config.txt"

# Load the last selected display option from the configuration file
def load_last_display_option():
    try:
        with open(config_file, "r") as file:
            last_display_option = file.read().strip()
            if last_display_option in display_options:
                display_var.set(last_display_option)
    except FileNotFoundError:
        pass

# Save the currently selected display option to the configuration file
def save_current_display_option():
    with open(config_file, "w") as file:
        file.write(display_var.get())

# List to store historical brightness values
brightness_history = []

def set_brightness():
    display = display_var.get()
    brightness = brightness_var.get()
    
    if brightness < 40:
        confirmation = messagebox.askokcancel("Brightness Alert", "Your screen will be darker! Risk of shutdown. Continue?")
        if not confirmation:
            return
    
    brightness_value = brightness / 100.0 + 0.1  # Adjusting brightness to range 1.1 - 2.0
    
    command = f"xrandr --output {display} --brightness {brightness_value}"
    subprocess.run(command, shell=True)
    
    # Add current brightness to history
    brightness_history.append(brightness)

def show_history():
    messagebox.showinfo("Brightness History", "\n".join(str(b) for b in brightness_history))

def reset_settings():
    brightness_var.set(100)  # Reset the brightness value to 100
    brightness_history.clear()  # Clear the brightness history

# Rest of the code remains the same...

# Create the GUI window
window = tk.Tk()
window.title("Display Brightness Control")

# Display selection
display_options = ["HDMI-1", "DP-1"]
display_var = tk.StringVar()

display_label = tk.Label(window, text="Select Display:")
display_label.pack()

display_combobox = tk.OptionMenu(window, display_var, *display_options)
display_combobox.pack()

# Load the last selected display option
load_last_display_option()


# Brightness level
brightness_label = tk.Label(window, text="Brightness (0-100):")
brightness_label.pack()

brightness_var = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)
brightness_var.pack()

# Execute button
execute_button = tk.Button(window, text="Execute", command=set_brightness)
execute_button.pack()

# History button
history_button = tk.Button(window, text="Show History", command=show_history)
history_button.pack()

# Reset button
reset_button = tk.Button(window, text="Reset", command=reset_settings)
reset_button.pack()

# Output label
output_label = tk.Label(window, text="Current Output: ")
output_label.pack()

def update_output_label():
    output_label.config(text="Current Output: " + display_var.get())

display_var.trace("w", lambda *args: update_output_label())

# Save the currently selected display option when changed
display_var.trace("w", lambda *args: save_current_display_option())

# Start the GUI event loop
window.mainloop()
