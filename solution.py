def check_pin(pinCode):
    pinc = pinCode.split('-')
    c = 0
    fl1 = False
    for i in range(1, int(pinc[0]) + 1):
        if int(pinc[0]) % i == 0:
            c += 1
    if c > 2:
        fl1 = False
    else:
        fl1 = True
    if pinc[1] == pinc[1]-1:]