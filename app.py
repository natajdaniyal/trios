import streamlit as st

from user_interface import (
    create_google_user,
    create_user,
    delete_user,
    google_profile,
    recover_user,
    user_profile,
)


st.set_page_config(page_title="TRIOS", page_icon="assets/trios_logo.png", layout="wide")


def show_logo():
    st.image("assets/trios_logo.png", width=180)


def google_is_logged_in():
    return bool(getattr(st.user, "is_logged_in", False))


def google_identity():
    return {
        "sub": getattr(st.user, "sub", None),
        "email": getattr(st.user, "email", ""),
        "name": getattr(st.user, "name", ""),
    }


def start_google_login(flow):
    st.session_state.google_flow = flow
    st.login("google")


def set_logged_in_user(data, welcome_message=None):
    st.session_state.user = data["username"]
    if welcome_message:
        st.session_state.welcome_message = welcome_message
    st.session_state.page = "dashboard"
    st.rerun()


def process_google_identity():
    """Map the authenticated Google identity to exactly one TRIOS profile."""
    if not google_is_logged_in() or "user" in st.session_state:
        return

    identity = google_identity()
    profile = google_profile(identity["sub"])
    flow = st.session_state.get("google_flow", "login")

    if profile:
        set_logged_in_user(
            profile,
            f"خوش برگشتی، {profile['username']}! 👋",
        )

    if flow == "recover":
        st.session_state.google_recovery_error = True
        st.session_state.page = "recover_google"
        return

    st.session_state.google_identity = identity
    st.session_state.page = "google_profile"


def show_home():
    show_logo()
    st.caption("آزمایشگاه شبیه‌سازی و بررسی مسئله سه‌جسمی")
    st.write("به آزمایشگاه TRIOS خوش آمدی.")

    if st.button("🚀 ورود به TRIOS", use_container_width=True):
        st.session_state.page = "entry"
        st.rerun()

    if st.button("🌌 TRIOS چیست؟", use_container_width=True):
        st.session_state.page = "about"
        st.rerun()


