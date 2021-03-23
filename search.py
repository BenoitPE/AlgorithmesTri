# Recherche dichotomique : recherche parmi un tableau trié
def rechercheDichotomique(element, A):
    length = len(A)
    m = length / 2 
    if(A[m] == element):
        return m

    if(A[m] > element):
        return rechercheDichotomique(element, A[1:m-1])
    else :
        return rechercheDichotomique(element, A[m+1:length])

def rechercheLineaire(A, x):
    n = len(A)
    i=0
    while(i < n) and (A[i] != x):
        i=i+1

    if (i != n):
        return i
    else:
        return -1