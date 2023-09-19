def compensate_printer(N: int, bits: str):
    # 将十六进制的 bits 转换为二进制的字符串，并转换为 list
    bits = list(bin(int(bits.replace(" ", ""), 16))[2:].zfill(N))

    # 定义二维矩阵 matrix，表示所有孔的开关状态
    matrix = [[int(bits[i * 8 + j]) for j in range(8)] for i in range((N + 7) // 8)]

    # 计算喷墨头堵塞的小孔位置
    clogged = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                clogged.append((i, j))

    # 计算所有可能的补偿方案
    solutions = []
    for i, j in clogged:
        # 向右平移
        if j + 1 < len(matrix[i]) and matrix[i][j + 1] == 1:
            # 计算平移的小孔数
            count = 1
            while j + count < len(matrix[i]) - 1 and matrix[i][j + count + 1] == 1:
                count += 1
            # 判断是否可以补偿
            if i > 0 and matrix[i - 1][j] == 1 and matrix[i - 1][j + count] == 1:
                # 生成补偿后的矩阵
                new_matrix = [[0] * len(row) for row in matrix]
                for x in range(len(matrix)):
                    for y in range(len(matrix[x])):
                        if i <= x < i + count and j <= y <= j + count:
                            new_matrix[x - i][y - j] = matrix[x][y]
                        else:
                            new_matrix[x][y] = matrix[x][y]
                solutions.append(("right", count, new_matrix))

        # 向左平移
        if j > 0 and matrix[i][j - 1] == 1:
            # 计算平移的小孔数
            count = 1
            while j - count > 0 and matrix[i][j - count - 1] == 1:
                count += 1
            # 判断是否可以补偿
            if i > 0 and matrix[i - 1][j - count] == 1 and matrix[i - 1][j] == 1:
                # 生成补偿后的矩阵
                new_matrix = [[0] * len(row) for row in matrix]
                for x in range(len(matrix)):
                    for y in range(len(matrix[x])):
                        if i <= x < i + count and j - count <= y < j:
                            new_matrix[x - i][y - j + count] = matrix[x][y]
                        else:
                            new_matrix[x][y] = matrix[x][y]
                solutions.append(("left", count, new_matrix))

    # 如果没有可以补偿的方案，输出 0
    if not solutions:
        return 0

    # 选择平移最少的方案
    solutions = sorted(solutions, key=lambda x: x[1])
    return solutions
print(compensate_printer(14,'0xE77F'))