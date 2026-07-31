# dates are easily constructed and formatted
import datetime as dt

now = dt.datetime.now(dt.UTC)


def greet(now: dt.datetime) -> str:
    with open("greet.txt", "w") as f:
        f.write(f"Hola! The current date and time is {now}")


greet(now)
