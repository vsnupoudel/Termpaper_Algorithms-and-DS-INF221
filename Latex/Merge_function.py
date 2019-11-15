def sort_two_sorted_lists(A,B):
    len_total= len(A)+len(B)
    C= [None]*len_total
    index_total= len_total-1
    a= A.pop()
    b= B.pop()

    while True:
        if a >= b:
            C[index_total]= a
            if len(A) >0 :
                a= A.pop()
            else:
                a= -math.inf
            index_total -= 1
        else:
            C[index_total]= b
            if len(B) >0 :
                b= B.pop()
            else:
                b= - math.inf
            index_total -= 1

        if a == - math.inf and\
                b == - math.inf:
            break
    return C