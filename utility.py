from datetime import datetime, timedelta
import json
import inspect

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


# JSONEncoder override
class ObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "to_json"):
            return self.default(obj.to_json())
        elif hasattr(obj, "__dict__"):
            d = dict(
                (key, value)
                for key, value in inspect.getmembers(obj)
                if not key.startswith("__")
                and not inspect.isabstract(value)
                and not inspect.isbuiltin(value)
                and not inspect.isfunction(value)
                and not inspect.isgenerator(value)
                and not inspect.isgeneratorfunction(value)
                and not inspect.ismethod(value)
                and not inspect.ismethoddescriptor(value)
                and not inspect.isroutine(value)
            )
            return self.default(d)
        return obj


def ExportModelToJSON(modelObj):
    return json.dumps(modelObj, cls=ObjectEncoder)