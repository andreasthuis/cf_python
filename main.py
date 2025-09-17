import os
import subprocess

try:
    __location__ = os.path.abspath(os.path.dirname(__file__))
except NameError:
    __location__ = os.getcwd()

file = input("Enter file name: ").strip()

full_path = os.path.join(__location__, file)

if not os.path.isfile(full_path):
    print(f"Error: File '{full_path}' does not exist.")
else:
    if full_path.endswith('.py'):
        cmd = ['python3', full_path]
    else:
        if not os.access(full_path, os.X_OK):
            print(f"File '{full_path}' is not executable. Setting execute permission.")
            os.chmod(full_path, 0o755)
        cmd = [full_path]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Execution failed: {e}")

