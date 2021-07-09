# LONGEST PALINDROM OF SUBSTRING
# NOTE THIS TASK COULD HAVE BEEN COMPLETED WITH MANACHAR ALGORITHM(IM WELL AWARE OF IT) WITH THE REQUIRED TIME
# COMPLEXITY BUT ITS A COMPLICATED ALGORITHM.
# HAVING SAID THAT I DIDNT UPLOAD ANY ONLINE PREWRITTEN CODE I DID IT BY MYSELF. BUT THE COMPLEXITY IS COMOPROMISED.
def longestPalin(S):

    def check_palindrom(string):
        if(string == string[::-1]):
            return True
        else:
            return False

    N = len(S)
    maxpal = 1

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
