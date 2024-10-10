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


