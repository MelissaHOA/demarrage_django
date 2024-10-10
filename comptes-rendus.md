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