def show_entry():
    show_logo()
    st.header("ورود به TRIOS")
    st.write("روش ورودت را انتخاب کن.")

    if st.button("🌌 TRIOS چیست؟", use_container_width=True):
        st.session_state.page = "about"
        st.rerun()

    if st.button("🔵 ادامه با Google", use_container_width=True):
        start_google_login("login")

    if st.button("✨ ساخت حساب با TRIOS", use_container_width=True):
        st.session_state.page = "register"
        st.rerun()

    if st.button("🔄 بازیابی حساب", use_container_width=True):
        st.session_state.page = "recover"
        st.rerun()

    if st.button("⬅️ بازگشت", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


def show_recover():
    st.header("🔄 بازیابی حساب")
    st.write("روش ورود قبلی خودت را انتخاب کن.")

    if st.button("🔵 بازیابی با Google", use_container_width=True):
        start_google_login("recover")

    if st.button("🔐 بازیابی با حساب TRIOS", use_container_width=True):
        st.session_state.page = "recover_trios"
        st.rerun()

    if st.button("⬅️ بازگشت", use_container_width=True):
        st.session_state.page = "entry"
        st.rerun()


def show_recover_trios():
    st.header("🔐 ورود با حساب TRIOS")
    st.info("نام کاربری و رمز عبور همان حساب TRIOS را وارد کن.")

    username = st.text_input("نام کاربری", key="recover_username")
    password = st.text_input("رمز عبور", type="password", key="recover_password")

    if st.button("ورود به حساب", use_container_width=True):
        try:
            data = recover_user(username, password)
        except ValueError as exc:
            st.error(str(exc))
        else:
            set_logged_in_user(data, f"خوش برگشتی، {data['username']}! 👋")

    if st.button("⬅️ بازگشت", use_container_width=True):
        st.session_state.page = "recover"
        st.rerun()


def show_recover_google():
    st.header("🔵 بازیابی با Google")
    st.error(
        "این حساب Google هنوز به یک حساب TRIOS متصل نشده است. "
        "برای جلوگیری از ساخت حساب تکراری، ابتدا با روش قبلی حسابت وارد شو."
    )

    if st.button("⬅️ بازگشت به بازیابی", use_container_width=True):
        st.session_state.pop("google_recovery_error", None)
        st.session_state.page = "recover"
        st.rerun()

    if st.button("خروج از Google", use_container_width=True):
        st.logout()


def show_register():
    st.header("✨ ساخت حساب TRIOS")

    username = st.text_input("نام کاربری", key="register_username")
    password = st.text_input("رمز عبور", type="password", key="register_password")
    confirm = st.text_input("تکرار رمز عبور", type="password", key="register_confirm")

    if st.button("ساخت حساب", use_container_width=True):
        if password != confirm:
            st.error("رمزهای عبور یکسان نیستند.")
        else:
            try:
                data = create_user(username, password)
            except ValueError as exc:
                st.error(str(exc))
            else:
                set_logged_in_user(data, f"خوش اومدی، {data['username']}! 🎉")

    if st.button("⬅️ بازگشت", use_container_width=True):
        st.session_state.page = "entry"
        st.rerun()


def show_google_profile():
    identity = st.session_state.get("google_identity", google_identity())

    st.header("✨ ساخت پروفایل TRIOS")
    st.write("ورود با Google انجام شد. حالا یک نام برای پروفایل TRIOS خودت انتخاب کن.")
    if identity.get("name"):
        st.caption(f"حساب Google: {identity['name']}")

    username = st.text_input("نام کاربری TRIOS", key="google_username")

    if st.button("ساخت پروفایل", use_container_width=True):
        try:
            data = create_google_user(
                username,
                identity["sub"],
                identity.get("email"),
                identity.get("name"),
            )
        except ValueError as exc:
            st.error(str(exc))
        else:
            st.session_state.pop("google_identity", None)
            st.session_state.pop("google_flow", None)
            set_logged_in_user(data, f"خوش اومدی، {data['username']}! 🎉")

    if st.button("⬅️ خروج از Google", use_container_width=True):
        st.logout()


def show_dashboard():
    username = st.session_state.user

    show_logo()
    greeting = st.session_state.pop("welcome_message", None)
    if greeting is None:
        greeting = f"خوش برگشتی، {username}! 👋"
    st.title(greeting)
    st.caption("آزمایشگاه شخصی TRIOS")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🚀 شروع آزمایش", use_container_width=True):
            st.session_state.page = "lab"
            st.rerun()
    with col2:
        if st.button("📊 گزارش من", use_container_width=True):
            st.session_state.page = "report"
            st.rerun()
    with col3:
        if st.button("👤 پروفایل", use_container_width=True):
            st.session_state.page = "profile"
            st.rerun()


def show_profile():
    username = st.session_state.user
    data = user_profile(username)

    st.header("👤 پروفایل")
    st.subheader("اطلاعات شخصی")
    st.write(f"**نام کاربری:** {data['username']}")
    if data.get("auth_method") == "google":
        st.caption("روش ورود: Google")

    st.divider()
    st.subheader("مدیریت حساب")

    if st.button("🚪 خروج از این دستگاه", use_container_width=True):
        st.session_state.pop("user", None)
        st.session_state.pop("welcome_message", None)
        st.session_state.pop("google_identity", None)
        st.session_state.pop("google_flow", None)
        if data.get("auth_method") == "google":
            st.logout()
        st.session_state.page = "home"
        st.rerun()

    st.divider()
    st.subheader("حذف حساب")
    st.warning("حذف حساب دائمی است و اطلاعات ذخیره‌شده‌ی این حساب را پاک می‌کند.")
    confirm_delete = st.checkbox("می‌خواهم حسابم را برای همیشه حذف کنم.")

    if st.button("🗑️ حذف دائمی حساب", use_container_width=True):
        if not confirm_delete:
            st.error("برای حذف حساب، ابتدا تأیید حذف را فعال کن.")
        elif delete_user(username):
            st.session_state.pop("user", None)
            st.session_state.pop("welcome_message", None)
            st.session_state.pop("google_identity", None)
            st.session_state.pop("google_flow", None)
            if data.get("auth_method") == "google":
                st.logout()
            st.session_state.page = "home"
            st.rerun()
        else:
            st.error("حساب پیدا نشد.")

    if st.button("⬅️ بازگشت به داشبورد", use_container_width=True):
        st.session_state.page = "dashboard"
        st.rerun()


def show_lab():
    st.header("🔬 آزمایشگاه من")
    st.info(
        "زیرساخت اجرای آزمایش‌های TRIOS آماده است. "
        "محتوای آزمایش‌های آموزشی هنوز جداگانه تعریف نشده و فعلاً در این بخش ساخته نمی‌شود."
    )
    if st.button("⬅️ بازگشت", use_container_width=True):
        st.session_state.page = "dashboard"
        st.rerun()


def show_report():
    data = user_profile(st.session_state.user)
    st.header("📊 گزارش من")

    st.subheader("خلاصه عملکرد")
    st.write(f"**سطح:** {data['level']}")
    st.write(f"**تعداد آزمایش‌ها / تلاش‌ها:** {data['total_attempts']}")
    st.write(f"**پاسخ‌های درست:** {data['correct_answers']}")
    st.write(f"**دقت:** {data['accuracy']}%")

    if data["experiments"]:
        st.subheader("آزمایش‌های ثبت‌شده")
        for experiment in data["experiments"]:
            st.write(
                f"**{experiment['name']}** — "
                f"{'درست' if experiment['correct'] else 'نادرست'}"
            )
    else:
        st.info("هنوز گزارشی برای این حساب ثبت نشده است.")

    if st.button("⬅️ بازگشت", use_container_width=True):
        st.session_state.page = "dashboard"
        st.rerun()


def show_about():
    show_logo()
    st.header("TRIOS چیست؟")
    st.write(
        "TRIOS یک سامانه برای شبیه‌سازی، مشاهده و مطالعه‌ی سیستم‌های فیزیکی چندجسمی "
        "با تمرکز بر مسئله‌ی سه‌جسمی است. هدف TRIOS فقط نمایش حرکت چند جرم نیست؛ "
        "بلکه فراهم کردن یک زیرساخت منظم برای تعریف شرایط فیزیکی، اجرای شبیه‌سازی، "
        "اندازه‌گیری نتایج و بررسی علمی آن‌هاست."
    )
    st.write(
        "در معماری TRIOS، هسته‌ی فیزیک مسئول قوانین و محاسبات فیزیکی است؛ "
        "لایه‌ی شبیه‌سازی اجرای گام‌های زمانی را مدیریت می‌کند؛ پیکربندی فیزیکی "
        "شرایط اولیه را نگه می‌دارد؛ زیرساخت آزمایش مراحل و نتایج را مدیریت می‌کند؛ "
        "و اعتبارسنجی علمی معیارهایی مانند انرژی، تکانه، تکانه‌ی زاویه‌ای و مرکز جرم را بررسی می‌کند."
    )
    st.write(
        "این جداسازی باعث می‌شود رابط کاربری و بخش آموزشی مجبور نباشند منطق فیزیک را "
        "دوباره پیاده‌سازی کنند. در نتیجه، TRIOS می‌تواند در آینده هم به‌عنوان یک ابزار "
        "مطالعاتی و هم به‌عنوان یک محیط آموزشی تعاملی توسعه پیدا کند، بدون اینکه هسته‌ی علمی پروژه به رابط کاربری وابسته شود."
    )
    st.write(
        "TRIOS همچنین برای آزمایش‌های تکرارپذیر طراحی شده است؛ یعنی شرایط فیزیکی، "
        "اجرای شبیه‌سازی، اندازه‌گیری‌ها و اعتبارسنجی می‌توانند از هم تفکیک شوند و "
        "نتایج قابل بررسی و مقایسه باشند."
    )
    st.info("فعلاً تمرکز پروژه روی تکمیل زیرساخت و معماری است؛ آزمایش‌های آموزشی واقعی در این مرحله ساخته نشده‌اند.")

    if st.button("⬅️ بازگشت", use_container_width=True):
        st.session_state.page = (
            "dashboard" if "user" in st.session_state else "home"
        )
        st.rerun()


if "page" not in st.session_state:
    st.session_state.page = "home"

process_google_identity()

if "user" in st.session_state:
    if st.session_state.page in {
        "home", "entry", "register", "recover", "recover_trios",
        "recover_google", "google_profile"
    }:
        st.session_state.page = "dashboard"
else:
    if st.session_state.page in {"dashboard", "lab", "report", "profile"}:
        st.session_state.page = "home"


page = st.session_state.page

if page == "home":
    show_home()
elif page == "entry":
    show_entry()
elif page == "recover":
    show_recover()
elif page == "recover_trios":
    show_recover_trios()
elif page == "recover_google":
    show_recover_google()
elif page == "register":
    show_register()
elif page == "google_profile":
    show_google_profile()
elif page == "dashboard":
    show_dashboard()
elif page == "profile":
    show_profile()
elif page == "lab":
    show_lab()
elif page == "report":
    show_report()
elif page == "about":
    show_about()
