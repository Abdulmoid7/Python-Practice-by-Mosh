numbers = [5, 4, 7, 8 ,5, 7, 7, 9, 10, 11, 15, 10, 18, 3, 6, 9, 12]
unique_numbers = list(set(numbers))
numbers2 = unique_numbers.copy()
numbers.append(10)
print(numbers2)

    # method 2

numbers = [3, 5, 7, 8, 10, 20, 34, 78, 5, 7, 8, 9, 3, 10]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

