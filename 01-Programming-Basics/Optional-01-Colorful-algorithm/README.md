## Contexte et Objectifs

Félicitations pour être arrivé au premier exercice optionnel ! Celui-ci est un peu plus complexe et devrait vous occuper plus longtemps. Il peut être vu comme un [Code Kata](http://fr.wikipedia.org/wiki/Kata_%28programmation%29), un exercice pour les programmeurs pour s’entraîner.

## Spécifications

Nous vous demandons d'écrire une méthode `is_colorful` qui prend un nombre en argument et renvoie `True` si le nombre est **coloré**, et `False` sinon.

Un nombre coloré est un nombre pour lequel tous les produits des sous-ensembles consécutifs de chiffres sont différents.

Pour cet exercice, considérez uniquement les nombres ayant jusqu'à **3** chiffres (pas plus).

Exemple :

- `263` est un nombre coloré car (2, 6, 3, 2x6, 6x3, 2x6x3) sont tous différents
- `236` ne l'est pas car (2, 3, **6**, **2x3**, 3x6, 2x3x6) contient deux fois le produit 6.
