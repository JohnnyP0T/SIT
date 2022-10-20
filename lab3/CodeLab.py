import DifferenceBoolList


def code1(x,k):
    s = []
    for i in range(len(x)):
        s.append(x[i])
        if i - k >= 0:
            s.append(int(bool(x[i]) != bool(x[i-k])))
        else:
            s.append(x[i])
    for i in range(len(x),len(x) + k):
            s.append(x[i-k])
    return s
def code(x,k):
    s = []
    count = 0
    for i in range(len(x)):
        if i + k >= len(x):
            s.append(x[i])
            s.append(int(bool(x[i]) != bool(x[count])))
            count = count + 1
        else:
            s.append(x[i])
            s.append(int(bool(x[i]) != bool(x[i+k])))
    return s

def deCode(x,dif,k):
    count = 0
    for i in range(len(x)):
        if i + k >= len(x):
            if dif[i] == 1 and dif[count] == 1:
                x[count] = int(not bool(x[count]))
            count = count + 1
        else:
            if dif[i] == 1 and dif[i+k] == 1:
                x[i+k] = int(not bool(x[i+k]))
    return x