Guide de démarrage rapide
==========================

Ce guide vous permet de démarrer rapidement avec OC Lettings.

Étape 1 : Installation
-----------------------

.. code-block:: bash

   git clone https://github.com/MaximeJB/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR
   python -m venv venv
   source venv/bin/activate  # Windows: .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt

Étape 2 : Lancer l'application
-------------------------------

.. code-block:: bash

   python manage.py runserver

Étape 3 : Explorer
------------------

* Page d'accueil : http://localhost:8000
* Lettings : http://localhost:8000/lettings/
* Profiles : http://localhost:8000/profiles/
* Admin : http://localhost:8000/admin (admin / Abc1234!)

Étape 4 : Lancer les tests
---------------------------

.. code-block:: bash

   pytest
   pytest --cov=. --cov-report=term-missing

Étape 5 : Vérifier le linting
------------------------------

.. code-block:: bash

   flake8
