op_stack = []
def reverse_stack(inp_arr):
    if len(inp_arr) ==1:
        op_stack.append(inp_arr[0])
        return
    op_stack.append(inp_arr.pop())
    reverse_stack(inp_arr)






if __name__ =='__main__':
    inp_arr = [1, 2, 3, 4, 5, 6, 7, 8]
    reverse_stack(inp_arr)
    print(op_stack)