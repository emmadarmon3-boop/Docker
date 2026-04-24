FROM python:3.11-slim

WORKDIR /app
COPY . .

# On définit une variable d'environnement par défaut
ENV USER_NAME="Apprenti DevSecOps"

CMD ["python", "hello.py"]