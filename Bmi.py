def bmi_calc(weight, height):
    return weight / (height ** 2)

def bmi_categorize(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def solti_input():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        return weight, height
    except ValueError:
        print("Entry Mistake Please Add Correct Number ")
        return solti_input()

def main():
    print("Welcome to the Swapneel BMI Calculator!")

    weight, height = solti_input()

    bmi = bmi_calc(weight, height)
    category = bmi_categorize(bmi)

    print("\nBMI Result:")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()

