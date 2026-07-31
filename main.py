# dates are easily constructed and formatted
import datetime as dt

now = dt.datetime.now(dt.UTC)


def greet(now: dt.datetime) -> str:
    with open("greet.txt", "w") as f:
        f.write(f"Hola! The week has just started! It is currently: {now}")


greet(now)
