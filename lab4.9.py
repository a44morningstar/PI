from datetime import datetime as dt
from datetime import timedelta as td


def main():
    print(
        f"Today is {dt.today().date()}. " f"Day of the week - {dt.today().isoweekday()}"
    )
    n = int(input())
    today = dt.today()
    res = today + td(days=n)
    print(
        f"In {n} days is gonna be {res.date()}. "
        f"Day of the week - {res.isoweekday()}"
    )


if __name__ == "__main__":
    main()
