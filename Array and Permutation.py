z = int(input())

for i in range(z):
    n = int(input())
    
    per = list(map(int, input().split()))
    a = list(map(int, input().split()))

    pos_map = {val: idx for idx, val in enumerate(per)}

    def check_chain(index, val, arr):
        while(index < len(arr) and val == arr[index]):
            index = index + 1
        return index - 1

    def find_window(arr):
        index = 0
        window_list = []
        while(index < len(arr)):
            val = arr[index]
            window = [index, check_chain(index,val,arr)]
            index = window[1] + 1
            window_list.append(window)
        return window_list

    def check_window(pos_map, a, window, last_idx_in_per):
        val = a[window[0]]
        
        current_idx_in_per = pos_map[val]

        if current_idx_in_per < last_idx_in_per:
            return False, current_idx_in_per
        if (current_idx_in_per >= window[0] - 1) and (current_idx_in_per <= window[1] + 1):
             return True, current_idx_in_per
        else:
             return False, current_idx_in_per

    win_list = find_window(a)
    
    possible = True
    last_idx_in_per = -1  

    for i in win_list:
        is_valid, new_idx = check_window(pos_map, a, i, last_idx_in_per)
        
        if is_valid:
            last_idx_in_per = new_idx
        else:
            possible = False
            break
            
    if possible:
        print("YES")
    else:
        print("NO")