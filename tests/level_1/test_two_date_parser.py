import datetime
import pytest
from functions.level_1.two_date_parser import compose_datetime_from

@pytest.mark.parametrize(
    "date_str,time_str,expected_result",
    [
        ("tomorrow", "12:30", datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), datetime.time(12, 30))),
        ("today", "14:44", datetime.datetime.combine(datetime.date.today(), datetime.time(14, 44))),
        ("anyday", "02:22", datetime.datetime.combine(datetime.date.today(), datetime.time(2, 22))),
        ("", "11:11", datetime.datetime.combine(datetime.date.today(), datetime.time(11, 11)))
    ]
)
def test__compose_datetime_from__returns_tomorrow_datetime_if_word_tomorrow_given(date_str, time_str, expected_result):
    assert compose_datetime_from(date_str, time_str) == expected_result


@pytest.mark.parametrize(
    "date_str,time_str",
    [
        ("tomorrow", "25:30"),
        ("today", "14:64"),
        ("anyday", "02-22"),
        ("nowadays", "0028")
    ]
)
def test__compose_datetime_from__raises_value_error_on_bad_time_format(date_str, time_str):
    with pytest.raises(ValueError):
        compose_datetime_from(date_str, time_str)
