# Se puede declarar variables con valor predeterminado, y que puede ser cambiado posteriormente.
# cuando se hace una reasignación.
# Usar mejor, "fstring".

def two_fer(name="you"):
     return f"One for {name}, one for me."

#    if name == "":
#        return "One for you, one for me."
#    else:
#        return f"One for {name}, one for me."

two_fer()
two_fer("Alice")
two_fer("Bob")
