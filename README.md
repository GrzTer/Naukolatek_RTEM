# **REAL TIME ENERGY MANAGER**
# [![chatgpt (1)](https://github.com/GrzegorzTwicz/Naukolatek_RTEM/assets/144318154/86c477b2-96bc-451a-9293-201fcb830042)](https://chat.openai.com/auth/login)**[CHAT GPT](https://chat.openai.com/auth/login)**[![chatgpt (1)](https://github.com/GrzegorzTwicz/Naukolatek_RTEM/assets/144318154/5a91fe2e-b438-48f7-96df-c7bc00ec4adb)](https://chat.openai.com/auth/login)
## Co do użycia:
- Django Channels
- PostgreSQL z rozszerzeniem TimescaleDB dla danych szeregów czasowych
- TensorFlow/Keras
- Django REST Framework
- Celery z Django
- WebSockets
- Django Background Tasks
---
# Każdy nowo zaczęty issue: 
- Clon/Pull
- RÓB NOWY BRANCH
- Zmiana w plikach models.py = ```python manage.py makemigrations```
---
## Funkcje do zrobienia:
- (MZE)Monitorowanie Zużycia Energetycznego: Wykorzystamy zaawansowane czujniki i technologię IoT do śledzenia zużycia energii elektrycznej na różnych poziomach, od pojedynczych urządzeń po całe budynki.
- (PZ)Prognozowanie Zużycia: Zastosujemy algorytmy uczenia maszynowego, takie jak TensorFlow, do prognozowania przyszłego zużycia energii na podstawie danych historycznych i bieżących trendów. 
- (OZ)Optymalizacja Zużycia: Nasza aplikacja będzie automatycznie proponować sposoby optymalizacji zużycia energii, uwzględniając m.in. zmiany czasu pracy urządzeń i wykorzystanie źródeł odnawialnych. 
- (PA)Powiadomienia i Alarmy: Aplikacja generuje powiadomienia w czasie rzeczywistym w przypadku awarii urządzeń lub nieprawidłowych wzorców zużycia energii. 
- (SG)Integracja z Smart Grid: Projekt zostanie zintegrowany z inteligentnymi sieciami energetycznymi, co umożliwi dostęp do danych dotyczących cen energii w czasie rzeczywistym.


---
# Przydatne linki
- [FIGMA RTEM FLOW](https://www.figma.com/file/Pkl86gwsODaW5lYygA1F1l/RTEM-FLOW?type=whiteboard&node-id=0%3A1&t=FW0Yp6fZ3LtkCLzH-1)
- [FIGMA MOCK'UP](https://www.figma.com/file/zaxl5wU608z9J7BesLggCP/naukolatek-team-library?type=design&node-id=0%3A1&mode=design&t=PuOzFr1hWV7bI672-1)
---
# Przydatne komendy
### Django
- Aktywacja środowiska: ```.\env\Scripts\activate``` / Windows
- Dezaktywacja środowiska: ```deactivate``` / Windows
- [CheatSheet](https://docs.google.com/document/d/1z2Mm_dkT3-zRV_uZ3sOxd9jDH--bTU4HZxVyXrb-sHo/edit?pli=1)
- ```pip install -r requirements.txt```
- ```python manage.py makemigrations```
- ```python manage.py runserver```
- ```python manage.py migrate --run-syncdb```
---
Superuser:
- Username: admin
- Password: 1234
---
