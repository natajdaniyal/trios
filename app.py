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



LANGUAGES = {
    "fa": "فارسی",
    "en": "English",
    "ar": "العربية",
    "zh": "简体中文",
    "es": "Español",
    "fr": "Français",
    "de": "Deutsch",
    "ja": "日本語",
}

TRANSLATIONS = {
    "fa": {
        "nav_tagline":"آزمایشگاه شبیه‌سازی مسئله‌ی سه‌جسمی","nav_login":"ورود","nav_signup":"ساخت حساب","nav_language":"زبان",
        "hero_kicker":"راهی تازه برای کشف گرانش","hero_title_1":"جهانِ","hero_title_2":"سه‌جسمی را کشف کن.","hero_copy":"TRIOS مسئله‌ی سه‌جسمی را به یک آزمایشگاه علمی زیبا تبدیل می‌کند؛ شرایط فیزیکی را تعریف کن، شبیه‌سازی را اجرا کن و حرکت گرانش را ببین.",
        "home_start":"شروع با TRIOS","about":"TRIOS چیست؟","section_title":"علم، بدون شلوغی.","section_copy":"فیزیک، شبیه‌سازی، آزمایش و رابط کاربری به‌صورت تمیز از هم جدا شده‌اند.",
        "feature_motion":"حرکت را کشف کن","feature_motion_copy":"تکامل سیستم‌های گرانشی را از شرایط اولیه‌ی دقیق مشاهده کن.","feature_lab":"آزمایش انجام بده","feature_lab_copy":"ایده‌ات را به یک آزمایش تکرارپذیر تبدیل کن، بدون اینکه علم با رابط کاربری قاطی شود.","feature_results":"نتایج را مطالعه کن","feature_results_copy":"اندازه‌گیری‌ها را ببین، رفتارها را مقایسه کن و از شبیه‌سازی شهود فیزیکی بساز.","footer":"TRIOS · آزمایشگاه شبیه‌سازی سه‌جسمی",
        "login_title":"ورود به TRIOS","choose_login":"روش ورودت را انتخاب کن.","google_login":"ادامه با Google","google_fast":"ورود سریع با حساب Google","native_account":"حساب TRIOS","native_fast":"ساخت حساب با نام کاربری و رمز عبور","create_native":"ساخت حساب با TRIOS","recover":"بازیابی حساب","recover_copy":"ورود دوباره به حساب قبلی","about_short":"TRIOS چه کاری انجام می‌دهد؟","back":"بازگشت",
        "recover_title":"بازیابی حساب","recover_choose":"روش ورود قبلی خودت را انتخاب کن.","recover_google":"بازیابی با Google","recover_google_copy":"بازیابی با همان حساب Google","recover_native":"بازیابی با حساب TRIOS","recover_native_copy":"ورود با اطلاعات حساب TRIOS","recover_native_title":"ورود با حساب TRIOS","recover_notice":"نام کاربری و رمز عبور همان حساب TRIOS را وارد کن.",
        "username":"نام کاربری","password":"رمز عبور","login_account":"ورود به حساب","register_title":"ساخت حساب TRIOS","register":"ساخت حساب","confirm_password":"تکرار رمز عبور","password_mismatch":"رمزهای عبور یکسان نیستند.",
        "welcome":"خوش آمدی، {name}!","welcome_back":"خوش برگشتی، {name}!","profile_title":"ساخت پروفایل TRIOS","profile_google_done":"ورود با Google انجام شد. حالا یک نام برای پروفایل TRIOS خودت انتخاب کن.","trios_username":"نام کاربری TRIOS","create_profile":"ساخت پروفایل","logout_google":"خروج از Google",
        "dashboard_kicker":"فضای شخصی TRIOS","dashboard_title":"خوش برگشتی،","dashboard_copy":"یک فضای آرام برای آزمایش، مشاهده و فکر کردن درباره‌ی حرکت.","path_title":"مسیر تو در TRIOS","path_copy":"از اینجا می‌توانی آزمایش‌ها، گزارش‌ها و پروفایلت را مدیریت کنی.","start_experiment":"شروع آزمایش","start_experiment_copy":"وارد آزمایشگاه شو و برای اجرای یک آزمایش آماده شو.","view_report":"مشاهده گزارش","report_copy":"نتایج و عملکرد ثبت‌شده‌ی این حساب را ببین.","profile":"پروفایل","profile_copy":"اطلاعات حساب و تنظیمات امنیتی خودت را مدیریت کن.",
        "lab_title":"آزمایشگاه من","lab_notice":"زیرساخت اجرای آزمایش‌های TRIOS آماده است. محتوای آزمایش‌های آموزشی هنوز جداگانه تعریف نشده و فعلاً در این بخش ساخته نمی‌شود.","report_title":"گزارش من","profile_info":"اطلاعات شخصی","account_management":"مدیریت حساب","logout_device":"خروج از این دستگاه","delete_account":"حذف دائمی حساب","delete_warning":"حذف حساب دائمی است و اطلاعات ذخیره‌شده‌ی این حساب را پاک می‌کند.","delete_confirm":"می‌خواهم حسابم را برای همیشه حذف کنم.","confirm_delete_error":"برای حذف حساب، ابتدا تأیید حذف را فعال کن.","account_not_found":"حساب پیدا نشد.",
        "level":"سطح","attempts":"تلاش‌ها","correct":"پاسخ درست","accuracy":"دقت","report_summary":"خلاصه عملکرد","experiments":"آزمایش‌های ثبت‌شده","no_report":"هنوز گزارشی برای این حساب ثبت نشده است.",
        "about_title":"TRIOS چیست؟","about_text_1":"TRIOS یک سامانه برای شبیه‌سازی، مشاهده و مطالعه‌ی سیستم‌های فیزیکی چندجسمی با تمرکز بر مسئله‌ی سه‌جسمی است.","about_text_2":"هسته‌ی فیزیک مسئول قوانین و محاسبات است؛ لایه‌ی شبیه‌سازی اجرای گام‌های زمانی را مدیریت می‌کند؛ پیکربندی فیزیکی شرایط اولیه را نگه می‌دارد؛ و زیرساخت آزمایش مراحل و نتایج را مدیریت می‌کند.","about_text_3":"این جداسازی باعث می‌شود رابط کاربری مجبور نباشد منطق فیزیک را دوباره پیاده‌سازی کند و TRIOS بتواند به‌عنوان یک ابزار مطالعاتی و آموزشی رشد کند.","about_text_4":"TRIOS برای آزمایش‌های تکرارپذیر طراحی شده است تا شرایط فیزیکی، اجرای شبیه‌سازی، اندازه‌گیری و اعتبارسنجی از هم تفکیک باشند.","about_notice":"فعلاً تمرکز پروژه روی تکمیل زیرساخت و معماری است؛ آزمایش‌های آموزشی واقعی در این مرحله ساخته نشده‌اند.",
        "google_recovery_title":"بازیابی با Google","google_not_linked":"این حساب Google هنوز به یک حساب TRIOS متصل نشده است. برای جلوگیری از ساخت حساب تکراری، ابتدا با روش قبلی حسابت وارد شو.","back_to_recovery":"بازگشت به بازیابی","google_account":"حساب Google: {name}",
        "account_stats_title":"آمار حساب‌ها و فعالیت",
        "total_accounts":"تعداد کل حساب‌ها",
        "active_users":"کاربران فعال",
        "active_sessions":"Sessionهای فعال",
        "session_count":"تعداد Sessionها",
        "active_window":"فعال در ۱۵ دقیقه گذشته",
        "refresh_stats":"تازه‌سازی",
        "active_users_definition":"فعال یعنی حسابی که در حال حاضر Session معتبر TRIOS دارد."
    },
    "en": {}
}

TRANSLATIONS["en"] = {
    "nav_tagline":"Three-body simulation laboratory","nav_login":"Sign in","nav_signup":"Create account","nav_language":"Language",
    "hero_kicker":"A new way to explore gravity","hero_title_1":"Discover the","hero_title_2":"three-body universe.","hero_copy":"TRIOS turns the three-body problem into a beautiful scientific playground: define physical conditions, run a simulation, and watch gravity move.",
    "home_start":"Start with TRIOS","about":"What is TRIOS?","section_title":"Science, without the clutter.","section_copy":"Physics, simulation, experiments, and the interface are cleanly separated.",
    "feature_motion":"Explore motion","feature_motion_copy":"Observe gravitational systems evolve from carefully defined initial conditions.","feature_lab":"Run experiments","feature_lab_copy":"Turn an idea into a repeatable experiment without mixing science with the interface.","feature_results":"Study results","feature_results_copy":"See measurements, compare behavior, and build physical intuition from simulation.","footer":"TRIOS · gravitational three-body simulation laboratory",
    "login_title":"Sign in to TRIOS","choose_login":"Choose how you want to sign in.","google_login":"Continue with Google","google_fast":"Quick sign-in with Google","native_account":"TRIOS account","native_fast":"Username and password","create_native":"Create TRIOS account","recover":"Recover account","recover_copy":"Get back into an existing account","about_short":"What does TRIOS do?","back":"Back",
    "recover_title":"Recover account","recover_choose":"Choose your previous sign-in method.","recover_google":"Recover with Google","recover_google_copy":"Use the same Google account","recover_native":"Recover with TRIOS","recover_native_copy":"Use your TRIOS credentials","recover_native_title":"Sign in with TRIOS","recover_notice":"Enter the username and password for your TRIOS account.",
    "username":"Username","password":"Password","login_account":"Sign in","register_title":"Create a TRIOS account","register":"Create account","confirm_password":"Confirm password","password_mismatch":"Passwords do not match.",
    "welcome":"Welcome, {name}!","welcome_back":"Welcome back, {name}!","profile_title":"Create your TRIOS profile","profile_google_done":"Google sign-in succeeded. Choose a name for your TRIOS profile.","trios_username":"TRIOS username","create_profile":"Create profile","logout_google":"Sign out of Google",
    "dashboard_kicker":"TRIOS workspace","dashboard_title":"Welcome back,","dashboard_copy":"A calm space to experiment, observe, and think about motion.","path_title":"Your TRIOS path","path_copy":"Manage experiments, reports, and your profile from one place.","start_experiment":"Start experiment","start_experiment_copy":"Enter the laboratory and get ready to run an experiment.","view_report":"View report","report_copy":"Review the results recorded for this account.","profile":"Profile","profile_copy":"Manage account details and security settings.",
    "lab_title":"My laboratory","lab_notice":"The TRIOS execution infrastructure is ready. Educational experiments are not defined yet.","report_title":"My report","profile_info":"Personal information","account_management":"Account management","logout_device":"Sign out on this device","delete_account":"Delete account permanently","delete_warning":"Deleting your account is permanent and removes the stored account data.","delete_confirm":"I want to permanently delete my account.","confirm_delete_error":"Confirm account deletion first.","account_not_found":"Account not found.",
    "level":"Level","attempts":"Attempts","correct":"Correct","accuracy":"Accuracy","report_summary":"Performance summary","experiments":"Recorded experiments","no_report":"No report has been recorded for this account yet.",
    "about_title":"What is TRIOS?","about_text_1":"TRIOS is a system for simulating, observing, and studying multi-body physical systems with a focus on the three-body problem.","about_text_2":"The physics core owns laws and calculations; simulation manages time steps; physical configuration stores initial conditions; and experiment infrastructure manages stages and results.","about_text_3":"This separation keeps the interface from reimplementing physics and lets TRIOS grow as both a scientific and educational environment.","about_text_4":"TRIOS is designed for repeatable experiments, separating physical conditions, simulation, measurement, and validation.","about_notice":"The project is currently focused on infrastructure and architecture; real educational experiments have not been built yet.",
    "google_recovery_title":"Recover with Google","google_not_linked":"This Google account is not linked to a TRIOS account yet. Sign in with the previous method to avoid creating a duplicate account.","back_to_recovery":"Back to recovery","google_account":"Google account: {name}"
}

