WEI = [1, 2, 3, 4, 5] # weights
INS = [1, 1, 1, 1, 1] # inputs

def neuron(WEI, INS):
    if len(WEI) != len(INS):
        print("number of weights does not match the number of inputs given.\npossible fixes:\n1: check if the number of weights is the same as the number of inputs.")
        while True:
            1
    WEIINS = []
    for x in range(len(WEI)):
        WEIINS.append(INS[x] * WEI[x])
    WEIINS.sort()
    NOROUT = WEIINS[len(WEIINS) - 1]
    if NOROUT >= 0:
        RELU = NOROUT
    else:
        RELU = 0
        global out
    out = RELU

neuron(WEI, INS)
print(out)