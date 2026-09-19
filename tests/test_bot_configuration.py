import pytest

from bot_configuration import BotConfiguration, KeywordMatcher, normalize_text
from experiment_definition import ExperimentDefinition
from physical_configuration import BodyPhysicalConfiguration, StagePhysicalConfiguration


def make_config():
    configuration = StagePhysicalConfiguration("stage-1")
    configuration.add_body(BodyPhysicalConfiguration("A", 10.0))
    return configuration


def test_bot_configuration_stores_question_and_keywords():
    configuration = BotConfiguration(
        "چه اتفاقی می‌افتد؟",
        ["جذب", "نزدیک"],
    )

    assert configuration.question == "چه اتفاقی می‌افتد؟"
    assert configuration.keywords == ("جذب", "نزدیک")
    assert configuration.minimum_matches == 1


def test_bot_configuration_rejects_empty_question_and_keywords():
    with pytest.raises(ValueError):
        BotConfiguration("", ["جذب"])

    with pytest.raises(ValueError):
        BotConfiguration("سؤال", [])

    with pytest.raises(ValueError):
        BotConfiguration("سؤال", [""])


def test_bot_configuration_deduplicates_keywords():
    configuration = BotConfiguration(
        "سؤال",
        ["Gravity", "gravity", " جذب "],
    )

    assert configuration.keywords == ("Gravity", "جذب")


def test_bot_configuration_validates_minimum_matches():
    with pytest.raises(ValueError):
        BotConfiguration("سؤال", ["a"], minimum_matches=0)

    with pytest.raises(ValueError):
        BotConfiguration("سؤال", ["a"], minimum_matches=2)

    with pytest.raises(TypeError):
        BotConfiguration("سؤال", ["a"], minimum_matches=True)


def test_keyword_matcher_matches_any_keyword_by_default():
    configuration = BotConfiguration("سؤال", ["جاذبه", "نزدیک"])
    matcher = KeywordMatcher(configuration)

    assert matcher.matches("دو جسم به خاطر جاذبه به هم نزدیک می‌شوند")
    assert matcher.match_count("دو جسم به خاطر جاذبه حرکت می‌کنند") == 1


def test_keyword_matcher_can_require_multiple_keywords():
    configuration = BotConfiguration(
        "سؤال",
        ["جاذبه", "نزدیک", "هم"],
        minimum_matches=2,
    )
    matcher = KeywordMatcher(configuration)

    assert matcher.matches("به خاطر جاذبه به هم نزدیک می‌شوند")
    assert not matcher.matches("فقط جاذبه")


def test_keyword_matcher_normalizes_case_and_persian_arabic_variants():
    assert normalize_text(" كِشِش  ي") == normalize_text("کِشِش ی")

    configuration = BotConfiguration("سؤال", ["کشش گرانشی"])
    matcher = KeywordMatcher(configuration)

    assert matcher.matches("کِشِش گرانشی")


def test_keyword_matcher_rejects_non_string_answer():
    matcher = KeywordMatcher(BotConfiguration("سؤال", ["جاذبه"]))

    with pytest.raises(TypeError):
        matcher.matches(None)

    assert not matcher.matches("")


def test_experiment_definition_accepts_bot_configuration():
    bot = BotConfiguration(
        "چه اتفاقی می‌افتد؟",
        ["جذب", "نزدیک"],
    )
    definition = ExperimentDefinition(
        "gravity",
        make_config(),
        bot_configuration=bot,
    )

    assert definition.bot_configuration is bot


def test_experiment_definition_rejects_invalid_bot_configuration():
    with pytest.raises(TypeError):
        ExperimentDefinition(
            "gravity",
            make_config(),
            bot_configuration=object(),
        )
