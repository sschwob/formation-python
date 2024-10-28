# Flow & List

## Contrôle du Flow

> Le Flow Basic du code : ligne par ligne.
> On peut changer ce flow basic avec des mots clés comme **if / else**.
> Comme pour les méthodes, l'**indentation** en Python est capitale.

### If / Else

> On utilise le mot clé **if** suivi d'une comparaison ou d'une méthode / variable

```python
# Structure de contrôle : if
if condition:
  # code exécuté seulement quand la condition est "vraie"
  pass
```

> En Python, tout ce qui est différent de `False`, `None`, `0`, `""`, `[]`, et `{}` est "truthy".

```python
# if not
if not condition:
  # code exécuté seulement quand la condition est "fausse"
  pass
```

```python
# Exemple interactif : âge de vote
age = int(input("Quel âge as-tu ? "))

if age >= 18:
  print("Tu peux voter !")
else:
  print("Trop jeune pour voter...")
```

### Opérateur ternaire

> syntaxe : valeur_si_vrai if condition else valeur_si_faux

```python
choice = input("Pile ou face ? ")
coin = random.choice(["pile", "face"])

result = "Gagné" if choice == coin else "Perdu"
print(f"{result}, c'était {coin}.")
```

### Structure conditionnelle étendue : if / elif / else

```python
import datetime

hour = datetime.datetime.now().hour

if hour < 12:
  print("Bonjour!")
elif 12 <= hour < 20:
  print("Bonne après-midi!")
else:
  print("Bonne soirée!")
```

### Structure de contrôle : match / case

```python
action = input("Que veux-tu faire ? ").lower()

match action:
  case "lire":
    print("Vous êtes en mode LECTURE")
  case "écrire":
    print("Vous êtes en mode ÉCRITURE")
  case "quitter":
    print("Au revoir")
  case _: # Valeur par défault
    print("Action inconnue")
```

### Conditions Multiples - AND

```python
True  and True           #=> True
False and False          #=> False
True  and False          #=> False
False and True           #=> False
True  and False and True #=> ?
```

### Conditions Multiples - OR

```python
True  or True            #=> True
False or False           #=> False
True  or False           #=> True
False or True            #=> True
True  or False or True   #=> ?
```

```python
if (hour > 9 and hour < 12) or (hour > 14 and hour < 18):
  print("Le magasin est ouvert !")
else:
  print("Désolé, le magasin est fermé...")
```

### Boucle `while` (tant que...)

```python
import random

price_to_find = random.randint(1, 5)
choice = None # Initialisation de la variable

while choice != price_to_find:
    choice = int(input("Quel est le prix (entre 1 et 5) ? "))
print(f"Gagné ! Le prix était {price_to_find}$")
```

### Boucle `for`

```python
for num in [1, 2, 3]:
  print(num)
```

## Listes

### Définir une liste

```python
empty_list = []                     # une liste vide
beatles = ["john", "ringo", "seb"]  # une liste de 3 strings
```

### Accéder à un élément par index

```python
beatles = ["john", "ringo", "seb"]
beatles[0]  #=> "john"
beatles[2]  #=> "seb"
beatles[8]  #=> Error > IndexError: list index out of range

# Note : Les index commencent à 0 en Python
beatles = ["john", "ringo", "seb"]
# index =>    0       1       2
```

### Modifier un élément

```python
beatles = ["john", "ringo", "seb"]
beatles[2] = "george"
print(beatles)  # => ["john", "ringo", "george"]
```

### Ajouter un élément

```python
beatles = ["john", "ringo", "seb"]
beatles.append("paul")
print(beatles)  # => ["john", "ringo", "george", "paul"]
```

### Supprimer un élément par valeur

```python
beatles = ["john", "ringo", "seb"]
beatles.remove("john")
print(beatles) #=> ['ringo', 'seb']
```

### Supprimer un élément par index

```python
beatles = ["john", "ringo", "seb"]
del beatles[2]
print(beatles) #=> ['john', 'ringo']
```

### Longueur de la liste
```python
beatles = ["john", "ringo", "seb"]
len(beatles)  #=> 3
```

### Parcourir la liste
```python
for beatle in beatles:
  print(f"{beatle} est dans les Beatles")
```
