import re


def is_valid(isbn):
    calc = []
    if len(isbn.replace("-", "")) == 10:
        patron = re.match(r"([0-9]{1})(-| |)([0-9]{1,3})(-| -|)([0-9]{5})(-| |)(X|[0-9]{1})", isbn)
        if patron is not None:
            if "X" in patron[0].replace("-", ""):
                n_isbn = [i for i in patron[0].replace("-", "")][::-1][1:]
                for x in range(len(n_isbn)):
                    calc.append(int(n_isbn[x]) * (x + 2))
                calc.insert(0, 10)
                if sum(calc) % 11 == 0:
                    print(True)
                    return True
                else:
                    print(False)
                    return False
            else:
                n_isbn = [i for i in patron[0].replace("-", "")][::-1]
                for x in range(len([i for i in patron[0].replace("-", "")])):
                    calc.append(int(n_isbn[x] * (x + 1)))
                if sum(calc) % 11 == 0:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False


#is_valid("3-598-21508-8") # True
#is_valid("3-581-21508-8") # False
#is_valid("4-098-87654-X") # True
#is_valid("1-234-X6789-5") # False
#is_valid("409887654X") # True
#is_valid("98245726788") # False
#print(is_valid("3-598-2X507-9"))
#print(is_valid("3132P34035"))
#print(is_valid("3-598-21507-A"))