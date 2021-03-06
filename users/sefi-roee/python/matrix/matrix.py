class Matrix:
    def __init__(self, matrix_string):
        self.data = [list(map(int, row.split())) for row in matrix_string.splitlines()]

    def row(self, index):
        return self.data[index - 1]
        
    def column(self, index):
        return [row[index - 1] for row in self.data]