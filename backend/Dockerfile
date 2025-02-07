FROM python:3.10-slim
WORKDIR /app

# Copie du fichier requirements.txt et installation des dépendances
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copie du reste de l'application
COPY . /app

# Exposition du port
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
