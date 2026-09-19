import pytest

from bot_configuration import (
    SUPPORTED_LANGUAGES,
    BotConfiguration,
    KeywordMatcher,
    normalize_text,
)
from experiment_definition import ExperimentDefinition
from physical_configuration import BodyPhysicalConfiguration, StagePhysicalConfiguration


def make_config():
    configuration = StagePhysicalConfiguration("stage-1")
    configuration.add_body(BodyPhysicalConfiguration("A", 10.0))
    return configuration


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


def test_bot_configuration_stores_all_supported_languages():
    configuration = BotConfiguration(make_translations())

    assert configuration.languages() == SUPPORTED_LANGUAGES
    assert configuration.question("fa") == "چه اتفاقی می‌افتد؟"
    assert configuration.question("en") == "What happens?"
    assert configuration.keywords("de") == ("gravitation", "näher")
    assert configuration.minimum_matches == 1


def test_bot_configuration_rejects_missing_or_unsupported_languages():
    translations = make_translations()
    translations.pop("ja")

    with pytest.raises(ValueError):
        BotConfiguration(translations)

    translations = make_translations()
    translations["it"] = {"question": "Cosa succede?", "keywords": ["gravità"]}

    with pytest.raises(ValueError):
        BotConfiguration(translations)


def test_bot_configuration_rejects_invalid_localized_data():
    translations = make_translations()
    translations["fa"] = {"question": "", "keywords": ["جاذبه"]}

    with pytest.raises(ValueError):
        BotConfiguration(translations)

    translations = make_translations()
    translations["en"] = {"question": "What happens?", "keywords": []}

    with pytest.raises(ValueError):
        BotConfiguration(translations)

    translations = make_translations()
    translations["en"] = {"question": "What happens?", "keywords": ["gravity"]}

    with pytest.raises(ValueError):
        BotConfiguration(translations, minimum_matches=2)


def test_bot_configuration_deduplicates_keywords_per_language():
    translations = make_translations()
    translations["en"]["keywords"] = ["Gravity", "gravity", " closer "]

    configuration = BotConfiguration(translations)

    assert configuration.keywords("en") == ("Gravity", "closer")
    assert configuration.keywords("fa") == ("جاذبه", "نزدیک")


def test_bot_configuration_validates_language():
    configuration = BotConfiguration(make_translations())

    with pytest.raises(ValueError):
        configuration.question("it")

    with pytest.raises(ValueError):
        configuration.keywords("it")


def test_keyword_matcher_uses_selected_language_keywords():
    configuration = BotConfiguration(make_translations())
    matcher = KeywordMatcher(configuration)

    assert matcher.matches("دو جسم به خاطر جاذبه به هم نزدیک می‌شوند", "fa")
    assert matcher.matches("The gravity makes the bodies closer.", "en")

    assert not matcher.matches("The gravity makes the bodies closer.", "fa")
    assert not matcher.matches("دو جسم به خاطر جاذبه به هم نزدیک می‌شوند", "en")


def test_keyword_matcher_can_require_multiple_keywords_per_language():
    configuration = BotConfiguration(
        make_translations(),
        minimum_matches=2,
    )
    matcher = KeywordMatcher(configuration)

    assert matcher.matches("gravity makes them closer", "en")
    assert not matcher.matches("gravity only", "en")
    assert matcher.match_count("جاذبه و نزدیک", "fa") == 2


def test_keyword_matcher_normalizes_case_and_persian_arabic_variants():
    assert normalize_text(" كِشِش  ي") == normalize_text("کِشِش ی")

    translations = make_translations()
    translations["fa"]["keywords"] = ["کشش گرانشی"]
    configuration = BotConfiguration(translations)
    matcher = KeywordMatcher(configuration)

    assert matcher.matches("کِشِش گرانشی", "fa")


def test_keyword_matcher_rejects_non_string_answer():
    matcher = KeywordMatcher(BotConfiguration(make_translations()))

    with pytest.raises(TypeError):
        matcher.matches(None, "fa")

    assert not matcher.matches("", "fa")


def test_experiment_definition_accepts_multilingual_bot_configuration():
    bot = BotConfiguration(make_translations())
    definition = ExperimentDefinition(
        "gravity",
        make_config(),
        bot_configuration=bot,
    )

    assert definition.bot_configuration is bot
    assert definition.bot_configuration.question("en") == "What happens?"


def test_experiment_definition_rejects_invalid_bot_configuration():
    with pytest.raises(TypeError):
        ExperimentDefinition(
            "gravity",
            make_config(),
            bot_configuration=object(),
        )
