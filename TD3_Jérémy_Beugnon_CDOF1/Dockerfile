#On utilise une image officielle de python 
FROM python:3.9-slim

#On definit le répertoire de travail de l'app
WORKDIR /app

#On copie le contenu du répertoire dans le containeur 
COPY . /app	

#On installe les packages/modules nécéssaire
RUN pip install --no-cache-dir -r requirements.txt

#On demande d'éxécuter app.py au lancement du containeur 
CMD ["python", "app.py"]
