För att köra projektet:

-Om Github strular och ger dig mapparna Ztraid/Ztraid så döp om den undre mappen till ztraid (litet z), annars bör du stöta på ett ModuleNotFoundError. Om Github strular och ger dig både mapparna Ztraid/Ztraid & Ztraid/ztraid så ta bort undre mappen med stort Z om du stöter på errors. Nya försök att fixa dessa återkommande problem görs snart.

-Starta kommandotolk och CD'a till Ztraid (översta mappen i projektet), kör sedan de kommandon som finns under "Ztraid/kommandon.html".

------------------------------------------------------------

För att köra: kommandotolken i "Ztraid" foldern:

pip install Django

pip install djangorestframework

pip install social-auth-app-django

manage.py migrate

manage.py runserver
