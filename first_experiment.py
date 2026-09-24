"""First TRIOS educational experiment content.

Stage 1 introduces why a three-body problem is harder than a two-body
interaction by using magnetic attraction, magnetic repulsion, and finally
three interacting magnets.
"""

from bot_configuration import BotConfiguration
from experiment_challenge import ExperimentChallenge


FIRST_EXPERIMENT_ID = "three-body-is-hard"


def _challenge(
    challenge_id,
    scenario_id,
    questions,
    keywords,
    answers,
    explanations,
    hints,
    minimum_matches=1,
):
    return ExperimentChallenge(
        challenge_id,
        BotConfiguration(
            {
                language: {
                    "question": questions[language],
                    "keywords": keywords[language],
                    "answer": answers[language],
                    "explanation": explanations[language],
                    "hint": hints[language],
                }
                for language in (
                    "fa", "en", "ar", "zh", "es", "fr", "de", "ja"
                )
            },
            minimum_matches=minimum_matches,
        ),
        scenario_id,
    )


_STAGE_ONE_SHARED_QUESTION = {
    "fa": "اگر این دو آهنربا را کنار هم بگذاری، فکر می‌کنی چه اتفاقی می‌افتد؟",
    "en": "What do you think will happen if you place these two magnets next to each other?",
    "ar": "ماذا تعتقد أنه سيحدث إذا وضعت هذين المغناطيسين بجانب بعضهما؟",
    "zh": "如果把这两个磁铁放在一起，你觉得会发生什么？",
    "es": "¿Qué crees que ocurrirá si colocas estos dos imanes uno junto al otro?",
    "fr": "Que penses-tu qu'il se passera si tu places ces deux aimants côte à côte ?",
    "de": "Was glaubst du, passiert, wenn du diese beiden Magnete nebeneinander legst?",
    "ja": "この2つの磁石を隣に置くと、何が起こると思いますか？",
}

_STAGE_ONE_CHALLENGE_THREE_QUESTION = {
    "fa": "اگر این سه آهنربا را کنار هم بگذاری، فکر می‌کنی چه اتفاقی می‌افتد؟ چرا این مسئله سخت‌تر می‌شود؟",
    "en": "What do you think will happen if you place these three magnets together? Why does this become harder?",
    "ar": "ماذا تعتقد أنه سيحدث إذا وضعت هذه المغناطيسات الثلاثة معًا؟ ولماذا تصبح المسألة أصعب؟",
    "zh": "如果把这三个磁铁放在一起，你觉得会发生什么？为什么这会变得更难？",
    "es": "¿Qué crees que ocurrirá si colocas estos tres imanes juntos? ¿Por qué se vuelve más difícil?",
    "fr": "Que penses-tu qu'il se passera avec ces trois aimants ? Pourquoi cela devient-il plus difficile ?",
    "de": "Was glaubst du, passiert mit diesen drei Magneten zusammen? Warum wird es schwieriger?",
    "ja": "この3つの磁石を一緒に置くと、何が起こると思いますか？ なぜ難しくなるのでしょうか？",
}

