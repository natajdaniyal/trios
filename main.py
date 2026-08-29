import os

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

    if not profile.create(password):

        print("\n❌ ساخت حساب انجام نشد.")
        return None

    profile.create_session()

    print("\n🎉 کاوشگر جدید ساخته شد!")
    print("🌌 به خانواده TRIOS خوش آمدی.")

    return username


def recover_account():

    print("\n==============================")
    print("🌌 بازیابی حساب")
    print("==============================")

    username = input("\n👤 نام کاربری: ")

    profile = Profile(username)

    if not profile.exists():

        print("\n❌ چنین کاوشگری پیدا نشد.")
        return None

    password = input("🔑 رمز عبور: ")

    if not profile.check_password(password):

        print("\n❌ رمز عبور اشتباه است.")
        return None

    profile.create_session()

    print(f"\n🌌 خوش برگشتی {username}!")

    return username


def delete_account(username):

    print("\n==============================")
    print("⚠️ حذف حساب")
    print("==============================")

    print(
        "\nتمام اطلاعات آزمایش‌ها و پروفایل پاک خواهند شد."
    )

    confirm = input(
        "\nبرای تأیید حذف بنویس YES: "
    )

    if confirm.upper() == "YES":

        profile = Profile(username)

        if profile.delete_account():

            print("\n🗑️ حساب حذف شد.")
            print("🌌 می‌توانی یک کاوشگر جدید بسازی.")

            return True

    print("\n❌ حذف حساب لغو شد.")

    return False


def main_menu(username):

    while True:

        print("\n==============================")
        print("🌌 MAIN MENU")
        print("==============================")

        print("1️⃣ شروع آزمایش")
        print("2️⃣ TRIOS چیست؟")
        print("3️⃣ آزمایشگاه من")
        print("4️⃣ حذف حساب")
        print("5️⃣ خروج از دستگاه")
        print("6️⃣ خروج")

        choice = input("\nانتخاب تو: ")

        if choice == "1":

            profile = Profile(username)

            run_test(profile)

        elif choice == "2":

            print(
                "\n🌌 TRIOS یک آزمایشگاه تعاملی برای بررسی "
                "سیستم‌های فیزیکی چندجسمی است."
            )

            print(
                "تمرکز اصلی پروژه روی شبیه‌سازی، نیرو، "
                "حرکت و رفتار سیستم‌های سه‌جسمی است."
            )

        elif choice == "3":

            profile = Profile(username)

            data = profile.load()

            report = Report()

            report.show_profile(data)

        elif choice == "4":

            deleted = delete_account(username)

            if deleted:

                return "account_deleted"

        elif choice == "5":

            profile = Profile(username)

            profile.clear_session()

            print(
                "\n📱 این دستگاه دیگر به حساب تو متصل نیست."
            )

            print(
                "🌌 اطلاعات حساب همچنان محفوظ است."
            )

            return "device_logout"

        elif choice == "6":

            print(
                f"\n🤖 خداحافظ {username}! 🌌"
            )

            return "exit"

        else:

            print(
                "\n❌ انتخاب نامعتبر است."
            )


def show_first_run_menu():

    print("\n===================================")
    print("🌌            TRIOS")
    print("===================================")

    print("\n1️⃣ TRIOS چیست؟")
    print("2️⃣ ساخت کاوشگر جدید")
    print("3️⃣ بازیابی حساب")
    print("4️⃣ خروج")


def show_about():

    print("\n==============================")
    print("🌌 TRIOS چیست؟")
    print("==============================")

    print(
        "\nTRIOS یک آزمایشگاه تعاملی برای بررسی "
        "سیستم‌های فیزیکی چندجسمی است."
    )

    print(
        "تمرکز اصلی پروژه روی شبیه‌سازی، نیرو، "
        "حرکت و بررسی رفتار سیستم سه‌جسمی است."
    )


while True:

    session_profile = Profile("")
    session_owner = session_profile.get_session()

    if session_owner:

        active_profile = Profile(session_owner)

        if active_profile.exists():

            print(
                f"\n🌌 خوش برگشتی {session_owner}!"
            )

            result = main_menu(session_owner)

            if result == "exit":

                break

            continue

        else:

            active_profile.clear_session()

    show_first_run_menu()

    choice = input("\nانتخاب تو: ")

    if choice == "1":

        show_about()

    elif choice == "2":

        user = create_account()

        if user:

            result = main_menu(user)

            if result == "exit":

                break

    elif choice == "3":

        user = recover_account()

        if user:

            result = main_menu(user)

            if result == "exit":

                break

    elif choice == "4":

        print(
            "\n🤖 خداحافظ کاوشگر! 🌌"
        )

        break

    else:

        print(
            "\n❌ انتخاب نامعتبر است."
        )
