from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")

    def calculate_future_date():
        user_input_days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=user_input_days)
        print(f"Future date: {future_date.strftime("%Y-%m-%d")}")
    calculate_future_date()


display_current_datetime()