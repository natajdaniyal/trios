import streamlit as st

from user_interface import (
    create_google_user,
    create_user,
    delete_user,
    google_profile,
    recover_user,
    user_profile,
)


st.set_page_config(
    page_title="TRIOS",
    page_icon="assets/trios_logo.png",
    layout="wide",
)


def apply_trios_design():
    """Presentation-only styling; application behavior remains unchanged."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        :root {
            --trios-bg: #050816;
            --trios-bg-2: #0a0f26;
            --trios-panel: rgba(17, 24, 52, .64);
            --trios-panel-strong: rgba(20, 27, 62, .84);
            --trios-border: rgba(183, 210, 255, .14);
            --trios-border-strong: rgba(183, 210, 255, .28);
            --trios-text: #f7f9ff;
            --trios-muted: #aeb9d8;
            --trios-cyan: #73ddff;
            --trios-blue: #6f9cff;
            --trios-violet: #ab83ff;
            --trios-pink: #ef82ff;
            --trios-shadow: 0 24px 80px rgba(0, 0, 0, .34);
        }

        html, body, [class*="css"] {
            font-family: Inter, "Segoe UI", sans-serif;
        }

        [data-testid="stAppViewContainer"] {
            background:
                radial-gradient(circle at 8% 6%, rgba(109, 123, 255, .21), transparent 28%),
                radial-gradient(circle at 90% 12%, rgba(61, 215, 255, .14), transparent 26%),
                radial-gradient(circle at 50% 92%, rgba(182, 92, 255, .12), transparent 30%),
                linear-gradient(155deg, var(--trios-bg) 0%, #090d21 47%, var(--trios-bg-2) 100%);
            color: var(--trios-text);
            min-height: 100vh;
            overflow-x: hidden;
        }

        [data-testid="stAppViewContainer"]::before,
        [data-testid="stAppViewContainer"]::after {
            content: "";
            position: fixed;
            inset: -25%;
            pointer-events: none;
            z-index: 0;
            opacity: .46;
            background-repeat: repeat;
        }

        [data-testid="stAppViewContainer"]::before {
            background-image:
                radial-gradient(circle at 12% 18%, rgba(255,255,255,.92) 0 1px, transparent 1.7px),
                radial-gradient(circle at 63% 14%, rgba(255,255,255,.72) 0 1px, transparent 1.6px),
                radial-gradient(circle at 34% 74%, rgba(255,255,255,.76) 0 1px, transparent 1.5px),
                radial-gradient(circle at 88% 82%, rgba(255,255,255,.74) 0 1px, transparent 1.6px);
            background-size: 260px 260px, 340px 340px, 300px 300px, 390px 390px;
            animation: trios-stars-a 26s linear infinite;
        }

        [data-testid="stAppViewContainer"]::after {
            background-image:
                radial-gradient(circle at 22% 38%, rgba(120,205,255,.6) 0 1px, transparent 1.8px),
                radial-gradient(circle at 78% 25%, rgba(183,132,255,.7) 0 1px, transparent 1.8px),
                radial-gradient(circle at 54% 88%, rgba(255,255,255,.5) 0 1px, transparent 1.7px);
            background-size: 420px 420px, 520px 520px, 460px 460px;
            animation: trios-stars-b 38s linear infinite reverse;
            opacity: .27;
        }

        @keyframes trios-stars-a {
            0% { transform: translate3d(0, 0, 0) scale(1); }
            50% { transform: translate3d(-3.5%, 2.5%, 0) scale(1.03); }
            100% { transform: translate3d(0, 5%, 0) scale(1); }
        }

        @keyframes trios-stars-b {
            0% { transform: translate3d(0, 0, 0) rotate(0deg); }
            50% { transform: translate3d(4%, -3%, 0) rotate(1deg); }
            100% { transform: translate3d(0, 0, 0) rotate(0deg); }
        }

        @keyframes trios-orbit {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        @keyframes trios-float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        @keyframes trios-pulse {
            0%, 100% { opacity: .54; transform: scale(.96); }
            50% { opacity: 1; transform: scale(1.06); }
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        .main .block-container {
            max-width: 1180px;
            padding: 1.15rem 1.25rem 4.8rem;
            position: relative;
            z-index: 1;
        }

        .trios-shell {
            position: relative;
            z-index: 2;
        }

        .trios-nav {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            padding: .72rem .82rem;
            margin-bottom: 2rem;
            border: 1px solid var(--trios-border);
            border-radius: 22px;
            background: rgba(8, 12, 30, .62);
            box-shadow: 0 12px 42px rgba(0,0,0,.19), inset 0 1px 0 rgba(255,255,255,.06);
            backdrop-filter: blur(18px);
        }

        .trios-brand {
            display: flex;
            align-items: center;
            gap: .76rem;
            font-weight: 800;
            font-size: 1.05rem;
            color: #fff;
            letter-spacing: -.025em;
        }

        .trios-brand-mark {
            width: 2.2rem;
            height: 2.2rem;
            display: grid;
            place-items: center;
            border-radius: 11px;
            background: rgba(255,255,255,.07);
            border: 1px solid rgba(255,255,255,.12);
            box-shadow: 0 0 28px rgba(104,177,255,.16);
        }

        .trios-brand-mark img {
            width: 1.52rem;
            height: 1.52rem;
            object-fit: contain;
            border-radius: 7px;
        }

        .trios-nav-label {
            color: var(--trios-muted);
            font-size: .92rem;
            white-space: nowrap;
        }

        .trios-hero {
            position: relative;
            padding: 4.2rem 2rem 3.2rem;
            margin: .4rem 0 2.4rem;
            text-align: center;
            overflow: hidden;
            border: 1px solid rgba(178, 214, 255, .09);
            border-radius: 34px;
            background:
                radial-gradient(circle at 50% 22%, rgba(100, 160, 255, .17), transparent 34%),
                linear-gradient(180deg, rgba(255,255,255,.045), rgba(255,255,255,.02));
            box-shadow: var(--trios-shadow);
            backdrop-filter: blur(12px);
        }

        .trios-kicker {
            display: inline-flex;
            align-items: center;
            gap: .48rem;
            padding: .48rem .8rem;
            border: 1px solid rgba(150, 202, 255, .16);
            border-radius: 999px;
            color: #cfe6ff;
            background: rgba(105, 162, 255, .08);
            font-size: .83rem;
            font-weight: 700;
            letter-spacing: .04em;
            text-transform: uppercase;
            box-shadow: 0 8px 26px rgba(0,0,0,.16);
        }

        .trios-kicker-dot {
            width: .45rem;
            height: .45rem;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--trios-cyan), var(--trios-violet));
            box-shadow: 0 0 18px rgba(107,222,255,.6);
            animation: trios-pulse 2.4s ease-in-out infinite;
        }

        .trios-hero h1 {
            max-width: 920px;
            margin: 1.2rem auto .85rem;
            font-size: clamp(2.85rem, 6.7vw, 5.9rem);
            line-height: .98;
            letter-spacing: -.06em;
            color: #fff;
            font-weight: 800;
            text-shadow: 0 18px 60px rgba(62, 113, 255, .18);
        }

        .trios-gradient-text {
            background: linear-gradient(110deg, #ffffff 15%, #b8ddff 42%, #cba9ff 72%, #f09cff 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .trios-hero-copy {
            max-width: 780px;
            margin: 0 auto;
            color: #aeb9d8;
            font-size: 1.06rem;
            line-height: 1.85;
        }

        .trios-orbit-stage {
            width: min(430px, 88vw);
            aspect-ratio: 1;
            margin: 2.5rem auto 1.2rem;
            position: relative;
            display: grid;
            place-items: center;
            animation: trios-float 7s ease-in-out infinite;
        }

        .trios-orbit-stage::before,
        .trios-orbit-stage::after {
            content: "";
            position: absolute;
            inset: 13%;
            border-radius: 50%;
            border: 1px solid rgba(122, 204, 255, .17);
            transform: rotate(-16deg);
            box-shadow: 0 0 42px rgba(82, 161, 255, .08);
        }

        .trios-orbit-stage::after {
            inset: 4%;
            transform: rotate(31deg);
            border-color: rgba(185, 129, 255, .13);
        }

        .trios-orbit-stage svg {
            width: 100%;
            height: 100%;
            overflow: visible;
        }

        .trios-orbit-ring {
            transform-origin: 220px 220px;
            animation: trios-orbit 22s linear infinite;
        }

        .trios-orbit-ring.reverse {
            animation-direction: reverse;
            animation-duration: 31s;
        }

        .trios-hero-glow {
            position: absolute;
            width: 38%;
            aspect-ratio: 1;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(113, 221, 255, .32), rgba(139, 92, 255, .12) 52%, transparent 70%);
            filter: blur(12px);
            animation: trios-pulse 5.5s ease-in-out infinite;
        }

        .trios-section-head {
            display: flex;
            justify-content: space-between;
            align-items: end;
            gap: 1rem;
            margin: 3.8rem 0 1.1rem;
        }

        .trios-section-head h2 {
            margin: 0;
            font-size: clamp(1.7rem, 3vw, 2.45rem);
            letter-spacing: -.045em;
        }

        .trios-section-head p {
            max-width: 530px;
            margin: 0;
            color: var(--trios-muted);
            line-height: 1.75;
        }

        .trios-card-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0,1fr));
            gap: 1rem;
        }

        .trios-card {
            min-height: 215px;
            padding: 1.35rem;
            border-radius: 24px;
            border: 1px solid var(--trios-border);
            background: linear-gradient(145deg, rgba(255,255,255,.07), rgba(255,255,255,.025));
            box-shadow: 0 14px 38px rgba(0,0,0,.15), inset 0 1px 0 rgba(255,255,255,.045);
            backdrop-filter: blur(16px);
            transition: transform .22s ease, border-color .22s ease, box-shadow .22s ease;
        }

        .trios-card:hover {
            transform: translateY(-5px);
            border-color: var(--trios-border-strong);
            box-shadow: 0 22px 48px rgba(0,0,0,.24), 0 0 32px rgba(105,168,255,.09);
        }

        .trios-icon-box {
            width: 3.15rem;
            height: 3.15rem;
            display: grid;
            place-items: center;
            border-radius: 17px;
            margin-bottom: 1rem;
            background:
                linear-gradient(145deg, rgba(113, 221, 255, .17), rgba(171, 131, 255, .12)),
                rgba(255,255,255,.035);
            border: 1px solid rgba(164, 211, 255, .15);
            box-shadow: inset 0 1px 0 rgba(255,255,255,.08), 0 10px 28px rgba(0,0,0,.16);
        }

        .trios-card h3,
        .trios-action-card h3 {
            color: #fff;
        }

        .trios-card h3 {
            margin: 0 0 .48rem;
            font-size: 1.08rem;
        }

        .trios-card p {
            margin: 0;
            color: var(--trios-muted);
            line-height: 1.75;
            font-size: .92rem;
        }

        .trios-footer {
            margin-top: 4rem;
            padding: 1.4rem 0 .2rem;
            color: #8290b0;
            text-align: center;
            font-size: .84rem;
        }

        .trios-page {
            max-width: 850px;
            margin: 2.6rem auto 0;
        }

        .trios-page-card {
            max-width: 850px;
            margin: 2.6rem auto 0;
            padding: 2rem;
            border-radius: 28px;
            border: 1px solid var(--trios-border);
            background: rgba(11, 16, 37, .62);
            box-shadow: var(--trios-shadow), inset 0 1px 0 rgba(255,255,255,.045);
            backdrop-filter: blur(18px);
        }

        .trios-action-card {
            height: 100%;
            padding: 1.15rem;
            border: 1px solid var(--trios-border);
            border-radius: 22px;
            background: rgba(255,255,255,.045);
            box-shadow: inset 0 1px 0 rgba(255,255,255,.05);
        }

        .trios-action-card h3 {
            margin: .8rem 0 .35rem;
            font-size: 1rem;
        }

        .trios-action-card p {
            margin: 0 0 1rem;
            color: var(--trios-muted);
            font-size: .88rem;
            line-height: 1.65;
        }

        .trios-stat {
            padding: 1rem 1.1rem;
            border-radius: 18px;
            border: 1px solid var(--trios-border);
            background: rgba(255,255,255,.04);
        }

        .trios-stat-value {
            font-size: 1.55rem;
            font-weight: 800;
            color: #fff;
        }

        .trios-stat-label {
            margin-top: .18rem;
            font-size: .77rem;
            color: #8f9cbb;
        }

        .stButton > button {
            min-height: 3.18rem;
            border: 1px solid var(--trios-border);
            border-radius: 16px;
            color: #ffffff;
            font-weight: 700;
            letter-spacing: -.01em;
            background:
                linear-gradient(135deg, rgba(255,255,255,.10), rgba(255,255,255,.045)),
                rgba(9, 14, 39, .72);
            box-shadow: 0 12px 30px rgba(0,0,0,.18), inset 0 1px 0 rgba(255,255,255,.07);
            backdrop-filter: blur(15px);
            transition: transform .18s ease, border-color .18s ease, box-shadow .18s ease, background .18s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            border-color: rgba(157, 211, 255, .5);
            box-shadow: 0 17px 34px rgba(0,0,0,.25), 0 0 28px rgba(113, 184, 255, .17);
            background:
                linear-gradient(135deg, rgba(113, 184, 255, .17), rgba(177, 124, 255, .14)),
                rgba(13, 19, 48, .86);
        }

        .stButton > button:focus {
            box-shadow: 0 0 0 2px rgba(116,183,255,.32), 0 14px 30px rgba(0,0,0,.22);
        }

        [data-testid="stTextInput"] input {
            min-height: 3.08rem;
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,.13);
            color: #fff;
            background: rgba(6,11,31,.48);
            box-shadow: inset 0 1px 0 rgba(255,255,255,.05);
        }

        [data-testid="stTextInput"] input:focus {
            border-color: rgba(126,189,255,.55);
            box-shadow: 0 0 0 1px rgba(126,189,255,.22), 0 0 24px rgba(110,160,255,.13);
        }

        [data-testid="stAlert"] {
            border-radius: 18px;
            border: 1px solid rgba(255,255,255,.1);
            background: rgba(255,255,255,.055);
            backdrop-filter: blur(14px);
        }

        [data-testid="stCheckbox"] label {
            color: var(--trios-muted) !important;
        }

        hr {
            border-color: rgba(255,255,255,.1) !important;
        }

        [data-testid="stCaptionContainer"] {
            color: #95a3c4 !important;
        }

        @media (max-width: 860px) {
            .trios-card-grid {
                grid-template-columns: 1fr;
            }

            .trios-section-head {
                display: block;
            }

            .trios-section-head p {
                margin-top: .65rem;
            }

            .trios-hero {
                padding: 3rem 1rem 2.4rem;
            }

            .trios-nav {
                margin-bottom: 1.2rem;
            }
        }

        @media (max-width: 640px) {
            .main .block-container {
                padding: .65rem .75rem 3rem;
            }

            .trios-nav-label {
                display: none;
            }

            .trios-hero h1 {
                font-size: 2.75rem;
            }

            .trios-hero-copy {
                font-size: .95rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def trios_icon(kind, size=28):
    icons = {
        "orbit": f'''
            <svg width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <ellipse cx="24" cy="24" rx="18" ry="9" transform="rotate(-28 24 24)" stroke="#79DBFF" stroke-width="2.4"/>
                <ellipse cx="24" cy="24" rx="18" ry="9" transform="rotate(32 24 24)" stroke="#AB83FF" stroke-width="2.4" opacity=".9"/>
                <circle cx="24" cy="24" r="4.1" fill="#F4FBFF"/>
                <circle cx="10.5" cy="17" r="2.8" fill="#79DBFF"/>
                <circle cx="37.8" cy="31.4" r="2.8" fill="#E58CFF"/>
            </svg>
        ''',
        "rocket": f'''
            <svg width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M27.8 10.6C33.9 7 39.2 8.1 39.2 8.1S40.3 13.4 36.7 19.5L27.6 28.6C24.3 31.9 18.4 29.6 18.4 29.6S16.1 23.7 19.4 20.4L27.8 10.6Z" stroke="#8CE9FF" stroke-width="2.4"/>
                <circle cx="31.8" cy="16.2" r="3" stroke="#C6A8FF" stroke-width="2.4"/>
                <path d="M18.4 29.6L12.2 35.8" stroke="#8CE9FF" stroke-width="2.4" stroke-linecap="round"/>
                <path d="M17.4 35.8C14.6 37.6 11 37 9.3 35.3C11 33.5 13.4 32 16.2 31.2" stroke="#B98DFF" stroke-width="2.4" stroke-linecap="round"/>
            </svg>
        ''',
        "lab": f'''
            <svg width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M19 8V21.2L10.6 35.7C8.7 39 11.1 43 14.9 43H33.1C36.9 43 39.3 39 37.4 35.7L29 21.2V8" stroke="#82E4FF" stroke-width="2.4" stroke-linecap="round"/>
                <path d="M16 8H32" stroke="#C19DFF" stroke-width="2.4" stroke-linecap="round"/>
                <path d="M14.7 34.2H33.3" stroke="#82E4FF" stroke-width="2.2" stroke-linecap="round"/>
                <circle cx="21" cy="29" r="2.2" fill="#DFA1FF"/>
                <circle cx="27.8" cy="32.3" r="1.6" fill="#7AE7FF"/>
            </svg>
        ''',
        "chart": f'''
            <svg width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 38V10M9 38H40" stroke="#8EDFFF" stroke-width="2.4" stroke-linecap="round"/>
                <path d="M14 31L21.5 24.5L27 28L36.8 15.2" stroke="#C49FFF" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
                <circle cx="14" cy="31" r="2" fill="#8EDFFF"/>
                <circle cx="21.5" cy="24.5" r="2" fill="#9EEAFF"/>
                <circle cx="27" cy="28" r="2" fill="#B79BFF"/>
                <circle cx="36.8" cy="15.2" r="2" fill="#EE9DFF"/>
            </svg>
        ''',
        "profile": f'''
            <svg width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="24" cy="17" r="7" stroke="#8CE5FF" stroke-width="2.4"/>
                <path d="M11 40C12.7 31.9 17.1 28 24 28C30.9 28 35.3 31.9 37 40" stroke="#BD9BFF" stroke-width="2.4" stroke-linecap="round"/>
            </svg>
        ''',
        "plus": f'''
            <svg width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="7" y="7" width="34" height="34" rx="12" stroke="#8CE3FF" stroke-width="2.4"/>
                <path d="M24 15V33M15 24H33" stroke="#C29DFF" stroke-width="2.6" stroke-linecap="round"/>
            </svg>
        ''',
        "refresh": f'''
            <svg width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M36.5 19.5C34.1 14.6 29.2 11 23.4 11C15.4 11 9 17.4 9 25.4C9 33.4 15.4 39.8 23.4 39.8C29.6 39.8 34.8 35.9 36.7 30.4" stroke="#84E6FF" stroke-width="2.6" stroke-linecap="round"/>
                <path d="M35.7 12.8V20.5H28" stroke="#C4A0FF" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        ''',
        "lock": f'''
            <svg width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="11" y="21" width="26" height="19" rx="5" stroke="#86E7FF" stroke-width="2.4"/>
                <path d="M16 21V16.5C16 12 19.6 9 24 9C28.4 9 32 12 32 16.5V21" stroke="#C09EFF" stroke-width="2.4"/>
                <circle cx="24" cy="30.5" r="2.2" fill="#F2B0FF"/>
            </svg>
        ''',
        "trash": f'''
            <svg width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M14 16L15.5 38.5H32.5L34 16" stroke="#8ADFFF" stroke-width="2.4" stroke-linejoin="round"/>
                <path d="M11 16H37M19 16V11H29V16" stroke="#C29CFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M20 21.5V32.5M28 21.5V32.5" stroke="#F0A6FF" stroke-width="2.1" stroke-linecap="round"/>
            </svg>
        ''',
        "info": f'''
            <svg width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="24" cy="24" r="16" stroke="#8CE2FF" stroke-width="2.4"/>
                <path d="M24 21V33" stroke="#C49FFF" stroke-width="2.6" stroke-linecap="round"/>
                <circle cx="24" cy="15.5" r="1.8" fill="#F0A4FF"/>
            </svg>
        ''',
        "google": f'''
            <svg width="{size}" height="{size}" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
                <path fill="#4285F4" d="M44.5 24.5c0-1.6-.1-2.8-.4-4.1H24v7.7h11.8c-.2 1.9-1.9 4.8-5.2 6.8l-.1.3 6.5 5c4.1-3.8 6.5-9.4 6.5-15.7z"/>
                <path fill="#34A853" d="M24 45c5.8 0 10.7-1.9 14.3-5.1l-6.8-5.3c-1.8 1.2-4.3 2.1-7.5 2.1-5.7 0-10.6-3.8-12.3-9.1l-.3.1-6.9 5.3-.1.3C7.9 40.3 15.3 45 24 45z"/>
                <path fill="#FBBC05" d="M11.7 27.6A12.9 12.9 0 0 1 11 24c0-1.2.2-2.4.5-3.5l-.1-.2-7-5.4-.2.1A21.2 21.2 0 0 0 3 24c0 3.5.8 6.8 2.3 9.8l6.4-6.2z"/>
                <path fill="#EA4335" d="M24 11.4c4.1 0 7 1.8 8.6 3.2l6.2-6C34.7 5.2 29.8 3 24 3 15.3 3 7.9 7.7 4.1 14.6l7.4 5.7C13.4 15.1 18.3 11.4 24 11.4z"/>
            </svg>
        ''',
    }
    return icons.get(kind, icons["orbit"])


def render_icon(kind, size=30, box=True):
    class_name = "trios-icon-box" if box else "trios-inline-icon"
    st.markdown(
        f'<div class="{class_name}" aria-hidden="true">{trios_icon(kind, size)}</div>',
        unsafe_allow_html=True,
    )


def show_logo():
    st.image("assets/trios_logo.png", width=150)


def show_public_nav():
    st.markdown('<div class="trios-shell">', unsafe_allow_html=True)
    left, mid, right = st.columns([2.2, 3.2, 2.2], vertical_alignment="center")

    with left:
        st.markdown(
            """
            <div class="trios-brand">
                <div class="trios-brand-mark">
                    <img src="assets/trios_logo.png" alt="TRIOS">
                </div>
                <span>TRIOS</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with mid:
        st.markdown(
            '<div class="trios-nav-label" style="text-align:center;">Explore the three-body universe</div>',
            unsafe_allow_html=True,
        )

    with right:
        c1, c2 = st.columns(2, gap="small")
        with c1:
            if st.button("ورود", use_container_width=True, key="nav_login"):
                st.session_state.page = "entry"
                st.rerun()
        with c2:
            if st.button("ساخت حساب", use_container_width=True, key="nav_signup"):
                st.session_state.page = "register"
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


