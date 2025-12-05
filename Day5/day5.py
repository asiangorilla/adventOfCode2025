filename = './input.txt'

with open(filename, 'r') as f:
    inp = f.read().split('\n')
    f.close()

in_range = 0
split = 0
ranges = []
for ind,inp_row in enumerate(inp):
    if inp_row == "":
        split = ind
        break
    ranges.append([int(inp_row.split('-')[0]), int(inp_row.split('-')[1])])

def check_in_range(ing:int):
    for range_ in ranges:
        if ing < range_[0]:
            continue
        if ing <= range_[1] and ing >= range_[0]:
            return True
    return False

for inp_row in inp[split+1:]:
    if check_in_range(int(inp_row)):
        in_range = in_range + 1

# part 2
checked_ranges = []

numb_in_range = 0
for range_ in ranges:
    curr_num_in_range = range_[1] - range_[0] + 1
    hit = False
    for checked_range in checked_ranges:
        
        if range_[1] < checked_range[0] and range_[1] < checked_range[1]:
            pass
        
        elif checked_range[1] < range_[0] and checked_range[1] < range_[1]:
            pass
        
        elif checked_range[0] <= range_[0] and range_[1] <= checked_range[1]:
            curr_num_in_range = 0
            hit = True
            break
        
        elif range_[0] < checked_range[0] and checked_range[1] < range_[1]:
            curr_num_in_range = checked_range[0] - range_[0] + range_[1] - checked_range[1]
            checked_range[0] = range_[0]
            checked_range[1] = range_[1]
            hit = True
            break
        
        elif range_[0] < checked_range[0] and range_[1] < checked_range[1]:
            curr_num_in_range = curr_num_in_range - (range_[1]-checked_range[0] + 1)
            checked_range[0] = range_[0]
            hit = True
            
        elif checked_range[0] < range_[0] and checked_range[1] < range_[1]:
            curr_num_in_range = curr_num_in_range - (checked_range[1] - range_[0] + 1)
            checked_range[1] = range_[1]
            hit = True
        
    if not hit:
        checked_ranges.append([range_[0], range_[1]])
    
    numb_in_range = numb_in_range + curr_num_in_range
#     print(curr_num_in_range)
#     print(numb_in_range)
print(numb_in_range)
            
