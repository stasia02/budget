import calendar

class budgetCalendar(calendar.TextCalendar):
    dates = {}
    
    def __init__(self, firstweekday: int = 0) -> None:
        super().__init__(firstweekday)