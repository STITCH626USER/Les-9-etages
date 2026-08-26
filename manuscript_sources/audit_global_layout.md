# AUDIT GLOBAL — TERRAIN & SOMMET
Analyse complète — 2026-08-24

## SYNTHÈSE

| Document  | Pages ~| Fichiers | Issues critiques | Issues mineures |
|-----------|--------|----------|-----------------|-----------------|
| TERRAIN   | ~137   | 18       | 2               | 3               |
| SOMMET    | ~132   | 20       | 0               | 3               |

Total ouvrage : ~269 pages (tête-bêche)

---

## TERRAIN (~137 pages)

### Cartographie

```
Prologue                p.1-2     (2kc,  0br)
Étage 0                 p.3-8     (7kc,  1br)
Étage 1                 p.9-14    (8kc,  1br)
Étage 2                 p.15-23   (12kc, 2br)
Étage 3                 p.24-30   (10kc, 1br)
Étage 4                 p.31-37   (10kc, 1br)
Étage 5                 p.38-46   (10kc, 2br)
Étage 6                 p.47-51   (6kc,  1br)
Étage 7                 p.52-56   (6kc,  1br)
Étage 8 CEO         ⚠  p.57-65   (5kc,  5br)  ← TROP DE BREAKS
Vue d'ensemble          p.66-72   (12kc, 0br)
Le Grand Départ         p.73-82   (12kc, 3br)
Et si ? (monde après)  p.83-91   (11kc, 2br)
Ceux qui ont commencé  p.92-100  (16kc, 0br)
Fiches pratiques        p.101-105 (7kc,  0br)
La Transition       ⚠  p.106-127 (43kc, 0br)  ← 22 PAGES SANS CONTRÔLE
Plan transformation     p.128-133 (8kc,  0br)
Hall Central            p.134-137 (4kc,  1br)
```

### ISSUE 1 — CRITIQUE : chap8 Terrain (CEO) — 5 breaks / 5kc

Chaque mini-section est seule sur sa page. Séquence actuelle :
- Break L18 → "L'écart mathématique absolu" (7 lignes) = page quasi-vide
- Break L28 → "La réalité du pouvoir" (7 lignes) = page quasi-vide
- Break L38 → VOIX + DONNÉES D'ÉTAGE
- Break L62 → LA QUESTION seule
- Break L72 → LE SAVIEZ-VOUS ? seul

ACTION : Supprimer les 3 premiers breaks. Garder 1 seul avant DONNÉES D'ÉTAGE.

### ISSUE 2 — CRITIQUE : la_transition.md (43kc, 0 break = ~22 pages)

Le plus grand fichier du document sans aucun contrôle de pagination.
Les sections se coupent aléatoirement sur 22 pages consécutives.

ACTION : Insérer ~3 breaks aux grandes transitions thématiques du fichier.

### ISSUE 3 — MINEURE : Hall Central Terrain incomplet

Le Terrain se termine sur hall_central_terrain.md (4.5kc).
Le Sommet enchaîne 4 fichiers Hall Central (9kc total) : contenu + 7 principes + miroir + mot auteur.
Un rewrite_hall_central_miroir.md EXISTE dans le répertoire mais N'EST PAS INCLUS dans le générateur Terrain.

QUESTION ÉDITORIALE : intentionnel (asymétrie tête-bêche) ou oubli ?

### ISSUE 4 — MINEURE : Déséquilibre étages hauts vs bas

- Étages 6, 7, 8 : 5-6kc = 3-4 pages chacun
- Étages 2, 3, 4, 5 : 10-12kc = 7-9 pages chacun
Cohérent (vision terrain = plus de détail sur le bas) mais asymétrie forte.

### ISSUE 5 — MINEURE : plan_transformation.md (8kc, 0 break)

À surveiller à la relecture finale.

---

## SOMMET (~132 pages)

### Cartographie

