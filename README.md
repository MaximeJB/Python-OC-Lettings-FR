## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Fonctionnement général

Le déploiement utilise un pipeline CI/CD automatisé :

1. **Push sur master** → GitHub Actions se déclenche
2. **CI (Intégration Continue)** → Exécute flake8 et pytest avec couverture >80%
3. **Build Docker** → Construit l'image et la push sur Docker Hub
4. **CD (Déploiement Continu)** → Déclenche le déploiement sur Render

### Configuration requise

#### Secrets GitHub (Settings → Secrets → Actions)

- `DOCKER_USERNAME` : Nom d'utilisateur Docker Hub
- `DOCKER_PASSWORD` : Token d'accès Docker Hub
- `RENDER_DEPLOY_HOOK_URL` : URL du webhook de déploiement Render

#### Variables d'environnement Render

- `SECRET_KEY` : Clé secrète Django 
- `DEBUG` : `False`
- `ALLOWED_HOSTS` : Domaine Render (ex: `mon-app.onrender.com`)
- `SENTRY_DSN` : DSN Sentry pour le monitoring

### Étapes de déploiement

1. **Cloner le repository**
   ```bash
   git clone https://github.com/MaximeJB/Python-OC-Lettings-FR.git
   ```

2. **Configurer les secrets GitHub**
   - Aller sur GitHub → Settings → Secrets and variables → Actions
   - Ajouter les 3 secrets requis

3. **Créer le service Render**
   - Créer un compte sur render.com
   - New Web Service → Connect to GitHub
   - Build Command : `pip install -r requirements.txt`
   - Start Command : `gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT`
   - Ajouter les variables d'environnement

4. **Récupérer le Deploy Hook**
   - Render Dashboard → Service → Settings → Deploy Hook
   - Copier l'URL et l'ajouter dans GitHub Secrets

5. **Déployer**
   ```bash
   git add .
   git commit -m "Deploy"
   git push origin master
   ```

6. **Vérifier le déploiement**
   - GitHub Actions : Vérifier que tous les jobs passent
   - Render Dashboard : Vérifier les logs de l'application
   - Visiter l'URL publique

### Récupérer l'image Docker

```bash
docker pull votre-username/oc-lettings:latest
docker run -p 8000:8000 votre-username/oc-lettings:latest
```

### Monitoring

Les erreurs sont automatiquement remontées sur Sentry. Consulter le dashboard Sentry pour voir les logs et erreurs en production.
