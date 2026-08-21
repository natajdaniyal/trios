from state import state


class CommandCenter:


    def execute(self, command):


        if command == "RIGHT":

            state.move(1, 0)

            print("🎮 Action: Move Right")



        elif command == "LEFT":

            state.move(-1, 0)

            print("🎮 Action: Move Left")



        elif command == "RESET":

            state.reset()

            print("🔄 Action: Reset")



        elif command == "QUIT":

            print("🚪 Action: Quit")



        else:

            print("❌ Unknown command")