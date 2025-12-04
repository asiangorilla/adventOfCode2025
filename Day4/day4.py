filename='./input.txt'

with open(filename, 'r') as f:
    inp = f.read().split('\n')
    f.close()
total_tp_counter = 0
inp_2 = inp.copy()
tp_counter = 1  # for do while
while not(tp_counter == 0):
    tp_counter = 0

    for row_n, row in enumerate(inp):
        for col_n, col in enumerate(row):
            if col == '@':
                neigh_counter = 0
                for i in range(3):
                    for j in range(3):
                        if ((row_n-1+i < 0) or (col_n-1+j < 0)) or (i == 1 and j == 1):
                            continue
                        try:
                            if inp[row_n-1+i][col_n-1+j] == '@':
                                neigh_counter = neigh_counter + 1
                        except IndexError:
                            pass
                if neigh_counter < 4:
                    inp_2[row_n] = inp_2[row_n][:col_n] + '.' + inp_2[row_n][col_n+1:]  
                    tp_counter = tp_counter + 1
    total_tp_counter = total_tp_counter + tp_counter
    inp = inp_2.copy()
print(total_tp_counter)
    