filename = './input.txt'

with open(filename, 'r') as f:
    inp = f.read()
    f.close()
  
inps = inp.split(',')

inv_idn_sum = 0

def check_id(idn_func):
    valid = True
    for i in range(len(idn_func), 1, -1):
        if not(len(idn_func)%i ==0):
            continue 
        div = len(idn_func)//i
        valid = False
        for j in range(div):
            for k in range(1,i):
                if not(idn_func[j] == idn_func[j+(k)*div]):
                    valid = True
                    break
            if valid == True:
                break
        if valid == False:
            return int(idn)
    return 0

for ids in inps:
    id_range = ids.split('-')
    for idn in range(int(id_range[0]), int(id_range[1])+1):
        return_val = check_id(str(idn))
        inv_idn_sum += return_val
print(inv_idn_sum)