def validate(matrix: list[list[int]]):
    if not isinstance(matrix, list):
        raise Exception("Матрица должна быть типа list.")
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_rows != num_cols:
        raise Exception()
   
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise Exception("Строка не может быт пустой.")
        
        for item in row:
            if not isinstance(item, int):
                raise Exception("Элементы матрицы должы быть целыми числами.")
            
def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    validate(matrix)
    
    order = len(matrix)
    
    if order == 1:
        return matrix[0][0]
 
    if order == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0  
    for idx, value in enumerate(matrix[0]):
        if value == 0:
            continue
        
        minor = [
            [row[col] for col in range(order) if col != idx]
            for row in matrix[1:]
        ]
        
        co_factor = (-1) ** idx * calculate_determinant(minor)
        
        det += value * co_factor
    
    return det

def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
