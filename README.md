# LES 9 ÉTAGES — Liseuse Interactive Tête-Bêche

> **Édition numérique interactive intégrale de l’ouvrage *« Les 9 étages »* par Alexandre ROUX.**

---

## Architecture & Fonctionnalités

- **Scène d’accueil 3D WebGL (Three.js)** : manipulation libre à 360° avec inertie physique, tranches de feuillets réalistes, dos imprimé continu et retournement tête-bêche à 180° (*Côté Terrain* ⇄ *Côté Sommet*).
- **Synchronisation exacte des folios imprimés (1:1)** : `Couverture` (`p. 0`) suivie des folios exacts `p. 1` à `141` (*Côté Terrain*) et `p. 1` à `149` (*Côté Sommet*), en affichage **1 page** ou **double-page reliée (2 pages)** respectant la parité pair/impair de l’édition imprimée.
- **Sommaire intégral des deux versants & Ascenseur des 9 Étages** : navigation directe entre les étages `0` à `8` et bascule miroir en un clic vers le même étage vu depuis le versant opposé.
- **Recherche plein texte instantanée (`⌘K` / `Ctrl+K` / `/`)** : indexation complète des 290 pages (insensible aux accents et ligatures), filtrage par versant et extraits surlignés en contexte.
- **Confort de lecture haute définition** : cache LRU hors-écran anti-scintillement avec préchargement des pages adjacentes, zoom fluide (`100 %` à `350 %`), trois ambiances éditoriales (*Nuit*, *Atelier*, *Ivoire*), filtres papier (*Fidèle*, *Crème*, *Inversé*), marque-pages persistants en local (`localStorage`) et jonction interactive au **Hall Central**.

---

## Raccourcis Clavier

| Touche | Action |
| :--- | :--- |
| `←` / `→` ou `Espace` | Page ou double-page précédente / suivante |
| `S` | Ouvrir / fermer le Sommaire & l’Ascenseur des 9 Étages |
| `⌘K` / `Ctrl+K` ou `/` | Recherche plein texte intégrale |
| `R` | Retourner physiquement le livre à 180° (*Terrain* ⇄ *Sommet*) |
| `D` | Basculer entre affichage 1 page et double-page (ordinateur/tablette) |
| `B` | Ajouter / retirer un marque-page sur la page courante |
| `+` / `-` / `0` | Zoomer, dézoomer, réinitialiser à 100 % |
| `F` | Activer / quitter le mode plein écran |

---

## Déploiement GitHub Pages

1. Ouvrez l’onglet **Settings → Pages** du dépôt GitHub.
2. Sélectionnez la branche principale (`main` / `master`) et le dossier racine `/ (root)`.
3. Enregistrez : l’application statique est immédiatement servie sans étape de build.
