# TP2: TP2- DESIGN PATTERNS MAP- REDUCE
Les Patrons de Conception Map Reduce (ou plus communément les Design Patterns) permettent
d’aider l’utilisateur à savoir QUAND utiliser Map-Reduce pour résoudre ses problèmes.
Chacun de ces patrons représente une classe de problèmes récurrents pour ceux qui manipulent
les Big Data. Ce qui est utile, car on peut ainsi appliquer une solution standardisée et unifiée pour
chacune de nos difficultés.
Les Design Patterns les plus utilisés sont:
- Les Patrons de Filtrage
- Les Patrons de Récapitulation
- Les Patrons Structurels


# A propos
Les codes du mapper et du reducer sont écrits en Python.

Lors de ce Tp, Nous avons utilisé la machine virtuelle de Cloudera qui est une machine Linux, sur laquelle est installé le framework Hadoop , ainsi qu’un grand nombre d’outils de son  écosystème, sont préinstallés.

Nous avons testé le mapper et le reducer en local, ensuite nous avons exécuté le code directement sur HDFS.


# Activité 1 : Patrons de Filtrage : Filtrage Simple

Nous allons compter le nombre de posts avec une seule phrase ou moins, en appliquant le patron de Filtrage
- Un Mapper s'occupe d'extraire uniquement les posts d’une phrase ou moins

- Un Reducer s'occupe de calculer le nombre de posts d'une phrase ou moins

- Resultat : On trouve 32562 posts ayant une phrase ou moins


# Activité 2 Et 3 : Patrons de Récapitulation

On distingue deux types pour ce patron de conception Index ,Récapitulation

* Activité 2 : INDEX

Dans l'activité 2 ,le but est de créer  un index pour les données c'est à dire réaliser un programme pour ecrire dans un fichier pour chaque mot dans quels postes du forum il a été mentionné et le nombre d'occurence

- Un Mapper: s'occupe  d’extraire tous les mots d’un post et donne le couple (mot,node_id)

- Un reducer: s'occupe de  calculer le nombre d'occurences de chaque mot recu des mappers.

Les mappers quant à eux vont découper chaque post en ses mots .

* Activité 3: Moyenne

Dans l'activité 3 ,le but est de calculer la moyenne des ventes pour chaque jour de la semaine 

- Un mapper:  s'occupe d'extraire le cout de vente pour chaque jour de la semaine le resultat sera sous la forme (jour de la semaine ,coût)

- Un reducer: s'occupe de calculer le coût total de chaque jour de la semaine ainsi que le nombre afin d'en générer la moyenne.

- Resultat : 6 249.946443251

# Activité 4 : Combiner

Dans cette activité,notre but est de calculer la somme des ventes par jour de la semaine.

- Un Mapper: s'occupe d’extraire le cout de vente pour chaque jour de la semaine le resultat sera le couple  (jour de la semaine ,coût)

- Un reducer: s'occupe de calculer la somme des ventes pour chaque jour de la semaine.

- Sans Combiner:

 * La somme des ventes le dimanche :  6 150296795.47

 * La valeur du Reduce Input Records: 4138476

 - Avec Combiner:

 * La somme des ventes le dimanche : 6 150296795.47

 * La valeur du Reduce Input Records: 14 

On constate qu'avec le combiner c'est plus rapide ,le job reducer est plus rapide ==> Diminuer le travail du Reducer 

# Homework :Patron de conception structurel

On se propose de réaliser une application mettant en oeuvre le patron de conception structurel.
Pour cela, nous allons réaliser la jointure de deux ensembles de données: les fichiers délimités
forum_nodeset forum_users.

Le fichier forum_nodes contient des informations sur les posts du forum, alors que forum_users
contient des informations sur les utilisateurs. Ils ont une clef en commun (author_id dans le fichier
forum_nodeset user_ptr_id dans forum_users). 

Un Mapper : s'occupe de parcourir les fichiers forum_users et forum_nodes et d'extraire de chacune des entrées les données nécessaires

Un Reducer : s'occupe de faire l’opération de jointure entre les deux fichiers

Les mappers executent le filtrage des champs demandés de chaque fichier ,en gardant la première colonne comme l'output l'id de l'auteur.Les reducers vont stocker pour toute série de lignes ayant le même identifiant de l'auteur, les données à récupérer sur cet auteur ainsi qu'une liste de celles des commentaires de cet auteur.

Résultat: La reputation de l'auteur ayant l'id 100002517 est 6149
