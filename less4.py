# display N numbers that are multiples of M and greater than K

# num = [1, 4, 28, 36, 35, 12, 29, 9]
# number_m = int(input("Input M: "))
# number_k = int(input("Input K: "))
# for i in num:
#     if i % number_m == 0 and i > number_k:
#         print(i)



# create calculator

i = True
while i == True:
    num1 = float(input("Input first number: "))
    oper = str(input("Input operation: "))
    num2 = float(input("Input second number: "))
    if oper == "+":
        total = num1 + num2
    elif oper == "-":
        total = num1 - num2
    elif oper == "*":
        total = num1 * num2
    elif oper == "/":
        total = num1 / num2
    print(f"Total: {total}")
    cont = input("Do you want continue? y/n: ")
    if cont == "n":
        i = False
