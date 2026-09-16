import streamlit as st

from user_interface import (
    create_user,
    delete_user,
    logout_user,
    recover_user,
    restore_user_session,
    user_profile,
)


st.set_page_config(page_title="TRIOS", page_icon="🪐", layout="wide")


def show_logo():
    st.markdown(
        """
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
            <div style="font-size:42px;line-height:1;">◉</div>
            <div>
                <div style="font-size:34px;font-weight:700;line-height:1.1;">TRIOS</div>
                <div style="font-size:14px;opacity:.7;">Three-Body Research & Interactive Orbit Simulation</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


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
    st.write("حساب خودت را بازیابی کن یا یک حساب جدید بساز.")

    if st.button("🔄 بازیابی حساب موجود", use_container_width=True):
        st.session_state.page = "recover"
        st.rerun()

    if st.button("✨ ساخت حساب جدید", use_container_width=True):
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
            st.session_state.welcome_message = f"خوش برگشتی، {data['username']}! 👋"
            st.session_state.page = "dashboard"
            st.rerun()

    if st.button("⬅️ بازگشت", use_container_width=True):
        st.session_state.page = "entry"
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
                st.session_state.welcome_message = f"خوش اومدی، {data['username']}! 🎉"
                st.session_state.page = "dashboard"
                st.rerun()

    if st.button("⬅️ بازگشت", use_container_width=True):
        st.session_state.page = "entry"
        st.rerun()


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

    st.divider()
    st.subheader("مدیریت حساب")

    if st.button("🚪 خروج از این دستگاه", use_container_width=True):
        logout_user(username)
        st.session_state.pop("user", None)
        st.session_state.pop("welcome_message", None)
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

if "user" not in st.session_state:
    restored = restore_user_session()
    if restored:
        st.session_state.user = restored["username"]
        st.session_state.page = "dashboard"

if "user" in st.session_state:
    if st.session_state.page in {"home", "entry", "register", "recover"}:
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
elif page == "register":
    show_register()
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
