from explorer import Profile
from report import Report
from experiment import run_test



def create_account():

    print("\n==============================")
    print("🚀 ساخت کاوشگر جدید")
    print("==============================")

    username = input("\n👤 نام کاربری: ")

    profile = Profile(username)

    if profile.exists():

        print("\n❌ این نام کاربری قبلاً استفاده شده است.")
        return None


    password = input("🔑 رمز عبور: ")

    profile.create(password)


    print("\n🎉 کاوشگر جدید ساخته شد!")
    print("🌌 به خانواده Trios خوش آمدی.")

    return username





def login():

    print("\n==============================")
    print("🌌 ورود کاوشگر")
    print("==============================")


    username = input("\n👤 نام کاربری: ")

    profile = Profile(username)


    if not profile.exists():

        print("\n❌ چنین کاوشگری پیدا نشد.")
        return None



    password = input("🔑 رمز عبور: ")


    if profile.check_password(password):

        print(f"\n🌌 خوش برگشتی {username}!")

        return username


    else:

        print("\n❌ رمز عبور اشتباه است.")

        return None





def delete_account(username):

    print("\n==============================")
    print("⚠️ حذف حساب")
    print("==============================")


    print(
        "\nتمام اطلاعات آزمایش‌ها و پروفایل پاک خواهد شد."
    )


    confirm = input(
        "\nبرای تأیید حذف بنویس YES: "
    )


    # تبدیل ورودی به حروف بزرگ
    confirm = confirm.upper()


    if confirm == "YES":


        profile = Profile(username)


        if profile.delete_account():

            print("\n🗑️ حساب حذف شد.")

            print(
                "🌌 می‌توانی یک کاوشگر جدید بسازی."
            )

            return True



    print("\n❌ حذف حساب لغو شد.")

    return False






def main_menu(username):


    while True:


        print("\n==============================")
        print("🌌 MAIN MENU")
        print("==============================")


        print("1️⃣ شروع آزمایش")
        print("2️⃣ Trios چیست؟")
        print("3️⃣ حذف حساب")
        print("4️⃣ آزمایشگاه من")
        print("5️⃣ خروج")


        choice = input("\nانتخاب تو: ")




        if choice == "1":


            profile = Profile(username)

            run_test(profile)





        elif choice == "2":


            print(
                "\n🌌 Trios یک آزمایشگاه تعاملی برای بررسی مسئله سه‌جسمی است."
            )

            print(
                "اینجا قرار است حرکت، نیرو و رفتار سه جسم را آزمایش کنیم."
            )





        elif choice == "3":


            deleted = delete_account(username)


            if deleted:

                break





        elif choice == "4":


            profile = Profile(username)

            data = profile.load()


            report = Report()

            report.show_profile(data)





        elif choice == "5":


            print(
                f"\n🤖 خداحافظ {username}! 🌌"
            )

            break





        else:

            print(
                "\n❌ انتخاب نامعتبر است."
            )









while True:


    print("\n===================================")
    print("🌌            TRIOS")
    print("===================================")


    print("\n1️⃣ ورود کاوشگر")
    print("2️⃣ ساخت کاوشگر جدید")
    print("3️⃣ خروج")


    choice = input("\nانتخاب تو: ")




    if choice == "1":


        user = login()


        if user:

            main_menu(user)





    elif choice == "2":


        user = create_account()


        if user:

            main_menu(user)





    elif choice == "3":


        print(
            "\n🤖 خداحافظ کاوشگر! 🌌"
        )

        break





    else:

        print(
            "\n❌ انتخاب نامعتبر است."
        )