numbers = [5, 4, 7, 8 ,5, 7, 7, 9, 10, 11, 15, 18, 3, 6, 9, 12]
print(numbers.count(5))

numbers = [5, 4, 7, 8 ,5, 7, 7, 9, 10, 11, 15, 18, 3, 6, 9, 12]
print(numbers.sort())
print(numbers) #Ascending Order

numbers = [5, 4, 7, 8 ,5, 7, 7, 9, 10, 11, 15, 18, 3, 6, 9, 12]
print(numbers.reverse())
print(numbers) #Descending order

numbers = [5, 4, 7, 8 ,5, 7, 7, 9, 10, 11, 15, 18, 3, 6, 9, 12]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)