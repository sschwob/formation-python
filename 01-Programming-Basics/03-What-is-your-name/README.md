## Contexte et objectifs

- Vérifier encore une fois ta connaissance des méthodes et des variables.
- Apprendre à utiliser l’interpolation de string (f-string).

## Spécifications

### Calcul du nom

- Implémente la méthode `compute_name` définie dans le fichier `lib/compute_name.py`. À partir de `first_name`, `middle_name` et `last_name`, elle doit retourner le nom complet de la personne.
- **contrainte** : Tu dois utiliser la **f-string** avec `f'{}'` pour former ce nom complet.

### Programme interactif

Le fichier `lib/interface.py` contient un programme pour interagir avec un utilisateur. Essaie avec :

```bash
python lib/interface.py
```

Ton programme devrait ensuite te demander d'entrer ton prénom, deuxième prénom et nom de famille dans le terminal.

En supposant que tu as saisi "Jean", puis "Baptiste" et enfin "Poquelin", le programme doit imprimer un message personnalisé ressemblant à `Hello, Jean Baptiste Poquelin!`.

- **contrainte** : ton programme `interface.py` doit bien entendu utiliser la méthode `compute_name` définie dans l’autre fichier.
- **perfectionnement** : tu peux améliorer ton `custom_message` en ajoutant d’autres informations comme le nombre de caractères du nom complet (exemple : `Jean Baptiste Poquelin has got 22 characters, including spaces`), ou d’autres détails très importants…

## Enseignements clés

Pose-toi encore une fois ces questions et assure-toi d’être capable de répondre à toutes :

### À propos des variables

- Quelles sont les variables utilisées dans ton code ?
- Où affecte-t-on des valeurs à ces variables et où les utilise-t-on ?
- Quel est la portée (scope) d’une variable ?

### À propos des méthodes

- Quelle est la méthode utilisée dans ton programme ? Où est-elle définie ?
- Où appelles-tu cette méthode et avec quels arguments ?
- Quel est le flux d'éxecution (execution flow) de ton programme lorsque tu essaies de le lire, ligne par ligne ?

### À propos des strings

- Qu’est-ce que l’interpolation de string ? Quelle est la syntaxe à utiliser pour "insérer" une expression Python dans une string ?
- Quelle est la différence entre les guillemets simples (single quotes `'`) et les guillemets doubles (double quotes) `"` ?

## Suggestions et ressources complémentaires

- Pour obtenir une réponse ou des données de l’utilisateur depuis le terminal, tu dois utiliser la méthode [input()](https://www.w3schools.com/python/ref_func_input.asp).
- Pour imprimer une reponse sur le terminal, tu dois utiliser la méthode [print()](https://www.w3schools.com/python/ref_func_print.asp)
