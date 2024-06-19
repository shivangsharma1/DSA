
def iscollinear(x1, y1, x2, y2, x3, y3):
    if ((y3-y2) * (x2 -x1) == (y2-y1)*(x3-x2)): return True
    else: return False





if __name__ == '__main__':

    x1, y1, x2, y2, x3, y3  = 2, 9, 4, 6, 6, 8

    print(iscollinear(x1, y1, x2, y2, x3, y3))