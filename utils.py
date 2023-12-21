# File: bookings/utils.py

import calendar
from datetime import datetime, timedelta

class Calendar:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def formatmonth(self, withyear=True):
        cal = calendar.monthcalendar(self.year, self.month)
        month_name = calendar.month_name[self.month]
        if withyear:
            return f"{month_name} {self.year}\n" + self._formatmonth(cal)
        else:
            return f"{month_name}\n" + self._formatmonth(cal)

    def formatweek(self, start_date, end_date):
        cal = calendar.monthcalendar(self.year, self.month)
        week_str = ""
        for week in cal:
            for day in week:
                if start_date <= datetime(self.year, self.month, day) <= end_date:
                    week_str += f"{day:2} "
                else:
                    week_str += "   "
            week_str += "\n"
        return week_str

    def _formatmonth(self, cal):
        month_str = ""
        for week in cal:
            for day in week:
                if day == 0:
                    month_str += "   "
                else:
                    month_str += f"{day:2} "
            month_str += "\n"
        return month_str
