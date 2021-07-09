# FIND MAXIMUM MEETINGS IN A ROOM
def maxMeetings(S, F, N):
    bucket = []
    for i in range(N):
        bucket.append([S[i], F[i]])

    bucket.sort(key=lambda x: x[1])
    limit = bucket[0][1]
    count = 1
    for i in range(1, N):
        if bucket[i][0] > limit:
            count += 1
            limit = bucket[i][1]
    return count


S = [1, 3, 0, 5, 8, 5]
F = [2, 4, 6, 7, 9, 9]
N = len(S)

maxMeetings(S, F, N)
