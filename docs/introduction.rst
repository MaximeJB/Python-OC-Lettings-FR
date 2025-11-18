Introduction
============

Description du projet
---------------------

OC Lettings est une application web Django développée pour Orange County Lettings, une start-up dans le secteur de la location de biens immobiliers aux États-Unis.

L'application permet de :

* Gérer des profils utilisateurs
* Gérer des locations immobilières avec leurs adresses
* Consulter les locations disponibles
* Consulter les profils des utilisateurs

Contexte
--------

Ce projet a été modernisé dans le cadre d'une amélioration technique incluant :

* Refonte de l'architecture modulaire (séparation en applications Django distinctes)
* Réduction de la dette technique (linting, tests, docstrings)
* Mise en place de monitoring avec Sentry
* Automatisation CI/CD avec GitHub Actions et Docker
* Documentation technique avec Sphinx et Read The Docs

Architecture
------------

Le projet est structuré en 3 applications Django :

* **oc_lettings_site** : Application principale et page d'accueil
* **lettings** : Gestion des locations et adresses
* **profiles** : Gestion des profils utilisateurs
