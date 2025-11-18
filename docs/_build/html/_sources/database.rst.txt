Structure de la base de données
================================

Modèles de données
------------------

Address
^^^^^^^

Modèle représentant une adresse physique.

**Champs :**

* ``number`` : Numéro de rue (entier positif, max 9999)
* ``street`` : Nom de la rue (chaîne, max 64 caractères)
* ``city`` : Ville (chaîne, max 64 caractères)
* ``state`` : Code d'état (chaîne, 2 caractères)
* ``zip_code`` : Code postal (entier positif, max 99999)
* ``country_iso_code`` : Code ISO du pays (chaîne, 3 caractères)

**Méthode :**

* ``__str__()`` : Retourne "{number} {street}"

Letting
^^^^^^^

Modèle représentant une location immobilière.

**Champs :**

* ``title`` : Titre de la location (chaîne, max 256 caractères)
* ``address`` : Relation OneToOne vers Address

**Méthode :**

* ``__str__()`` : Retourne le titre de la location

Profile
^^^^^^^

Modèle représentant un profil utilisateur.

**Champs :**

* ``user`` : Relation OneToOne vers Django User
* ``favorite_city`` : Ville favorite (chaîne, max 64 caractères, optionnel)

**Méthode :**

* ``__str__()`` : Retourne le nom d'utilisateur

Relations
---------

* **Address ↔ Letting** : Relation OneToOne (une adresse = une location)
* **User ↔ Profile** : Relation OneToOne (un utilisateur = un profil)

Migrations
----------

Les migrations Django gèrent automatiquement les modifications de schéma.

**Commandes utiles :**

.. code-block:: bash

   python manage.py makemigrations  # Créer des migrations
   python manage.py migrate         # Appliquer les migrations
   python manage.py showmigrations  # Voir l'état des migrations
