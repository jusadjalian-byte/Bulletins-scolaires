# ======================================================
#   BULLETINS DE FIN DE TRIMESTRE DES ELEVES
# ======================================================
MAXIMUM = 20
#Fonction notifiant les erreurs
def saisir_entier( message) :
    while True :
        try :
            return int(input(message))
        except ValueError :
            print("Erreur : Veuillez entrer un nombre entier.")

def saisir_decimal(message) :
    while True :
        try :
            return float(input(message))
        except ValueError:
            print("Erreur : Veuillez entrer un nombre.")

#Fonction sur la valeur maximale d'une note :

def saisir_note(message, maximum) :
    while True :
        try :
            note = float(input(message))
            if 0 <= note <=maximum :
                return note
            else :
                print(f"Erreur : La note doit être comprise entre 0 et {maximum}.")
        except ValueError :
            print("Erreur : Veuillez entrer un nombre.")

#Fonction pour calculer les moyennes :
def calculer_moyenne(notes) :
    if len(notes) == 0 :
        return None
    return sum(notes) / len(notes)

def calculer_moyenne_generale(matieres) :
    somme_ponderee = sum(m["moyenne"] *m["coef"] for m in matieres)
    somme_coefs = sum(m["coef"] for m in matieres)
    if somme_coefs == 0 :
        return 0
    return somme_ponderee / somme_coefs


# fonction structure :
def saisir_structure() :
    nb_matiere = saisir_entier("combien de matiere :")
    while nb_matiere < 1 :
             print("Erreur : il faut aumoins une matière.")
             nb_matiere = saisir_entier("combien de matiere : ")
    structure = []
    for j in range(nb_matiere):
            nom_matiere = input(f"Nom de la matière {j+1} : ")
            coef = saisir_decimal(f"Coefficient de {nom_matiere} : ")
            while coef <= 0 :
                print("Erreur : Le coefficient doit être superieure à 0")
                coef = saisir_decimal(f"Coefficient de {nom_matiere} : ")
            structure.append({"nom" : nom_matiere, "coef" : coef})
    return structure



# Fonctions pour le fonctionnement du programme

def saisir_matieres(structure):
        matieres = []
        for s in structure :
            nom_matiere = s["nom"]
            coef = s["coef"]
            print(f"\n{nom_matiere} (coef {coef})")
     
            nb_interro = saisir_entier(f"Combien d'interrogations avez-vous fait :")
            interrogations = []
            for k in range(nb_interro) :
                interrogation =saisir_note(f"Interrogation {k+1} :", MAXIMUM)
                interrogations.append(interrogation)
            nb_dev =saisir_entier(f"Combien de devoir avez-vous fait :")
            devoirs = []
            for l in range(nb_dev) :
                dev = saisir_note(f"Devoir {l+1} :", MAXIMUM) 
                devoirs.append(dev)
             
            moyenne_interrogation = calculer_moyenne(interrogations)
            moyenne_devoirs = calculer_moyenne(devoirs)
            if moyenne_interrogation is None and moyenne_devoirs is None :
               moyenne_matiere = 0
            elif moyenne_interrogation is None :
                 moyenne_matiere = moyenne_devoirs
            elif moyenne_devoirs is None :
                 moyenne_matiere = moyenne_interrogation
            else : 
                 moyenne_matiere = (moyenne_interrogation + moyenne_devoirs) / 2
                
            matieres.append({
                "nom": nom_matiere,
                "coef": coef,
                "notes": interrogations + devoirs,
                "moyenne": moyenne_matiere

            })
            print(f"Moyenne en {nom_matiere} : {moyenne_matiere:.2f} x coef {coef} = {moyenne_matiere * coef:.2f}")

        return matieres


def determiner_mention(moyenne):
    if moyenne >= 16:
        return "Félicitations"
    elif moyenne >= 14:
        return "Compliments"
    elif moyenne >= 12:
        return "Encouragements"
    elif moyenne >= 10:
        return "Passable"
    else:
        return "Avertissement"


def classer(eleves, obtenir_moyenne) :
    classement = sorted(eleves,key=obtenir_moyenne, reverse=True)
    resultat =[]
    rang_actuel = 0
    moyenne_precedente = None
    for position, e in enumerate(classement, start=1) :
        moyenne = obtenir_moyenne(e)
        if moyenne != moyenne_precedente:
            rang_actuel = position
        resultat. append((rang_actuel,e))
        moyenne_precedente = moyenne
    return resultat

    


# ------------------------------------------------------
# SAISIE DES ELEVES
# ------------------------------------------------------

print("-------BULLETINS DE FIN DE TRIMESTRE DES ELEVES-------")
nb_eleves = saisir_entier("Combien d'élèves avez-vous dans votre classe : \n")


structure = saisir_structure()
eleves = []

for i in range(nb_eleves):
    print(f"\n--- Élève {i+1} ---")
    nom = input("Nom et prénom(s) : ")

    semestre = {}
    for numero in (1, 2) :
        print(f"\nSemestre {numero}")
        matieres = saisir_matieres(structure)
        moyenne = calculer_moyenne_generale(matieres)
        mention = determiner_mention(moyenne)
        semestre[numero] = {"matieres": matieres, "moyenne": moyenne, "mention": mention}
        print(f"Moyenne du semestre {numero} : {moyenne : .2f} / 20 - {mention}")

    moyenne_annuelle = (semestre[1]["moyenne"] + 2* semestre[2]["moyenne"]) / 3
    mention_annuelle = determiner_mention(moyenne_annuelle)

    eleves.append({
        "nom" : nom,
        "semestres" : semestre,
        "moyenne_annuelle": moyenne_annuelle,
        "mention_annuelle": mention_annuelle
    })
    print(f"Moyenne annuelle de {nom} : {moyenne_annuelle:.2f}/20 -{mention_annuelle}")

    
# Calcul des rangs
for numero in (1, 2) :
    for rang, e in classer(eleves , lambda e: e["semestres"] [numero]["moyenne"]) :
        e["semestres"][numero]["rang"] = rang
for rang, e in classer(eleves, lambda e: e["moyenne_annuelle"]) :
    e["rang_annuel"] = rang 


#Affichage final

for numero in (1, 2) :
    print("\n\n===================================")
    print(f"     CLASSEMENT SEMESTRE {numero}")
    print("===========================================")
    for rang, e in classer(eleves , lambda e: e["semestres"] [numero]["moyenne"]) :
        s = e["semestres"][numero]
        print(f"{rang}. {e['nom']} - {s['moyenne']:.2f}/20 - {s['mention']}")

print("\n\n===================================")
print(f"     CLASSEMENT ANNUEL    ")
print("===========================================")
for rang, e in classer(eleves, lambda e: e["moyenne_annuelle"]) :
    print(f"{rang}. {e['nom']} -{e['moyenne_annuelle'] :.2f} /20 -{e['mention_annuelle']}")



for e in eleves :
    print(f"\n{e['nom']}")
    for numero in (1, 2) :
        s = e["semestres"][numero]
        print(f"Semestre {numero} - Rang : {s['rang']}- Moyenne : {s['moyenne']:.2f}/20 - {s['mention']}")
        for m in s["matieres"] :
            print(f"   {m['nom']} (coef {m['coef']}) : notes {m['notes']} -> moyenne {m['moyenne']:.2f}")
    print(f"  ANNUEL- Rang : {e['rang_annuel']} - Moyenne : {e['moyenne_annuelle'] :.2f} / 20 - {e['mention_annuelle']}")
