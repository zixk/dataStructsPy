
def largestConnectedCell(x, y, points):
    matrix = [[0]*x for _ in range(y)]
    for tuplePair in points:
        xPoint = tuplePair[0]
        yPoint = tuplePair[1]
        matrix[xPoint][yPoint] = 1

    maxRegion = 0
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[row])):
            if(matrix[row][column] == 1):
                size = getRegionSize(matrix, row, column)
                maxRegion = max(size, maxRegion)
    print(f'Max region size is: {maxRegion}')


def getRegionSize(matrix, row, column):
    if row < 0 or column < 0 or row >= len(matrix) or column >= len(matrix[row]):
        return 0
    if matrix[row][column] == 0:
        return 0
    matrix[row][column] = 0
    size = 1
    for r in range(row-1, row+2):
        for c in range(column-1, column+2):
            if(r != row or c != column):
                size += getRegionSize(matrix, r, c)

    return size

if __name__ == "__main__":
    x = 4
    y = 4
    points = [(1,1),(1,2)]
    largestConnectedCell(x, y, points)
    points2=[(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]
    largestConnectedCell(x, y, points2)
    points_with_gap=[(0,0),(0,1),(0,2),(0,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]
    largestConnectedCell(x,y,points_with_gap)