# AUDIT TON, LANGUE & STYLE — TERRAIN + SOMMET
*23 août 2026 — Analyse complète*

---

## I. ANGLICISMES — Bilan global

### Termes acceptables tels quels (pas d'équivalent français satisfaisant)
`KPI`, `CEO`, `VP`, `COMEX`, `DRH`, `PowerPoint`, `MBA`, `ROI`, `SCOP`, `ETI`
→ Ces acronymes sont passés dans l'usage courant, leur traduction serait artificielle.

### Termes à mettre systématiquement en italiques (convention à appliquer)
Le livre utilise les italiques pour signaler les anglicismes — mais de façon **très incohérente** :

| Terme | Avec *italiques* | Sans italiques | Verdict |
| :--- | :--- | :--- | :--- |
| *reporting* | 6 | **25** | ⚠️ Majoritairement sans |
| *feedback* | 4 | **12** | ⚠️ Majoritairement sans |
| *management* | 14 | **59** | ⚠️ Très majoritairement sans |
| **manager** | 0 | 89 | ✅ Accepté sans italiques (substantif francisé) |
| *leadership* | 2 | **5** | ⚠️ Souvent sans |
| *burnout* / *burn-out* | 5+1 | **7+2** | ⚠️ Incohérent |
| *process* | 2 | **5** | ⚠️ Souvent sans |
| *dashboard* | 2 | 2 | 🟡 50/50 |

**Recommandation :** Choisir une règle et l'appliquer partout.
- Option A : *italiques systématiques* pour les anglicismes non francisés (`reporting`, `feedback`, `leadership`, `burnout`, `process`, `dashboard`, `sponsor`, `slide`, `benchmark`)
- Option B : les accepter tous sans italiques (style plus fluide, moins pédant)
- **`manager` et `management`** : déjà tellement francisés qu'ils peuvent rester sans italiques dans les deux cas.

---

## II. RÉPÉTITIONS LEXICALES

### Répétitions globales structurelles (légitimes — ce sont les mots-clés du livre)
`terrain` (202×), `étage` (198×), `équipe` (178×), `travail` (149×), `manager` (126×)
→ **Pas de problème** : ce sont les piliers thématiques du livre.

### Répétitions globales à surveiller
- **`chose`** (68×) — terme passe-partout qui affaiblit les phrases. À remplacer par le substantif précis à chaque occurrence.
- **`réalité`** (52×) — utilisé à toutes les sauces. Dans certains passages, il peut être remplacé par : le concret, le terrain, les faits, le quotidien, la matière.
- **`livre`** (44×) — le manuscrit se cite lui-même 44 fois. Dans certains passages cela crée une distanciation qui sort le lecteur du flux.

### Répétitions locales problématiques (même mot 4-6× dans 10 lignes)
| Localisation | Mot répété | Contexte |
| :--- | :--- | :--- |
| `terrain_chap2.md` ~l.40 | **« service »** ×6 | Section sur les silos — acceptable car c'est le sujet, mais peut être allégé |
| `sommet_angles_morts.md` ~l.126 | **« cadres »** ×4 | Section sur le coût des relations — à varier |
| `sommet_guide_manager.md` ~l.75 | **« pourquoi »** ×4 | Section questions rhétoriques — intentionnel mais vérifier |
| `sommet_guide_manager.md` ~l.137 | **« expérimentation »** ×5 | Section sur l'autonomie — à alléger avec pronoms |
| `terrain_vue_ensemble.md` ~l.61 | **« ouvrier »** ×4 | Section Taylor/Ford — acceptable historiquement |

---

## III. STRUCTURES RHÉTORIQUES RÉPÉTÉES

Le livre utilise certains patterns rhétoriques très efficaces — mais leur répétition trop fréquente les émousse.

