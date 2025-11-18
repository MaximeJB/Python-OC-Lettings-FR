Interfaces de programmation
===========================

Views (Vues)
------------

oc_lettings_site.views
^^^^^^^^^^^^^^^^^^^^^^^

``index(request)``
    Affiche la page d'accueil avec liens vers Lettings et Profiles.

``custom_404(request, exception)``
    Gère les erreurs 404 avec une page personnalisée.

``custom_500(request)``
    Gère les erreurs 500 avec une page personnalisée.

lettings.views
^^^^^^^^^^^^^^

``lettings_index(request)``
    Affiche la liste de toutes les locations disponibles.

    **Returns:** Template 'lettings/lettings_index.html' avec ``lettings_list``

``letting(request, letting_id)``
    Affiche les détails d'une location spécifique.

    **Args:**
        * ``letting_id`` : ID de la location

    **Returns:** Template 'lettings/letting.html' avec ``title`` et ``address``

    **Raises:** Http404 si la location n'existe pas

profiles.views
^^^^^^^^^^^^^^

``profiles_index(request)``
    Affiche la liste de tous les profils utilisateurs.

    **Returns:** Template 'profiles/profiles_index.html' avec ``profiles_list``

``profile(request, username)``
    Affiche les détails d'un profil utilisateur spécifique.

    **Args:**
        * ``username`` : Nom d'utilisateur du profil

    **Returns:** Template 'profiles/profile.html' avec ``profile``

    **Raises:** Http404 si le profil n'existe pas

URL Patterns
------------

**oc_lettings_site.urls**

* ``/`` - Page d'accueil
* ``/lettings/`` - Application lettings (include)
* ``/profiles/`` - Application profiles (include)
* ``/admin/`` - Panel d'administration Django

**lettings.urls**

* ``/lettings/`` - Liste des locations
* ``/lettings/<int:letting_id>/`` - Détail d'une location

**profiles.urls**

* ``/profiles/`` - Liste des profils
* ``/profiles/<str:username>/`` - Détail d'un profil

Modèles
-------

Voir la section :doc:`database` pour les détails des modèles Address, Letting et Profile.
