import sys

print("=== Command Quest ===")
if len(sys.argv) < 2:
    print(f"Program name: {sys.argv[0]}\nNo argument provided!")
    print(f"Total arguments: {len(sys.argv)}")
elif len(sys.argv) == 2:
    print(f"Program name {sys.argv[0]}")
    print(f"Arguments received: {len(sys.argv) - 1}")
    print(f"Argument {len(sys.argv) - 1}: {sys.argv[1]}")
    print(f"Total arguments: {len(sys.argv)}")
else:
    i = 1
    length = len(sys.argv
    print(f"Program name {sys.argv[0]}")
    print(f"Arguments received: {lenght - 1}")
    while i < length:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {length - 1}")
