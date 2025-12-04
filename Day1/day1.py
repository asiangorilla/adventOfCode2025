filename = './input.txt'

with open(filename, 'r') as f:
    inp = f.read()
    f.close()
    
inp = inp.split('\n')

max = 99
min = 0

dial = 50

counter = 0

for turn in inp:
    amount = int(turn[1:])
    if turn[0] == 'L':
        amount = amount* -1
        if dial == 0:
            counter -=1
    dial += amount
    while dial > max:
        if dial == 100:
            dial -= max+1
        else:
            dial -= max+1
            counter = counter +1
    while dial < min:
        dial += max+1
        counter = counter + 1
    
    if dial == 0:
        counter = counter + 1
        
print(counter)