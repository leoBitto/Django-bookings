from datetime import datetime, timedelta
from django.urls import reverse
import calendar

class Calendar:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def formatmonth(self, withyear=True):
        cal = self._get_month_calendar()
        month_name = calendar.month_name[self.month]
        if withyear:
            return f"{month_name} {self.year}\n" + self._formatmonth(cal)
        else:
            return f"{month_name}\n" + self._formatmonth(cal)

    def formatweek(self, start_date, end_date):
        week_str = "<div class='row'>"
        for day in range(7):
            current_day = start_date + timedelta(days=day)
            day_url = reverse('day_view', args=[current_day.year, current_day.month, current_day.day])
            week_str += f"<div class='col'><a href='{day_url}'>{current_day.day}</a></div>"
        week_str += "</div>"
        return week_str

    def _get_month_calendar(self):
        cal = calendar.monthcalendar(self.year, self.month)
        month_days = []
        for week in cal:
            week_days = []
            for day in week:
                if day != 0:
                    current_day = datetime(self.year, self.month, day)
                    week_days.append(current_day)
            month_days.append(week_days)
        return month_days

    def _formatmonth(self, cal):
        month_str = "<div class='container'>"
        for week in cal:
            month_str += "<div class='row'>"
            for day in week:
                if day:
                    month_str += f"<div class='col'><a href='{day.url}'>{day.day:2}</a></div>"
                else:
                    month_str += "<div class='col'></div>"
            month_str += "</div>"
        month_str += "</div>"
        return month_str
