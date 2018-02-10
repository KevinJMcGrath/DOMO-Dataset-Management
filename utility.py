from datetime import datetime, timedelta

# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior


def GetCurrentQuarterStartDate() -> datetime:
    return FindQuarterDates(datetime.now())[0]


def GetCurrentQuarterEndDate() -> datetime:
    return FindQuarterDates(datetime.now())[1]


def FindQuarterDates(dt: datetime) -> (datetime, datetime):
    quarter = (dt.month - 1) // 3 + 1
    sDate = datetime(dt.year, 3 * quarter - 2, 1)
    eDate = datetime(dt.year, int(3 * quarter + 1), 1) + timedelta(days=-1)

    return sDate, eDate


def DateTimeToISO8601(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def DateTimeAddSeconds(dt: datetime, secs: int) -> datetime:
    return dt + timedelta(seconds=secs)


def CurrentDateTimeAddSeconds(secs: int) -> datetime:
    return DateTimeAddSeconds(datetime.now(), secs)