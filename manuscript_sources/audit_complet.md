# AUDIT COMPLET — TERRAIN & SOMMET
*Généré le 23 août 2026*

---

## ✅ POINTS TECHNIQUES — TOUT PROPRE

| Contrôle | Résultat |
| :--- | :--- |
| Sauts de page en fin de fichier | ✅ Aucun |
| Sauts de page doublons consécutifs | ✅ Aucun |
| Infographies précédées d'un saut manuel (doublon CSS) | ✅ Aucun |
| Balises HTML non fermées (`<div>`) | ✅ Aucune |
| `[!NOTE]` markdown non supporté | ✅ Supprimés |
| `Senior Manager` (terme incohérent) | ✅ Remplacé par "Manager de Managers" |
| « Prochain chapitre » | ✅ Supprimés |

---

## ✅ STRUCTURE DES FICHIERS — COMPLÈTE

### Terrain (18 fichiers)
Prologue → Chap 0–8 → Vue d'ensemble → Générations → Et si ? → Ceux qui ont commencé → Fiches pratiques → La Transition → Plan de transformation → Hall Central Terrain

### Sommet (19 fichiers)
Prologue → Chap 8→0 → Les managers qui ont changé → Angles morts → Pourquoi le changement n'a pas lieu → Le premier pas → Guide du manager → Hall Central (4 fichiers)

---

## ✅ H1 MULTIPLES PAR FICHIER — SAUTS DE PAGE OK

| Fichier | H1 | Saut avant chaque H1 interne |
| :--- | :--- | :--- |
| `rewrite_terrain_vue_ensemble.md` | 2 | ✅ CSS `page-break-after` de l'infographie suffit |
| `rewrite_hall_central_terrain.md` | 2 | ✅ `page-break-before` explicite avant "LE MOT DE L'AUTEUR" |
| `rewrite_sommet_angles_morts.md` | 3 | ✅ `page-break-before` explicite avant chaque H1 interne |
| `rewrite_sommet_pourquoi_ne_pas_changer.md` | 2 | ✅ `page-break-before` explicite avant "LE COÛT DE NE RIEN FAIRE" |

---

## ✅ TON — "VOUS" ACCUSATEUR

### Fichiers neutralisés (corps analytique → troisième personne)
- `rewrite_sommet_angles_morts.md` ✅
- `rewrite_sommet_pourquoi_ne_pas_changer.md` ✅
- `rewrite_sommet_chap0.md` (sections descriptives) ✅

### "Vous" LÉGITIMES conservés
- **`▌ LA QUESTION`** — intentionnellement interpellant dans tous les chapitres
- **`▌ LE TRADUCTEUR DU SOMMET`** — adresse directe délibérée
- **Prologue** — les 4 "vous" sont dans une conclusion rhétorique ("si la réponse vous met mal à l'aise…") → ton d'invitation, pas d'accusation
- **`rewrite_sommet_chap0.md` lignes 49/52** — dans la narration de Thierry (un personnage), le "vous" est fondu dans le narratif de tiers, pas accusateur
- **`rewrite_sommet_chap5.md` lignes 72-75** — dans `▌ LA QUESTION`, légitime
- **`rewrite_sommet_chap6.md` lignes 55-59** — dans `▌ LA QUESTION`, légitime
- **`rewrite_sommet_chap7.md` ligne 51-54** — dans `▌ LA QUESTION`, légitime
- **`rewrite_sommet_chap8.md` lignes 52-55** — dans `▌ LA QUESTION`, légitime

---

## ⚠️ POINTS ÉDITORIAUX À SURVEILLER

### 1. `rewrite_terrain_vue_ensemble.md` — "QUI A CONSTRUIT LA TOUR ?" sans saut explicite
Le H1 `# QUI A CONSTRUIT LA TOUR ?` (ligne 37) n'a pas de `page-break-before` explicite.
Il compte sur le `page-break-after: always` du CSS de `infographie-style-4` pour être poussé sur une nouvelle page.
→ **À vérifier visuellement dans le PDF** que ce H1 démarre bien sur une nouvelle page.

### 2. `rewrite_hall_central_terrain.md` — "vous" dans le texte du Hall Central
Le Hall Central contient quelques "vous" dans son texte littéraire ("Levez les yeux… il vous tend la main"). Ce sont des "vous" d'invitation universelle (comme dans une lettre ouverte), pas des "vous" accusateurs. Acceptable éditorialement.

### 3. `rewrite_sommet_les_managers_qui_ont_change.md` — commence par une infographie
Le fichier commence directement par `<div class="infographie-style-4">`. Le script injecte un saut de page avant ce fichier → la CSS `page-break-before` de l'infographie est redondante mais **non problématique** car le saut de page du script s'applique en premier.

---

## 📊 VOLUME TOTAL ESTIMÉ

| Manuscrit | Fichiers | Lignes totales | PDF actuel |
| :--- | :--- | :--- | :--- |
| **Terrain** | 18 | ~2 300 | 144 pages |
| **Sommet** | 19 | ~1 850 | ~130 pages |

---

## 🔲 CONTENU AJOUTÉ DANS CETTE SESSION
1. **Terrain chap2** : Section "Ce que la verticalité fait à l'horizontale" (silos, coopération inter-services)
2. **Sommet angles_morts** : Angle mort n°7 "Les silos que la tour a construits"
3. **Sommet les_managers** : Page de transition PARTIE II "LES LEVIERS"
4. **Terrain vue_ensemble** : Page de transition PARTIE II "LES ROUAGES" (déjà existante, reformatée)
