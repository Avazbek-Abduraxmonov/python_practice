# def function(nums):
#     if nums >0:
#         return "pos"
#     else:
#         return "neg"

# num = int(input("Sonni kiriting: "))
# x = function(num)

# print(x)


# ======================



# def roman_to_integer(roman):
#     roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     result = 0
#     prev_value = 0

#     for char in reversed(roman):
#         value = roman_dict[char]
#         if value >= prev_value:
#             result += value
#         else:
#             result -= value
#         prev_value = value

#     return result

# numeral = input("Enter a Roman numeral: ")
# converted_integer = roman_to_integer(numeral)
# print(f"The equivalent integer value is: {converted_integer}")