for code, overrides in {
    "ar":{"nav_language":"اللغة","nav_login":"تسجيل الدخول","nav_signup":"إنشاء حساب","hero_kicker":"طريقة جديدة لاستكشاف الجاذبية","hero_title_1":"اكتشف","hero_title_2":"عالم الأجسام الثلاثة.","hero_copy":"حوّل TRIOS مسألة الأجسام الثلاثة إلى مختبر علمي جميل: حدّد الشروط الفيزيائية، شغّل المحاكاة، وشاهد الجاذبية تتحرك.","home_start":"ابدأ مع TRIOS","about":"ما هو TRIOS؟","section_title":"العلم، بلا فوضى.","feature_motion":"استكشف الحركة","feature_lab":"أجرِ التجارب","feature_results":"ادرس النتائج","login_title":"تسجيل الدخول إلى TRIOS","google_login":"المتابعة مع Google","create_native":"إنشاء حساب TRIOS","recover":"استعادة الحساب","back":"رجوع","dashboard_title":"مرحبًا بعودتك،","profile":"الملف الشخصي","report_title":"تقاريري","lab_title":"مختبري","about_title":"ما هو TRIOS؟"},
    "zh":{"nav_language":"语言","nav_login":"登录","nav_signup":"创建账户","hero_kicker":"探索引力的新方式","hero_title_1":"探索","hero_title_2":"三体宇宙。","home_start":"开始使用 TRIOS","about":"什么是 TRIOS？","section_title":"科学，不再拥挤。","feature_motion":"探索运动","feature_lab":"进行实验","feature_results":"研究结果","login_title":"登录 TRIOS","google_login":"使用 Google 继续","create_native":"创建 TRIOS 账户","recover":"恢复账户","back":"返回","dashboard_title":"欢迎回来，","profile":"个人资料","report_title":"我的报告","lab_title":"我的实验室","about_title":"什么是 TRIOS？"},
    "es":{"nav_language":"Idioma","nav_login":"Iniciar sesión","nav_signup":"Crear cuenta","hero_kicker":"Una nueva forma de explorar la gravedad","hero_title_1":"Descubre el","hero_title_2":"universo de tres cuerpos.","home_start":"Empezar con TRIOS","about":"¿Qué es TRIOS?","section_title":"Ciencia, sin ruido.","feature_motion":"Explora el movimiento","feature_lab":"Realiza experimentos","feature_results":"Estudia resultados","login_title":"Iniciar sesión en TRIOS","google_login":"Continuar con Google","create_native":"Crear cuenta de TRIOS","recover":"Recuperar cuenta","back":"Volver","dashboard_title":"Bienvenido de nuevo,","profile":"Perfil","report_title":"Mi informe","lab_title":"Mi laboratorio","about_title":"¿Qué es TRIOS?"},
    "fr":{"nav_language":"Langue","nav_login":"Connexion","nav_signup":"Créer un compte","hero_kicker":"Une nouvelle façon d'explorer la gravité","hero_title_1":"Découvrez l'","hero_title_2":"univers des trois corps.","home_start":"Commencer avec TRIOS","about":"Qu'est-ce que TRIOS ?","section_title":"La science, sans surcharge.","feature_motion":"Explorer le mouvement","feature_lab":"Mener des expériences","feature_results":"Étudier les résultats","login_title":"Connexion à TRIOS","google_login":"Continuer avec Google","create_native":"Créer un compte TRIOS","recover":"Récupérer le compte","back":"Retour","dashboard_title":"Bon retour,","profile":"Profil","report_title":"Mon rapport","lab_title":"Mon laboratoire","about_title":"Qu'est-ce que TRIOS ?"},
    "de":{"nav_language":"Sprache","nav_login":"Anmelden","nav_signup":"Konto erstellen","hero_kicker":"Eine neue Art, Gravitation zu entdecken","hero_title_1":"Entdecke das","hero_title_2":"Dreikörper-Universum.","home_start":"Mit TRIOS starten","about":"Was ist TRIOS?","section_title":"Wissenschaft, ohne Ballast.","feature_motion":"Bewegung erkunden","feature_lab":"Experimente durchführen","feature_results":"Ergebnisse untersuchen","login_title":"Bei TRIOS anmelden","google_login":"Mit Google fortfahren","create_native":"TRIOS-Konto erstellen","recover":"Konto wiederherstellen","back":"Zurück","dashboard_title":"Willkommen zurück,","profile":"Profil","report_title":"Mein Bericht","lab_title":"Mein Labor","about_title":"Was ist TRIOS?"},
    "ja":{"nav_language":"言語","nav_login":"ログイン","nav_signup":"アカウント作成","hero_kicker":"重力を探る新しい方法","hero_title_1":"発見しよう、","hero_title_2":"三体宇宙。","home_start":"TRIOSを始める","about":"TRIOSとは？","section_title":"科学を、すっきりと。","feature_motion":"運動を探る","feature_lab":"実験する","feature_results":"結果を学ぶ","login_title":"TRIOSにログイン","google_login":"Googleで続行","create_native":"TRIOSアカウントを作成","recover":"アカウントを復元","back":"戻る","dashboard_title":"おかえりなさい、","profile":"プロフィール","report_title":"レポート","lab_title":"マイラボ","about_title":"TRIOSとは？"}
}.items():
    TRANSLATIONS[code] = {**TRANSLATIONS["en"], **overrides}


TRANSLATIONS["fa"].update({
    "github_eyebrow":"متن‌باز • TRIOS",
    "github_title":"TRIOS در GitHub",
    "github_copy":"پروژه را ببین، توسعه‌اش را دنبال کن و با ساختار TRIOS آشنا شو.",
    "github_button":"مشاهده GitHub ↗",
    "status_correct":"درست",
    "status_incorrect":"نادرست",
    "username_required":"نام کاربری نمی‌تواند خالی باشد.",
    "password_required":"رمز عبور نمی‌تواند خالی باشد.",
    "account_exists":"این حساب از قبل وجود دارد.",
    "incorrect_password":"رمز عبور نادرست است.",
    "google_identity_missing":"اطلاعات هویت Google موجود نیست.",
    "google_account_exists":"این حساب Google از قبل یک حساب TRIOS دارد.",
    "google_email_linked":"این حساب Google از قبل به یک حساب TRIOS متصل است.",
    "account_stats_title":"آمار حساب‌ها و فعالیت",
    "total_accounts":"تعداد کل حساب‌ها",
    "active_users":"کاربران فعال",
    "active_sessions":"جلسه‌های فعال",
    "session_count":"تعداد Sessionها",
    "active_window":"فعال در ۱۵ دقیقه گذشته",
    "refresh_stats":"تازه‌سازی",
    "active_users_definition":"فعال یعنی حسابی که در حال حاضر Session معتبر TRIOS دارد.",
})

TRANSLATIONS["en"].update({
    "github_eyebrow":"OPEN SOURCE • TRIOS",
    "github_title":"TRIOS on GitHub",
    "github_copy":"Explore the project, follow its development, and see how TRIOS is built.",
    "github_button":"View GitHub ↗",
    "status_correct":"Correct",
    "status_incorrect":"Incorrect",
    "username_required":"Username cannot be empty.",
    "password_required":"Password cannot be empty.",
    "account_exists":"This account already exists.",
    "incorrect_password":"Incorrect password.",
    "google_identity_missing":"Google identity is missing.",
    "google_account_exists":"This Google account already has a TRIOS account.",
    "google_email_linked":"This Google account is already linked to a TRIOS account.",
    "account_stats_title":"Account activity",
    "total_accounts":"Total accounts",
    "active_users":"Active users",
    "active_sessions":"Active sessions",
    "session_count":"Sessions",
    "active_window":"Active in the last {minutes} minutes",
    "refresh_stats":"Refresh",
    "active_users_definition":"Active = accounts with a currently valid TRIOS session.",
})

