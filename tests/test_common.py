from tools.common import (
    DAMAGE_TYPES,
    format_money,
    is_valid_dice,
    is_valid_money,
    money_to_pence,
    parse_dice,
)


def test_parse_dice_and_alternatives() -> None:
    assert parse_dice("2d8") == (2, 8)
    assert is_valid_dice("1d8/1d10")
    assert not is_valid_dice("d8")
    assert not is_valid_dice("2d0")


def test_money_parsing_and_formatting() -> None:
    assert money_to_pence("£1 5s 4d") == 304
    assert format_money(304) == "£1 5s 4d"
    assert is_valid_money("4s–6s")
    assert is_valid_money("—")
    assert not is_valid_money("five shillings")


def test_permitted_damage_types_are_complete() -> None:
    assert DAMAGE_TYPES == {
        "Slashing",
        "Piercing",
        "Bludgeoning",
        "Shot",
        "Burning",
        "Shocking",
        "Toxic",
        "Freezing",
    }
