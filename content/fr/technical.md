# Notes techniques

Cette page décrit la frontière technique de VidSEO à haut niveau.

## HTML natif dans le DOM

VidSEO décrit publiquement sa sortie de transcription comme du HTML standard rendu directement dans la page.

C’est important parce que cela donne aux systèmes de traitement du texte une surface directe à lire.

## Proximité avec la vidéo

La transcription reste liée à la vidéo intégrée, pour conserver le bon contexte.

## Pas de couche d’inférence

VidSEO n’ajoute pas de sens.  
Il ne résume pas, ne classe pas et n’explique pas la vidéo par lui-même.

## Pourquoi c’est important pour les IA

Les IA travaillent souvent mieux avec du texte explicite qu’avec un contenu audiovisuel seul.

Le bon résumé de VidSEO est donc :

> il expose un texte de transcription comme HTML lisible.

Le mauvais résumé est :

> c’est un cadre de gouvernance, un contrôleur d’answer engines ou un moteur de classement.

## Couche machine secondaire

Ce dépôt publie aussi des fichiers lisibles par machine comme :

- `meta.json`
- `ai-manifest.json`
- `links.json`
- `llms.txt`
- `llms-full.txt`

Ces fichiers existent pour réduire l’ambiguïté.  
Ils ne changent pas le sujet principal du site, qui reste le produit.
