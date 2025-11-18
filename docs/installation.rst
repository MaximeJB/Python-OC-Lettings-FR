Installation
============

Prérequis
---------

* Python 3.12 ou supérieur
* Git
* Compte GitHub avec accès au repository

Installation locale
-------------------

1. Cloner le repository
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   git clone https://github.com/MaximeJB/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR

2. Créer l'environnement virtuel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Windows PowerShell :**

.. code-block:: powershell

   python -m venv venv
   .\venv\Scripts\Activate.ps1

**macOS / Linux :**

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate

3. Installer les dépendances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   pip install -r requirements.txt

4. Lancer le serveur de développement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python manage.py runserver

L'application est accessible sur http://localhost:8000

Panel d'administration
----------------------

Accédez au panel d'administration sur http://localhost:8000/admin

**Identifiants par défaut :**

* Utilisateur : ``admin``
* Mot de passe : ``Abc1234!``
