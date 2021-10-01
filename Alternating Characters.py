# s = AABAAB
#Remove an A at positions 0 and 3 to make s= ABAB in 2 deletions.
def alternatingCharacters(s):
    cnt = 0
    k = list(s)
    c_value = k[0]
    for i in range(0,len(k)-1) :
        if c_value == k[i+1] :
            cnt += 1
        else : #different
            c_value = k[i+1]
    return cnt