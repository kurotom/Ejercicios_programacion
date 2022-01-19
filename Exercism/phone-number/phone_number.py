import re


class PhoneNumber:
    def __init__(self, number):
        self.number = self.limpiado(number)
        self.area_code = self.code_area()
        self.exchange_code = self.code_exchange()
        self.suscriber_number = self.member_suscriber()

    def limpiado(self, numero):
        numbers = re.findall(r"\d+", numero)
        string_numbers = "".join(numbers)
        if string_numbers.isnumeric():
            if 10 <= len(string_numbers) <= 11:
                if len(string_numbers) == 11:
                    if int(string_numbers[0]) == 1:
                        return string_numbers[1:]
                    else:
                        raise ValueError("Number not start with 1")
                else:
                    return string_numbers
            else:
                raise ValueError("Min 10 digits, Max 11 digits")

    def code_area(self):
        if 2 <= int(self.number[0]) <= 9:
            return self.number[:3]
        else:
            raise ValueError("Invalid Code Area")

    def code_exchange(self):
        if 2 <= int(self.number[3]) <= 9:
            return self.number[3:6]
        else:
            raise ValueError("Invalid Code Exchange")

    def member_suscriber(self):
        if 2 <= int(self.number[0]) <= 9:
            return self.number[6:]
        else:
            raise ValueError("Invalid Member Suscriber")

    def pretty(self):
        return f"({self.code_area()})-{self.code_exchange()}-{self.member_suscriber()}"
