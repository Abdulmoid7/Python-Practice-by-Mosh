numbers = [5, 2, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)

numbers = [2, 2, 2, 2, 2, 2, 50]
for y_count in numbers:
    print('&' * y_count)

characters = [3, 3, 3, 3, 3, 3, 10]
for z_count in numbers:
    print('+' * z_count)

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
        print(output)

numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
    output += 'L'
    print(output)
