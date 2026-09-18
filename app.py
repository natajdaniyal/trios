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


apply_trios_design()


def apply_trios_design():
    """Presentation-only styling; does not change TRIOS behavior."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        :root {
            --trios-bg-1: #070b24;
            --trios-bg-2: #13113b;
            --trios-bg-3: #0b1738;
            --trios-text: #f7f9ff;
            --trios-muted: #b9c5e6;
            --trios-card: rgba(255, 255, 255, 0.075);
            --trios-card-border: rgba(255, 255, 255, 0.14);
            --trios-glow: rgba(113, 173, 255, 0.34);
            --trios-purple: rgba(164, 114, 255, 0.22);
        }

        html, body, [class*="css"] {
            font-family: Inter, "Segoe UI", sans-serif;
        }

        [data-testid="stAppViewContainer"] {
            background:
                radial-gradient(circle at 12% 8%, var(--trios-purple) 0, transparent 30%),
                radial-gradient(circle at 88% 15%, rgba(0, 214, 255, 0.15) 0, transparent 26%),
                radial-gradient(circle at 52% 92%, rgba(85, 89, 255, 0.13) 0, transparent 32%),
                linear-gradient(155deg, var(--trios-bg-1) 0%, var(--trios-bg-2) 48%, var(--trios-bg-3) 100%);
            color: var(--trios-text);
            min-height: 100vh;
            overflow-x: hidden;
        }

        [data-testid="stAppViewContainer"]::before {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            opacity: 0.43;
            background-image:
                radial-gradient(circle at 12% 22%, rgba(255,255,255,.9) 0 1px, transparent 1.7px),
                radial-gradient(circle at 74% 17%, rgba(255,255,255,.75) 0 1px, transparent 1.6px),
                radial-gradient(circle at 42% 78%, rgba(255,255,255,.65) 0 1px, transparent 1.5px),
                radial-gradient(circle at 91% 68%, rgba(255,255,255,.8) 0 1px, transparent 1.6px);
            background-size: 230px 230px, 310px 310px, 270px 270px, 360px 360px;
            z-index: 0;
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        .main .block-container {
            max-width: 1100px;
            padding: 3.2rem 2rem 4.5rem;
            position: relative;
            z-index: 1;
        }

        [data-testid="stImage"] {
            display: flex;
            justify-content: center;
            margin: 0 auto 1.25rem;
        }

        [data-testid="stImage"] img {
            border-radius: 30px;
            filter: drop-shadow(0 18px 42px rgba(0, 0, 0, .34));
        }

        h1, h2, h3 {
            color: var(--trios-text) !important;
            letter-spacing: -0.035em;
            font-weight: 800;
            text-shadow: 0 0 24px rgba(132, 170, 255, .14);
        }

        p, label, [data-testid="stCaptionContainer"] {
            color: var(--trios-muted) !important;
        }

        [data-testid="stVerticalBlock"] > div:has(> .stButton) {
            transition: transform .2s ease;
        }

        .stButton > button {
            width: 100%;
            min-height: 3.35rem;
            border: 1px solid var(--trios-card-border);
            border-radius: 18px;
            color: #ffffff;
            font-weight: 700;
            letter-spacing: -0.01em;
            background:
                linear-gradient(135deg, rgba(255,255,255,.11), rgba(255,255,255,.045)),
                rgba(9, 14, 39, .72);
            box-shadow:
                0 12px 30px rgba(0, 0, 0, .2),
                inset 0 1px 0 rgba(255,255,255,.08);
            backdrop-filter: blur(16px);
            transition: transform .18s ease, border-color .18s ease, box-shadow .18s ease, background .18s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            border-color: rgba(153, 208, 255, .48);
            box-shadow:
                0 18px 34px rgba(0, 0, 0, .28),
                0 0 28px var(--trios-glow),
                inset 0 1px 0 rgba(255,255,255,.11);
            background:
                linear-gradient(135deg, rgba(117, 179, 255, .18), rgba(174, 119, 255, .13)),
                rgba(14, 20, 51, .86);
        }

        .stButton > button:focus {
            box-shadow:
                0 0 0 2px rgba(116, 183, 255, .35),
                0 14px 30px rgba(0, 0, 0, .22);
        }

        [data-testid="stTextInput"] input {
            min-height: 3.1rem;
            border-radius: 16px;
            border: 1px solid rgba(255,255,255,.13);
            color: #fff;
            background: rgba(6, 11, 31, .48);
            box-shadow: inset 0 1px 0 rgba(255,255,255,.05);
        }

        [data-testid="stTextInput"] input:focus {
            border-color: rgba(126, 189, 255, .55);
            box-shadow: 0 0 0 1px rgba(126, 189, 255, .22), 0 0 24px rgba(110, 160, 255, .13);
        }

        [data-testid="stAlert"] {
            border-radius: 18px;
            border: 1px solid rgba(255,255,255,.1);
            background: rgba(255,255,255,.055);
            backdrop-filter: blur(14px);
        }

        [data-testid="stExpander"] {
            border-radius: 18px;
            border: 1px solid rgba(255,255,255,.11);
            background: rgba(255,255,255,.045);
        }

        hr {
            border-color: rgba(255,255,255,.1) !important;
        }

        .trios-google-row {
            display: flex;
            align-items: stretch;
            gap: .7rem;
            margin: .2rem 0 .35rem;
        }

        .trios-google-icon {
            width: 3.35rem;
            min-width: 3.35rem;
            height: 3.35rem;
            border-radius: 18px;
            display: grid;
            place-items: center;
            border: 1px solid rgba(255,255,255,.14);
            background: rgba(255,255,255,.08);
            box-shadow:
                0 12px 28px rgba(0,0,0,.2),
                inset 0 1px 0 rgba(255,255,255,.1);
            backdrop-filter: blur(14px);
        }

        .trios-google-icon svg {
            width: 1.55rem;
            height: 1.55rem;
            display: block;
        }

        @media (max-width: 700px) {
            .main .block-container {
                padding: 2.25rem 1rem 3.25rem;
            }

            h1 {
                font-size: 2rem;
            }

            h2 {
                font-size: 1.55rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def trios_google_icon():
    st.markdown(
        """
        <div class="trios-google-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path fill="#EA4335" d="M12 10.2v3.9h5.45c-.24 1.26-.96 2.33-2.03 3.05l3.27 2.54c1.91-1.76 3.01-4.35 3.01-7.45 0-.71-.06-1.39-.18-2.04H12z"/>
                <path fill="#4285F4" d="M12 21c2.73 0 5.02-.9 6.69-2.44l-3.27-2.54c-.91.61-2.07.98-3.42.98-2.63 0-4.86-1.78-5.66-4.17l-3.37 2.6C4.64 18.71 8.01 21 12 21z"/>
                <path fill="#FBBC05" d="M6.34 12.83A5.99 5.99 0 0 1 6 11c0-.64.11-1.26.34-1.83l-3.37-2.6A10.13 10.13 0 0 0 2 11c0 1.63.39 3.17 1.08 4.43l3.26-2.6z"/>
                <path fill="#34A853" d="M6.34 9.17C7.13 6.78 9.37 5 12 5c1.55 0 2.94.53 4.04 1.57l3.01-3.01C17.01 1.89 14.72 1 12 1 8.01 1 4.64 3.29 2.97 6.57l3.37 2.6z"/>
            </svg>
        </div>
        """,
        unsafe_allow_html=True,
    )




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

    google_col_icon, google_col_button = st.columns([1, 8], vertical_alignment="center")
    with google_col_icon:
        trios_google_icon()
    with google_col_button:
        if st.button("ادامه با Google", use_container_width=True, key="google_login_button"):
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

    google_col_icon, google_col_button = st.columns([1, 8], vertical_alignment="center")
    with google_col_icon:
        trios_google_icon()
    with google_col_button:
        if st.button("بازیابی با Google", use_container_width=True, key="google_recover_button"):
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
