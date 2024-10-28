## Contexte et objectifs

La [classe `List`](https://docs.python.org/3/tutorial/datastructures.html) est l’une des deux structures principales utilisées pour stocker et accéder à des données en Python.

Une list est ordonnée, si bien que chaque élément est accessible par son **indice** (index). Cet exercice t’aidera
à comprendre comment créer une list, comment stocker des données dedans et comment récupérer ces données en utilisant l’indice.
Souviens-toi que les indices des lists commencent à `0`, et non à `1`.

On demande souvent aux développeurs de trier des choses ; on te conseille donc de te renseigner sur [les algorithmes de tri](https://fr.wikipedia.org/wiki/Algorithme\_de\_tri).

## Spécifications

- Implémente une méthode `class_sort` qui prend un argument, une list de noms d’étudiants (`String`), et retourne une list de ces noms d’étudiants triés par ordre alphabétique.
- La méthode de tri ne doit pas tenir compte de la casse; `bob` doit apparaître avant `Felix` (regarde la [table de caractères ASCII](http://www.asciitable.com/))
- La méthode doit respecter l’orthographe des noms.

### Programme interactif

Ouvrez le fichier `interface.py` et assurez-vous d'utiliser la méthode `class_sort`. L'interface devrait avoir une sortie correctement stylisée. Les noms doivent être séparés par des virgules (`, `) sauf pour les deux derniers qui doivent être séparés par le mot `and`. Les noms doivent également être sur une nouvelle ligne.

Elle doit fonctionner comme ceci :

```bash
ruby lib/interface.py

Type a student name:
felix
Type another student name or press enter to finish:
Cedric
Type another student name or press enter to finish:
bob
Type another student name or press enter to finish:

Congratulations! Your Wagon has 3 students:
bob, Cedric and felix
```

## Enseignements clés

Familiarise-toi avec les opérations de base des listes. Tu dois maintenant connaître la syntaxe à utiliser pour :

- créer une list
- ajouter un nouvel élément à la list
- accéder au n-ième élément
- mettre à jour un élément
- supprimer un élément situé à un indice donné
