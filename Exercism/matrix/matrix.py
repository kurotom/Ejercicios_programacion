"""
So given a string with embedded newlines like:
    9 8 7
    5 3 2
    6 6 7
Your code should be able to spit out:
    * A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
    * A list of the columns, reading each column top-to-bottom while moving from left-to-right.
The rows for our example matrix:
    9, 8, 7
    5, 3, 2
    6, 6, 7
And its columns:
    9, 5, 6
    8, 3, 6
    7, 2, 7
"""


class Matrix:
    lista_numeros = []
    str_to_int = []

    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        if "\n" not in matrix_string:
            self.lista_numeros.clear()
            for i in self.matrix_string.split("\n"):
                for x in range(len(i.split())):
                    self.str_to_int.append(int(i.split()[x]))
                self.lista_numeros.append(list(self.str_to_int))
                self.str_to_int.clear()
        else:
            self.lista_numeros.clear()
            for i in self.matrix_string.split("\n"):
                for x in range(len(i.split())):
                    self.str_to_int.append(int(i.split()[x]))
                self.lista_numeros.append(list(self.str_to_int))
                self.str_to_int.clear()

    def row(self, index):
        row_list = []
        indice = index - 1
        for eje_X in range(len(self.lista_numeros)):
            for eje_Y in range(len(self.lista_numeros[eje_X])):
                if eje_X == indice:
                    row_list.append(self.lista_numeros[eje_X][eje_Y])
        print(row_list)
        return row_list

    def column(self, index):
        column_list = []
        indice = index - 1
        for eje_x in range(len(self.lista_numeros)):
            for eje_y in range(len(self.lista_numeros[eje_x])):
                if eje_y == indice:
                    column_list.append(self.lista_numeros[eje_x][eje_y])
        print(column_list)
        return column_list


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

#matrix = Matrix("1 2 3 4\n5 6 7 8\n9 8 7 6")
#matrix.column(4) # [4, 8, 6]

#matrix = Matrix("89 1903 3\n18 3 1\n9 4 800")
#matrix.column(2) # [1903, 3, 4]