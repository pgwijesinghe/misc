array = [1,2,3,4,5,6]
size = 2

i = 0  # index
mov_avg = []  # empty array for the output

mov_avg.append((array[0] + array[1])/2)  # first element
while i < len(array) - size + 1:  # middle elements
    temp_arr = array[i : i + size]
    temp_arr_avg = sum(temp_arr) / size
    mov_avg.append(temp_arr_avg)
    i += 1
mov_avg.append((array[-1] + array[-2])/2)  # final element

print(mov_avg)