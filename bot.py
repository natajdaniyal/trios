class TriosBot:

    def __init__(self, name="Trios-Bot"):
        self.name = name

    def say(self, message):
        print(f"\n🤖 {self.name}: {message}")

    def welcome(self):
        self.say("سلام کاوشگر!")
        self.say("به Trios خوش آمدی.")
        self.say("اینجا فقط جواب سؤال‌ها را نمی‌خوانی...")
        self.say("اینجا آن‌ها را آزمایش می‌کنی.")

    def ask_name(self):
        name = input("\n👤 کاوشگر، دوست داری با چه نامی صدات کنم؟ ")

        self.say(f"خوش اومدی، {name}.")
        self.say("از این لحظه تو یکی از کاوشگران Trios هستی. 🌌")

        return name

    def show_menu(self):

        print("\n==============================")
        print("🌌        MAIN MENU")
        print("==============================")
        print("1️⃣  شروع آزمایش")
        print("2️⃣  Trios چیست؟")
        print("3️⃣  خروج")

        choice = input("\nانتخاب تو: ")

        return choice

    def about(self):

        self.say(
            "Trios یک آزمایشگاه تعاملی علمی است."
        )
        self.say(
            "در آن پیش‌بینی می‌کنی، آزمایش انجام می‌دهی "
            "و نتیجه را تحلیل می‌کنی."
        )

    def check_command(self, command):

        command = command.lower()

        if command in ["exit", "خروج"]:
            return "exit"

        if command in ["menu", "منو"]:
            return "menu"

        return None