STAGE_ONE_CHALLENGES = (
    _challenge(
        "stage-1-challenge-1",
        "opposite-poles",
        _STAGE_ONE_SHARED_QUESTION,
        {
            "fa": ["جذب", "نزدیک", "می‌کشند"],
            "en": ["attract", "closer", "pull"],
            "ar": ["تجذب", "تقترب", "تسحب"],
            "zh": ["吸引", "靠近", "拉"],
            "es": ["atraen", "acercan", "empujan"],
            "fr": ["attirent", "rapprochent", "tirent"],
            "de": ["anziehen", "näher", "ziehen"],
            "ja": ["引き合う", "近づく", "引っ張る"],
        },
        {
            "fa": "آن‌ها همدیگر را جذب می‌کنند و به هم نزدیک می‌شوند.",
            "en": "They attract each other and move closer together.",
            "ar": "سيتجاذبان ويتحركان نحو بعضهما.",
            "zh": "它们会相互吸引并靠近。",
            "es": "Se atraen y se acercan.",
            "fr": "Ils s'attirent et se rapprochent.",
            "de": "Sie ziehen sich an und bewegen sich aufeinander zu.",
            "ja": "互いに引き合い、近づきます。",
        },
        {
            "fa": "قطب‌های مخالف یکدیگر را جذب می‌کنند.",
            "en": "Opposite poles attract each other.",
            "ar": "القطبان المتعاكسان يتجاذبان.",
            "zh": "相反的磁极会相互吸引。",
            "es": "Los polos opuestos se atraen.",
            "fr": "Les pôles opposés s'attirent.",
            "de": "Entgegengesetzte Pole ziehen sich an.",
            "ja": "異なる極同士は引き合います。",
        },
        {
            "fa": "به علامت قطب‌های دو آهنربا نگاه کن.",
            "en": "Look at the pole labels on the two magnets.",
            "ar": "انظر إلى علامتي القطبين على المغناطيسين.",
            "zh": "看看两个磁铁的磁极标记。",
            "es": "Mira las etiquetas de los polos de los dos imanes.",
            "fr": "Regarde les indications des pôles sur les deux aimants.",
            "de": "Schau dir die Polmarkierungen der beiden Magnete an.",
            "ja": "2つの磁石の極の表示に注目してください。",
        },
    ),
    _challenge(
        "stage-1-challenge-2",
        "same-poles",
        _STAGE_ONE_SHARED_QUESTION,
        {
            "fa": ["دفع", "دور", "هل می‌دهند"],
            "en": ["repel", "apart", "push"],
            "ar": ["تتنافر", "تبتعد", "تدفع"],
            "zh": ["排斥", "远离", "推开"],
            "es": ["repelen", "alejan", "empujan"],
            "fr": ["repoussent", "s'éloignent", "poussent"],
            "de": ["abstoßen", "auseinander", "drücken"],
            "ja": ["反発", "離れる", "押し合う"],
        },
        {
            "fa": "آن‌ها همدیگر را دفع می‌کنند و از هم دور می‌شوند.",
            "en": "They repel each other and move apart.",
            "ar": "سيتنافران ويبتعدان عن بعضهما.",
            "zh": "它们会相互排斥并远离。",
            "es": "Se repelen y se alejan.",
            "fr": "Ils se repoussent et s'éloignent.",
            "de": "Sie stoßen sich ab und bewegen sich auseinander.",
            "ja": "互いに反発し、離れていきます。",
        },
        {
            "fa": "قطب‌های هم‌نام یکدیگر را دفع می‌کنند.",
            "en": "Like poles repel each other.",
            "ar": "الأقطاب المتشابهة تتنافر.",
            "zh": "相同的磁极会相互排斥。",
            "es": "Los polos iguales se repelen.",
            "fr": "Les pôles identiques se repoussent.",
            "de": "Gleichnamige Pole stoßen sich ab.",
            "ja": "同じ極同士は反発します。",
        },
        {
            "fa": "این بار به این توجه کن که قطب‌ها هم‌نام هستند.",
            "en": "This time, notice that the poles have the same label.",
            "ar": "هذه المرة، لاحظ أن القطبين يحملان العلامة نفسها.",
            "zh": "这一次，注意两个磁极的标记相同。",
            "es": "Esta vez, fíjate en que los polos tienen la misma etiqueta.",
            "fr": "Cette fois, remarque que les deux pôles portent la même indication.",
            "de": "Diesmal sind die beiden Pole gleichnamig.",
            "ja": "今回は、2つの極が同じ種類であることに注目してください。",
        },
    ),
    _challenge(
        "stage-1-challenge-3",
        "three-magnets",
        _STAGE_ONE_CHALLENGE_THREE_QUESTION,
        {
            "fa": ["همزمان", "دو آهنربای دیگر", "اثر", "وابسته"],
            "en": ["at the same time", "two other magnets", "affect", "depend"],
            "ar": ["في الوقت نفسه", "المغناطيسين الآخرين", "يؤثر", "يعتمد"],
            "zh": ["同时", "另外两个磁铁", "影响", "取决于"],
            "es": ["al mismo tiempo", "los otros dos imanes", "afecta", "depende"],
            "fr": ["en même temps", "deux autres aimants", "influence", "dépend"],
            "de": ["gleichzeitig", "die beiden anderen Magnete", "beeinflusst", "abhängt"],
            "ja": ["同時に", "他の2つの磁石", "影響", "左右される"],
        },
        {
            "fa": "هر آهنربا هم‌زمان از دو آهنربای دیگر اثر می‌گیرد؛ بنابراین حرکت هرکدام به حرکت بقیه وابسته است.",
            "en": "Each magnet is affected by the other two at the same time, so the motion of each depends on the others.",
            "ar": "يتأثر كل مغناطيس بالمغناطيسين الآخرين في الوقت نفسه، لذلك تعتمد حركة كل واحد على الآخرين.",
            "zh": "每个磁铁都会同时受到另外两个磁铁的影响，所以每个磁铁的运动都取决于其他磁铁。",
            "es": "Cada imán recibe al mismo tiempo la influencia de los otros dos, así que el movimiento de cada uno depende de los demás.",
            "fr": "Chaque aimant est influencé en même temps par les deux autres, donc le mouvement de chacun dépend des autres.",
            "de": "Jeder Magnet wird gleichzeitig von den beiden anderen beeinflusst, daher hängt seine Bewegung von den anderen ab.",
            "ja": "それぞれの磁石は同時に他の2つの磁石から影響を受けるため、それぞれの動きは他の磁石に左右されます。",
        },
        {
            "fa": "وقتی سه جسم داریم، هرکدام هم‌زمان تحت تأثیر دو جسم دیگر قرار می‌گیرد؛ برای همین پیش‌بینی رفتار کل سیستم سخت‌تر می‌شود.",
            "en": "With three bodies, each one is affected by the other two at the same time, making the whole system harder to predict.",
            "ar": "عندما توجد ثلاثة أجسام، يتأثر كل واحد بالاثنين الآخرين في الوقت نفسه، لذلك يصبح سلوك النظام كله أصعب في التنبؤ.",
            "zh": "当有三个物体时，每个物体都会同时受到另外两个物体的影响，因此整个系统更难预测。",
            "es": "Con tres cuerpos, cada uno recibe al mismo tiempo la influencia de los otros dos, por lo que todo el sistema es más difícil de predecir.",
            "fr": "Avec trois corps, chacun est influencé en même temps par les deux autres, ce qui rend le système entier plus difficile à prévoir.",
            "de": "Bei drei Körpern wird jeder gleichzeitig von den beiden anderen beeinflusst, wodurch das Gesamtsystem schwerer vorherzusagen ist.",
            "ja": "3つの物体があると、それぞれが同時に他の2つから影響を受けるため、全体の予測が難しくなります。",
        },
        {
            "fa": "فقط یک جفت را نگاه نکن؛ هر آهنربا را نسبت به هر دو آهنربای دیگر در نظر بگیر.",
            "en": "Do not look at only one pair; consider each magnet in relation to both of the others.",
            "ar": "لا تنظر إلى زوج واحد فقط؛ فكّر في كل مغناطيس بالنسبة إلى المغناطيسين الآخرين.",
            "zh": "不要只看一对磁铁；要同时考虑每个磁铁与另外两个磁铁的关系。",
            "es": "No mires solo un par; considera cada imán en relación con los otros dos.",
            "fr": "Ne regarde pas seulement une paire ; considère chaque aimant par rapport aux deux autres.",
            "de": "Betrachte nicht nur ein Paar, sondern jeden Magneten im Verhältnis zu den beiden anderen.",
            "ja": "1組だけを見ないで、それぞれの磁石と他の2つとの関係を考えてみてください。",
        },
        minimum_matches=2,
    ),
)


def first_stage_challenges():
    """Return the immutable sequence of challenges for stage 1."""
    return STAGE_ONE_CHALLENGES
