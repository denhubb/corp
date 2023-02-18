# Fill in the list with powers of 2 (2^1 - 2^n)

# number = int(input("Input: "))
# print([2**i for i in range(number)])


# create a dictionary to count of each letters to text entered by the user

# text = input("text: ")
# counter = {i: text.count(i) for i in set(text)}
# print(counter)



# fill the dictionary from 0 to 'n' and nested dictionary values with keys "name" and "email" are entered by the user

n = int(input("n: "))
users = {
    i: {"name": input("name: "), "email": input("email: ")}
    for i in range(n)
}
print(users)

