class Report:


    def show_profile(self, data):

        print("\n==============================")
        print("🔬        آزمایشگاه من")
        print("==============================")


        print(f"\n👨‍🚀 کاوشگر: {data['username']}")

        print(f"⭐ سطح: {data['level']}")

        print(
            f"\n🧪 تعداد تلاش‌ها: {data['total_attempts']}"
        )

        print(
            f"📈 دقت پاسخ‌ها: {data['accuracy']}%"
        )


        print("\n------------------------------")


        if len(data["experiments"]) == 0:

            print(
                "هنوز آزمایشی انجام نداده‌ای."
            )

            print(
                "اولین آزمایش تو اینجا ثبت خواهد شد."
            )


        else:

            print("🧪 آزمایش‌های انجام شده:\n")


            for i, exp in enumerate(
                data["experiments"],
                start=1
            ):

                print(
                    f"{i}) {exp['name']}"
                )

                print(
                    f"   فرضیه: {exp['prediction']}"
                )

                print(
                    f"   نتیجه: {exp['result']}"
                )


                if exp["correct"]:

                    print(
                        "   وضعیت: موفق ✅"
                    )

                else:

                    print(
                        "   وضعیت: نیاز به بررسی 🔍"
                    )


                print()