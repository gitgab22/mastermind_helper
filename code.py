import random
import copy

def creation_tableau():
    L=[]
    for a in range (8):
        for b in range (8):
            for c in range (8):
                for d in range (8):
                    Q=[a,b,c,d]
                    L.append(Q)
    return L

def supprimer_sous_listes_similaires(L):
    Q=[]
    for sous_liste in L:
        Lp=[sous_liste[0]]
        Test=True
        for i in range(1,4):
            if sous_liste[i] in Lp:
                Test=False
            Lp.append(sous_liste[i])
        if Test == True:
            Q.append(sous_liste)
    return Q

Couleurs=["rouge" , "jaune", "bleu", "orange"," vert", "blanc", "violet", "rose"]

def conversion_chiffre_to_couleur(L):
    C=[]
    for i in range(4):
        C.append(Couleurs[L[i]])
    return C


def programme(doublons,debut_double,choix_optimise):
    if doublons:
        L = creation_tableau()
    else:
        L = supprimer_sous_listes_similaires(creation_tableau())
    Testfinale = True
    compteur=0
    while Testfinale and len(L) > 1:
        if debut_double and compteur==0:
                Current=[0,0,1,1]
        else:
            if choix_optimise:
                if compteur==0:
                    Current = random.choice(L)
                else:
                    Current=choix(L)
            else:
                Current = random.choice(L)
        print("Il reste", len(L), "possibilitées")
        print("A mettre ", conversion_chiffre_to_couleur(Current))
        b = int(input("Combien de couleurs bonnes mals placées ? --> "))
        p = int(input("Combien de couleurs bien placées ? --> "))
        if b+p > 4:
            print("ERREUR : couleurs > 4")
            return
        if doublons:
            L = conserver_sous_listes_communes_doublons(L, b+p, Current)
        elif not doublons:
            L = conserver_sous_listes_communes(L, b+p, Current)
        L=conserver_sous_listes_emplacements(L,p,Current)
        compteur+=1
        if len(L) <= 1:
            Testfinale = False
    if len(L)==1:
        print("SOLUTION : ", conversion_chiffre_to_couleur(L[0]))
        print(compteur, "essai(s) ")
        return compteur
    else:
        print("ERREUR liste vide")
        return

def choix(L):
    M=[]
    P=[[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[3,0],[3,1],[4,0]]
    for liste in L:
        Somme=0
        for couple in P:
            Communs=conserver_sous_listes_communes_doublons(L,couple[0],liste)
            Emplacements=conserver_sous_listes_emplacements(L,couple[1],liste)
            Union_sans_doublon = set(tuple(x) for x in Communs + Emplacements)
            Somme+=len(L)-len(Union_sans_doublon)
        M.append(Somme)
    i=indice_max(M)
    return L[i]

def choix_simplifie(L,doublons):
    M=[]
    P=[[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[3,0],[3,1],[4,0]]
    for liste in L:
        Somme=0
        for couple in P:
            if doublons:
                Communs=compteur_sous_listes_communes_doublons(L,couple[0],liste)
            else:
                Communs=compteur_sous_listes_communes(L,couple[0],liste)
            Emplacements=compteur_sous_listes_emplacements(L,couple[1],liste)
            Somme+=Communs+Emplacements
        M.append(Somme)
    i=indice_max(M)
    return L[i]

def indice_max(M):
    max=M[0]
    L=[]
    for i in range(len(M)):
        if M[i]>max:
            max=M[i]
    for i in range(len(M)):
        if M[i]==max:
            L.append(i)
    return random.choice(L)

def conserver_sous_listes_communes(L, c, sous_liste):
    nouvelle_liste = []
    for liste in L:
        elements_communs = len(set(liste) & set(sous_liste))
        if elements_communs == c:
            nouvelle_liste.append(liste)
    return nouvelle_liste

def conserver_sous_listes_communes_doublons(L, c, Current):
    nouvelle_liste = []
    for liste in L:
        elements_communs = 0
        for element in set(liste):
            occurences_liste = liste.count(element)
            occurences_Current = Current.count(element)
            elements_communs += min(occurences_liste, occurences_Current)
        if c==elements_communs:
            nouvelle_liste.append(liste)
    return nouvelle_liste

def conserver_sous_listes_emplacements(L, p, sous_liste):
    nouvelle_liste = []
    for liste in L:
        count = 0
        for i in range(4):
            if liste[i] == sous_liste[i]:
                count += 1
        if count == p:
            nouvelle_liste.append(liste)
    return nouvelle_liste

def compteur_sous_listes_communes(L, c, sous_liste):
    compteur=len(L)
    for liste in L:
        elements_communs = len(set(liste) & set(sous_liste))
        if elements_communs == c:
            compteur-=1
    return compteur

def compteur_sous_listes_communes_doublons(L, c, Current):
    compteur=len(L)
    for liste in L:
        elements_communs = 0
        for element in set(liste):
            occurences_liste = liste.count(element)
            occurences_Current = Current.count(element)
            elements_communs += min(occurences_liste, occurences_Current)
        if c==elements_communs:
            compteur-=1
    return compteur

def compteur_sous_listes_emplacements(L, p, sous_liste):
    compteur=len(L)
    for liste in L:
        count = 0
        for i in range(4):
            if liste[i] == sous_liste[i]:
                count += 1
        if count == p:
            compteur-=1
    return compteur