for code, overrides in {
    "ar": {
        "section_copy":"تم فصل الفيزياء والمحاكاة والتجارب وواجهة المستخدم بشكل واضح.",
        "feature_motion_copy":"راقب تطور الأنظمة الجاذبية انطلاقًا من شروط أولية محددة بدقة.",
        "feature_lab_copy":"حوّل فكرتك إلى تجربة قابلة للتكرار دون خلط العلم بواجهة المستخدم.",
        "feature_results_copy":"شاهد القياسات وقارن السلوك وابنِ حدسك الفيزيائي من خلال المحاكاة.",
        "footer":"TRIOS · مختبر محاكاة الأجسام الثلاثة",
        "choose_login":"اختر طريقة تسجيل الدخول.",
        "google_fast":"تسجيل سريع باستخدام Google",
        "native_fast":"اسم المستخدم وكلمة المرور",
        "recover_copy":"العودة إلى حساب موجود",
        "recover_choose":"اختر طريقة تسجيل الدخول السابقة.",
        "recover_google_copy":"استخدم حساب Google نفسه",
        "recover_native_copy":"استخدم بيانات TRIOS الخاصة بك",
        "recover_native_title":"تسجيل الدخول بحساب TRIOS",
        "recover_notice":"أدخل اسم المستخدم وكلمة مرور حساب TRIOS الخاص بك.",
        "username":"اسم المستخدم","password":"كلمة المرور","login_account":"تسجيل الدخول",
        "register_title":"إنشاء حساب TRIOS","register":"إنشاء حساب","confirm_password":"تأكيد كلمة المرور","password_mismatch":"كلمتا المرور غير متطابقتين.",
        "welcome":"مرحبًا، {name}!","welcome_back":"مرحبًا بعودتك، {name}!","profile_title":"إنشاء ملف TRIOS الشخصي",
        "profile_google_done":"تم تسجيل الدخول باستخدام Google. اختر اسمًا لملف TRIOS الشخصي.",
        "trios_username":"اسم مستخدم TRIOS","create_profile":"إنشاء الملف الشخصي","logout_google":"تسجيل الخروج من Google",
        "dashboard_kicker":"مساحة TRIOS الشخصية","dashboard_title":"مرحبًا بعودتك،","dashboard_copy":"مساحة هادئة للتجربة والملاحظة والتفكير في الحركة.",
        "path_title":"مسارك في TRIOS","path_copy":"يمكنك من هنا إدارة التجارب والتقارير وملفك الشخصي.",
        "start_experiment":"بدء تجربة","start_experiment_copy":"ادخل إلى المختبر واستعد لتشغيل تجربة.",
        "view_report":"عرض التقرير","report_copy":"راجع النتائج المسجلة لهذا الحساب.","profile_copy":"إدارة بيانات الحساب وإعدادات الأمان.",
        "lab_notice":"بنية تشغيل تجارب TRIOS جاهزة. لم يتم تعريف التجارب التعليمية بعد.",
        "report_title":"تقاريري","profile_info":"المعلومات الشخصية","account_management":"إدارة الحساب",
        "logout_device":"تسجيل الخروج من هذا الجهاز","delete_account":"حذف الحساب نهائيًا",
        "delete_warning":"حذف الحساب نهائي ولا يمكن التراجع عنه، وسيزيل البيانات المخزنة لهذا الحساب.",
        "delete_confirm":"أريد حذف حسابي نهائيًا.","confirm_delete_error":"أكد حذف الحساب أولًا.","account_not_found":"لم يتم العثور على الحساب.",
        "level":"المستوى","attempts":"المحاولات","correct":"الإجابات الصحيحة","accuracy":"الدقة",
        "report_summary":"ملخص الأداء","experiments":"التجارب المسجلة","no_report":"لا يوجد تقرير مسجل لهذا الحساب حتى الآن.",
        "about_short":"ماذا يفعل TRIOS؟","about_text_1":"TRIOS هو نظام لمحاكاة ومراقبة ودراسة الأنظمة الفيزيائية متعددة الأجسام مع التركيز على مسألة الأجسام الثلاثة.",
        "about_text_2":"يتولى قلب الفيزياء القوانين والحسابات؛ وتدير المحاكاة الخطوات الزمنية؛ وتحفظ البنية الفيزيائية الشروط الأولية؛ وتدير بنية التجارب المراحل والنتائج.",
        "about_text_3":"يحافظ هذا الفصل على عدم إعادة واجهة المستخدم تنفيذ منطق الفيزياء، ويسمح لـTRIOS بالنمو كبيئة علمية وتعليمية.",
        "about_text_4":"صُمم TRIOS للتجارب القابلة للتكرار، مع فصل الشروط الفيزيائية والمحاكاة والقياس والتحقق.",
        "about_notice":"يركز المشروع حاليًا على البنية التحتية والمعمارية؛ ولم تُبنَ التجارب التعليمية الحقيقية بعد.",
        "google_recovery_title":"الاستعادة باستخدام Google","google_not_linked":"حساب Google هذا غير مرتبط بحساب TRIOS حتى الآن. سجّل الدخول بالطريقة السابقة لتجنب إنشاء حساب مكرر.",
        "back_to_recovery":"العودة إلى الاستعادة","google_account":"حساب Google: {name}",
        "github_eyebrow":"مفتوح المصدر • TRIOS","github_title":"TRIOS على GitHub","github_copy":"استكشف المشروع وتابع تطويره وتعرّف على كيفية بناء TRIOS.","github_button":"عرض GitHub ↗",
        "status_correct":"صحيح","status_incorrect":"غير صحيح",
        "username_required":"لا يمكن أن يكون اسم المستخدم فارغًا.","password_required":"لا يمكن أن تكون كلمة المرور فارغة.",
        "account_exists":"هذا الحساب موجود بالفعل.","incorrect_password":"كلمة المرور غير صحيحة.",
        "google_identity_missing":"هوية Google مفقودة.","google_account_exists":"هذا الحساب من Google لديه حساب TRIOS بالفعل.",
        "google_email_linked":"حساب Google هذا مرتبط بالفعل بحساب TRIOS."
    },
    "zh": {
        "section_copy":"物理、模拟、实验和用户界面彼此清晰分离。",
        "feature_motion_copy":"从精确定义的初始条件出发，观察引力系统的演化。",
        "feature_lab_copy":"把想法变成可重复的实验，同时保持科学与界面分离。",
        "feature_results_copy":"查看测量结果、比较行为，并通过模拟建立物理直觉。",
        "footer":"TRIOS · 三体模拟实验室",
        "choose_login":"选择登录方式。",
        "google_fast":"使用 Google 快速登录","native_fast":"用户名和密码","recover_copy":"找回已有账户",
        "recover_choose":"选择你之前使用的登录方式。","recover_google_copy":"使用同一个 Google 账户",
        "recover_native_copy":"使用 TRIOS 账户信息","recover_native_title":"使用 TRIOS 登录",
        "recover_notice":"请输入 TRIOS 账户的用户名和密码。","username":"用户名","password":"密码","login_account":"登录",
        "register_title":"创建 TRIOS 账户","register":"创建账户","confirm_password":"确认密码","password_mismatch":"两次密码不一致。",
        "welcome":"欢迎，{name}！","welcome_back":"欢迎回来，{name}！","profile_title":"创建 TRIOS 个人资料",
        "profile_google_done":"Google 登录成功。为你的 TRIOS 个人资料选择一个名称。",
        "trios_username":"TRIOS 用户名","create_profile":"创建个人资料","logout_google":"退出 Google",
        "dashboard_kicker":"TRIOS 工作区","dashboard_title":"欢迎回来，","dashboard_copy":"一个用于实验、观察和思考运动的安静空间。",
        "path_title":"你的 TRIOS 路径","path_copy":"从这里管理实验、报告和个人资料。",
        "start_experiment":"开始实验","start_experiment_copy":"进入实验室并准备运行实验。",
        "view_report":"查看报告","report_copy":"查看此账户记录的实验结果。","profile_copy":"管理账户信息和安全设置。",
        "lab_notice":"TRIOS 实验执行基础设施已准备就绪，教育实验尚未定义。",
        "report_title":"我的报告","profile_info":"个人信息","account_management":"账户管理",
        "logout_device":"退出此设备","delete_account":"永久删除账户",
        "delete_warning":"删除账户是永久操作，将删除此账户存储的数据。",
        "delete_confirm":"我要永久删除我的账户。","confirm_delete_error":"请先确认删除账户。","account_not_found":"未找到账户。",
        "level":"等级","attempts":"尝试次数","correct":"正确回答","accuracy":"准确率",
        "report_summary":"表现摘要","experiments":"已记录的实验","no_report":"此账户还没有报告记录。",
        "about_short":"TRIOS 是什么？","about_text_1":"TRIOS 是一个用于模拟、观察和研究多体物理系统的系统，重点研究三体问题。",
        "about_text_2":"物理核心负责定律和计算；模拟层管理时间步；物理配置保存初始条件；实验基础设施管理阶段和结果。",
        "about_text_3":"这种分离让界面无需重新实现物理逻辑，也让 TRIOS 能够发展成为科学和教育环境。",
        "about_text_4":"TRIOS 面向可重复实验设计，将物理条件、模拟、测量和验证分开。",
        "about_notice":"项目目前专注于基础设施和架构；真正的教育实验尚未建立。",
        "google_recovery_title":"使用 Google 恢复","google_not_linked":"此 Google 账户尚未关联 TRIOS 账户。请使用之前的方式登录，以避免创建重复账户。",
        "back_to_recovery":"返回账户恢复","google_account":"Google 账户：{name}",
        "github_eyebrow":"开源 • TRIOS","github_title":"TRIOS on GitHub","github_copy":"探索项目、跟进开发，并了解 TRIOS 的构建方式。","github_button":"查看 GitHub ↗",
        "status_correct":"正确","status_incorrect":"不正确",
        "username_required":"用户名不能为空。","password_required":"密码不能为空。","account_exists":"账户已存在。","incorrect_password":"密码不正确。",
        "google_identity_missing":"缺少 Google 身份信息。","google_account_exists":"此 Google 账户已有 TRIOS 账户。","google_email_linked":"此 Google 账户已关联 TRIOS 账户。"
    },
    "es": {
        "section_copy":"La física, la simulación, los experimentos y la interfaz están claramente separados.",
        "feature_motion_copy":"Observa cómo evolucionan los sistemas gravitatorios desde condiciones iniciales precisas.",
        "feature_lab_copy":"Convierte una idea en un experimento repetible sin mezclar la ciencia con la interfaz.",
        "feature_results_copy":"Consulta las mediciones, compara comportamientos y desarrolla intuición física mediante la simulación.",
        "footer":"TRIOS · laboratorio de simulación de tres cuerpos",
        "choose_login":"Elige cómo quieres iniciar sesión.","google_fast":"Inicio rápido con Google","native_fast":"Nombre de usuario y contraseña",
        "recover_copy":"Volver a una cuenta existente","recover_choose":"Elige tu método de inicio de sesión anterior.","recover_google_copy":"Usa la misma cuenta de Google",
        "recover_native_copy":"Usa tus credenciales de TRIOS","recover_native_title":"Iniciar sesión con TRIOS","recover_notice":"Introduce el nombre de usuario y la contraseña de tu cuenta TRIOS.",
        "username":"Nombre de usuario","password":"Contraseña","login_account":"Iniciar sesión","register_title":"Crear una cuenta de TRIOS","register":"Crear cuenta",
        "confirm_password":"Confirmar contraseña","password_mismatch":"Las contraseñas no coinciden.","welcome":"¡Bienvenido, {name}!","welcome_back":"¡Bienvenido de nuevo, {name}!",
        "profile_title":"Crear tu perfil de TRIOS","profile_google_done":"Has iniciado sesión con Google. Elige un nombre para tu perfil de TRIOS.",
        "trios_username":"Nombre de usuario de TRIOS","create_profile":"Crear perfil","logout_google":"Cerrar sesión de Google",
        "dashboard_kicker":"Espacio de TRIOS","dashboard_title":"Bienvenido de nuevo,","dashboard_copy":"Un espacio tranquilo para experimentar, observar y pensar sobre el movimiento.",
        "path_title":"Tu recorrido en TRIOS","path_copy":"Gestiona experimentos, informes y tu perfil desde aquí.",
        "start_experiment":"Iniciar experimento","start_experiment_copy":"Entra en el laboratorio y prepárate para ejecutar un experimento.",
        "view_report":"Ver informe","report_copy":"Revisa los resultados registrados para esta cuenta.","profile_copy":"Gestiona los datos de la cuenta y la configuración de seguridad.",
        "lab_notice":"La infraestructura de ejecución de TRIOS está lista. Los experimentos educativos todavía no están definidos.",
        "report_title":"Mi informe","profile_info":"Información personal","account_management":"Gestión de la cuenta",
        "logout_device":"Cerrar sesión en este dispositivo","delete_account":"Eliminar cuenta permanentemente",
        "delete_warning":"Eliminar la cuenta es permanente y borra los datos almacenados de esta cuenta.",
        "delete_confirm":"Quiero eliminar mi cuenta permanentemente.","confirm_delete_error":"Confirma primero la eliminación de la cuenta.","account_not_found":"Cuenta no encontrada.",
        "level":"Nivel","attempts":"Intentos","correct":"Respuestas correctas","accuracy":"Precisión","report_summary":"Resumen del rendimiento",
        "experiments":"Experimentos registrados","no_report":"Todavía no hay ningún informe registrado para esta cuenta.",
        "about_short":"¿Qué hace TRIOS?","about_text_1":"TRIOS es un sistema para simular, observar y estudiar sistemas físicos de múltiples cuerpos, con especial atención al problema de los tres cuerpos.",
        "about_text_2":"El núcleo físico contiene las leyes y cálculos; la simulación gestiona los pasos temporales; la configuración física guarda las condiciones iniciales; y la infraestructura de experimentos gestiona etapas y resultados.",
        "about_text_3":"Esta separación evita que la interfaz tenga que volver a implementar la física y permite que TRIOS crezca como entorno científico y educativo.",
        "about_text_4":"TRIOS está diseñado para experimentos repetibles, separando condiciones físicas, simulación, medición y validación.",
        "about_notice":"El proyecto se centra actualmente en la infraestructura y la arquitectura; todavía no se han creado experimentos educativos reales.",
        "google_recovery_title":"Recuperar con Google","google_not_linked":"Esta cuenta de Google aún no está vinculada a una cuenta de TRIOS. Inicia sesión con el método anterior para evitar crear una cuenta duplicada.",
        "back_to_recovery":"Volver a recuperación","google_account":"Cuenta de Google: {name}",
        "github_eyebrow":"CÓDIGO ABIERTO • TRIOS","github_title":"TRIOS en GitHub","github_copy":"Explora el proyecto, sigue su desarrollo y descubre cómo está construido TRIOS.","github_button":"Ver GitHub ↗",
        "status_correct":"Correcto","status_incorrect":"Incorrecto",
        "username_required":"El nombre de usuario no puede estar vacío.","password_required":"La contraseña no puede estar vacía.","account_exists":"La cuenta ya existe.","incorrect_password":"La contraseña es incorrecta.",
        "google_identity_missing":"Falta la identidad de Google.","google_account_exists":"Esta cuenta de Google ya tiene una cuenta de TRIOS.","google_email_linked":"Esta cuenta de Google ya está vinculada a una cuenta de TRIOS."
    },
    "fr": {
        "section_copy":"La physique, la simulation, les expériences et l’interface sont clairement séparées.",
        "feature_motion_copy":"Observez l’évolution des systèmes gravitationnels à partir de conditions initiales précises.",
        "feature_lab_copy":"Transformez une idée en expérience reproductible sans mélanger la science et l’interface.",
        "feature_results_copy":"Consultez les mesures, comparez les comportements et développez votre intuition physique grâce à la simulation.",
        "footer":"TRIOS · laboratoire de simulation à trois corps",
        "choose_login":"Choisissez votre méthode de connexion.","google_fast":"Connexion rapide avec Google","native_fast":"Nom d’utilisateur et mot de passe",
        "recover_copy":"Retrouver un compte existant","recover_choose":"Choisissez votre ancienne méthode de connexion.","recover_google_copy":"Utiliser le même compte Google",
        "recover_native_copy":"Utiliser vos identifiants TRIOS","recover_native_title":"Se connecter avec TRIOS","recover_notice":"Saisissez le nom d’utilisateur et le mot de passe de votre compte TRIOS.",
        "username":"Nom d’utilisateur","password":"Mot de passe","login_account":"Se connecter","register_title":"Créer un compte TRIOS","register":"Créer un compte",
        "confirm_password":"Confirmer le mot de passe","password_mismatch":"Les mots de passe ne correspondent pas.","welcome":"Bienvenue, {name} !","welcome_back":"Bon retour, {name} !",
        "profile_title":"Créer votre profil TRIOS","profile_google_done":"Connexion Google réussie. Choisissez un nom pour votre profil TRIOS.",
        "trios_username":"Nom d’utilisateur TRIOS","create_profile":"Créer le profil","logout_google":"Se déconnecter de Google",
        "dashboard_kicker":"Espace TRIOS","dashboard_title":"Bon retour,","dashboard_copy":"Un espace calme pour expérimenter, observer et réfléchir au mouvement.",
        "path_title":"Votre parcours TRIOS","path_copy":"Gérez ici vos expériences, rapports et profil.",
        "start_experiment":"Démarrer une expérience","start_experiment_copy":"Entrez dans le laboratoire et préparez-vous à lancer une expérience.",
        "view_report":"Voir le rapport","report_copy":"Consultez les résultats enregistrés pour ce compte.","profile_copy":"Gérez les informations du compte et les paramètres de sécurité.",
        "lab_notice":"L’infrastructure d’exécution de TRIOS est prête. Les expériences éducatives ne sont pas encore définies.",
        "report_title":"Mon rapport","profile_info":"Informations personnelles","account_management":"Gestion du compte",
        "logout_device":"Se déconnecter de cet appareil","delete_account":"Supprimer définitivement le compte",
        "delete_warning":"La suppression du compte est définitive et efface les données stockées pour ce compte.",
        "delete_confirm":"Je veux supprimer définitivement mon compte.","confirm_delete_error":"Confirmez d’abord la suppression du compte.","account_not_found":"Compte introuvable.",
        "level":"Niveau","attempts":"Tentatives","correct":"Réponses correctes","accuracy":"Précision","report_summary":"Résumé des performances",
        "experiments":"Expériences enregistrées","no_report":"Aucun rapport n’est encore enregistré pour ce compte.",
        "about_short":"Que fait TRIOS ?","about_text_1":"TRIOS est un système destiné à simuler, observer et étudier des systèmes physiques à plusieurs corps, avec un accent sur le problème des trois corps.",
        "about_text_2":"Le cœur physique contient les lois et les calculs ; la simulation gère les pas de temps ; la configuration physique stocke les conditions initiales ; l’infrastructure des expériences gère les étapes et les résultats.",
        "about_text_3":"Cette séparation évite à l’interface de réimplémenter la physique et permet à TRIOS d’évoluer comme environnement scientifique et éducatif.",
        "about_text_4":"TRIOS est conçu pour des expériences reproductibles, en séparant conditions physiques, simulation, mesure et validation.",
        "about_notice":"Le projet se concentre actuellement sur l’infrastructure et l’architecture ; les véritables expériences éducatives n’ont pas encore été créées.",
        "google_recovery_title":"Récupérer avec Google","google_not_linked":"Ce compte Google n’est pas encore lié à un compte TRIOS. Connectez-vous avec la méthode précédente pour éviter de créer un compte en double.",
        "back_to_recovery":"Retour à la récupération","google_account":"Compte Google : {name}",
        "github_eyebrow":"OPEN SOURCE • TRIOS","github_title":"TRIOS sur GitHub","github_copy":"Explorez le projet, suivez son développement et découvrez comment TRIOS est construit.","github_button":"Voir GitHub ↗",
        "status_correct":"Correct","status_incorrect":"Incorrect",
        "username_required":"Le nom d’utilisateur ne peut pas être vide.","password_required":"Le mot de passe ne peut pas être vide.","account_exists":"Ce compte existe déjà.","incorrect_password":"Mot de passe incorrect.",
        "google_identity_missing":"L’identité Google est manquante.","google_account_exists":"Ce compte Google possède déjà un compte TRIOS.","google_email_linked":"Ce compte Google est déjà lié à un compte TRIOS."
    },
    "de": {
        "section_copy":"Physik, Simulation, Experimente und Benutzeroberfläche sind klar voneinander getrennt.",
        "feature_motion_copy":"Beobachte die Entwicklung gravitativer Systeme aus präzise definierten Anfangsbedingungen.",
        "feature_lab_copy":"Verwandle eine Idee in ein wiederholbares Experiment, ohne Wissenschaft und Oberfläche zu vermischen.",
        "feature_results_copy":"Sieh dir Messungen an, vergleiche Verhalten und entwickle physikalische Intuition durch Simulation.",
        "footer":"TRIOS · Labor für Dreikörpersimulation",
        "choose_login":"Wähle deine Anmeldemethode.","google_fast":"Schnelle Anmeldung mit Google","native_fast":"Benutzername und Passwort",
        "recover_copy":"Zu einem bestehenden Konto zurückkehren","recover_choose":"Wähle deine bisherige Anmeldemethode.","recover_google_copy":"Dasselbe Google-Konto verwenden",
        "recover_native_copy":"Deine TRIOS-Zugangsdaten verwenden","recover_native_title":"Mit TRIOS anmelden","recover_notice":"Gib den Benutzernamen und das Passwort deines TRIOS-Kontos ein.",
        "username":"Benutzername","password":"Passwort","login_account":"Anmelden","register_title":"TRIOS-Konto erstellen","register":"Konto erstellen",
        "confirm_password":"Passwort bestätigen","password_mismatch":"Die Passwörter stimmen nicht überein.","welcome":"Willkommen, {name}!","welcome_back":"Willkommen zurück, {name}!",
        "profile_title":"TRIOS-Profil erstellen","profile_google_done":"Die Google-Anmeldung war erfolgreich. Wähle einen Namen für dein TRIOS-Profil.",
        "trios_username":"TRIOS-Benutzername","create_profile":"Profil erstellen","logout_google":"Von Google abmelden",
        "dashboard_kicker":"TRIOS-Arbeitsbereich","dashboard_title":"Willkommen zurück,","dashboard_copy":"Ein ruhiger Ort zum Experimentieren, Beobachten und Nachdenken über Bewegung.",
        "path_title":"Dein TRIOS-Weg","path_copy":"Verwalte von hier aus Experimente, Berichte und dein Profil.",
        "start_experiment":"Experiment starten","start_experiment_copy":"Betritt das Labor und bereite dich auf ein Experiment vor.",
        "view_report":"Bericht anzeigen","report_copy":"Überprüfe die für dieses Konto gespeicherten Ergebnisse.","profile_copy":"Verwalte Kontodaten und Sicherheitseinstellungen.",
        "lab_notice":"Die Ausführungsinfrastruktur von TRIOS ist bereit. Bildungs-Experimente sind noch nicht definiert.",
        "report_title":"Mein Bericht","profile_info":"Persönliche Informationen","account_management":"Kontoverwaltung",
        "logout_device":"Auf diesem Gerät abmelden","delete_account":"Konto dauerhaft löschen",
        "delete_warning":"Das Löschen des Kontos ist dauerhaft und entfernt die gespeicherten Daten dieses Kontos.",
        "delete_confirm":"Ich möchte mein Konto dauerhaft löschen.","confirm_delete_error":"Bestätige zuerst die Kontolöschung.","account_not_found":"Konto nicht gefunden.",
        "level":"Level","attempts":"Versuche","correct":"Richtige Antworten","accuracy":"Genauigkeit","report_summary":"Leistungsübersicht",
        "experiments":"Aufgezeichnete Experimente","no_report":"Für dieses Konto wurde noch kein Bericht aufgezeichnet.",
        "about_short":"Was macht TRIOS?","about_text_1":"TRIOS ist ein System zum Simulieren, Beobachten und Untersuchen physikalischer Mehrkörpersysteme mit Fokus auf das Dreikörperproblem.",
        "about_text_2":"Der Physikkern enthält Gesetze und Berechnungen; die Simulation verwaltet Zeitschritte; die physische Konfiguration speichert Anfangsbedingungen; die Experimentinfrastruktur verwaltet Phasen und Ergebnisse.",
        "about_text_3":"Diese Trennung verhindert, dass die Oberfläche Physiklogik neu implementieren muss, und ermöglicht TRIOS als wissenschaftliche und pädagogische Umgebung zu wachsen.",
        "about_text_4":"TRIOS ist für wiederholbare Experimente ausgelegt und trennt physische Bedingungen, Simulation, Messung und Validierung.",
        "about_notice":"Das Projekt konzentriert sich derzeit auf Infrastruktur und Architektur; echte Bildungs-Experimente wurden noch nicht erstellt.",
        "google_recovery_title":"Mit Google wiederherstellen","google_not_linked":"Dieses Google-Konto ist noch nicht mit einem TRIOS-Konto verknüpft. Melde dich mit der vorherigen Methode an, um ein doppeltes Konto zu vermeiden.",
        "back_to_recovery":"Zurück zur Wiederherstellung","google_account":"Google-Konto: {name}",
        "github_eyebrow":"OPEN SOURCE • TRIOS","github_title":"TRIOS auf GitHub","github_copy":"Entdecke das Projekt, verfolge die Entwicklung und erfahre, wie TRIOS aufgebaut ist.","github_button":"GitHub ansehen ↗",
        "status_correct":"Richtig","status_incorrect":"Falsch",
        "username_required":"Der Benutzername darf nicht leer sein.","password_required":"Das Passwort darf nicht leer sein.","account_exists":"Dieses Konto existiert bereits.","incorrect_password":"Falsches Passwort.",
        "google_identity_missing":"Die Google-Identität fehlt.","google_account_exists":"Dieses Google-Konto hat bereits ein TRIOS-Konto.","google_email_linked":"Dieses Google-Konto ist bereits mit einem TRIOS-Konto verknüpft."
    },
    "ja": {
        "section_copy":"物理、シミュレーション、実験、インターフェースを明確に分離しています。",
        "feature_motion_copy":"正確に定義した初期条件から、重力系がどのように進化するかを観察します。",
        "feature_lab_copy":"科学とインターフェースを混ぜずに、アイデアを再現可能な実験へ変えます。",
        "feature_results_copy":"測定結果を見て挙動を比較し、シミュレーションから物理的な直感を身につけます。",
        "footer":"TRIOS · 三体シミュレーション研究室",
        "choose_login":"ログイン方法を選んでください。","google_fast":"Googleでクイックログイン","native_fast":"ユーザー名とパスワード",
        "recover_copy":"既存のアカウントに戻る","recover_choose":"以前使用したログイン方法を選んでください。","recover_google_copy":"同じGoogleアカウントを使用",
        "recover_native_copy":"TRIOSの認証情報を使用","recover_native_title":"TRIOSでログイン","recover_notice":"TRIOSアカウントのユーザー名とパスワードを入力してください。",
        "username":"ユーザー名","password":"パスワード","login_account":"ログイン","register_title":"TRIOSアカウントを作成","register":"アカウントを作成",
        "confirm_password":"パスワードを確認","password_mismatch":"パスワードが一致しません。","welcome":"ようこそ、{name}さん！","welcome_back":"おかえりなさい、{name}さん！",
        "profile_title":"TRIOSプロフィールを作成","profile_google_done":"Googleでのログインに成功しました。TRIOSプロフィールの名前を選んでください。",
        "trios_username":"TRIOSユーザー名","create_profile":"プロフィールを作成","logout_google":"Googleからログアウト",
        "dashboard_kicker":"TRIOSワークスペース","dashboard_title":"おかえりなさい、","dashboard_copy":"実験し、観察し、運動について考えるための静かな空間です。",
        "path_title":"TRIOSでのあなたの道","path_copy":"ここから実験、レポート、プロフィールを管理できます。",
        "start_experiment":"実験を開始","start_experiment_copy":"ラボに入り、実験を実行する準備をします。",
        "view_report":"レポートを見る","report_copy":"このアカウントに記録された結果を確認します。","profile_copy":"アカウント情報とセキュリティ設定を管理します。",
        "lab_notice":"TRIOSの実験実行基盤は準備済みです。教育用実験はまだ定義されていません。",
        "report_title":"マイレポート","profile_info":"個人情報","account_management":"アカウント管理",
        "logout_device":"このデバイスからログアウト","delete_account":"アカウントを完全に削除",
        "delete_warning":"アカウントの削除は永久的で、このアカウントに保存されたデータを削除します。",
        "delete_confirm":"アカウントを完全に削除したい。","confirm_delete_error":"まずアカウント削除を確認してください。","account_not_found":"アカウントが見つかりません。",
        "level":"レベル","attempts":"試行回数","correct":"正解","accuracy":"正確率","report_summary":"成績概要",
        "experiments":"記録された実験","no_report":"このアカウントにはまだレポートがありません。",
        "about_short":"TRIOSとは？","about_text_1":"TRIOSは、多体系の物理システムをシミュレーション、観察、研究するためのシステムで、三体問題を中心に扱います。",
        "about_text_2":"物理コアは法則と計算を担当し、シミュレーションは時間ステップを管理し、物理設定は初期条件を保持し、実験基盤はステージと結果を管理します。",
        "about_text_3":"この分離により、インターフェースが物理ロジックを再実装する必要がなくなり、TRIOSは科学・教育環境として成長できます。",
        "about_text_4":"TRIOSは再現可能な実験向けに設計され、物理条件、シミュレーション、測定、検証を分離しています。",
        "about_notice":"現在はインフラとアーキテクチャの完成に集中しており、実際の教育用実験はまだ作成されていません。",
        "google_recovery_title":"Googleで復元","google_not_linked":"このGoogleアカウントはまだTRIOSアカウントにリンクされていません。重複アカウントを避けるため、以前の方法でログインしてください。",
        "back_to_recovery":"復元に戻る","google_account":"Googleアカウント：{name}",
        "github_eyebrow":"オープンソース • TRIOS","github_title":"GitHubのTRIOS","github_copy":"プロジェクトを見て、開発を追い、TRIOSの仕組みを確認できます。","github_button":"GitHubを見る ↗",
        "status_correct":"正解","status_incorrect":"不正解",
        "username_required":"ユーザー名は空にできません。","password_required":"パスワードは空にできません。","account_exists":"このアカウントはすでに存在します。","incorrect_password":"パスワードが正しくありません。",
        "google_identity_missing":"Googleの本人情報がありません。","google_account_exists":"このGoogleアカウントにはすでにTRIOSアカウントがあります。","google_email_linked":"このGoogleアカウントはすでにTRIOSアカウントにリンクされています。"
    }
}.items():
    TRANSLATIONS[code].update(overrides)


