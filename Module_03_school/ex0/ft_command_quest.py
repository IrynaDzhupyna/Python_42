import sys

print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
length = len(sys.argv)
i = 1
if length < 2:
    print("No arguments provided!")
    print(f"Total arguments:{length}")
else:
    print(f"Arguments received: {length - 1}")
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1
    print(f"Total arguments: {length}")
