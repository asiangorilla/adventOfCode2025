import re

filename = './input.txt'

with open(filename, 'r') as f:
    inp = f.read().split('\n')
    f.close()
    
# inp2 = []
# pattern = re.compile(r'\S+')
# for line in inp:
#     inp2.append(re.findall(pattern,line))
# 
# total = 0
# numb_len = len(inp)-1
# for ind, operator in enumerate(inp2[-1]):
#     if operator == '*':
#         inter_total = 1
#         for j in range(numb_len):
#             inter_total = inter_total * int(inp2[j][ind])
#     elif operator == '+':
#         inter_total = 0
#         for j in range(numb_len):
#             inter_total = inter_total + int(inp2[j][ind])
#     else:
#         raise ValueError('operator unknown')
#     total = total + inter_total
# print(total)
numbs = []
numb_rows = len(inp)-1
total = 0
for i in range(-1, 0-len(inp[-1])-1, -1):
    if inp[-1][i] == '*':
        numb=''
        for j in range(numb_rows):
            if not inp[j][i].isspace():
                numb = numb + inp[j][i]
        numbs.append(int(numb))
        inter_total = 1
        for mult in numbs:
            inter_total = inter_total * mult
        total = total + inter_total
        numbs = []
    elif inp[-1][i] == '+':
        numb=''
        for j in range(numb_rows):
            if not inp[j][i].isspace():
                numb = numb + inp[j][i]
        numbs.append(int(numb))
        inter_total = 0
        for summnd in numbs:
            inter_total = inter_total + summnd
        total = total + inter_total
        numbs = []
    elif inp[-1][i] == ' ':
        numb = ''
        for j in range(numb_rows):
            if not inp[j][i].isspace():
                numb = numb + inp[j][i]
        if not numb == '':
            numbs.append(int(numb))
    else:
        raise ValueError
print(total)