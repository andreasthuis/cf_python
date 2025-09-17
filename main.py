import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = input("Enter file name: ")

full_path = os.path.join(__location__, file)

with open(full_path, 'r') as f:
    content = f.read()

print(content)
