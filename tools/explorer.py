import json
import os


class Profile:

    def __init__(self, username):
        self.username = username
        self.file = f"data/{username}.json"


    # Ø¢ÛŒØ§ Ø­Ø³Ø§Ø¨ ÙˆØ¬ÙˆØ¯ Ø¯Ø§Ø±Ø¯ØŸ
    def exists(self):
        return os.path.exists(self.file)



    # Ø³Ø§Ø®Øª Ø­Ø³Ø§Ø¨
    def create(self, password):

        if self.exists():
            return False


        data = {
            "username": self.username,
            "password": password,

            "level": 1,

            "experiments": [],

            "total_attempts": 0,
            "correct_answers": 0,
            "accuracy": 0
        }


        self.save(data)

        return True



    # ÙˆØ±ÙˆØ¯ Ø¨Ø§ Ø±Ù…Ø²
    def check_password(self, password):

        if not self.exists():
            return False


        data = self.load()

        return data.get("password") == password



    # Ø®ÙˆØ§Ù†Ø¯Ù† Ø§Ø·Ù„Ø§Ø¹Ø§Øª
    def load(self):

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)



    # Ø°Ø®ÛŒØ±Ù‡ Ø§Ø·Ù„Ø§Ø¹Ø§Øª
    def save(self, data):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )



    # Ø«Ø¨Øª ÛŒÚ© ØªÙ„Ø§Ø´ Ø¢Ø²Ù…Ø§ÛŒØ´
    def add_experiment(
            self,
            name,
            prediction,
            result,
            correct):


        data = self.load()


        experiment = {

            "name": name,

            "prediction": prediction,

            "result": result,

            "correct": correct
        }


        data["experiments"].append(experiment)


        data["total_attempts"] += 1



        if correct:

            data["correct_answers"] += 1



        data["accuracy"] = round(
            (
                data["correct_answers"]
                /
                data["total_attempts"]
            )
            *
            100
        )



        self.save(data)



    # Ú¯Ø±ÙØªÙ† Ú¯Ø²Ø§Ø±Ø´ Ú©Ù„ÛŒ
    def get_report(self):

        data = self.load()


        return {

            "level": data["level"],

            "experiments": data["experiments"],

            "attempts": data["total_attempts"],

            "accuracy": data["accuracy"]

        }



    # Ø­Ø°Ù Ø­Ø³Ø§Ø¨
    def delete_account(self):

        if not self.exists():
            return False

        os.remove(self.file)

        self.clear_session()

        return True

    def create_session(self):

        if not self.exists():
            return False

        session_data = {
            "username": self.username
        }

        with open(
            "data/session.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                session_data,
                f,
                ensure_ascii=False,
                indent=4
            )

        return True


    # Ø¯Ø±ÛŒØ§ÙØª Session ÙØ¹Ù„ÛŒ
    def get_session(self):

        session_file = "data/session.json"

        if not os.path.exists(session_file):
            return None

        with open(
            session_file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        return data.get("username")


    # Ø­Ø°Ù Session Ø§ÛŒÙ† Ø¯Ø³ØªÚ¯Ø§Ù‡
    def clear_session(self):

        session_file = "data/session.json"

        if os.path.exists(session_file):
            os.remove(session_file)

            return True

        return False
