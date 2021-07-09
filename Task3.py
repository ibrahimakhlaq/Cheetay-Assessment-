# LONGEST PALINDROM OF SUBSTRING
# NOTE THIS TASK COULD HAVE BEEN COMPLETED WITH MANACHAR ALGORITHEM(IM WELL AWARE OF IT) WITH THE REQUIRED TIME
# COMPLEXITY BUT ITS A COMPLICATED ALGORITHEM AND VERY TOUGH TO WRAP YOUR HEAD AROUND.
# HAVING SAID THAT I DIDNT UPLOAD ANY PREWRITTEN CODE ONLINE I DID IT BY MYSELF. BUT THE COMPLEXITY IS COMOPROMISED.
def longestPalin(S):

    def check_palindrom(string):
        if(string == string[::-1]):
            return True
        else:
            return False

    N = len(S)
    maxpal = 1
    start = 0

    longpal = S[0]
    for i in range(N):
        temp = ""
        for j in range(i, N):
            temp = temp + S[j]
            if(check_palindrom(temp) == True):
                if(maxpal < len(temp)):
                    maxpal = len(temp)
                    longpal = temp
    return longpal


S = "asdasdasdnoaabbbaaonasdasdasdpeeweeppip"

longestPalin(S)
