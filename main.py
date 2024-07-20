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

# def greet_with(name, location):
#     print(f"Hello {name}, how is {location} today?")

# greet_with("Anna", "Huntingdon" )

# #Functions with Keyword arguments
# greet_with(location="Huntingdon", name="Anna",)

# FUNCTIONS WITH OUTPUTS


# def format_name(f_name, l_name):
#     strip_f = f_name.lower()
#     strip_l = l_name.lower()
#     cap_first = strip_f[0].upper()
#     cap_last = strip_l[0].upper()
#     final_first = cap_first + strip_f[1:]
#     final_last = cap_last + strip_l[1:]
#     print(f"{final_first} {final_last}")

def format_name(f_name, l_name):
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return f"{formatted_fname} {formatted_lname}"

formatted_name = format_name("frEd", "iNOh")
print(formatted_name)