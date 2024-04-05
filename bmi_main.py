from bmi_lib import bmi_calc, bmi_categorize, solti_input

def ram():
    print("Welcome to the Swapneel BMI Calculator!")

    weight, height = solti_input()

    bmi = bmi_calc(weight, height)
    category = bmi_categorize(bmi)

    print("\nBMI Result:")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    ram()