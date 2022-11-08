
# using f string


# Using format
name = "Bob"
greeting = "Hello, {}"
print(greeting)
with_name = greeting.format(name)
with_name_two = greeting.format("Udin")
print(with_name)

longer_pharse = "Hello, {}, Today is {}"
formatted= longer_pharse.format("Rolf", "Monday")
print(formatted)