| Structure | Occurrences | Verdict |
| :--- | :--- | :--- |
| *« Ce n'est pas X. C'est Y. »* | **23×** | ⚠️ Overused — à réserver aux moments forts |
| *« Parce que »* en début de phrase | 7× | ✅ Acceptable |
| *« Pas parce que X. Mais parce que Y. »* | 5× | 🟡 Limite haute |
| Phrases commençant par *« Et »* | **40×** | ⚠️ Trop fréquent — stylistique mais à doser |

**Recommandation :** La structure *« Ce n'est pas X. C'est Y. »* est percutante — mais 23 répétitions sur l'ensemble du livre la banalisent. Conserver dans les 8-10 moments clés, reformuler les autres.

---

## IV. NIVEAU DE LANGUE — COHÉRENCE

### Problème unique détecté
**`rewrite_terrain_ceux_qui_ont_commence.md` — ligne 26 :**
> *« Mais ça marche vachement bien. »*

Ce terme (`vachement`) apparaît dans une citation directe de témoignage (entre guillemets) — ce qui le rend **légitime** : c'est la voix du personnage, pas la voix narratrice. Aucune correction nécessaire.

### Conclusion sur le registre
Le niveau de langue est globalement **bien maîtrisé et cohérent** :
- Le corps analytique est dans un registre soutenu-accessible (ce qui est exactement le bon niveau pour ce type d'ouvrage)
- Les VOIX DU TERRAIN/SOMMET descendent volontairement dans un registre plus familier — c'est délibéré et juste
- Aucun mélange de registres dans les sections analytiques

---

## V. TYPOGRAPHIE

### Guillemets droits (à vérifier)
76 occurrences de guillemets droits `"..."` ont été détectées — principalement dans les **attributs HTML** des blocs d'infographie et de mise en page. Ces guillemets droits dans le code HTML sont **normaux et ne doivent pas être modifiés**. Dans le corps du texte, les guillemets français `«` et `»` sont bien utilisés.
→ **Pas d'action nécessaire.**

### Espace avant les deux-points
643 occurrences d'espace avant `:` — ce qui est **correct en typographie française** (espace fine insécable avant `:`, `!`, `?`, `;`). Le rendu PDF Puppeteer gère cela. Pas de problème.

---

## VI. FORMULES CREUSES

**« Mettre en place »** — expression bureaucratique, utilisée 14× dans les fiches pratiques principalement. Dans ce contexte (fiches d'action), elle est fonctionnelle et attendue. Dans le corps narratif, elle peut être avantageusement remplacée par un verbe d'action direct : *installer, créer, instaurer, lancer, déployer.*

---

## VII. SYNTHÈSE — ACTIONS PRIORITAIRES

| Priorité | Problème | Action |
| :--- | :--- | :--- |
| 🟠 Recommandé | Italiques incohérents sur anglicismes | Choisir une règle et l'appliquer globalement (sed automatisable) |
| 🟠 Recommandé | *« Ce n'est pas X. C'est Y. »* ×23 | Réduire à ~10 occurrences — reformuler les autres |
| 🟡 Optionnel | `chose` (68×) | Remplacer par le substantif précis au cas par cas |
| 🟡 Optionnel | `réalité` (52×) | Varier avec : concret, quotidien, terrain, matière |
| 🟡 Optionnel | Phrases commençant par `Et` (40×) | En réduire 15-20 par fusion ou reformulation |
| ✅ Rien à faire | Niveau de langue | Cohérent et bien calibré |
| ✅ Rien à faire | Guillemets / typographie | OK en contexte PDF |
| ✅ Rien à faire | Mots argotiques dans les témoignages | Légitimes — voix des personnages |

---

## RECOMMANDATION GLOBALE

Le manuscrit est **stylisitquement solide**. La voix est identifiable, le ton est constant, le registre est bien calibré pour le lectorat visé (managers + terrain cultivé, pas un public académique). Les vrais chantiers sont :

1. **Les italiques** — c'est une correction automatisable en 5 minutes (sed)
2. **La structure rhétorique répétitive** — ciblée sur quelques passages spécifiques

Rien qui nécessite une réécriture profonde.
