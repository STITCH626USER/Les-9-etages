# Plan d'implémentation : Génération des PDF Typographiés

## Le Défi Technique
Vous souhaitez que je regénère intégralement les PDF avec les nouveaux textes, tout en conservant le style typographique (polices, tableaux, mise en page) des originaux. 

Il est techniquement **impossible de modifier directement le texte à l'intérieur d'un fichier PDF existant** (le format PDF fige les lettres à des coordonnées précises ; on ne peut pas insérer un paragraphe sans détruire toute la pagination et la justification des 160 pages suivantes).

## La Solution Proposée : Le Pipeline Markdown -> HTML/CSS -> PDF
Pour relever ce défi et vous livrer de véritables PDF professionnels reprenant votre charte, voici ce que je vous propose de mettre en place :

1. **Extraction de la charte graphique**
   J'ai analysé les métadonnées de vos PDF originaux. Le format est **A5** (14.8 x 21 cm). Les polices utilisées sont **Georgia** pour le corps de texte (élégant, classique) et **Helvetica Neue Bold** pour les titres.

2. **Création d'un gabarit CSS (Style Sheet)**
   Je vais coder une feuille de style (CSS) de qualité éditoriale qui va répliquer fidèlement votre mise en page originale : 
   - Marges de reliure asymétriques pour l'impression A5.
   - Justification du texte, césures, et indentation des paragraphes.
   - Stylisation stricte des tableaux et des encarts (infographies pleine page en nuances de gris, comme nous l'avons évoqué).

3. **Génération via WeasyPrint**
   Nous allons installer un moteur de rendu professionnel (`WeasyPrint`) dans notre environnement. Un script Python prendra nos textes réécrits (Markdown), les convertira en HTML, leur appliquera la feuille de style CSS "Georgia/Helvetica", et générera des PDF parfaits.

4. **L'Imposition Tête-Bêche Finale**
   Une fois ces nouveaux PDF sources générés, notre script `generer_tete_beche.py` s'en emparera pour créer le grand PDF final de 334 pages, prêt pour l'imprimeur.

---

> [!IMPORTANT]
> **User Review Required**
> 
> Êtes-vous d'accord avec cette méthode technique ? Si oui, je vais commencer par :
> 1. Installer les bibliothèques requises (`weasyprint`, `markdown`).
> 2. Coder la feuille de style CSS pour reproduire votre charte (Georgia/Helvetica A5).
> 3. Générer un premier PDF d'essai avec les chapitres que nous avons déjà réécrits pour que vous puissiez valider le rendu visuel.
