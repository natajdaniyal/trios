import keyboard

from command import CommandCenter
from state import state


def start_input_engine():

    controller = CommandCenter()

    # هر بار که موتور ورودی اجرا می‌شود
    state.running = True

    print("🎮 Trios Input Engine Started")
    print("----------------------------")
    print("→ Move Right")
    print("← Move Left")
    print("R Reset")
    print("Q Quit")
    print("----------------------------")

    while state.running:

        event = keyboard.read_event()

        if event.event_type != keyboard.KEY_DOWN:
            continue

        key = str(event.name).lower()

        # کلیدهای کمکی را نادیده بگیر
        if key in ["shift", "ctrl", "alt"]:
            continue

        if key == "right":
            controller.execute("RIGHT")

        elif key == "left":
            controller.execute("LEFT")

        elif key == "r":
            controller.execute("RESET")

        elif key == "q":
            controller.execute("QUIT")


if __name__ == "__main__":
    start_input_engine()