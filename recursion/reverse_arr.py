
def reverse_arr(inp_arr):
    print("inp array", inp_arr)
    if len(inp_arr) == 1:
        return
    alpha = inp_arr.pop(0)
    print(alpha)
    reverse_arr(inp_arr)
    inp_arr.append(alpha)
    print("out time inp_arr", inp_arr)
    






if __name__ == '__main__':
    inp_arr = [1, 2, 3, 4, 5, 6, 7, 8]
    reverse_arr(inp_arr)
    print(inp_arr)