filename = './input.txt'

battery_amount = 12

with open(filename, 'r') as f:
    inp = f.read().split('\n')
    f.close()

total_jolt = 0

for bank in inp:
    battery_bank = ''
    m_prev_battery_ind = -1
    for limit in range(1-battery_amount, 1):
        if limit == 0:
            end = None
        else:
            end = limit
        
        max_current_battery = '0'
#         print('start_index '+ str(m_prev_battery_ind+1))
        current_battery_index = m_prev_battery_ind+1
        for index, battery in enumerate(bank[m_prev_battery_ind+1:end]): 
            if battery > max_current_battery:
                max_current_battery = battery
#                 print("   " + battery)
                current_battery_index = index + m_prev_battery_ind+1
        m_prev_battery_ind = current_battery_index
#         print(max_current_battery)
        battery_bank = battery_bank + max_current_battery
#     print(battery_bank)
    total_jolt = total_jolt + int(battery_bank)
print(total_jolt)
