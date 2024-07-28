def simple_interest(principal, rate, time):
    """
    Calculate the simple interest for given principal, rate, and time.

    Returns:
    float: The simple interest calculated, rounded to two decimal places.
    """
    Simple_Interest = (principal * rate * time) / 100
    value = round(Simple_Interest) 
    return value
    


print("Example 1:", simple_interest(23000, 4, 7))
print("Example 2:", simple_interest(10000, 1, 10)) 
print("Example 3:", simple_interest(100000, 5, 4)) 