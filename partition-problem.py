def partition(sArray):
    '''
    It divides a multiset S into two partitions (S1 and S2) 
    that have equal sums. For example, if S = {2,2,10,5,15,4,1} then it can produce S1 = {5,15} and
    S2 = {2,2,1,1,10,4}, both of which sum to 20.

    It also aims to minimise the absolute difference between two sums. For example, if S = {2,6,15,10} then
    the optimal partition is S1 = {2,15} and S2 = {6,10}, which have sums of 17 and 16 respectively,
    giving an absolute difference of 1.
    '''

    # Approach A: Divide S into two equally-sized partitions (S1 and S2) by 
    # splitting the array in the middle
    m = len(sArray)//2
    S1 = sArray[:m]
    S2 = sArray[m:]
    dif = abs(sum(S1) - sum(S2))
    #print("S1: ", S1)
    #print("S2: ", S2)
    #print("difference = ", dif, "target = ",target)
    return dif