ERROR_TRANSLATION_KEYS = {
    "Username cannot be empty.": "username_required",
    "Password cannot be empty.": "password_required",
    "User account already exists.": "account_exists",
    "User account does not exist.": "account_not_found",
    "Incorrect password.": "incorrect_password",
    "Google identity is missing.": "google_identity_missing",
    "This Google account already has a TRIOS account.": "google_account_exists",
    "This Google account is already linked to a TRIOS account.": "google_email_linked",
}


def localized_error(exc):
    """Return a translated user-facing error while preserving unknown errors."""
    message = str(exc)
    return t(ERROR_TRANSLATION_KEYS.get(message, message))

def current_language():
    return st.session_state.get("language", "fa")

def t(key, **kwargs):
    value = TRANSLATIONS.get(current_language(), TRANSLATIONS["en"]).get(key, TRANSLATIONS["en"].get(key, key))
    return value.format(**kwargs) if kwargs else value

def language_rtl():
    return current_language() in {"fa", "ar"}

def apply_language_direction():
    direction = "rtl" if language_rtl() else "ltr"
    st.markdown(
        f"""
        <style>
        .main .block-container {{ direction:{direction}; }}
        .stSelectbox, .stTextInput, .stCheckbox, .stButton {{ direction:{direction}; }}
        .trios-nav, .trios-brand, .trios-hero, .trios-card, .trios-page-card, .trios-action-card {{ direction:{direction}; }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def show_language_selector(key="language_selector"):
    options = list(LANGUAGES.keys())
    current = current_language()
    index = options.index(current) if current in options else 0
    selected = st.selectbox(
        t("nav_language"),
        options,
        index=index,
        format_func=lambda code: LANGUAGES[code],
        label_visibility="collapsed",
        key=key,
    )
    if selected != current:
        st.session_state.language = selected
        st.rerun()

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

        .trios-css-icon {
            width: 1.8rem;
            height: 1.8rem;
            position: relative;
            opacity: .95;
        }
        .trios-css-icon.orbit::before,
        .trios-css-icon.orbit::after {
            content:"";
            position:absolute;
            inset:.15rem;
            border:2px solid #7bdfff;
            border-radius:50%;
            transform:rotate(34deg) scaleY(.48);
        }
        .trios-css-icon.orbit::after {
            border-color:#b48cff;
            transform:rotate(-34deg) scaleY(.48);
        }
        .trios-css-icon.flask::before {
            content:"";
            position:absolute;
            left:.57rem;
            top:.08rem;
            width:.62rem;
            height:.8rem;
            border-left:2px solid #8ae5ff;
            border-right:2px solid #b28bff;
        }
        .trios-css-icon.flask::after {
            content:"";
            position:absolute;
            left:.28rem;
            bottom:.1rem;
            width:1.22rem;
            height:1rem;
            border:2px solid #8ae5ff;
            border-top:0;
            border-radius:0 0 .55rem .55rem;
        }
        .trios-css-icon.chart::before {
            content:"";
            position:absolute;
            left:.12rem;
            right:.12rem;
            bottom:.18rem;
            height:1.25rem;
            border-left:2px solid #8ae5ff;
            border-bottom:2px solid #8ae5ff;
        }
        .trios-css-icon.chart::after {
            content:"";
            position:absolute;
            left:.42rem;
            top:.52rem;
            width:1.08rem;
            height:.62rem;
            border-top:2px solid #b58dff;
            border-right:2px solid #b58dff;
            transform:skew(-26deg) rotate(-18deg);
        }
        .stSelectbox { min-width:7.6rem; }
        .stSelectbox [data-baseweb="select"] > div {
            min-height:2.55rem;
            border-radius:13px !important;
            border:1px solid rgba(183,210,255,.14) !important;
            background:rgba(255,255,255,.055) !important;
            color:#f5f8ff !important;
        }

        .trios-nav-subtitle {
            color: #a8b7dc;
            font-size: .78rem;
            font-weight: 500;
            margin-inline-start: .55rem;
        }

        .trios-brand strong {
            background: linear-gradient(110deg, #ffffff 0%, #9deaff 38%, #c2a1ff 72%, #ff9cda 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 0 28px rgba(119, 205, 255, .10);
        }

        .trios-kicker {
            background:
                linear-gradient(90deg, rgba(92,220,255,.10), rgba(184,128,255,.12), rgba(255,137,211,.10));
            border-color: rgba(169, 211, 255, .22);
        }

        .trios-kicker-dot {
            background: linear-gradient(135deg, #67eaff, #a986ff 55%, #ff90cf);
            box-shadow:
                0 0 12px rgba(103,234,255,.56),
                0 0 24px rgba(219,133,255,.22);
        }

        .trios-card,
        [data-testid="stVerticalBlockBorderWrapper"] {
            background:
                linear-gradient(145deg,
                    rgba(101, 222, 255, .075),
                    rgba(180, 129, 255, .06) 48%,
                    rgba(255, 146, 211, .045)),
                rgba(14, 20, 48, .54) !important;
        }

        .trios-card:hover,
        [data-testid="stVerticalBlockBorderWrapper"]:hover {
            border-color: rgba(159, 220, 255, .34) !important;
            box-shadow:
                0 22px 48px rgba(0,0,0,.21),
                0 0 30px rgba(86,214,255,.12),
                0 0 44px rgba(217,125,255,.07),
                inset 0 1px 0 rgba(255,255,255,.08) !important;
        }

        .trios-icon-box {
            background:
                linear-gradient(145deg,
                    rgba(102, 224, 255, .20),
                    rgba(176, 132, 255, .16) 52%,
                    rgba(255, 139, 207, .11)),
                rgba(255,255,255,.035);
        }

        .trios-hero {
            background:
                radial-gradient(circle at 28% 18%, rgba(83, 225, 255, .15), transparent 24%),
                radial-gradient(circle at 74% 30%, rgba(193, 126, 255, .14), transparent 26%),
                radial-gradient(circle at 50% 70%, rgba(255, 129, 203, .08), transparent 30%),
                linear-gradient(180deg, rgba(255,255,255,.05), rgba(255,255,255,.018));
        }

        .trios-hero-glow {
            background:
                radial-gradient(circle,
                    rgba(103, 232, 255, .34),
                    rgba(156, 115, 255, .18) 43%,
                    rgba(255, 131, 204, .10) 58%,
                    transparent 72%);
        }

        .trios-github {
            margin: 3.2rem auto 1.2rem;
            max-width: 900px;
            padding: 1.35rem 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.25rem;
            border: 1px solid rgba(159, 220, 255, .16);
            border-radius: 22px;
            background:
                linear-gradient(120deg,
                    rgba(89, 220, 255, .08),
                    rgba(177, 129, 255, .07),
                    rgba(255, 139, 207, .06)),
                rgba(10, 16, 40, .48);
            box-shadow: 0 18px 45px rgba(0,0,0,.16);
        }

        .trios-github-eyebrow {
            font-size: .72rem;
            letter-spacing: .13em;
            color: #8edfff;
            font-weight: 700;
        }

        .trios-github h3 {
            margin: .18rem 0 .2rem;
        }

        .trios-github p {
            margin: 0;
            color: #9da9c8;
        }

        .trios-github a {
            flex: 0 0 auto;
            padding: .7rem 1rem;
            border-radius: 13px;
            text-decoration: none;
            color: #f8fbff;
            border: 1px solid rgba(160, 220, 255, .24);
            background: linear-gradient(135deg, rgba(92,220,255,.16), rgba(186,126,255,.16));
        }

        .trios-github a:hover {
            border-color: rgba(160, 220, 255, .48);
            box-shadow: 0 0 26px rgba(91, 216, 255, .12);
        }

        .trios-footer {
            color: #91a1c6;
        }


            color: #95a3c4;
            font-size: .78rem;
            font-weight: 500;
            margin-inline-start: .55rem;
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 24px !important;
            border-color: rgba(183, 210, 255, .13) !important;
            background:
                linear-gradient(145deg, rgba(255,255,255,.07), rgba(255,255,255,.025)),
                rgba(14, 20, 48, .52) !important;
            box-shadow:
                0 18px 42px rgba(0,0,0,.16),
                inset 0 1px 0 rgba(255,255,255,.055) !important;
            backdrop-filter: blur(14px);
        }

        [data-testid="stVerticalBlockBorderWrapper"]:hover {
            border-color: rgba(151, 214, 255, .30) !important;
            box-shadow:
                0 22px 48px rgba(0,0,0,.22),
                0 0 30px rgba(115, 196, 255, .10),
                inset 0 1px 0 rgba(255,255,255,.07) !important;
        }

        [data-testid="stSelectbox"] [data-baseweb="select"] > div {
            min-height: 2.65rem;
            border-radius: 14px !important;
            border: 1px solid rgba(183,210,255,.16) !important;
            background: rgba(255,255,255,.06) !important;
            color: #f7f9ff !important;
        }

        [data-testid="stSelectbox"] svg {
            fill: #9edfff !important;
        }

        .trios-hero {
            box-shadow:
                0 30px 100px rgba(0,0,0,.35),
                0 0 70px rgba(108,176,255,.08),
                inset 0 1px 0 rgba(255,255,255,.055);
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
    left, middle, admin_col, language_col = st.columns(
        [0.65, 2.75, 1.15, 1.15],
        vertical_alignment="center",
    )

    with left:
        st.image("assets/trios_logo.png", width=46)

    with middle:
        st.markdown(
            f"""
            <div class="trios-brand">
                <strong>TRIOS</strong>
                <span class="trios-nav-subtitle">{t("nav_tagline")}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with admin_col:
        if _is_admin():
            if st.button(t("account_stats_title"), use_container_width=True, key="nav_account_stats"):
                navigate("account_stats")

    with language_col:
        show_language_selector("public_language")


def show_hero_orbit():
    st.markdown(
        """
        <div class="trios-orbit-stage" aria-hidden="true">
            <div class="trios-hero-glow"></div>
            <svg viewBox="0 0 440 440" fill="none" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <radialGradient id="triosCore" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(220 220) rotate(90) scale(74)">
                        <stop stop-color="#FFFFFF"/>
                        <stop offset=".24" stop-color="#9DEBFF"/>
                        <stop offset=".72" stop-color="#A78BFF"/>
                        <stop offset="1" stop-color="#A78BFF" stop-opacity="0"/>
                    </radialGradient>
                    <filter id="triosBlur"><feGaussianBlur stdDeviation="12"/></filter>
                </defs>
                <g opacity=".84">
                    <ellipse cx="220" cy="220" rx="160" ry="74" stroke="#66E0FF" stroke-opacity=".25" stroke-width="1.5"/>
                    <ellipse cx="220" cy="220" rx="160" ry="74" transform="rotate(62 220 220)" stroke="#C28CFF" stroke-opacity=".20" stroke-width="1.5"/>
                    <ellipse cx="220" cy="220" rx="160" ry="74" transform="rotate(-62 220 220)" stroke="#7FA6FF" stroke-opacity=".18" stroke-width="1.5"/>
                </g>
                <g class="trios-orbit-ring">
                    <circle cx="220" cy="64" r="7" fill="#83E7FF"/>
                    <circle cx="220" cy="64" r="18" fill="#83E7FF" fill-opacity=".08"/>
                </g>
                <g class="trios-orbit-ring reverse">
                    <circle cx="220" cy="70" r="6" fill="#D49AFF"/>
                    <circle cx="220" cy="70" r="15" fill="#D49AFF" fill-opacity=".08"/>
                </g>
                <g class="trios-orbit-ring" style="animation-duration: 17s;">
                    <circle cx="220" cy="58" r="5.2" fill="#FFFFFF"/>
                </g>
                <circle cx="220" cy="220" r="72" fill="#79E4FF" fill-opacity=".08" filter="url(#triosBlur)"/>
                <circle cx="220" cy="220" r="56" fill="url(#triosCore)"/>
                <circle cx="220" cy="220" r="12" fill="#F7FCFF"/>
            </svg>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_action_card(icon, title, description, button_label, callback_key):
    with st.container(border=True):
        render_icon(icon, size=28)
        st.subheader(title)
        st.caption(description)
        return st.button(button_label, use_container_width=True, key=callback_key)


def google_is_logged_in():
    return bool(getattr(st.user, "is_logged_in", False))


def google_identity():
    return {
        "sub": getattr(st.user, "sub", None),
        "email": getattr(st.user, "email", ""),
        "name": getattr(st.user, "name", ""),
    }


NAVIGATION_PAGES = {}


def navigate(page):
    target = NAVIGATION_PAGES.get(page)
    if target is None:
        raise ValueError(f"Unknown TRIOS page: {page}")
    st.switch_page(target)


def start_google_login(flow):
    st.session_state.google_flow = flow
    st.login("google")


def set_logged_in_user(data, welcome_message=None, new_account=False):
    st.session_state.user = data["username"]
    st.session_state.pop("welcome_message", None)
    st.session_state.new_account = new_account
    if welcome_message:
        st.session_state.welcome_message = welcome_message

    try:
        from cloud_storage import cloud_enabled, create_session

        if cloud_enabled():
            token = create_session(data["username"])
            st.query_params["session"] = token
    except Exception:
        pass

    navigate("dashboard")


def restore_web_session():
    if "user" in st.session_state:
        return

    token = st.query_params.get("session")
    if not token:
        return

    try:
        from cloud_storage import cloud_enabled, get_session_user

        if not cloud_enabled():
            return

        username = get_session_user(token)
        if not username:
            del st.query_params["session"]
            return

        profile = user_profile(username)
        st.session_state.user = profile["username"]
    except Exception:
        return


def clear_web_session():
    token = st.query_params.get("session")

    if token:
        try:
            from cloud_storage import cloud_enabled, delete_session

            if cloud_enabled():
                delete_session(token)
        except Exception:
            pass

        try:
            del st.query_params["session"]
        except KeyError:
            pass

    st.session_state.pop("user", None)
    st.session_state.pop("welcome_message", None)
    st.session_state.pop("google_identity", None)
    st.session_state.pop("google_flow", None)
    st.session_state.pop("new_account", None)


def process_google_identity():
    """Map the authenticated Google identity to a TRIOS profile."""
    if not google_is_logged_in() or "user" in st.session_state:
        return

    identity = google_identity()
    flow = st.session_state.get("google_flow", "login")
    st.session_state.google_identity = identity

    # Admin Google authentication is intentionally independent from TRIOS
    # account creation. The /admin page handles the authenticated state itself.
    if flow == "admin":
        return

    profile = google_profile(identity["sub"])

    if profile:
        set_logged_in_user(
            profile,
            t("welcome_back", name=profile["username"]),
            new_account=False,
        )

    if flow == "recover":
        st.session_state.google_recovery_error = True
        navigate("recover_google")

    navigate("google_profile")


def show_home():
    show_public_nav()

    st.markdown(
        f"""
        <section class="trios-hero">
            <div class="trios-kicker">
                <span class="trios-kicker-dot"></span>
                {t("hero_kicker")}
            </div>
            <h1>
                {t("hero_title_1")}
                <span class="trios-gradient-text">{t("hero_title_2")}</span>
            </h1>
            <p class="trios-hero-copy">{t("hero_copy")}</p>
        """,
        unsafe_allow_html=True,
    )

    show_hero_orbit()

    action_about, action_signup = st.columns([1, 1], gap="medium")
    with action_about:
        if st.button(t("about"), use_container_width=True, key="hero_about"):
            navigate("about")
    with action_signup:
        if st.button(t("nav_signup"), use_container_width=True, key="hero_signup"):
            navigate("register")

    st.markdown(
        f'<div class="trios-section-head"><div><h2>{t("section_title")}</h2></div><p>{t("section_copy")}</p></div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3, gap="medium")

    with c1:
        with st.container(border=True):
            render_icon("orbit", size=32)
            st.subheader(t("feature_motion"))
            st.caption(t("feature_motion_copy"))

    with c2:
        with st.container(border=True):
            render_icon("lab", size=32)
            st.subheader(t("feature_lab"))
            st.caption(t("feature_lab_copy"))

    with c3:
        with st.container(border=True):
            render_icon("chart", size=32)
            st.subheader(t("feature_results"))
            st.caption(t("feature_results_copy"))

    st.markdown(
        f"""
        <div class="trios-github">
            <div>
                <div class="trios-github-eyebrow">{t("github_eyebrow")}</div>
                <h3>{t("github_title")}</h3>
                <p>{t("github_copy")}</p>
            </div>
            <a href="https://github.com/natajdaniyal/trios" target="_blank" rel="noopener noreferrer">
                {t("github_button")}
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="trios-footer">{t("footer")}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("</section>", unsafe_allow_html=True)


def show_entry():
    show_public_nav()
    st.markdown('<div class="trios-page">', unsafe_allow_html=True)
    render_icon("orbit", size=32)
    st.markdown(
        f'<h1 style="text-align:center;margin-bottom:.35rem;">{t("login_title")}</h1>'
        f'<p style="text-align:center;color:#aeb9d8;">{t("choose_login")}</p>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2, gap="medium")

    with c1:
        with st.container(border=True):
            render_icon("google", size=30)
            st.subheader("Google")
            st.caption(t("google_fast"))
            if st.button(t("google_login"), use_container_width=True, key="google_login_button"):
                start_google_login("login")

    with c2:
        with st.container(border=True):
            render_icon("plus", size=30)
            st.subheader(t("native_account"))
            st.caption(t("native_fast"))
            if st.button(t("create_native"), use_container_width=True, key="register_button"):
                navigate("register")

    st.divider()

    c3, c4 = st.columns(2, gap="medium")
    with c3:
        if st.button(t("recover"), use_container_width=True, key="recover_button"):
            navigate("recover")
    with c4:
        if st.button(t("about"), use_container_width=True, key="entry_about_button"):
            navigate("about")

    if st.button(t("back"), use_container_width=True, key="entry_back"):
        navigate("home")

    st.markdown("</div>", unsafe_allow_html=True)


def show_recover():
    show_public_nav()
    st.markdown('<div class="trios-page">', unsafe_allow_html=True)
    render_icon("refresh", size=32)
    st.markdown(
        f'<h1 style="text-align:center;margin-bottom:.35rem;">{t("recover_title")}</h1>'
        f'<p style="text-align:center;color:#aeb9d8;">{t("recover_choose")}</p>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            render_icon("google", size=30)
            st.subheader("Google")
            st.caption(t("recover_google_copy"))
            if st.button(t("recover_google"), use_container_width=True, key="google_recover_button"):
                start_google_login("recover")

    with c2:
        with st.container(border=True):
            render_icon("lock", size=30)
            st.subheader(t("native_account"))
            st.caption(t("recover_native_copy"))
            if st.button(t("recover_native"), use_container_width=True):
                navigate("recover_trios")

    if st.button(t("back"), use_container_width=True, key="recover_back"):
        navigate("entry")

    st.markdown("</div>", unsafe_allow_html=True)


def show_recover_trios():
    show_public_nav()
    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("lock", size=30)
    st.header(t("recover_native_title"))
    st.info(t("recover_notice"))

    username = st.text_input(t("username"), key="recover_username")
    password = st.text_input(t("password"), type="password", key="recover_password")

    if st.button(t("login_account"), use_container_width=True):
        try:
            data = recover_user(username, password)
        except ValueError as exc:
            st.error(localized_error(exc))
        else:
            set_logged_in_user(
                data,
                t("welcome_back", name=data["username"]),
                new_account=False,
            )

    st.markdown("</div>", unsafe_allow_html=True)
    if st.button(t("back"), use_container_width=True, key="recover_trios_back"):
        navigate("recover")


def show_recover_google():
    show_public_nav()
    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("google", size=30)
    st.header(t("google_recovery_title"))
    st.error(t("google_not_linked"))

    if st.button(t("back_to_recovery"), use_container_width=True):
        st.session_state.pop("google_recovery_error", None)
        navigate("recover")

    if st.button(t("logout_google"), use_container_width=True):
        st.logout()

    st.markdown("</div>", unsafe_allow_html=True)


def show_register():
    show_public_nav()
    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("plus", size=30)
    st.header(t("register_title"))
    st.caption(t("choose_login"))

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            render_icon("google", size=30)
            st.subheader("Google")
            st.caption(t("google_fast"))
            if st.button(t("google_login"), use_container_width=True, key="register_google_button"):
                start_google_login("login")

    with c2:
        with st.container(border=True):
            render_icon("plus", size=30)
            st.subheader(t("native_account"))
            st.caption(t("native_fast"))

            username = st.text_input(t("username"), key="register_username")
            password = st.text_input(t("password"), type="password", key="register_password")
            confirm = st.text_input(t("confirm_password"), type="password", key="register_confirm")

            if st.button(t("register"), use_container_width=True, key="register_native_button"):
                if password != confirm:
                    st.error(t("password_mismatch"))
                else:
                    try:
                        data = create_user(username, password)
                    except ValueError as exc:
                        st.error(str(exc))
                    else:
                        set_logged_in_user(
                            data,
                            t("welcome", name=data["username"]),
                            new_account=True,
                        )

    st.divider()

    if st.button(t("recover"), use_container_width=True, key="register_recover_button"):
        navigate("recover")

    if st.button(t("back"), use_container_width=True, key="register_back"):
        navigate("entry")

    st.markdown("</div>", unsafe_allow_html=True)


def show_google_profile():
    show_public_nav()
    identity = st.session_state.get("google_identity", google_identity())

    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("google", size=30)
    st.header(t("profile_title"))
    st.write(t("profile_google_done"))

    if identity.get("name"):
        st.caption(t("google_account", name=identity["name"]))

    username = st.text_input(t("trios_username"), key="google_username")

    if st.button(t("create_profile"), use_container_width=True):
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
            set_logged_in_user(
                data,
                t("welcome", name=data["username"]),
                new_account=True,
            )

    if st.button(t("logout_google"), use_container_width=True):
        st.logout()

    st.markdown("</div>", unsafe_allow_html=True)


def show_dashboard():
    username = st.session_state.user

    show_public_nav()

    left, right = st.columns([1, 8], vertical_alignment="center")
    with left:
        st.image("assets/trios_logo.png", width=94)
    with right:
        is_new_account = st.session_state.pop("new_account", False)
        greeting = st.session_state.pop("welcome_message", None)
        if is_new_account:
            title = t("welcome", name=username)
        elif greeting:
            title = greeting
        else:
            title = f'{t("dashboard_title")} <span class="trios-gradient-text">{username}</span>'
        st.markdown(
            f"""
            <div class="trios-hero" style="padding:2.5rem 1.5rem 1.7rem;margin-top:0;">
                <div class="trios-kicker">
                    <span class="trios-kicker-dot"></span>
                    {t("dashboard_kicker")}
                </div>
                <h1 style="font-size:clamp(2rem,4.8vw,4rem);">
                    {title}
                </h1>
                <p class="trios-hero-copy">{t("dashboard_copy")}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f'<div class="trios-section-head"><div><h2>{t("path_title")}</h2></div><p>{t("path_copy")}</p></div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        if render_action_card("rocket", t("start_experiment"), t("start_experiment_copy"), t("start_experiment"), "dashboard_lab"):
            navigate("lab")
    with c2:
        if render_action_card("chart", t("view_report"), t("report_copy"), t("view_report"), "dashboard_report"):
            navigate("report")
    with c3:
        if render_action_card("profile", t("profile"), t("profile_copy"), t("profile"), "dashboard_profile"):
            navigate("profile")

    st.markdown("<div style='height:.5rem'></div>", unsafe_allow_html=True)
    if _is_admin():
        if st.button(t("account_stats_title"), use_container_width=True, key="dashboard_account_stats"):
            navigate("account_stats")


def show_profile():
    username = st.session_state.user
    data = user_profile(username)

    show_public_nav()
    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("profile", size=32)
    st.header(t("profile"))
    st.subheader(t("profile_info"))
    st.write(f"**{t('username')}:** {data['username']}")
    if data.get("auth_method") == "google":
        st.caption("Google")

    st.divider()
    st.subheader(t("account_management"))

    if st.button(t("logout_device"), use_container_width=True):
        clear_web_session()
        if data.get("auth_method") == "google":
            st.logout()
        navigate("home")

    st.divider()
    st.subheader(t("delete_account"))
    st.warning(t("delete_warning"))
    confirm_delete = st.checkbox(t("delete_confirm"))

    if st.button(t("delete_account"), use_container_width=True):
        if not confirm_delete:
            st.error(t("confirm_delete_error"))
        elif delete_user(username):
            clear_web_session()
            if data.get("auth_method") == "google":
                st.logout()
            navigate("home")
        else:
            st.error(t("account_not_found"))

    st.markdown("</div>", unsafe_allow_html=True)
    if st.button(t("back"), use_container_width=True):
        navigate("dashboard")

    st.markdown(
        f"""
        <div class="trios-github">
            <div>
                <div class="trios-github-eyebrow">{t("github_eyebrow")}</div>
                <h3>{t("github_title")}</h3>
                <p>{t("github_copy")}</p>
            </div>
            <a href="https://github.com/natajdaniyal/trios" target="_blank" rel="noopener noreferrer">
                {t("github_button")}
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_lab():
    show_public_nav()
    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("lab", size=32)
    st.header(t("lab_title"))
    st.info(t("lab_notice"))
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button(t("back"), use_container_width=True):
        navigate("dashboard")


def show_report():
    data = user_profile(st.session_state.user)

    show_public_nav()
    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("chart", size=32)
    st.header(t("report_title"))
    st.subheader(t("report_summary"))

    st.write(f"**{t('level')}:** {data['level']}")
    st.write(f"**{t('attempts')}:** {data['total_attempts']}")
    st.write(f"**{t('correct')}:** {data['correct_answers']}")
    st.write(f"**{t('accuracy')}:** {data['accuracy']}%")

    if data["experiments"]:
        st.subheader(t("experiments"))
        for experiment in data["experiments"]:
            status = t("status_correct") if experiment["correct"] else t("status_incorrect")
            st.write(f"**{experiment['name']}** — {status}")
    else:
        st.info(t("no_report"))

    st.markdown("</div>", unsafe_allow_html=True)
    if st.button(t("back"), use_container_width=True):
        navigate("dashboard")


def _touch_current_web_session():
    token = st.query_params.get("session")
    if not token:
        return
    try:
        from cloud_storage import cloud_enabled, touch_session
        if cloud_enabled():
            touch_session(token)
    except Exception:
        pass


def _admin_email():
    """Read the admin Google email from common Streamlit Secrets locations."""
    try:
        direct = st.secrets.get("TRIOS_ADMIN_EMAIL")
        if direct:
            return str(direct).strip().casefold()

        for section_name in ("admin", "auth"):
            section = st.secrets.get(section_name, {})
            if isinstance(section, dict):
                value = section.get("TRIOS_ADMIN_EMAIL") or section.get("email")
                if value:
                    return str(value).strip().casefold()

        connections = st.secrets.get("connections", {})
        if isinstance(connections, dict):
            trios_db = connections.get("trios_db", {})
            if isinstance(trios_db, dict):
                value = trios_db.get("TRIOS_ADMIN_EMAIL")
                if value:
                    return str(value).strip().casefold()
    except Exception:
        return ""

    return ""



def _is_admin():
    """Admin access is independent from TRIOS accounts and is tied to one Google email."""
    if not bool(getattr(st.user, "is_logged_in", False)):
        return False

    admin_email = _admin_email()
    google_email = str(getattr(st.user, "email", "")).strip().casefold()

    return bool(admin_email) and bool(google_email) and google_email == admin_email


def show_account_stats():
    if not google_is_logged_in():
        st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
        render_icon("google", size=32)
        st.header("TRIOS Admin")
        st.caption("Sign in with the authorized Google account to continue.")
        if st.button(t("google_login"), use_container_width=True, key="admin_google_login"):
            start_google_login("admin")
        st.markdown("</div>", unsafe_allow_html=True)
        return

    if not _is_admin():
        st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
        render_icon("profile", size=32)
        st.header("TRIOS Admin")
        st.error("This Google account is not authorized for the private admin panel.")
        if not _admin_email():
            st.caption("Admin email is not configured in Streamlit Secrets.")
        else:
            st.caption("The Admin email is configured, but this Google account does not match it.")
        st.markdown("</div>", unsafe_allow_html=True)
        return

    show_public_nav()

    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)
    render_icon("chart", size=32)
    st.header(t("account_stats_title"))

    try:
        from cloud_storage import get_account_stats
        stats = get_account_stats()
    except Exception:
        st.error("Account statistics are temporarily unavailable.")
        st.markdown("</div>", unsafe_allow_html=True)
        return

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.metric(t("total_accounts"), stats["total_accounts"])
    with c2:
        st.metric(t("active_users"), stats["active_users"])

    st.caption(t("active_users_definition"))
    st.caption(f'{t("active_sessions")}: {stats["active_sessions"]}')

    if st.button(t("refresh_stats"), use_container_width=True, key="refresh_account_stats"):
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

def show_about():
    show_public_nav()
    st.markdown('<div class="trios-page-card">', unsafe_allow_html=True)

    logo_col, content_col = st.columns([1.15, 4.85], vertical_alignment="center")
    with logo_col:
        st.image("assets/trios_logo.png", width=92)
    with content_col:
        st.header(t("about_title"))

    st.write(t("about_text_1"))
    st.write(t("about_text_2"))
    st.write(t("about_text_3"))
    st.write(t("about_text_4"))
    st.info(t("about_notice"))

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button(t("back"), use_container_width=True, key="about_back"):
        navigate("dashboard" if "user" in st.session_state else "home")


apply_trios_design()
apply_language_direction()

NAVIGATION_PAGES.update(
    {
        "home": st.Page(show_home, title="TRIOS", default=True, visibility="hidden"),
        "entry": st.Page(show_entry, title=t("login_title"), url_path="login", visibility="hidden"),
        "register": st.Page(show_register, title=t("register_title"), url_path="register", visibility="hidden"),
        "recover": st.Page(show_recover, title=t("recover_title"), url_path="recover", visibility="hidden"),
        "recover_trios": st.Page(
            show_recover_trios,
            title=t("recover_native_title"),
            url_path="recover-trios",
            visibility="hidden",
        ),
        "recover_google": st.Page(
            show_recover_google,
            title=t("google_recovery_title"),
            url_path="recover-google",
            visibility="hidden",
        ),
        "google_profile": st.Page(
            show_google_profile,
            title=t("profile_title"),
            url_path="google-profile",
            visibility="hidden",
        ),
        "dashboard": st.Page(
            show_dashboard,
            title=t("dashboard_title"),
            url_path="dashboard",
            visibility="hidden",
        ),
        "profile": st.Page(
            show_profile,
            title=t("profile"),
            url_path="profile",
            visibility="hidden",
        ),
        "lab": st.Page(
            show_lab,
            title=t("lab_title"),
            url_path="lab",
            visibility="hidden",
        ),
        "report": st.Page(
            show_report,
            title=t("report_title"),
            url_path="report",
            visibility="hidden",
        ),
        "account_stats": st.Page(
            show_account_stats,
            title=t("account_stats_title"),
            url_path="admin",
            visibility="hidden",
        ),
        "about": st.Page(
            show_about,
            title=t("about_title"),
            url_path="about",
            visibility="hidden",
        ),
    }
)

navigation = st.navigation(
    list(NAVIGATION_PAGES.values()),
    position="hidden",
)

restore_web_session()
_touch_current_web_session()
process_google_identity()

if "user" not in st.session_state and navigation.url_path in {
    "dashboard",
    "profile",
    "lab",
    "report",
}:
    st.switch_page(NAVIGATION_PAGES["home"])

navigation.run()
