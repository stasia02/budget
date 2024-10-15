from budget_app.budget import budget
from budget_app.budgetCalendar import budgetCalendar
def main():
    b = budget("testBudget.json")
    calendar = budgetCalendar(b)
    calendar()

if __name__ == "__main__":
    main()