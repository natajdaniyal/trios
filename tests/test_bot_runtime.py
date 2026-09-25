import pytest

from bot_configuration import BotConfiguration
from bot_runtime import BotEvaluationResult, BotRuntime


def make_translations():
    return {
        "fa": {"question": "چه اتفاقی می‌افتد؟", "keywords": ["جاذبه", "نزدیک"]},
        "en": {"question": "What happens?", "keywords": ["gravity", "closer"]},
        "ar": {"question": "ماذا يحدث؟", "keywords": ["جاذبية", "أقرب"]},
        "zh": {"question": "会发生什么？", "keywords": ["引力", "靠近"]},
        "es": {"question": "¿Qué sucede?", "keywords": ["gravedad", "cerca"]},
        "fr": {"question": "Que se passe-t-il ?", "keywords": ["gravité", "proche"]},
        "de": {"question": "Was passiert?", "keywords": ["gravitation", "näher"]},
        "ja": {"question": "何が起こりますか？", "keywords": ["重力", "近づく"]},
    }


def test_bot_runtime_returns_question():
    runtime = BotRuntime(BotConfiguration(make_translations()))

    assert runtime.question("en") == "What happens?"
    assert runtime.question("fa") == "چه اتفاقی می‌افتد؟"


def test_bot_runtime_evaluates_correct_prediction():
    runtime = BotRuntime(
        BotConfiguration(make_translations(), minimum_matches=2)
    )

    result = runtime.evaluate(
        "Gravity makes the bodies closer.",
        "en",
    )

    assert isinstance(result, BotEvaluationResult)
    assert result.language == "en"
    assert result.matched_keywords == ("gravity", "closer")
    assert result.match_count == 2
    assert result.required_matches == 2
    assert result.is_correct is True


def test_bot_runtime_evaluates_incomplete_prediction():
    runtime = BotRuntime(
        BotConfiguration(make_translations(), minimum_matches=2)
    )

    result = runtime.evaluate("Gravity affects them.", "en")

    assert result.matched_keywords == ("gravity",)
    assert result.match_count == 1
    assert result.required_matches == 2
    assert result.is_correct is False


def test_bot_runtime_supports_multilingual_evaluation():
    runtime = BotRuntime(BotConfiguration(make_translations()))

    result = runtime.evaluate(
        "دو جسم به خاطر جاذبه به هم نزدیک می‌شوند.",
        "fa",
    )

    assert result.matched_keywords == ("جاذبه", "نزدیک")
    assert result.is_correct is True


def test_bot_runtime_rejects_invalid_configuration():
    with pytest.raises(TypeError):
        BotRuntime(object())


def test_bot_runtime_preserves_answer_in_result():
    answer = "The gravity makes them closer."
    runtime = BotRuntime(BotConfiguration(make_translations()))

    result = runtime.evaluate(answer, "en")

    assert result.answer == answer


def test_bot_runtime_delegates_validation():
    runtime = BotRuntime(BotConfiguration(make_translations()))

    with pytest.raises(TypeError):
        runtime.evaluate(None, "en")

    with pytest.raises(ValueError):
        runtime.evaluate("gravity", "it")




def test_bot_accepts_persian_spacing_variants():
    from first_experiment import first_stage_challenges
    from first_experiment_runtime import evaluate_challenge_prediction
    challenge = first_stage_challenges()[2]
    answer = "هر آهن‌ربا هم زمان از دو آهنربای دیگر تأثیر می‌گیرد؛ بنابراین حرکت هرکدام به حرکت بقیه وابسته است."
    assert evaluate_challenge_prediction(challenge, answer, "fa").is_correct is True
