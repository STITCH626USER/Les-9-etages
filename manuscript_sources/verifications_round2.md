# Vérifications restantes — Round 2

> Résultat des 3 nouvelles recherches + liste complète des points non encore vérifiés

---

## 🔴 À CORRIGER MAINTENANT

### Linux — "90 % des serveurs mondiaux" ❌
| | |
|---|---|
| **Chiffre utilisé** | *"Linux fait tourner 90 % des serveurs mondiaux"* |
| **Réalité** | Linux représente environ **44,8 %** du marché des OS serveurs en 2024. En revanche, Linux fait tourner **100 % des 500 supercalculateurs les plus puissants** du monde (TOP500 depuis 2017) et domine l'infrastructure cloud (AWS, GCP, Azure). |
| **Fichier** | `rewrite_terrain_et_si.md` — ligne 80 |
| **Correction** | *"Linux fait tourner la quasi-totalité de l'infrastructure cloud mondiale (AWS, Google, Azure) et 100 % des 500 supercalculateurs les plus puissants de la planète."* |

### Android — "quasi-totalité des smartphones" ⚠️
| | |
|---|---|
| **Chiffre utilisé** | *"la quasi-totalité des smartphones (Android)"* |
| **Réalité** | Android = **~72 %** des smartphones mondiaux. iOS = ~28 %. "Quasi-totalité" est exagéré — "la grande majorité" ou "72 %" seraient exacts. |
| **Correction** | Remplacer *"quasi-totalité"* par *"environ 72 %"* |

---

## ✅ CONFIRMÉS — Rien à changer

| Claim | Verdict |
|---|---|
| **Mondragon ratio 1:6** | ✅ Confirmé — c'est le ratio de référence officiellement documenté (range réel 3:1 à 9:1 selon les coopératives, 6:1 est la norme citée) |
| **Buurtzorg "35 % de coûts en moins"** | ✅ Confirmé par Ernst & Young (jusqu'à 40 % d'économies système) et Swiss Re (35,7 % moins d'heures de soin par patient). Le chiffre est dans la fourchette documentée. |
| **Loi Pacte 2019 + ratio 1:96 CAC 40** | ✅ Cohérent avec notre correction à ×95 (Proxinvest) — la Loi Pacte oblige bien la publication de ce ratio depuis 2019. |
| **Taylor, Principles of Scientific Management, 1911** | ✅ |
| **FAVI — suppression contremaîtres, Zobrist, 1983** | ✅ |
| **Mondragon — coopérative basque** | ✅ |
| **"De 20 pour 1 dans les années 1960"** | ✅ Cohérent avec les données historiques US/France sur l'écart salarial CEO/travailleur |

---

## 🟡 NON ENCORE VÉRIFIÉS — À faire

### Dans le texte des chapitres TERRAIN

| Claim | Fichier | Priorité |
|---|---|---|
| Toyota : "700 000 suggestions/an, 90 % mises en œuvre" | `rewrite_terrain_fiches_pratiques.md` ligne 136 | 🟠 Moyen |
| FAVI : "absentéisme tombé en dessous de 1 %, moyenne industrie ~5 %" | `rewrite_terrain_la_transition.md` ligne 98 | 🟠 Moyen |
| "4 000 SCOP en France en 2024" | `rewrite_terrain_et_si.md` | 🟠 Moyen |
| "Up Group / Chèque Déjeuner — 3 700 salariés" | `rewrite_terrain_et_si.md` | 🟡 Faible |
| "Acome — 1 800 salariés, leader mondial des câbles" | `rewrite_terrain_et_si.md` | 🟡 Faible |
| Témoignage "36 millions" CEO + "164 000 salariés" | `rewrite_terrain_chap8.md` | 🔴 **Risque juridique** |
| Buurtzorg : "10 000 infirmières aux Pays-Bas" + "850 équipes en 5 ans" | `rewrite_terrain_la_transition.md` | 🟡 Faible |

### ⚠️ Risque juridique — le témoignage CEO 36M€ / 164 000 salariés

Le témoignage *"Le salaire annuel de notre grand patron avoisine les 36 millions. L'entreprise compte 164 000 salariés."* est très précis. En cherchant rapidement : **Orange** en France compte environ 137 000 salariés, **Carrefour** ~320 000, **SNCF** ~146 000, **EDF** ~165 000, **Véolia** ~220 000.

**EDF ou SNCF** (164 000 salariés) combiné à une rémunération de 36M€ ne correspond à aucun dirigeant récent de ces groupes (leurs PDG gagnent ~500k à 2M€ sous plafonnement public). Ce témoignage ne désigne donc pas une entreprise publique — il pourrait pointer vers un groupe privé du CAC 40. Même anonymisé, si un lecteur identifie l'entreprise via les chiffres, cela crée un risque.

**Recommandation** : Rendre les chiffres moins précis (ex: *"avoisine les dizaines de millions"* + *"plus de 100 000 salariés"*) pour garantir une anonymisation réelle.

---

### LES CHAPITRES SOMMET — jamais lus 🔴

**C'est le plus grand angle mort** de toutes nos vérifications. Nous n'avons pas encore lu le contenu des chapitres Sommet (rewrite_sommet_chap0.md à chap8.md, guide_manager, angles_morts, pourquoi_ne_pas_changer, etc.)

Ces fichiers sont l'autre moitié du livre — ils parlent AUX dirigeants. Si le ton y est trop accusateur, condescendant ou au contraire trop complaisant, le livre perd sa cohérence têtebêche.

**À vérifier en priorité :**
- Chap0 Sommet : le ton d'ouverture (équivalent du lundi matin opérationnel côté Terrain)
- `rewrite_sommet_pourquoi_ne_pas_changer.md` : souvent le chapitre le plus polarisant
- `rewrite_sommet_angles_morts.md` : est-ce bienveillant ou accusateur ?
- `rewrite_sommet_guide_manager.md` : les solutions côté dirigeant sont-elles réalistes ?

---

## Ce que je recommande de faire dans l'ordre

1. **🔴 Corriger Linux + Android** dans `rewrite_terrain_et_si.md` → immédiatement
2. **🔴 Anonymiser davantage** le témoignage CEO 36M€ / 164 000 salariés → risque juridique réel
3. **🟠 Lire et auditer les chapitres Sommet** → angle mort majeur
4. **🟠 Vérifier Toyota 700k suggestions** → facile à vérifier, souvent cité
5. **🟠 Vérifier FAVI absentéisme 1%** → spécifique, vérifiable
6. **🟡 Vérifier 4 000 SCOP** → anecdotique mais mieux d'être exact
