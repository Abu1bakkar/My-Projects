def hello():
    print("hello " , end="")

name = input ("What's your name?")
name=name.title()
name=name.strip()
hello()
print(name)
