def consecutive_zeros(num):
    lis = list(num)
    khali = []
    sum = 0

    for i in lis:

        if i == '0':
            sum += 1

        elif i == '1':
            khali.append(sum)
            sum = 0
        khali.append(sum)

    if khali == []:
        return 0
    
    else: return max(khali)
