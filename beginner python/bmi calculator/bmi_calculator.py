# User input
# kg *1000g
weight = float(input("Enter your weight (kg): "))
# km *1000 m *100 cm 10
height = float(input("Enter your height (cm): "))
height_m = height/100

def BMI(weight, height):
    bmi = weight / (height_m  * height_m)
    
    if bmi >= 16 and bmi < 18.5:
        return "Underweight", bmi
    
    elif bmi >= 18.5 and bmi <= 22.9:
        return "Normal", bmi
        
    elif bmi >= 23.0 and bmi <= 27.4:
        return "Overweight", bmi
        
    else:
        # bmi >= 27.5
        return "Obese", bmi

# Call function and print result
result, bmi = BMI(weight, height)
print("BMI = ", bmi, "kg/m²", result)
