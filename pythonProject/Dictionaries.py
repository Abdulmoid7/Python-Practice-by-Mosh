customer = {
    "name": "Abdul Moid",
    "age": 18,
    "is_verified": True
}
print(customer["name"])
print(customer["age"])
print(customer.get("birthdate"))

customer["name"] = "Abdul Moid"
print(customer["name"])

customer["birthdate"] = "7th August 2005"
print(customer["birthdate"])

customer["Phone number"] = "03352876726"   #practice of problem (not accurate)
print(customer["Phone number"])


phone = input("phone:")
digits_mapping = {
"0": "Zero",
"3": "Three",
"3": "Three",
"5": "Five",
"2": "Two",
"8": "Eight",
"7": "Seven",
"6": "Six",
"7": "Seven",
"2": "Two",
"6": "Six"
}
output = ""       # empty string
for ch in phone:
    output += digits_mapping.get(ch, "!") +  " "    # here using .get because in order to use not all values provided.
print(output)