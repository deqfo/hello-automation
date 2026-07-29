# dates are easily constructed and formatted
import datetime as dt

now = dt.datetime.now(dt.UTC)


def greet(now: dt.datetime) -> str:
    return f"Hola! The current date and time is {now}"


print(greet(now))
