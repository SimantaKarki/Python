def bitsChecker(bits):
    count0 = 0
    count1 = 0
    l0 = []
    l1 = []
    f0 = 0
    f1 = 1

    for i in bits:
        if i == '0':
            count0 += 1
        else:
            l0.append(count0)
            count0 = 0
    
    for i in bits:
        if i == '1':
            count1 += 1

        else:
            l1.append(count1)
            count1 = 0

    l1.append(count1)
    l0.append(count0)

    for i in l0:
        if i>0 and i%2 != 0:
            f0 = 1
            break
    for i in l1:
        if i > 0 and i%2 == 0:
            f1 = 0
            break
    
    if f0 == 0 and f1 == 1:
        return "Yes"
    else:
        return "No"


print(bitsChecker('00111011'))