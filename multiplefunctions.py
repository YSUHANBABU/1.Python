class multiplefunctions:
    
    def subfields():
        lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("subfields in AI are")
        for i in lists:
            print(i)
    def OddEven():
        num=int(input("Enter the number :"))
        if num%2==0:
                print(num,"is even")
        else:
                print(num,"is odd")
    def Elegible():
        age=int(input("Enter Your Age "))
        gender=input("Enter Male or female, 'M' for Male and 'F' for female:")
        if gender=="M" and age>=21:
            print("Your gender is:",age)
            print("Your age is:",age)
            print("Elegible for  Marriage")
        elif gender=="F" and age>=18:
            print("Your gender is:",age)
            print("Your age is:",age)
            print("Elegible for  Marriage")
        else:
            print("Your gender is:",age)
            print("Your age is:",age)
            print("Not Elegible for Marriage")
    def percentage():
        subject1=int(input("Enter the marks: "))
        subject2=int(input("Enter the marks: "))
        subject3=int(input("Enter the marks: "))
        subject4=int(input("Enter the marks: "))
        subject5=int(input("Enter the marks: "))
        total=subject1+subject2+subject3+subject4+subject5
        percentage=float(total/500)*100
        print("Total is:",total)
        print("Percentage is ",percentage)
    def triangle():
        Height=int(input("Height: "))
        Breadth=int(input("Breadth: "))
        print("Area formula (Height*Breadth)/2")
        area=(Height*Breadth)/2
        print("Area of triangle is :",area)
        Height1=int(input("height1: "))
        Height2=int(input("height2: "))
        Breadth=int(input("Breadth: "))
        print("Perimeterformula:Height1+Height2+Breadth")
        Perimeterformula=Height1+Height2+Breadth
        print("Perimeter of triangle  :",Perimeterformula)

