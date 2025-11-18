Procédures de déploiement
==========================

Architecture CI/CD
------------------

Le déploiement utilise un pipeline automatisé en 4 étapes :

1. **Tests** : Linting et tests unitaires
2. **Build** : Construction de l'image Docker
3. **Push** : Envoi sur Docker Hub
4. **Deploy** : Déploiement sur Render

Configuration initiale
----------------------

Secrets GitHub
^^^^^^^^^^^^^^

Configurez les secrets dans votre repository GitHub (Settings → Secrets → Actions) :

* ``DOCKER_USERNAME`` : Nom d'utilisateur Docker Hub
* ``DOCKER_PASSWORD`` : Token d'accès Docker Hub (généré sur hub.docker.com)
* ``RENDER_DEPLOY_HOOK_URL`` : URL webhook Render

Variables d'environnement Render
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sur Render, configurez ces variables :

* ``SECRET_KEY`` : Clé secrète Django (générer avec ``python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"``
)
* ``DEBUG`` : ``False``
* ``ALLOWED_HOSTS`` : Votre domaine Render (ex: ``mon-app.onrender.com``)
* ``SENTRY_DSN`` : DSN Sentry pour le monitoring

Configuration Render
^^^^^^^^^^^^^^^^^^^^

Créez un Web Service sur render.com :

* **Build Command** : ``pip install -r requirements.txt``
* **Start Command** : ``gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT``
* **Environment Variables** : Ajoutez les variables ci-dessus

Processus de déploiement
-------------------------

Déploiement automatique
^^^^^^^^^^^^^^^^^^^^^^^^

1. Faites vos modifications en local
2. Committez sur la branche master :

.. code-block:: bash

   git add .
   git commit -m "Description des changements"
   git push origin master

3. GitHub Actions se déclenche automatiquement
4. Si les tests passent, l'image Docker est construite et pushée
5. Render déploie automatiquement la nouvelle version

Vérification du déploiement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **GitHub Actions** : Vérifiez que tous les jobs sont verts
2. **Docker Hub** : Vérifiez que la nouvelle image est présente avec le tag du commit
3. **Render Dashboard** : Vérifiez les logs de déploiement
4. **Site en production** : Visitez l'URL et testez les fonctionnalités

Déploiement manuel
^^^^^^^^^^^^^^^^^^^

Si besoin de redéployer manuellement :

1. Sur Render Dashboard, cliquez sur votre service
2. Cliquez sur "Manual Deploy" → "Deploy latest commit"

Rollback
--------

En cas de problème en production :

1. **Via Render** : Utilisez "Rollback" pour revenir à la version précédente
2. **Via Git** : Revert le commit problématique et push

.. code-block:: bash

   git revert <commit_hash>
   git push origin master

Récupération de l'image Docker
-------------------------------

Pour tester l'image en local :

.. code-block:: bash

   docker pull votre-username/oc-lettings:latest
   docker run -p 8000:8000 \
     -e SECRET_KEY="votre-cle" \
     -e DEBUG="False" \
     -e ALLOWED_HOSTS="localhost" \
     votre-username/oc-lettings:latest

Monitoring post-déploiement
----------------------------

Après chaque déploiement, vérifiez :

* **Sentry** : Pas de nouvelles erreurs
* **Logs Render** : Pas d'erreurs au démarrage
* **Tests manuels** : Parcourez les principales pages
* **Performance** : Temps de réponse acceptable

Troubleshooting
---------------

Erreur "Tests failed" sur GitHub Actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Vérifiez les logs du job "Test and Lint"
* Relancez les tests en local : ``pytest``
* Corrigez les erreurs et recommittez

Erreur "Build failed" sur Render
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Vérifiez que ``requirements.txt`` est à jour
* Vérifiez les variables d'environnement
* Consultez les logs de build sur Render

Site inaccessible après déploiement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Vérifiez ``ALLOWED_HOSTS`` dans les variables Render
* Vérifiez que le service Render est bien "Live"
* Consultez les logs de l'application
