import matplotlib.pyplot as plt
import time

def distribution_graphique(n,doublons,debut_double,choix_optimise):
    if doublons:
        L = creation_tableau()
    else:
        L = supprimer_sous_listes_similaires(creation_tableau())
    compteur=[]
    S=0
    start=time.time()
    T=[]
    Courbe_pos=[]
    for i in range(n):
        if i%1000==0 and i!=0:
            print("fin calcul ",i)
            end=time.time()
            temps=end-start
            print("temps mis ",temps)
            T.append(temps)
            start=time.time()
            print("debut calcul ",i+10)
        Solution=random.choice(L)
        c,nb_pos=programme_choix_aleatoire_stats(Solution,doublons,debut_double,choix_optimise)
        S+=c
        compteur.append(c)
        Courbe_pos.append(nb_pos)
    print ("Moyenne : ", S/n)
    if len(T)!=0:
        print("Temps moyen à la dizaine: ", sum(T)/len(T))
    valeurs, frequences = [], []
    for valeur in set(compteur):
        valeurs.append(valeur)
        frequences.append(compteur.count(valeur))
    plt.subplot(1,2,1)
    plt.bar(valeurs, frequences)
    plt.xlabel('Valeur')
    plt.ylabel('Fréquence')
    plt.title('Distribution pour n={}'.format(n))


    plt.subplot(1,2,2)
    for i in range(n):
        y=Courbe_pos[i]
        plt.plot([j for j in range(len(y))],y)
    plt.xlabel('Nombre de coup(s) joué(s)')
    plt.ylabel('Nombre de possibilités')
    plt.title('Evolution du nombre de possibilités pour n={}'.format(n))
    plt.show()


def programme_choix_aleatoire_stats(Solution,doublons,debut_double,choix_optimise):
    if doublons:
        L = creation_tableau()
    else:
        L = supprimer_sous_listes_similaires(creation_tableau())
    Testfinale = True
    compteur=0
    nb_possibilites=[len(L)]
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
        c = compteur_total(Current,Solution)
        p = compteur_emplacements(Current,Solution)
        if doublons:
            L = conserver_sous_listes_communes_doublons(L, c, Current)
        elif not doublons:
            L = conserver_sous_listes_communes(L, c, Current)
        L = conserver_sous_listes_emplacements(L,p,Current)
        compteur+=1
        if len(L) == 1:
            Testfinale = False
        nb_possibilites.append(len(L))
    return compteur,nb_possibilites


def compteur_emplacements(Current, Solution):
    count=0
    for i in range(4):
        if Current[i] == Solution[i]:
            count += 1
    return count


def compteur_total(Current,Solution):
    elements_communs = 0
    for element in set(Solution):
        occurences_Solution = Solution.count(element)
        occurences_Current = Current.count(element)
        elements_communs += min(occurences_Solution, occurences_Current)
    return elements_communs