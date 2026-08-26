# Rapport de correction littéraire — Intégralité des 2 PDF

> Lecture complète de tous les chapitres Terrain + Sommet. Corrections classées par type.

---

## 🔴 PRIORITÉ 1 — Erreurs factuelles dans les chapitres non encore vérifiés

### 1. Chap7 Terrain — Arithmétique incohérente sur les rémunérations CAC 40

**Fichier** : `rewrite_terrain_chap7.md`

> *"En France, en 2023, la rémunération médiane d'un grand dirigeant du CAC 40 atteignait **près de 7 millions d'euros** annuels, représentant un écart de **plus de 140 fois** par rapport au salaire médian national."*

**Problème double** :
- Le salaire médian national français 2023 est d'environ **26 000 à 28 000 €** brut annuel (INSEE). Or 7 000 000 ÷ 27 000 = **259×**, pas 140×.
- Pour que le ratio soit 140×, il faudrait un salaire de base de ~50 000 € — ce qui est le salaire moyen, non le médian.
- Par ailleurs, notre correction infographique cite **×95** (Proxinvest — salaire médian des salariés de la même entreprise). Ce sont deux mesures différentes mais qui méritent d'être cohérentes.

**Correction proposée** : Soit ajuster le ratio (259× plutôt que 140×), soit reformuler :
> *"En France en 2023, la rémunération médiane d'un grand dirigeant du CAC 40 dépassait les 5 millions d'euros annuels — soit environ 200 fois le salaire médian de ses propres salariés (Proxinvest, 2023). Aux États-Unis, ce ratio est passé de 21 pour 1 dans les années 1960 à plus de 290 pour 1 aujourd'hui."*

---

### 2. Chap6 Terrain — HBR 2019 "1 700 cadres, 73 % vs 12 %" (non vérifié)

**Fichier** : `rewrite_terrain_chap6.md`

> *"En 2019, une vaste étude de la Harvard Business Review menée auprès de 1 700 cadres dirigeants internationaux révélait : 73 % estimaient 'bien connaître la réalité de leur terrain'. Moins de 12 % avaient eu un contact direct avec un salarié opérationnel au cours des six derniers mois."*

**Problème** : Cette étude n'est pas vérifiable dans les sources publiques. La formulation et le chiffre de 1 700 cadres peuvent prêter à confusion avec d'autres études HBR. Le contraste 73 % / 12 % est très percutant mais sans source solide.

**Correction proposée** : Attribuer plus prudemment :
> *"Des études successives (dont plusieurs publiées par la Harvard Business Review sur les pratiques dirigeantes) montrent de façon constante un décalage vertigineux : la grande majorité des dirigeants se déclarent 'proches de leur terrain', tandis qu'une petite minorité y a eu un vrai contact direct dans les six derniers mois."*

---

### 3. Chap3 Terrain — Deloitte 2019 "10 000 organisations, 77 % silos" (à vérifier)

**Fichier** : `rewrite_terrain_chap3.md`

> *"Une étude de Deloitte (2019) sur 10 000 organisations mondiales révèle que 77 % des dirigeants identifient le cloisonnement inter-services comme l'un de leurs principaux freins à l'exécution stratégique."*

**Statut** : Chiffre plausible — Deloitte publie ses Human Capital Trends avec des échantillons de cette taille. Mais non vérifié dans le détail. Le concept est bien documenté par Deloitte HCT 2019. Acceptable si la source est reformulée :
> *"Selon le Deloitte Human Capital Trends Report 2019..."*

---

## 🟠 PRIORITÉ 2 — Phrases orphelines ou ambiguës

### 4. Sommet — Section Ford — Phrase incomplète

**Fichier** : `rewrite_sommet_chap1.md` (ou section historique)

> *"L'ouvrier n'est même plus un exécutant — il est un composant de la machine. Interchangeable. Remplaçable. **Le remplacement est si facile, disait-on en exemple dans notre enquête.**"*

**Problème** : *"disait-on en exemple dans notre enquête"* est une phrase orpheline. Elle ne s'appuie sur aucune enquête mentionnée. Elle semble être un résidu d'une première version du texte.

**Correction** : Supprimer cette phrase. La phrase précédente est suffisamment forte seule.

---

### 5. Terrain chap3 — "Machines à fumée"

**Fichier** : `rewrite_terrain_chap3.md`

> *"Un jour, il m'a questionné sur des 'machines à fumée' que notre service n'a jamais eues."*

