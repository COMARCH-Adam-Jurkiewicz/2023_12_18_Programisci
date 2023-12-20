Przygotuj bazę danych z danymi z Fakera do pracy z fastAPI.

tabela users:
 - ID_user
 - imie
 - nazwisko
tabela miasto: ("Warszawa", "Poznań", "Gdańsk", Wrocław")
 - ID_user
 - Miasto

from random import choice
miasto_losowe = choice(("Warszawa", "Poznań", "Gdańsk", "Wrocław"))