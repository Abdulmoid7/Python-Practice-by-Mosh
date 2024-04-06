from pathlib import Path

path = Path()
for file in path.glob('*.py'):   # we can find multiple types of files like .py .xls * for directory
    print(file)

