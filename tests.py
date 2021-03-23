import sorts
import search

def testTriInsertion():
    print("Test du Tri Insertion")
    A = [31, 41, 59, 26, 41, 58]
    B = sorts.triInsertion(A)
    print("A = " + str(A))
    print("B = " + str(B))

def testTriInsertionInverse():
    print("Test du Tri Insertion Inverse")
    A = [31, 41, 59, 26, 41, 58]
    B = sorts.triInsertionInverse(A)
    print("A = " + str(A))
    print("B = " + str(B))

def testRechercheLineaire():
    A = [31, 41, 59, 26, 41, 58]
    x = 59
    y = 1
    print("rechercheLineaire, x = " + str(x) + ", retourne = " + str(search.rechercheLineaire(A,x)))
    print("rechercheLineaire, y = " + str(y) + ", retourne = " + str(search.rechercheLineaire(A,y)))

def testEchanger():
    T = [31, 41, 59, 26, 41, 58]
    a = 0
    b = 2
    print("Avant echange : a = " + str(a) + ", b = " + str(b) + ", T = " + str(T))
    sorts.echanger(T,a,b)
    print("Après echange : a = " + str(a) + ", b = " + str(b) + ", T = " + str(T))

def testTriRapide():
    T = [31, 41, 59, 26, 41, 58]
    print("Avant tri rapide : T = " + str(T))
    sorts.triRapide(T,0, len(T)-1)
    print("Après tri rapide : T = " + str(T))

def testTriFusion():
    T = [31, 41, 59, 26, 41, 58]
    print("Avant tri fusion : T = " + str(T))
    T = sorts.triFusion(T)
    print("Après tri fusion : T = " + str(T))

def testTriSelection():
    T = [31, 41, 59, 26, 41, 58]
    print("Avant tri par selection : T = " + str(T))
    T = sorts.triSelection(T)
    print("Après tri par selection : T = " + str(T))

def testTriABulles():
    T = [31, 41, 59, 26, 41, 58]
    print("Avant tri à bulles : T = " + str(T))
    T = sorts.triABulles(T)
    print("Après tri à bulles : T = " + str(T))
