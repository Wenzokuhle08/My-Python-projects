def weight_checker():
     while True:
        weight = input("What is your weight?: ")
       
        if weight.isdigit():
            user_input = int(weight)
            print(f"Your weight is: {weight}kg")
            return user_input
        else:
            print("Please enter a valid number: ")
            

    
def height_checker():
    while True:
        height = input("What is your height?: ")
        
        if height.isdigit():
            user_input = int(height) / 100
            print(f"Your height is: {height}cm")
            return user_input
        else:
            print("Please enter a valid number")
    
def your_BMI(weight, height):
    bmi = weight / (height * height)
    if bmi <= 18.5:
        print(f"Your BMI is {bmi}, you are underweight.")
    elif bmi <= 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    elif bmi <= 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    elif bmi <= 35:
        print(f"Your BMI is {bmi}, you are obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")
        
    
    
if __name__ == "__main__":
    weight = weight_checker()
    height = height_checker()
    your_BMI(weight, height)


