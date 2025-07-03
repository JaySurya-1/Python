

print("Jay Surya \n1AY24AI048\nAIML 'M' ")

from datetime import datetime, timedelta
def show_today():
    today = datetime.today()
    print("Today's date:", today.date())
    print("Day of the week:", today.strftime("%A"))  # e.g., Monday
def birthday_info():
    bday_str = input("Enter your birthday (YYYY-MM-DD): ")
    birthday = datetime.strptime(bday_str, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1
    print(f"You are {age} years old.")
    next_birthday = birthday.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    time_until = next_birthday - today
    total_seconds = int(time_until.total_seconds())
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(f"Time until your next birthday: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

def double_day(birth1_str, birth2_str):
    b1 = datetime.strptime(birth1_str, "%Y-%m-%d")
    b2 = datetime.strptime(birth2_str, "%Y-%m-%d")
    if b1 > b2:
        b1, b2 = b2, b1

    delta = b2 - b1
    double_day = b2 + delta
    print("Double Day is:", double_day.date())

def n_times_day(birth1_str, birth2_str, n):
    b1 = datetime.strptime(birth1_str, "%Y-%m-%d")
    b2 = datetime.strptime(birth2_str, "%Y-%m-%d")
    
    if b1 > b2:
        b1, b2 = b2, b1

    delta = b2 - b1
    n_day = b2 + delta / (n - 1)
    print(f"The day one person is {n} times older is:", n_day.date())
if __name__ == "__main__":
    print("\n1. Show Today's Date and Day of Week")
    show_today()

    print("\n2. Birthday Info")
    birthday_info()
    
    print("\n3. Double Day")
    double_day("2000-01-01", "2005-01-01")

    print("\n4. N-times Older Day")
    n_times_day("2000-01-01", "2005-01-01", 3)
