#Simple Function

# def greet():
#     print("Hi")
#     print("Welcome")
#     print("Hw are you doing?")

# greet()

# #Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do{name}")

def greet_with(name, location):
    print(f"Hello {name}, how is {location} today?")

greet_with("Anna", "Huntingdon" )

#Functions with Keyword arguments
greet_with(location="Huntingdon", name="Anna",)