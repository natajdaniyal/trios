import streamlit as st

from user_interface import user_profile


st.set_page_config(page_title="TRIOS", page_icon="🌌", layout="wide")

st.title("🌌 TRIOS")
st.caption("آزمایشگاه شبیه‌سازی و بررسی مسئله سه‌جسمی")

if "page" not in st.session_state:
    st.session_state.page = "home"

st.subheader("منوی TRIOS")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚀 شروع", use_container_width=True):
        st.session_state.page = "start"

with col2:
    if st.button("🔬 آزمایشگاه من", use_container_width=True):
        st.session_state.page = "lab"

with col3:
    if st.button("🌌 TRIOS چیست؟", use_container_width=True):
        st.session_state.page = "about"

st.divider()

if st.session_state.page == "about":
    st.header("🌌 TRIOS چیست؟")
    st.write(
        "TRIOS یک سامانه برای شبیه‌سازی و مطالعه سیستم‌های فیزیکی چندجسمی "
        "با تمرکز بر مسئله سه‌جسمی است."
    )

elif st.session_state.page == "lab":
    st.header("🔬 آزمایشگاه من")
    username = st.text_input("نام کاربری")

    if st.button("نمایش پروفایل", use_container_width=True):
        if not username.strip():
            st.warning("نام کاربری را وارد کن.")
        else:
            try:
                data = user_profile(username.strip())
            except ValueError as exc:
                st.error(str(exc))
            else:
                st.write(f"**کاوشگر:** {data['username']}")
                st.write(f"**سطح:** {data['level']}")
                st.write(f"**تعداد تلاش‌ها:** {data['total_attempts']}")
                st.write(f"**دقت:** {data['accuracy']}%")

elif st.session_state.page == "start":
    st.header("🚀 آماده‌ای؟")
    st.info(
        "رابط وب TRIOS آماده شده است. اجرای آزمایش‌ها بعد از اتصال رابط "
        "کاربری به زیرساخت آزمایش‌ها انجام می‌شود."
    )

else:
    st.header("خوش آمدی 🌌")
    st.write("از دکمه‌های بالا برای ورود به بخش موردنظر استفاده کن.")
