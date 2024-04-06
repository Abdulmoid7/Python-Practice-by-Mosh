numbers = [1, 3, 5, 6, 8, 9, 16, 76, 89, 99, 100]
max_number = numbers[0]
min_number = numbers[0]

for number in numbers:
      if number > max_number:
          max_number = number
      elif number < min_number:
          min_number = number
print("The largest number in the list:", max_number)
print("The smallest number in the list:", min_number)
