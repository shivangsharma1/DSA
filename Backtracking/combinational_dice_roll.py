def combinational_dice_rolls(n, m):
    comb, result = [], []
    
    def roll_recursive(i, m, comb):
        if i == n:
            result.append(comb.copy())
            return
        
        for j in range(1, m + 1):
            roll_recursive(i+1, m, comb + [j])

    roll_recursive(0, m, comb)
    return result


n = 3
m = 2
output = combinational_dice_rolls(n, m)
print(output)
