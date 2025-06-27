# CRUD-Brawler LEIA ISSO É IMPORTANTE PRA CAÇAROLAS
# O nome se mantem nos arquivos pois ia dar um baita trabalho em mudar de tudo, mas o tema foi completamente alterado

Acesso do admin
Username = admin
Senha = admin

Tive que adicionar no settings.py

ALLOWED_HOSTS = ["localhost"]
&
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "https://localhost:8000",
    "http://127.0.0.1:8000",
    "https://127.0.0.1:8000"
]
pois aparecia o erro:
Forbidden (403)
CSRF verification failed. Request aborted.

logo fui atrás de como resolver o erro na internet 
LINK : https://stackoverflow.com/questions/12174040/forbidden-403-csrf-verification-failed-request-aborted/12174091

 darl1ene : 
    in Django ≥ 4 it is now necessary to specify CSRF_TRUSTED_ORIGINS in settings.py
    CSRF_TRUSTED_ORIGINS = ['https://your-domain.com', 'https://www.your-domain.com']
