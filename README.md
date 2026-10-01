## Bulletins scolaires

Programme Python qui génère les bulletins d'une classe de collège : saisie des notes, moyennes, classements et moyenne annuelle.

## Fonctionnalités
- Saisie des notes par matière, pour deux semestres (Semestre 1 et Semestre 2)
- Calcul des moyennes avec un barème fixe sur 20
- Moyenne annuelle : (S1 + 2 × S2) / 3
- Classement par semestre et classement annuel

## Lancer le programme
```
python Bulletins.py`
```

## Comment j'ai travaillé
J'ai d'abord fait une version de base qui calcule les moyennes, puis je l'ai améliorée pour gérer deux semestres et la moyenne annuelle.

## Difficultés rencontrées
- **Division par zéro :** si un élève n'a aucune note, le calcul de la moyenne plantait. J'ai écrit une fonction `calculer_moyenne` qui renvoie `None` quand la liste est vide, au lieu de forcer au moins une note.
- **Avancer par étapes :** il m'a fallu du temps pour organiser le programme.

## Ce que j'ai appris
- Gérer les cas particuliers (liste vide) avant qu'ils provoquent une erreur
- Découper un problème en fonctions
- Faire évoluer un programme par versions successives
