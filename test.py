Q
L=test(Q)
L

Q=[[1,2,6],[1,3,1],[1,4,0],[2,3,8],[2,2,5]]
Q
C=[1,5,6,4]
C1=[1,2,1,0]
C2=[1,1,1,1]
Q=suppression(Q,0,1,Current)

Q=[[1,2,6,4],[1,3,1,9],[1,4,0,2],[2,3,8,5],[2,2,5,1]]
#Q = [sublist for sublist in Q if not any(element == 1 for element in sublist)]

def suppression(Q, p, c, Current):
    L = copy.deepcopy(Q)
    for sous_liste in Q:
        if memenombre(sous_liste, Current, c)==False:
            L = retirer(L, sous_liste)
    return L

def test(Q):
    for sous_liste in Q:
        if not (1 in sous_liste) ^ (3 in sous_liste) ^ (4 in sous_liste):
            Q=retirer(Q,sous_liste)
    return Q

def retirer(L,sous_liste):
    n=len(L)
    Q=[]
    for i in range(n):
        if L[i]==sous_liste:
            Q=L[:i]+L[i+1:]
            return Q
    return L

def memenombre(liste1, liste2, nombre):
    communs = set(liste1) & set(liste2)
    if len(communs) == nombre:
        return True
    else:
        return False

def supprimer_sous_listes_similaires(liste):
    nouvelle_liste = []
    for sous_liste in liste:
        if len(set(sous_liste)) == len(sous_liste):
            nouvelle_liste.append(sous_liste)
    return nouvelle_liste

