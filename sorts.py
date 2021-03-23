# Complexite :
# Pire cas	:       O(n^2)
# Moyenne :         O(n^2)
# Meilleur cas :    O(n)
def triInsertion(A):
    B = A.copy()
    n = len(B)

    for i in range(1, n, 1):
        # mémoriser B[i] dans x
        x = B[i]                            

        # décaler vers la droite les éléments de B[0]..B[i-1] qui sont plus grands que x en partant de B[i-1]
        j = i                               
        while (j > 0) and (B[j - 1] > x):
            B[j] = B[j - 1]
            j = j - 1

        # placer x dans le "trou" laissé par le décalage
        B[j] = x
    return B


# Complexite :
# Pire cas	:       O(n^2)
# Moyenne :         O(n^2)
# Meilleur cas :    O(n)
def triInsertionInverse(A):
    B = A.copy()
    n = len(B)

    for i in range(1, n, 1):
        # mémoriser B[i] dans x
        x = B[i]                            

        # décaler vers la droite les éléments de B[0]..B[i-1] qui sont plus grands que x en partant de B[i-1]
        j = i                               
        while (j > 0) and (B[j - 1] < x):
            B[j] = B[j - 1]
            j = j - 1

        # placer x dans le "trou" laissé par le décalage
        B[j] = x
    return B

def echanger(T, a, b):
    c = T[a]
    T[a] = T[b]
    T[b] = c
    return T

def partitionner(T, premier, dernier, pivot):
    echanger(T, pivot, dernier)
    j = premier
    for i in range(premier, dernier, 1):
        if(T[i] <= T[dernier]):
            echanger(T, i, j)
            j = j + 1
    echanger(T, dernier, j)
    return j

# Complexite :
# Pire cas	:       O(n^2)
# Moyenne :         O(n log n)
# Meilleur cas :    O(n log n)
def triRapide(T, premier, dernier):
    if (premier < dernier):
        pivot = premier
        pivot = partitionner(T, premier, dernier, pivot)
        triRapide(T, premier, pivot-1)
        triRapide(T, pivot+1, dernier)

def fusion(A, B):
	if len(A) == 0:
		return B
	if len(B) == 0:
		return A
	if A[0] <= B[0]:
		return [A[0]] + fusion(A[1:len(A)], B)
	else:
		return [B[0]] + fusion(A, B[1:len(B)])

# Complexite :
# Pire cas	:       O(n log n)
# Moyenne :         O(n log n)
# Meilleur cas :    O(n log n)
def triFusion(A):
	if len(A) <= 1:
		return A
	else:
		return fusion(triFusion(A[0:int(len(A) / 2)]), triFusion(A[int(len(A) / 2):len(A)]))


# Complexite :
# Pire cas	:       O(n^2)
# Moyenne :         O(n^2)
# Meilleur cas :    O(n^2)
def triSelection(A):
    B = A.copy()
    for i in range(0, len(B) - 1, 1):
        indexMin = i
        for j in range(i + 1, len(B), 1):
            if B[j] < B[indexMin]:
                indexMin = j
        if indexMin != i:
            echanger(B, i, indexMin)
    return B


# Complexite :
# Pire cas	:       O(n^2)
# Moyenne :         O(n^2)
# Meilleur cas :    O(n^2)
def triABulles(A):
    B = A.copy()
    for i in range(len(B)-1, 1, -1):
        for j in range(0, i-1, 1):
            if(B[j+1] < B[j]):
                echanger(B, j, j+1)
    return B