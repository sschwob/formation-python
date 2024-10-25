## Contexte et objectifs

- Apprendre à chercher la bonne méthode dans la documentation Python.
- Te familiariser avec la console pour tester de nouvelles méthodes et te les approprier.

la console Python est une boucle de lecture-évaluation-impression [REPL](http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop). Elle fonctionne comme ceci :

1.  Le **R** (première lettre de l’acronyme anglais REPL - Read) lit l’expression écrite par l’utilisateur ; il peut s’agir de n’importe quelle expression Python valide comme `"Hello"`, `2+2`, `"hello".upper()`…
2.  Le **E** (deuxième lettre de l’acronyme anglais REPL - Evaluate) évalue le résultat de l’expression.
3.  Le **P** (troisième lettre de l’acronyme anglais REPL - Print) imprime ce résultat.
4.  Le **L** (dernière lettre de l’acronyme anglais REPL - Loop) revient en boucle au point 1 et attend une nouvelle saisie de la part de l’utilisateur.

- **Teste les lignes suivantes** dans IRB :

```python
type("A string object")
type(19)
type([1, 2, 3])
"A string object".upper()
"A string object".lower()
```

Dans Python, tout (une chaîne de caractères, un nombre entier ou décimal, un tableau…) est un objet. On peut appeler des méthodes sur ces objets. Ces méthodes sont appelées des **méthodes d’instance**, car elles peuvent uniquement être appelées sur les instances d’une classe. L’objet sur lequel on appelle la méthode est le **récepteur**.

## Spécifications

Trouve les bonnes méthodes Python dans [la classe String](https://docs.python.org/fr/3/library/stdtypes.html#string-methods) et [la classe List](https://docs.python.org/fr/3/tutorial/datastructures.html) à utiliser pour faire passer les tests.

Coder implique d’être malin et de savoir où et comment chercher l’info dont tu as besoin ! Souvent, le plus difficile est de bien formuler la question que tu poses à Google. Pour trouver les méthodes utiles à ce challenge, utilise :

- Google et [Stack Overflow](http://stackoverflow.com/)
- [La documentation Python](https://docs.python.org/fr/3/) si tu as déjà une petite idée de la méthode que tu cherches.

Une fois que tu penses avoir trouvé la méthode dont tu as besoin, et que tu penses savoir comment t’en servir, utilise la console pour tester cette méthode sur quelque chose ! Les tests représentent une étape clé pour les débutants.

## Enseignements clés

Es-tu capable de répondre aux questions suivantes ? Si ce n’est pas le cas, alors tu n’es pas prêt à passer à la suite !

- Combien de classes intégrées à Python connais-tu ? Lesquelles ?
- Quelle est la syntaxe pour appeler une méthode sur un objet de ces classes ?
- Quelle doit être la toute première étape lorsque tu cherches à effectuer une opération standard (trier une liste, mettre un mot en majuscules, etc.) ?
- Quelle est la deuxième étape à effectuer pour vérifier que tu as bien compris la méthode que tu as trouvée ?
