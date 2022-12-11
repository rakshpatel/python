from operator import ne


def floodFill(image, sr, sc, newColor):
    if image[sr][sc] == newColor:
        return image

    rowLen = len(image) - 1
    colLen = len(image[0]) - 1
    currentColor = image[sr][sc]
    visited = set()

    def getNeighbours(image, rowLen, colLen, cell):
        st = set()
        currentRow = cell[0]
        currentCol = cell[1]
        if cell[0] + 1 <= rowLen:
            st.add((currentRow + 1, currentCol))
        if cell[0] - 1 >= 0:
            st.add((currentRow - 1, currentCol))
        
        if cell[1] + 1 <= colLen:
            st.add((currentRow, currentCol + 1))
        
        if cell[1] - 1 >= 0:
            st.add((currentRow, currentCol - 1))

        return st

    image[sr][sc] = newColor
    visited.add((sr, sc))
    for neightbour in getNeighbours(image, rowLen, colLen, [sr, sc]):        
        if neightbour not in visited and image[neightbour[0]][neightbour[1]] == currentColor:
            # image[neightbour[0]][neightbour[1]] = newColor
            floodFill(image, neightbour[0], neightbour[1], newColor)
    
    return image


        

    


if __name__ == "__main__":
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    img = floodFill(image, sr, sc, color)
    print(img)
    # print(getNeighbours(image, len(image) - 1, len(image[0]) - 1, [sr, sc]))
    