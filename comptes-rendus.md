# DJANGO -- Tutoriel
## ---- Excercice d'admnistration ----

### 4.1. rajouter 2 classes d'admin :

Page des questions : 
* liste des questions
* affichage date
* filtre par date
* ordre par date
* Barre de recherche

```python
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date"]
    list_filter = ["question_text", "pub_date"]
    ordering = ["pub_date"]
    search_fields = ["question_text"]
```

Page des choix : 
* liste des choix 
* affichage question correspondante
* filtre par question
* Barre de recherche

```python
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["choice_text", "question"]
    list_filter = ["question"]
    search_fields = ["choice_text"]
```

### 4.3. enregistrer les classes d'admin avec leur classe correspondante
```python
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
```

### 5. Ajoutez un nouvel utilisateur via l'interface d'admin.
Déconnectez-vous et essayer de vous reconnecter avec ce nouveau compte.
<br> Y parvenez-vous ?
* Non

### 6.faites en sorte que l'utilisateur puisse se connecter à l'interface d'admin. Profitez-en pour changer son mot de passe.
* Dans la fiche utilisateur cocher Actif et statut d'équipe
* Pour changer le mot de passe l'utilisateur doit se connecter et aller sur son compte pour changer le mdp

### 7. L'utilisateur ayant quitté l'organisation, cherchez maintenant à désactiver son compte plutôt que de le supprimez. Vérifiez qu'il ne peut plus se connecter.
* En tant que super utilisateur sur la fiche utilisateur décocher toutes les permissions. l'utilisateur ne peux plus se connecter


## ---- Exercice shell ----
### Préambule
Dans : 
```python
C:\Users\HoarauM\Documents\Formation\17_Django\demarrage_django\mysite>
```
Aller dans le Shell django
```python
python manage.py shell
```
Résultat :
```python
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.27.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```
### Questions

#### 1. Lister tous les objets de type Question
1ere étape : 
```python
In [1]: from polls.models import Question
```
Boucle Liste toutes les questions

```python
In [2]: questions = Question.objects.all()
   ...: for question in questions:
   ...:     print(f"ID: {question.id}, Texte: {question.question_text}, Date de publication: {question.pub_date}")
```
Résultat : 
```python
   ...:
ID: 1, Texte: What's up?, Date de publication: 2024-10-09 08:19:04+00:00
ID: 2, Texte: Météo ?, Date de publication: 2024-10-09 08:19:49+00:00
ID: 3, Texte: aimes tu lire ?, Date de publication: 2024-10-07 10:00:00+00:00
ID: 4, Texte: La destination de tes prochaine vacances ?, Date de publication: 2024-10-08 08:53:32+00:00
ID: 6, Texte: Un apéro ?, Date de publication: 2024-10-08 10:00:00+00:00
ID: 7, Texte: Python ou Java ?, Date de publication: 2024-10-03 22:00:00+00:00
ID: 8, Texte: Ta couleur préféré ?, Date de publication: 2024-09-30 22:00:00+00:00
```
#### 2. Ajoutez un filtre sur la date de publication
par année 2024
```python
In [3]: questions_by_year = Question.objects.filter(pub_date__year=2024)
    ...: for question in questions_by_year:
    ...:     print(f"ID: {question.id}, Texte: {question.question_text}, Date de publication: {question.pub_date}")
    ...:
ID: 1, Texte: What's up?, Date de publication: 2024-10-09 08:19:04+00:00
ID: 2, Texte: Météo ?, Date de publication: 2024-10-09 08:19:49+00:00
ID: 3, Texte: aimes tu lire ?, Date de publication: 2024-10-07 10:00:00+00:00
ID: 4, Texte: La destination de tes prochaine vacances ?, Date de publication: 2024-10-08 08:53:32+00:00
ID: 6, Texte: Un apéro ?, Date de publication: 2024-10-08 10:00:00+00:00
ID: 7, Texte: Python ou Java ?, Date de publication: 2024-10-03 22:00:00+00:00
ID: 8, Texte: Ta couleur préféré ?, Date de publication: 2024-09-30 22:00:00+00:00
```
Par n° du jour
```python
In [4]: questions_by_day = Question.objects.filter(pub_date__day=9)
    ...: for question in questions_by_day:
    ...:     print(f"ID: {question.id}, Texte: {question.question_text}, Date de publication: {question.pub_date}")
    ...:
ID: 1, Texte: What's up?, Date de publication: 2024-10-09 08:19:04+00:00
ID: 2, Texte: Météo ?, Date de publication: 2024-10-09 08:19:49+00:00
```
AUTRE METHODE :
```python
In [5]: from datetime import datetime
    ...: from polls.models import Question
    ...:
    ...: date_specifique = datetime(2024, 10, 9)
    ...:
    ...: questions_filtrees = Question.objects.filter(pub_date__year=date_specifique.year,
    ...:                                              pub_date__month=date_specifique.month,
    ...:                                              pub_date__day=date_specifique.day)
    ...:
    ...: for question in questions_filtrees:
    ...:     print(f"ID: {question.id}, Texte: {question.question_text}, Date de publication: {question.pub_date}")
    ...:
ID: 1, Texte: What's up?, Date de publication: 2024-10-09 08:19:04+00:00
ID: 2, Texte: Météo ?, Date de publication: 2024-10-09 08:19:49+00:00
```

