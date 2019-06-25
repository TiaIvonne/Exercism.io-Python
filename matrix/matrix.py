class Matrix():
    ## method
    def __init__(self, matrix_string):
        ## self = this in javascript/rows
        self.__matrix_rows = [[int(i) for i in row.split(' ')] for row in matrix_string.split('\n')]
        ## atributo column
        self.__matrix_col = \
            [list(column) for column in zip(*self.__matrix_rows)]

    def row(self, index):
        return self.__matrix_rows[index-1]

    def column(self, index):
        return self.__matrix_col[index-1]