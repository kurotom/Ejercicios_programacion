def convert(number):
    converted_numbers = []
    if number % 3 == 0:
        converted_numbers.append("Pling")
    if number % 5 == 0:
        converted_numbers.append("Plang")
    if number % 7 == 0:
        converted_numbers.append("Plong")

    if converted_numbers:
        return "".join(converted_numbers)
    else:
        return str(number)


print(convert(28))
print(convert(30))
print(convert(34))
