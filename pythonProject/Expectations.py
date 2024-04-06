try:
     age = int(input('Age: '))
     income = 2000
     risk = income / age
     print(age)       # we have to generate a proper error message because once we put a text instead of number we get an error.
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Syntax Error')