#### 3. Trouvez la deuxième question
```python
In [6]: Question.objects.filter(id=2)
Out[6]: <QuerySet [<Question: Météo ?>]>
```
ou
```python
In [5]: Question.objects.get(id=2)
Out[5]: <Question: Météo ?>
```
Afficher les choix 
```python
In [6]:  Question.objects.filter(id=2)
    ...:
    ...: print(f"Question: {question.question_text}")
    ...: choices = question.choice_set.all()
    ...:
    ...: for choice in choices:
    ...:     print(f"Choix: {choice.choice_text}")
    ...:
Question: Météo ?
Choix: il fait beau
Choix: c'est nuageux
Choix: il pleut
```

#### 4. Faites une boucle pour afficher les attributs de chaque question et leurs choix associés.
```python
In [7]: questions = Question.objects.all()
    ...:
    ...: for question in questions :
    ...:     print(f"Question : {question.question_text} (ID : {question.id}, Publié le : {question.pub_date})")
    ...:     
    ...:     choices = question.choice_set.all()
    ...:     if choices.exists():
    ...:         for choice in choices:
    ...:             print(f"- Choix : {choice.choice_text}")
    ...:     else :
    ...:         print(" Aucun choix disponible")
    ...:
```
Résultat : 
```python
...: Question : What's up? (ID : 1, Publié le : 2024-10-09 08:19:04+00:00)
- Choix : Not much
- Choix : The sky
- Choix : rien
- Choix : une bonne nouvelle
Question : Météo ? (ID : 2, Publié le : 2024-10-09 08:19:49+00:00)
- Choix : il fait beau
- Choix : c'est nuageux
- Choix : il pleut
Question : aimes tu lire ? (ID : 3, Publié le : 2024-10-07 10:00:00+00:00)
- Choix : oui
- Choix : non
- Choix : Parfois
Question : La destination de tes prochaine vacances ? (ID : 4, Publié le : 2024-10-08 08:53:32+00:00)
- Choix : Islande
- Choix : USA
- Choix : Japon
Question : Un apéro ? (ID : 6, Publié le : 2024-10-08 10:00:00+00:00)
- Choix : Toujours partant
- Choix : Cela ne se refuse pas
- Choix : Non, je bois de l'eau
Question : Python ou Java ? (ID : 7, Publié le : 2024-10-03 22:00:00+00:00)
- Choix : Aucun des deux
- Choix : Python
- Choix : Java mais python c'est mieux
Question : Ta couleur préféré ? (ID : 8, Publié le : 2024-09-30 22:00:00+00:00)
- Choix : vert
- Choix : rose
- Choix : bleouge
```
#### 5. Affichez le nombre de choix enregistrés pour chaque question
```python
In [8]: questions = Question.objects.all()
    ...: for question in questions:
    ...:     print(f"ID : {question.id} - Question : {question.question_text} ")
    ...:
    ...:     choices = question.choice_set.all()
    ...:     count_choices = choices.count()
    ...:
    ...:     if count_choices > 0:
    ...:         print(f"Nombre de choix : {count_choices}")
    ...:
    ...:     else:
    ...:         print("Aucun choix disponible")
```
Résultat : 
```python
ID : 1 - Question : What's up?
Nombre de choix : 4
ID : 2 - Question : Météo ?
Nombre de choix : 3
ID : 3 - Question : aimes tu lire ?
Nombre de choix : 3
ID : 4 - Question : La destination de tes prochaine vacances ?
Nombre de choix : 3
ID : 6 - Question : Un apéro ?
Nombre de choix : 3
ID : 7 - Question : Python ou Java ?
Nombre de choix : 3
ID : 8 - Question : Ta couleur préféré ?
Nombre de choix : 3
```

### 7.Triez les questions par ordre antéchronologique.
```python
In [9]: questions = Question.objects.all().order_by('-pub_date')
    ...: for question in questions:
    ...:     pub_date_formatted = question.pub_date.date()
    ...:     print(f"Publié le : {pub_date_formatted} -- ID = {question.id} ---> Question : {question.question_text}")
```
Résultat :
```python
...:
Publié le : 2024-10-09 -- ID = 2 ---> Question : Météo ?
Publié le : 2024-10-09 -- ID = 1 ---> Question : What's up?
Publié le : 2024-10-08 -- ID = 6 ---> Question : Un apéro ?
Publié le : 2024-10-08 -- ID = 4 ---> Question : La destination de tes prochaine vacances ?
Publié le : 2024-10-07 -- ID = 3 ---> Question : aimes tu lire ?
Publié le : 2024-10-03 -- ID = 7 ---> Question : Python ou Java ?
Publié le : 2024-09-30 -- ID = 8 ---> Question : Ta couleur préféré ?
```
### 9.Créez une question en utilisant le shell.
```python
In [10]: from polls.models import Question
In [11]:from django.utils import timezone

In [12]: new_question = Question(question_text="Quel est votre film favori ?", pub_date=timezone.now())
    ...: new_question.save()
    ...: print(f"Question créée : {new_question.question_text} (ID : {new_question.id}, Publié le : {new_question.pub_date})")
Question créée : Quel est votre film favori ? (ID : 9, Publié le : 2024-10-10 13:22:41.726850+00:00)
```
### 10.Ajoutez 3 choix à cette question en utilisant le shell.
```python
In [13]: question = Question.objects.get(id=9)
    ...:
In [14]: Choice.objects.create(question=question, choice_text="Titanic")
    ...: Choice.objects.create(question=question, choice_text="Harry Potter")
    ...: Choice.objects.create(question=question, choice_text="Saw")
    ...:
In [15]: for choice in question.choice_set.all():
    ...:     print(f"- {choice.choice_text}")
    ...:
- Titanic
- Harry Potter
- Saw
```

### 11.Listez les questions publiées récemment.
```python

```
Résultat :
```python

```




_________________________________________________________
```python

```