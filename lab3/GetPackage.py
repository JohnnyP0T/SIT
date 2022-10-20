def getInformationPackage(s):
    result = []
    for i in range(len(s)):
        if i % 2 == 0:
            result.append(s[i])
    return result

def getVerificationPackage(s):
    result = []
    for i in range(len(s)):
        if i % 2 == 1:
            result.append(s[i])
    return result