def show_hero_orbit():
    st.markdown(
        """
        <div class="trios-orbit-stage" aria-hidden="true">
            <div class="trios-hero-glow"></div>
            <svg viewBox="0 0 440 440" fill="none" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <radialGradient id="triosCore" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(220 220) rotate(90) scale(74)">
                        <stop stop-color="#F9FDFF"/>
                        <stop offset=".22" stop-color="#A9F1FF"/>
                        <stop offset=".65" stop-color="#8B8CFF"/>
                        <stop offset="1" stop-color="#8B8CFF" stop-opacity="0"/>
                    </radialGradient>
                    <filter id="triosBlur"><feGaussianBlur stdDeviation="12"/></filter>
                </defs>
                <g opacity=".8">
                    <ellipse cx="220" cy="220" rx="160" ry="74" stroke="#69DFFF" stroke-opacity=".16" stroke-width="1.4"/>
                    <ellipse cx="220" cy="220" rx="160" ry="74" transform="rotate(62 220 220)" stroke="#B189FF" stroke-opacity=".13" stroke-width="1.4"/>
                    <ellipse cx="220" cy="220" rx="160" ry="74" transform="rotate(-62 220 220)" stroke="#7E9CFF" stroke-opacity=".12" stroke-width="1.4"/>
                </g>
                <g class="trios-orbit-ring">
                    <circle cx="220" cy="64" r="7" fill="#83E7FF" />
                    <circle cx="220" cy="64" r="18" fill="#83E7FF" fill-opacity=".07" />
                </g>
                <g class="trios-orbit-ring reverse">
                    <circle cx="220" cy="70" r="6" fill="#D19BFF" />
                    <circle cx="220" cy="70" r="15" fill="#D19BFF" fill-opacity=".07" />
                </g>
                <g class="trios-orbit-ring" style="animation-duration: 17s;">
                    <circle cx="220" cy="58" r="5.2" fill="#FFFFFF"/>
                </g>
                <circle cx="220" cy="220" r="64" fill="#75E1FF" fill-opacity=".07" filter="url(#triosBlur)"/>
                <circle cx="220" cy="220" r="54" fill="url(#triosCore)"/>
                <circle cx="220" cy="220" r="12" fill="#F7FCFF"/>
            </svg>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_action_card(icon, title, description, button_label, callback_key):
    st.markdown('<div class="trios-action-card">', unsafe_allow_html=True)
    render_icon(icon, size=28)
    st.markdown(f"<h3>{title}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p>{description}</p>", unsafe_allow_html=True)
    clicked = st.button(button_label, use_container_width=True, key=callback_key)
    st.markdown("</div>", unsafe_allow_html=True)
    return clicked


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
            f"خوش برگشتی، {profile['username']}!",
        )

    if flow == "recover":
        st.session_state.google_recovery_error = True
        st.session_state.page = "recover_google"
        return

    st.session_state.google_identity = identity
    st.session_state.page = "google_profile"


def show_home():
    show_public_nav()

    st.markdown(
        """
        <section class="trios-hero">
            <div class="trios-kicker">
                <span class="trios-kicker-dot"></span>
                A new way to explore gravity
            </div>
            <h1>
                Discover the
                <span class="trios-gradient-text">three-body universe.</span>
            </h1>
            <p class="trios-hero-copy">
                TRIOS turns the three-body problem into a beautiful scientific playground:
                define physical conditions, run precise simulations, observe what happens,
                and learn from the motion of gravity.
            </p>
        """,
        unsafe_allow_html=True,
    )

    show_hero_orbit()

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        if st.button("شروع با TRIOS", use_container_width=True, key="home_start"):
            st.session_state.page = "entry"
            st.rerun()
    with c2:
        if st.button("TRIOS چیست؟", use_container_width=True, key="home_about"):
            st.session_state.page = "about"
            st.rerun()

    st.markdown(
        """
            <div class="trios-section-head">
                <div>
                    <h2>Science, without the clutter.</h2>
                </div>
                <p>
                    Built around a clean separation between physics, simulation,
                    experiments and the interface you use to explore them.
                </p>
            </div>

            <div class="trios-card-grid">
                <div class="trios-card">
                    <div class="trios-icon-box">__ORBIT__</div>
                    <h3>Explore motion</h3>
                    <p>Watch gravitational systems evolve from carefully defined physical conditions.</p>
                </div>
                <div class="trios-card">
                    <div class="trios-icon-box">__LAB__</div>
                    <h3>Run experiments</h3>
                    <p>Turn an idea into a repeatable experiment without mixing the science with the interface.</p>
                </div>
                <div class="trios-card">
                    <div class="trios-icon-box">__CHART__</div>
                    <h3>Study results</h3>
                    <p>Observe measurements, compare behavior and build intuition from the simulation.</p>
                </div>
            </div>

            <div class="trios-footer">
                TRIOS · gravitational three-body simulation laboratory
            </div>
        """.replace("__ORBIT__", trios_icon("orbit", 34))
          .replace("__LAB__", trios_icon("lab", 34))
          .replace("__CHART__", trios_icon("chart", 34)),
        unsafe_allow_html=True,
    )

    st.markdown("</section>", unsafe_allow_html=True)


def show_entry():
    st.markdown('<div class="trios-page">', unsafe_allow_html=True)
    render_icon("orbit", size=32)
    st.markdown(
        '<h1 style="text-align:center;margin-bottom:.35rem;">ورود به TRIOS</h1>'
        '<p style="text-align:center;color:#aeb9d8;">روش ورودت را انتخاب کن.</p>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        render_icon("google", size=30)
        st.subheader("Google")
        st.caption("ورود سریع با حساب Google")
        if st.button("ادامه با Google", use_container_width=True, key="google_login_button"):
            start_google_login("login")

    with c2:
        render_icon("plus", size=30)
        st.subheader("حساب TRIOS")
        st.caption("ساخت حساب با نام کاربری و رمز عبور")
        if st.button("ساخت حساب با TRIOS", use_container_width=True, key="register_button"):
            st.session_state.page = "register"
            st.rerun()

    st.divider()

    c3, c4 = st.columns(2, gap="medium")
    with c3:
        render_icon("refresh", size=28)
        st.subheader("بازیابی")
        st.caption("ورود دوباره به حساب قبلی")
        if st.button("بازیابی حساب", use_container_width=True, key="recover_button"):
            st.session_state.page = "recover"
            st.rerun()
    with c4:
        render_icon("info", size=28)
        st.subheader("درباره TRIOS")
        st.caption("TRIOS چه کاری انجام می‌دهد؟")
        if st.button("TRIOS چیست؟", use_container_width=True, key="entry_about_button"):
            st.session_state.page = "about"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("بازگشت", use_container_width=True, key="entry_back"):
        st.session_state.page = "home"
        st.rerun()


def show_recover():
    st.markdown('<div class="trios-page">', unsafe_allow_html=True)
    render_icon("refresh", size=32)
    st.markdown(
        '<h1 style="text-align:center;margin-bottom:.35rem;">بازیابی حساب</h1>'
        '<p style="text-align:center;color:#aeb9d8;">روش ورود قبلی خودت را انتخاب کن.</p>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        render_icon("google", size=30)
        st.subheader("Google")
        st.caption("بازیابی با همان حساب Google")
        if st.button("بازیابی با Google", use_container_width=True, key="google_recover_button"):
            start_google_login("recover")
    with c2:
        render_icon("lock", size=30)
        st.subheader("حساب TRIOS")
        st.caption("ورود با اطلاعات حساب TRIOS")
        if st.button("بازیابی با حساب TRIOS", use_container_width=True):
            st.session_state.page = "recover_trios"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("بازگشت", use_container_width=True, key="recover_back"):
        st.session_state.page = "entry"
        st.rerun()


def show_recover_trios():
    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("lock", size=30)
    st.header("ورود با حساب TRIOS")
    st.info("نام کاربری و رمز عبور همان حساب TRIOS را وارد کن.")

    username = st.text_input("نام کاربری", key="recover_username")
    password = st.text_input("رمز عبور", type="password", key="recover_password")

    if st.button("ورود به حساب", use_container_width=True):
        try:
            data = recover_user(username, password)
        except ValueError as exc:
            st.error(str(exc))
        else:
            set_logged_in_user(data, f"خوش برگشتی، {data['username']}!")

    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("بازگشت", use_container_width=True, key="recover_trios_back"):
        st.session_state.page = "recover"
        st.rerun()


def show_recover_google():
    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("google", size=30)
    st.header("بازیابی با Google")
    st.error(
        "این حساب Google هنوز به یک حساب TRIOS متصل نشده است. "
        "برای جلوگیری از ساخت حساب تکراری، ابتدا با روش قبلی حسابت وارد شو."
    )

    if st.button("بازگشت به بازیابی", use_container_width=True):
        st.session_state.pop("google_recovery_error", None)
        st.session_state.page = "recover"
        st.rerun()

    if st.button("خروج از Google", use_container_width=True):
        st.logout()

    st.markdown("</div>", unsafe_allow_html=True)


def show_register():
    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("plus", size=30)
    st.header("ساخت حساب TRIOS")

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
                set_logged_in_user(data, f"خوش اومدی، {data['username']}!")

    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("بازگشت", use_container_width=True, key="register_back"):
        st.session_state.page = "entry"
        st.rerun()


def show_google_profile():
    identity = st.session_state.get("google_identity", google_identity())

    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("google", size=30)
    st.header("ساخت پروفایل TRIOS")
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
            set_logged_in_user(data, f"خوش اومدی، {data['username']}!")

    if st.button("خروج از Google", use_container_width=True):
        st.logout()

    st.markdown("</div>", unsafe_allow_html=True)


def show_dashboard():
    username = st.session_state.user
    data = user_profile(username)

    st.markdown(
        f"""
        <div class="trios-hero" style="padding:2.4rem 1.5rem 1.5rem;">
            <div class="trios-kicker">
                <span class="trios-kicker-dot"></span>
                TRIOS workspace
            </div>
            <h1 style="font-size:clamp(2rem,4.8vw,4rem);">
                Welcome back,
                <span class="trios-gradient-text">{username}</span>
            </h1>
            <p class="trios-hero-copy">یک فضای آرام برای آزمایش، مشاهده و فکر کردن درباره‌ی حرکت.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    s1, s2, s3, s4 = st.columns(4, gap="small")
    with s1:
        st.markdown(f'<div class="trios-stat"><div class="trios-stat-value">{data["level"]}</div><div class="trios-stat-label">سطح</div></div>', unsafe_allow_html=True)
    with s2:
        st.markdown(f'<div class="trios-stat"><div class="trios-stat-value">{data["total_attempts"]}</div><div class="trios-stat-label">تلاش‌ها</div></div>', unsafe_allow_html=True)
    with s3:
        st.markdown(f'<div class="trios-stat"><div class="trios-stat-value">{data["correct_answers"]}</div><div class="trios-stat-label">پاسخ درست</div></div>', unsafe_allow_html=True)
    with s4:
        st.markdown(f'<div class="trios-stat"><div class="trios-stat-value">{data["accuracy"]}%</div><div class="trios-stat-label">دقت</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="trios-section-head"><div><h2>مسیر تو در TRIOS</h2></div><p>از اینجا می‌توانی آزمایش‌ها، گزارش‌ها و پروفایلت را مدیریت کنی.</p></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        if render_action_card("rocket", "شروع آزمایش", "وارد آزمایشگاه شو و برای اجرای یک آزمایش آماده شو.", "شروع آزمایش", "dashboard_lab"):
            st.session_state.page = "lab"
            st.rerun()
    with c2:
        if render_action_card("chart", "گزارش من", "نتایج و عملکرد ثبت‌شده‌ی این حساب را ببین.", "مشاهده گزارش", "dashboard_report"):
            st.session_state.page = "report"
            st.rerun()
    with c3:
        if render_action_card("profile", "پروفایل", "اطلاعات حساب و تنظیمات امنیتی خودت را مدیریت کن.", "باز کردن پروفایل", "dashboard_profile"):
            st.session_state.page = "profile"
            st.rerun()


def show_profile():
    username = st.session_state.user
    data = user_profile(username)

    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("profile", size=32)
    st.header("پروفایل")
    st.subheader("اطلاعات شخصی")
    st.write(f"**نام کاربری:** {data['username']}")
    if data.get("auth_method") == "google":
        st.caption("روش ورود: Google")

    st.divider()
    st.subheader("مدیریت حساب")

    if st.button("خروج از این دستگاه", use_container_width=True):
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

    if st.button("حذف دائمی حساب", use_container_width=True):
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

    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("بازگشت به داشبورد", use_container_width=True):
        st.session_state.page = "dashboard"
        st.rerun()


def show_lab():
    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("lab", size=32)
    st.header("آزمایشگاه من")
    st.info(
        "زیرساخت اجرای آزمایش‌های TRIOS آماده است. "
        "محتوای آزمایش‌های آموزشی هنوز جداگانه تعریف نشده و فعلاً در این بخش ساخته نمی‌شود."
    )
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("بازگشت", use_container_width=True):
        st.session_state.page = "dashboard"
        st.rerun()


def show_report():
    data = user_profile(st.session_state.user)

    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("chart", size=32)
    st.header("گزارش من")

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

    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("بازگشت", use_container_width=True):
        st.session_state.page = "dashboard"
        st.rerun()


def show_about():
    show_public_nav()
    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("info", size=32)
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
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("بازگشت", use_container_width=True, key="about_back"):
        st.session_state.page = (
            "dashboard" if "user" in st.session_state else "home"
        )
        st.rerun()


apply_trios_design()

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
