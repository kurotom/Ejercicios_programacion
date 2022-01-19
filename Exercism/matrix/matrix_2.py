class Matrix:
    lista_numeros = []

    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        if "\n" not in matrix_string:
            self.lista_numeros.append(matrix_string.split())
        else:
            saltos = len(matrix_string[:matrix_string.index("\n")].split())
#            print(matrix_string.split(), len(matrix_string.split()))
            for i in range(0, len(matrix_string.split()), saltos):
                self.lista_numeros.append(list(self.matrix_string.split()[i:i + saltos]))

    def row(self, index):
        row_list = []
        index = index - 1
        for x in range(len(self.lista_numeros)):
            for y in range(len(self.lista_numeros[x])):
#                print(self.lista_numeros[x][y], end=" ")
                if x == index:
                    row_list.append(self.lista_numeros[x][y])
#            print()
        text_row = ", ".join(row_list)
        print(f"[{text_row}]")
        self.lista_numeros.clear()
        return f"[{text_row}]"

    def column(self, index):
        column_list = []
        index = index - 1
        for x in range(len(self.lista_numeros)):
            for y in range(len(self.lista_numeros[x])):
                if y == index:
                    column_list.append(self.lista_numeros[x][y])
#            print()
        column_text = ", ".join(column_list)
        print(f"[{column_text}]")
        self.lista_numeros.clear()
        return f"[{column_text}]"


#ma = Matrix("9 8 7\n5 3 2\n6 6 7")
#ma.row(1) # [9, 8, 7]


#matrix = Matrix("1")
#matrix.row(1) # [1]

#matrix = Matrix("1 2\n3 4")
#matrix.row(2) # [3, 4])

#matrix = Matrix("1 2\n10 20")
#matrix.row(2) # [10, 20]

#matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
#matrix.row(4) # [8, 7, 6]

#matrix = Matrix("1")
#matrix.column(1) # [1]

#matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
#matrix.column(3) # [3, 6, 9]

matrix = Matrix("1 2 3 4\n5 6 7 8\n9 8 7 6")
matrix.column(4) # [4, 8, 6]

#matrix = Matrix("89 1903 3\n18 3 1\n9 4 800")
#matrix.column(2) # [1903, 3, 4]