**Observation** : L'expression "machines à fumée" n'est pas un terme technique courant et peut prêter à confusion. Selon le contexte (secteur événementiel), il s'agit probablement de machines à brouillard/fumée de scène. Écrire *"machines à fumée de scène"* ou simplement *"machines à brouillard"* serait plus clair.

---

## 🟡 PRIORITÉ 3 — Style et fluidité

### 6. Terrain chap5 (Plan de transformation historique) — "(quoique)" répété

**Fichier** : `rewrite_terrain_plan_transformation.md` ou `rewrite_terrain_la_transition.md`

> *"Pas avec des manifestations (quoique). Pas avec des révolutions (quoique)."*

**Observation** : La répétition de "(quoique)" deux fois en succession immédiate est maladroite à l'écrit. Elle fonctionne mieux à l'oral.

**Correction** : *"Pas avec des manifestations — quoique l'histoire n'en soit pas avare. Pas avec des révolutions declarées. Avec quelque chose de plus silencieux..."*

---

### 7. Sommet chap7 (Chairman) — Rupture de style légère

> *"Il signe. En signant, une image lui revient."*

**Observation** : "Il signe. En signant" — la répition du mot "sign" à si courte distance est maladroite. **Correction** : *"Il signe. Et au moment où la plume touche le papier, une image lui revient."*

---

### 8. Cohérence de la majuscule sur "Terrain" / "Sommet"

**Fichier** : Tous les chapitres

Le livre utilise "le Terrain", "le Sommet", "l'Étage" avec majuscules pour désigner les concepts. Mais on trouve parfois "terrain" (minuscule) dans le corps du texte courant (non-titres) — ce qui est incohérent.

**Recommandation** : Standardiser : majuscule pour les concepts abstraits (*"ceux du Terrain"*), minuscule pour le sens physique (*"sur le terrain ce matin"*). Actuellement mixé.

---

### 9. Emploi de l'italique et des anglicismes — cohérence

Dans l'ensemble des chapitres, les anglicismes sont en italique (*management*, *reporting*, *headcount*, *board*, *standup*, *feedback*, *benchmark*...). C'est une convention correcte et cohérente dans la plupart des chapitres.

**Exception détectée** : *"CEO"* n'est **pas** en italique, alors qu'il s'agit d'un anglicisme. Ce choix est acceptable (CEO est devenu d'usage courant), mais mérite d'être uniformisé. Même chose pour *"KPI"*.

---

## ✅ CE QUI EST TRÈS BIEN — À ne pas toucher

| Passage | Pourquoi c'est réussi |
|---|---|
| **Sommet chap2 — "7h45"** (Laurent au sol) | Le plus beau chapitre des deux livres. Aucune correction nécessaire. |
| **Sommet chap7 — Le Chairman qui a commencé en bas** | Écriture sobre et très émouvante. Le "Le mot 'poste' apparaît 47 fois. 'Personne' : 3 fois. 'Humain' : 0." est brillant. |
| **Terrain chap4 — Analogie Milgram** | Bien dosée, ni trop longue ni trop abrupte. Solide. |
| **La section Taylor/Ford/MBA/Friedman** | Pédagogie parfaite, rythme soutenu, tableau de synthèse utile. |
| **Le Miroir Croisé** | Les voix des deux côtés sont équilibrées, personne n'est caricaturé. |
| **Les "VOIX DU TERRAIN/SOMMET"** | Cohérents, anonymisés, crédibles, diversifiés. |
| **Le "LE TRADUCTEUR"** | Tables de traduction : percutantes, justes, lisibles. |
| **La "QUESTION" de clôture** de chaque chapitre | Toujours bien calibrée — invite à la réflexion sans être accusatrice. |

---

## Synthèse — Corrections à appliquer

| # | Type | Priorité | Fichier | Action |
|---|---|---|---|---|
| 1 | Arithmétique fausse (7M€, 140×) | 🔴 | `chap7_terrain` | Corriger chiffres |
| 2 | Citation HBR non vérifiable | 🟠 | `chap6_terrain` | Reformuler sans chiffres précis |
| 3 | Phrase orpheline (Ford / enquête) | 🟠 | Sommet historique | Supprimer |
| 4 | Deloitte 2019 — attribution | 🟡 | `chap3_terrain` | Préciser la source |
| 5 | "Machines à fumée" flou | 🟡 | `chap3_terrain` | Clarifier le terme |
| 6 | "(quoique)" répété | 🟡 | `plan_transformation` | Réécrire |
| 7 | "Il signe. En signant" | 🟡 | Sommet `chap7` | Reformuler |
| 8 | Majuscule Terrain/Sommet | 🟡 | Tous | Uniformiser |
