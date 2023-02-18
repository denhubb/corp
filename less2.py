# replace all space on "-" in user text

# text = input("Input text with space: ")
# print(text.replace(" ", "-"))



# user input 3 numbers, find average value with 3 numbers after comma

# first_num = int(input("Input first number: "))
# second_num = int(input("input second number: "))
# third_num = int(input("input third number: "))
# print(f"Average numbers: {round((first_num + second_num + third_num) / 3, 3)}")



# user input name, age, city, create welcome message use user information

# name = str(input("Input name: "))
# age = int(input("Input age: "))
# city = str(input("Input city: "))
# print("Hello %s. Age - %d. City - %s." % (name, age, city))



# user input 3 numbers, say how many positive and negative

nums = []
positive = 0
negative = 0
try:
    nums.append(float(input("Input first number: ")))
    nums.append(float(input("Input second number: ")))
    nums.append(float(input("Input third number: ")))
    for i in nums:
        if i < 0:
            positive += 1
        else:
            negative += 1
    print(f"Quantity of positive numbers: {positive}", f"Quantity of negative numbers: {negative}", sep="\n")
except ValueError:
    print("Incorrect value. Input number!")