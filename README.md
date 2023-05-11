# BrightnessControl
Controlling the display brightness.

The code provided a Python script that uses the tkinter library to create a graphical user interface (GUI) for controlling the display brightness. Here's a breakdown of the code:

1. The necessary libraries are imported: `tkinter`, `messagebox`, and `subprocess`.

2. The configuration file path is specified as `"config.txt"`.

3. The `load_last_display_option()` function is defined to read the last selected display option from the configuration file and set it as the default value in the GUI.

4. The `save_current_display_option()` function is defined to save the currently selected display option to the configuration file.

5. A list called `brightness_history` is created to store the historical brightness values.

6. The `set_brightness()` function is defined to set the brightness of the selected display. It retrieves the display and brightness values from the GUI, prompts a confirmation message box if the brightness is below 40, adjusts the brightness value to the range 1.1-2.0, and uses the `subprocess.run()` function to execute an `xrandr` command with the specified display and brightness values. It also adds the current brightness to the `brightness_history` list.

7. The `show_history()` function is defined to display a message box with the historical brightness values.

8. The `reset_settings()` function is defined to reset the brightness value to 100 and clear the brightness history.

9. The GUI window is created using `tkinter.Tk()`.

10. The display selection is created using a label (`display_label`) and an option menu (`display_combobox`). The last selected display option is loaded using the `load_last_display_option()` function.

11. The brightness level is created using a label (`brightness_label`) and a scale (`brightness_var`).

12. An execute button (`execute_button`) is created to call the `set_brightness()` function when clicked.

13. A history button (`history_button`) is created to call the `show_history()` function when clicked.

14. A reset button (`reset_button`) is created to call the `reset_settings()` function when clicked.

15. An output label (`output_label`) is created to display the currently selected display option. The `update_output_label()` function is defined to update the output label when the display option changes. The `save_current_display_option()` function is called whenever the display option changes to save the selection to the configuration file.

16. The GUI event loop is started using `window.mainloop()`, which waits for user interactions and updates the GUI accordingly.

Overall, this script provides a GUI interface to control the display brightness, save the last selected display option, show the historical brightness values, and reset the settings.

GUI application for controlling the display brightness. It allows the user to select a display from a dropdown menu, adjust the brightness using a scale widget, and execute the brightness change by clicking a button. The application also provides features to show the historical brightness values and reset the settings.

Based on this concept, you can further enhance the application by adding additional functionality and features. Here are a few ideas:

1. Profiles: Allow users to create and save profiles for different display configurations, including brightness settings. This way, users can quickly switch between different profiles based on their preferences or usage scenarios.

2. Automatic Brightness Adjustment: Implement an algorithm to automatically adjust the brightness based on ambient light conditions. You can utilize light sensors or utilize system APIs to detect the ambient light level and adjust the display brightness accordingly.

3. Keyboard Shortcuts: Enable users to assign keyboard shortcuts to control the display brightness. This can provide a convenient and quick way to adjust the brightness without relying solely on the GUI.

4. Dark Mode Switch: Expand the application to include a switch for enabling or disabling dark mode. When the dark mode is enabled, the application can adjust the display brightness and color scheme to provide a better viewing experience in low-light environments.

5. Multi-monitor Support: Enhance the application to support multiple displays and allow users to independently adjust the brightness of each monitor. This can be useful for users with multiple monitors connected to their system.

6. System Tray Integration: Add a system tray icon for the application, allowing users to access brightness controls directly from the system tray. This provides easy access to the application without keeping the main window always open.

7. Notifications and Alerts: Implement notifications or alerts when the brightness reaches certain levels or when the user tries to set a brightness below a certain threshold. This can help prevent potential issues such as screen shutdown due to extremely low brightness.

8. Schedule Brightness Changes: Allow users to schedule brightness changes at specific times or based on specific events. This feature can be handy for automatically adjusting the brightness based on user-defined preferences or during specific activities like presentations or nighttime usage.

Remember to consider user experience and usability when implementing these additional features. You can also incorporate user feedback and iterate on the application to make it more intuitive and user-friendly.

![Untitled](https://github.com/Coding-Crab/BrightnessControl/assets/121975087/b99e9693-0535-468c-b76a-2f792811d3d7)

