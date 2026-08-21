import json
import os


class Profile:

    def __init__(self, username):
        self.username = username
        self.file = f"data/{username}.json"


    # آیا حساب وجود دارد؟
    def exists(self):
        return os.path.exists(self.file)



    # ساخت حساب
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



    # ورود با رمز
    def check_password(self, password):

        if not self.exists():
            return False


        data = self.load()

        return data.get("password") == password



    # خواندن اطلاعات
    def load(self):

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)



    # ذخیره اطلاعات
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



    # ثبت یک تلاش آزمایش
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



    # گرفتن گزارش کلی
    def get_report(self):

        data = self.load()


        return {

            "level": data["level"],

            "experiments": data["experiments"],

            "attempts": data["total_attempts"],

            "accuracy": data["accuracy"]

        }



    # حذف حساب
    def delete_account(self):

        if self.exists():

            os.remove(self.file)

            return True


        return False