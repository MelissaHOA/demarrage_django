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

```
#### 4. Faites une boucle pour afficher les attributs de chaque question et leurs choix associés.
```python

```
#### 5. Affichez le nombre de choix enregistrés pour chaque question
```python

```



```python

```