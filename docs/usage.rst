Guide d'utilisation
===================

Navigation dans l'application
------------------------------

Page d'accueil
^^^^^^^^^^^^^^

La page d'accueil présente deux liens principaux :

* **Profiles** : Accès à la liste des profils utilisateurs
* **Lettings** : Accès à la liste des locations

Gestion des locations
^^^^^^^^^^^^^^^^^^^^^

**Liste des locations**

Accédez à ``/lettings/`` pour voir toutes les locations disponibles.

Chaque location affiche son titre. Cliquez sur une location pour voir ses détails.

**Détail d'une location**

La page de détail (``/lettings/<id>/``) affiche :

* Le titre de la location
* L'adresse complète (numéro, rue, ville, état, code postal, pays)

Gestion des profils
^^^^^^^^^^^^^^^^^^^^

**Liste des profils**

Accédez à ``/profiles/`` pour voir tous les profils utilisateurs.

**Détail d'un profil**

La page de détail (``/profiles/<username>/``) affiche :

* Le nom d'utilisateur
* La ville favorite (si renseignée)

Administration
--------------

Accès au panel d'administration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Allez sur ``/admin/``
2. Connectez-vous avec les identifiants admin
3. Vous pouvez gérer :
   * Les utilisateurs
   * Les profils
   * Les locations
   * Les adresses

Ajouter une location
^^^^^^^^^^^^^^^^^^^^

1. Créez d'abord une adresse dans la section "Adresses"
2. Créez ensuite une location et associez-la à l'adresse
3. La location apparaîtra automatiquement dans la liste

Ajouter un profil
^^^^^^^^^^^^^^^^^

1. Créez d'abord un utilisateur dans la section "Users"
2. Créez ensuite un profil et associez-le à l'utilisateur
3. Ajoutez optionnellement une ville favorite

Cas d'utilisation
-----------------

Scénario 1 : Consulter les locations disponibles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Visitez la page d'accueil
2. Cliquez sur "Lettings"
3. Parcourez la liste
4. Cliquez sur une location pour voir les détails

Scénario 2 : Rechercher un utilisateur
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Visitez la page d'accueil
2. Cliquez sur "Profiles"
3. Trouvez l'utilisateur dans la liste
4. Cliquez pour voir son profil et sa ville favorite
