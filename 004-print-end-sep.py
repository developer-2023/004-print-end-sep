# docs.python.org/3/library/functions.html
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# Positional and named parameters

# Ask user for his name
name = input("What's your name? ")

# Say hello to user (using end parameter)
print("hello, ", end="")
print(name)

# Say hello to user (using sep parameter)
print("hello,", name, sep="...")
