"""
menggunakan tanda titik dua/colon(:)


"""

# Float to format
x = 8798.87887343344
print(f"{x:.6}")         # f-string version
print("{:.6}".format(x)) # format method version 
# output 8798.88


# specify 3 decimal
print(f"{x:.3f}")

# separator
s = 1000000000

print(f"{x:f}")

print(f"{s:,}")
print(f"{s:_}")

print(f"{s:,.3f}")
print(f"{s:_.3f}")


# Percentages
questions = 30
correct_answer = 23
print(f"You got {correct_answer / questions :.2%} correct!")
# You got 76.67% correct!


