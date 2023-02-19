# display N numbers that are multiples of M and greater than K

# N = int(input("N: "))
# M = int(input("M: "))
# K = int(input("K: "))
# numbers = []
# while len(numbers) < N:
#     if K % M == 0:
#         numbers.append(K)
#         K += M
#     else:
#         K += 1
# print(numbers)



# create calculator

# i = True
# while i == True:
#     num1 = float(input("Input first number: "))
#     oper = str(input("Input operation: "))
#     num2 = float(input("Input second number: "))
#     if oper == "+":
#         total = num1 + num2
#     elif oper == "-":
#         total = num1 - num2
#     elif oper == "*":
#         total = num1 * num2
#     elif oper == "/":
#         total = num1 / num2
#     print(f"Total: {total}")
#     cont = input("Do you want continue? y/n: ")
#     if cont == "n":
#         i = False



# Output even numbers from 2 to N by 5 in a line

N = int(input("N: "))
count = 0
for i in range(2, N+1, 2):
    if count < 5:
        count += 1
    else:
        print()
        count = 1
    print(i, end=" ")