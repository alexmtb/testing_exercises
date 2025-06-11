import datetime


def compose_datetime_from(date_str: str, time_str: str) -> datetime.datetime:
    date = datetime.date.today()
    if date_str == "tomorrow":
        date += datetime.timedelta(days=1)

    hour_str, minute_str = time_str.strip().split(":")
    return datetime.datetime(
        date.year,
        date.month,
        date.day,
        int(hour_str),
        int(minute_str),
    )

if __name__ == "__main__":
    # Example usage
    print(compose_datetime_from("tomorrow", "12:30"))
    print(compose_datetime_from("today", "14:45"))
    print(compose_datetime_from("yesterday", "08:15"))

