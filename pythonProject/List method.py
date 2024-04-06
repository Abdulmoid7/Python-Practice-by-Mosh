numbers = [5, 4, 7, 8, 10, 11, 15, 18]
numbers.append(20)
print(numbers)

numbers = [5, 4, 7, 8, 10, 11, 15, 18]
numbers.insert(0, 99)
print(numbers)

numbers = [5, 4, 7, 8, 10, 11, 15, 18]
numbers.remove(18)
print(numbers)

numbers = [5, 4, 7, 8, 10, 11, 15, 18]
numbers.clear()
print(numbers)


numbers = [5, 4, 7, 8, 10, 11, 15, 18]
numbers.pop()
print(numbers)


numbers = [5, 4, 7, 8, 10, 11, 15, 18]
print(numbers.index(5))
print(numbers.index(99)) # this value doesn't exists

numbers = [5, 4, 7, 8, 10, 11, 15, 18, 3, 6, 9, 12]
print(5 in numbers)

numbers = [5, 4, 7, 8 ,5, 7, 7, 9, 10, 11, 15, 18, 3, 6, 9, 12]
print(numbers.count(5))