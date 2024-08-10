# define the functions needed
def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer) + "\n")

def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer) + "\n")

while True:
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Divission")
    print("E. Exit")

    choice = input("Input your choice: ")
    if choice == "A" or choice =="a":
        print("Addition")
        a = int(input("Input the first number: "))
        b = int(input("Input the second number: "))
        add(a, b)
    elif choice == "B" or choice =="b":
        print("Substraction")
        a = int(input("Input the first number: "))
        b = int(input("Input the second number: "))
        sub(a, b)
    elif choice == "C" or choice =="c":
        print("Multiplication")
        a = int(input("Input the first number: "))
        b = int(input("Input the second number: "))
        mul(a, b)
    elif choice == "D" or choice =="d":
        print("Divission")
        a = int(input("Input the first number: "))
        b = int(input("Input the second number: "))
        div(a, b)
    elif choice == "E" or choice =="e":
        print("Program Ended")
        quit()