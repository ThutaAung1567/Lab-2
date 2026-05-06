def calculate_bmi(height, weight):
    print("Height= "+str(height))
    print("Weight="+str(weight))
    bmi= weight /(height**2)
    print("BMI="+str(bmi))
    if bmi<18.5:
        print(underweight())
    elif bmi<=25.0:
        print(Normalweight())
    else:
        print(Overweight())
def underweight():
    return ("-1")
def Normalweight():
    return("0")
def Overweight():
    return ("1")

calculate_bmi(weight=57,height=1.73)