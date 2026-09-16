import streamlit as st

from user_interface import (
    authenticate_user,
    create_user,
    logout_user,
    recover_user,
    user_profile,
)


st.set_page_config(page_title="TRIOS", page_icon="🌌", layout="wide")


def show_home():
    st.title("🌌 TRIOS")
    st.caption("آزمایشگاه شبیه‌سازی و بررسی مسئله سه‌جسمی")
    st.write("به آزمایشگاه TRIOS خوش آمدی.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 ورود به TRIOS", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()
    with col2:
        if st.button("🔄 بازیابی حساب", use_container_width=True):
            st.session_state.page = "recover"
            st.rerun()

    if st.button("🌌 TRIOS چیست؟", use_container_width=True):
        st.session_state.page = "about"
        st.rerun()


def show_login():
    st.header("🚀 ورود به TRIOS")

    username = st.text_input("نام کاربری", key="login_username")
    password = st.text_input("رمز عبور", type="password", key="login_password")

    if st.button("ورود", use_container_width=True):
        try:
            data = authenticate_user(username, password)
        except ValueError as exc:
            st.error(str(exc))
        else:
            st.session_state.user = data["username"]
            st.session_state.page = "dashboard"
            st.rerun()

    if st.button("🔄 بازیابی حساب موجود", use_container_width=True):
        st.session_state.page = "recover"
        st.rerun()

    if st.button("ساخت حساب جدید", use_container_width=True):
        st.session_state.page = "register"
        st.rerun()

    if st.button("⬅️ بازگشت", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


def show_recover():
    st.header("🔄 بازیابی حساب")
    st.info("حساب حذف نمی‌شود؛ با نام کاربری و رمز عبور، حساب موجودت را روی این دستگاه بازیابی می‌کنی.")

    username = st.text_input("نام کاربری", key="recover_username")
    password = st.text_input("رمز عبور", type="password", key="recover_password")

    if st.button("بازیابی حساب", use_container_width=True):
        try:
            data = recover_user(username, password)
        except ValueError as exc:
            st.error(str(exc))
        else:
            st.session_state.user = data["username"]
            st.session_state.page = "dashboard"
            st.rerun()

    if st.button("⬅️ بازگشت", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


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
                st.session_state.user = data["username"]
                st.session_state.page = "dashboard"
                st.rerun()

    if st.button("⬅️ بازگشت به ورود", use_container_width=True):
        st.session_state.page = "login"
        st.rerun()


def show_dashboard():
    username = st.session_state.user
    data = user_profile(username)

    st.title(f"🌌 خوش آمدی، {username}!")
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
        if st.button("🌌 درباره TRIOS", use_container_width=True):
            st.session_state.page = "about"
            st.rerun()

    st.divider()
    st.subheader("حساب کاربری")
    st.write(f"**سطح:** {data['level']}")
    st.write(f"**تعداد تلاش‌ها:** {data['total_attempts']}")
    st.write(f"**دقت:** {data['accuracy']}%")

    if st.button("🚪 خروج از این دستگاه", use_container_width=True):
        logout_user(username)
        st.session_state.pop("user", None)
        st.session_state.page = "home"
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
    st.write(f"**سطح:** {data['level']}")
    st.write(f"**تعداد تلاش‌ها:** {data['total_attempts']}")
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
    st.header("🌌 TRIOS چیست؟")
    st.write(
        "TRIOS یک سامانه برای شبیه‌سازی و مطالعه سیستم‌های فیزیکی چندجسمی "
        "با تمرکز بر مسئله سه‌جسمی است."
    )
    st.write(
        "هسته فیزیک، شبیه‌سازی، پیکربندی فیزیکی، قوانین انتخاب، "
        "اجرای آزمایش و اعتبارسنجی علمی از رابط کاربری جدا نگه داشته شده‌اند."
    )

    if st.button("⬅️ بازگشت", use_container_width=True):
        st.session_state.page = (
            "dashboard" if "user" in st.session_state else "home"
        )
        st.rerun()


if "page" not in st.session_state:
    st.session_state.page = "home"

if "user" in st.session_state:
    if st.session_state.page in {"home", "login", "register", "recover"}:
        st.session_state.page = "dashboard"
else:
    if st.session_state.page in {"dashboard", "lab", "report"}:
        st.session_state.page = "home"


page = st.session_state.page

if page == "home":
    show_home()
elif page == "login":
    show_login()
elif page == "recover":
    show_recover()
elif page == "register":
    show_register()
elif page == "dashboard":
    show_dashboard()
elif page == "lab":
    show_lab()
elif page == "report":
    show_report()
elif page == "about":
    show_about()
