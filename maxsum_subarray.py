def max_sum(a):
    max_sum = a[0]
    cur_sum = 0

    for i in range(len(a)):
        cur_sum += a[i]
        max_sum = max(cur_sum, max_sum)

        if cur_sum <0:
            cur_sum=0

    return max_sum


if __name__ == '__main__':
    a = [-1, -3, 5, -4, 3, -6, 9, 2]
    print(max_sum(a))