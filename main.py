import os
import subprocess

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = input("Enter file name: ")

full_path = os.path.join(__location__, file)

subprocess.run(full_path)
