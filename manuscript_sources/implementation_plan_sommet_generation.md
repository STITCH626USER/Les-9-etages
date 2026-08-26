# Plan d'implémentation — Partie "Sommet"

Ce plan détaille les étapes nécessaires pour compiler et générer la seconde moitié du livre (le point de vue du "Sommet"), en utilisant le même niveau d'exigence typographique et esthétique que la partie "Terrain".

## Objectif

Créer le script de génération et produire le fichier `NOUVEAU_DESIGN_SOMMET.pdf` contenant la descente de la tour (de l'étage 8 jusqu'à l'étage 0).

## Modifications proposées

### 1. Création du script de génération dédié
- Duplication du script `generate_pdf_puppeteer.js` vers `generate_pdf_puppeteer_sommet.js`.
- Mise à jour de la liste des fichiers markdown à compiler, dans un ordre de "descente" logique :
  1. `rewrite_sommet_prologue.md`
  2. `rewrite_sommet_chap8.md` (CEO)
  3. `rewrite_sommet_chap7.md` (Chairman)
  4. `rewrite_sommet_chap6.md` (Président International)
  5. `rewrite_sommet_chap5.md` (Président Division)
  6. `rewrite_sommet_chap4.md` (Vice-Président)
  7. `rewrite_sommet_chap3.md` (Directeur)
  8. `rewrite_sommet_chap2.md` (Responsable de Service)
  9. `rewrite_sommet_chap1.md` (Manager de proximité)
  10. `rewrite_sommet_chap0.md` (Retour au réel)

### 2. Typographie et Mise en page (Héritage)
- Les règles CSS affinées précédemment (marges réduites à 12mm, `keep-together` pour éviter les sauts orphelins, tableaux compactés, espaces insécables avant la ponctuation) seront **intégralement conservées** pour assurer une cohérence visuelle absolue entre les deux moitiés du livre.
- Le système visuel d'ascenseur continuera de fonctionner parfaitement car il se base sur la détection automatique du numéro d'étage dans les titres `<h1>`.

## Vérification prévue

1. Lancement du script de génération.
2. Audit visuel du PDF résultant pour s'assurer qu'aucun orphelin n'apparaît.
3. Vérification de l'ordre décroissant des chapitres.

> [!IMPORTANT]
> **Validation requise**
> Êtes-vous d'accord avec cet ordre de lecture (de l'étage 8 vers l'étage 0) pour la partie Sommet ? Si l'ordre vous convient, vous pouvez valider ce plan et je lancerai la génération du PDF immédiatement.
