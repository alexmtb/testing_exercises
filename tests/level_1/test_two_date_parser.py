import datetime
from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from_tomorrow():
    # Test that passing "tomorrow" yields a datetime with tomorrow's date.
    tomorrow_date = datetime.date.today() + datetime.timedelta(days=1)
    expected_dt = datetime.datetime(
        tomorrow_date.year,
        tomorrow_date.month,
        tomorrow_date.day,
        hour=12,
        minute=30
    )
    assert compose_datetime_from("tomorrow", "12:30") == expected_dt