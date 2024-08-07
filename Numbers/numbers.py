def all_numbers():
    """
    This python program will only print numbers from 0 to 8 except the numbers 2 and 3.
    Note : Use 'continue' statement.
    """

    num1 = int(input("Enter the number of your choice: "))
    num2 = int(input("Enter the number of your choice: "))

    for i in range(0, 9):
        if i == num1 or i == num2 or i == 2 or i == 3:
            continue
        print(i, end=' ')
        
all_numbers()