def safe_divide(numerator, denominator):
    
    try:
        denominator= float(denominator)
        numerator=float(numerator)
    except ValueError:
        return ("Error: Please enter numeric values only.") 
    try: 
        result = numerator / denominator
    except ZeroDivisionError:
        return ("Error: Cannot divide by zero.")

    return f"The result of the division is {result:.2f}"

