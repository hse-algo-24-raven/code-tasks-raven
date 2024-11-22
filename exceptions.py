class EmptyListException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'EmptyMatrixException, {self.message}'
        else:
            return f"Параметр не является трехдиагональной матрицей"


class ItemMatrixException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'EmptyMatrixException, {self.message}'
        else:
            return f"Параметр не является трехдиагональной матрицей"


class NotSquareMatrixException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'NotSquareMatrix, {self.message}'
        else:
            return f"Параметр не является трехдиагональной матрицей"


