customer = {
    "name":"John",
    "age":28,
    "mailid":"john28@gmail.com",
    "verified":True
    }
print(customer)

print(customer["name"])
print(customer.get("name"))
print(customer.get("birthdate","Jan 1 1980"))
print(customer.get("birthdate"))

customer["age"] = 41
print(customer)


phone = input("phone: ")

digits_mapping = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero",
    }
output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!") + " "

print(output)