```
Titre                  p.1-2     (2kc,  0br)
Prologue               p.3-5     (3kc,  0br)
Étage 8 CEO        ⚠  p.6-7     (3kc,  0br)  ← TROP COURT
Étage 7                p.8-12    (4kc,  1br)
Étage 6                p.13-15   (4kc,  0br)
Étage 5                p.16-21   (6kc,  2br)
Étage 4                p.22-28   (9kc,  1br)
Étage 3                p.29-34   (9kc,  0br)
Étage 2                p.35-41   (12kc, 0br)
Étage 1                p.42-47   (7kc,  1br)
Étage 0                p.48-55   (8kc,  3br)
Les managers changés  p.56-68   (19kc, 2br)
Ce que Sommet ne voit p.69-86   (23kc, 6br)
Pourquoi pas changer  p.87-96   (11kc, 3br)
Le premier pas        p.97-104  (9kc,  2br)
Guide manager         p.105-122 (25kc, 5br)
Hall Central          p.123-126 (4kc,  1br)
7 Principes           p.127-128 (2kc,  0br)
Miroir croisé         p.129-130 (1kc,  0br)
Mot de l'auteur       p.131-132 (1kc,  0br)
```

### ISSUE 6 — IMPORTANTE : chap8 Sommet (CEO) trop court (2 pages)

Premier chapitre des étages après le prologue, seulement 3kc = 2 pages.
Manquent : DONNÉES D'ÉTAGE et LE TRADUCTEUR DU SOMMET (présents dans étages 1-5).
Le CEO est le pivot narratif du Sommet — il mérite plus de développement.

ACTION RECOMMANDÉE : Étoffer pour atteindre 6-8kc.

### ISSUE 7 — MINEURE : Étages 6-7 Sommet courts (4kc/4kc)

Même tendance qu'en Terrain (sommet de la tour = moins de détail côté Sommet).
Acceptable mais à vérifier si voulu.

### ISSUE 8 — MINEURE : miroir_croise.md sans H1

Commence par ### (H3) sans H1. Invisible en table des matières automatique.
Intentionnel ou oubli ?

---

## ÉTAT CSS/LAYOUT — MÉCANISMES ACTIFS

| Mécanisme                              | Statut      |
|----------------------------------------|-------------|
| Marges A5 cohérentes (12-18mm)         | OK          |
| Numéros de page footer centré          | OK          |
| orphans/widows 3 lignes min            | OK          |
| p + table groupés                      | OK          |
| hr groupé avec son contexte            | OK          |
| blockquote break-inside avoid !        | OK          |
| LE SAVIEZ-VOUS wrapper div             | OK          |
| Sections ▌ keep-together via regex     | OK          |
| Infographies 3 niveaux de gris         | OK          |
| Chiffres % avec espace insécable       | OK          |
| Fiches pratiques flex 2 colonnes       | A VERIFIER  |
| la_transition.md 43kc sans breaks      | RISQUE      |
| chap8 terrain 5 breaks/5kc             | A CORRIGER  |

---

## COMPARAISON TERRAIN / SOMMET

| Dimension              | TERRAIN               | SOMMET             |
|------------------------|-----------------------|--------------------|
| Pages estimées         | ~137                  | ~132               |
| Fichiers sources       | 18                    | 20                 |
| Chars totaux           | ~172kc                | ~141kc             |
| Chapitres étages       | 9 (Étage 0 vers 8)    | 9 (Étage 8 vers 0) |
| Hall Central           | 1 fichier (4.5kc)     | 4 fichiers (9kc)   |
| Fiches pratiques       | Oui (7 fiches)        | Non                |
| Guide manager          | Non                   | Oui (25kc)         |
| Miroir croisé          | Existe, non inclus    | Inclus             |

---

## PLAN D'ACTION PRIORITAIRE

| Priorité | Action                                    | Effort    |
|----------|-------------------------------------------|-----------|
| 1 ROUGE  | Réduire breaks chap8 Terrain (5→1)        | Rapide    |
| 2 ROUGE  | Ajouter breaks la_transition.md           | Moyen     |
| 3 ORANGE | Étoffer chap8 Sommet CEO (2→6 pages)     | Moyen     |
| 4 CHOIX  | Décider miroir terrain inclus ou non      | Éditorial |
| 5 VERT   | Vérifier rendu fiches flex sur PDF        | Relecture |
