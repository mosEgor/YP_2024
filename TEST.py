
# Функция для генерации случайной матрицы заданного размера
def generate_random_matrix(rows, cols):
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

# Функция для поиска числа K в матрице и подсчета шагов
def find_number_in_random_matrix(matrix, K):
    if not matrix or not matrix[0]:
        return False, 0

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1
    iterations = 0

    while row < rows and col >= 0:
        iterations += 1
        current = matrix[row][col]

        if K == current:
            return True, iterations
        elif K < current:
            col -= 1
        else:
            row += 1

    return False, iterations

# Генерируем случайную матрицу 5x5
rows, cols = 5, 5
random_matrix = generate_random_matrix(rows, cols)
K = 7

# Вывод сгенерированной матрицы
print("Сгенерированная матрица:")
for row in random_matrix:
    print(row)

# Поиск числа K в случайно сгенерированной матрице
result, steps = find_number_in_random_matrix(random_matrix, K)

# Вывод результата поиска и количества шагов
print("\nЧисло K найдено:", result)
print("Количество шагов для поиска:", steps)