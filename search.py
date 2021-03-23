def rechercheDichotomique(A):
    # A coder
    return 1

def rechercheLineaire(A, x):
    n = len(A)
    i=0
    while(i < n) and (A[i] != x):
        i=i+1

    if (i != n):
        return i
    else:
        return -1