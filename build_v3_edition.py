import os
import subprocess
import shutil
import fitz

SCRATCH = '/Users/basile/.gemini/antigravity-ide/scratch'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
V3_DIR = '/Users/basile/Desktop/Les-9-etages/V3'

os.makedirs(SCRATCH, exist_ok=True)
os.makedirs(V3_DIR, exist_ok=True)

def render_html_to_pdf(html_content, output_pdf):
    temp_html = os.path.join(SCRATCH, 'temp_page.html')
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    cmd = [
        CHROME,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={output_pdf}',
        temp_html
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def standardize_all_footers(doc):
    """
    Standardize footers across all numbered pages (from page 4, index 3, to end):
    1. Redact footer area y in [555, 585]
    2. Re-open to clear text cache
    3. Center page number with font helv 8.5pt at exact baseline y=571.92
    """
    for pno in range(3, len(doc)):
        page = doc[pno]
        page.add_redact_annot(fitz.Rect(170, 555, 250, 585), fill=(1, 1, 1))
        page.apply_redactions()
    tmp_bytes = doc.tobytes()
    doc.close()
    doc_clean = fitz.open('pdf', tmp_bytes)
    for pno in range(3, len(doc_clean)):
        page = doc_clean[pno]
        page_num_str = str(pno + 1)
        tw = fitz.get_text_length(page_num_str, fontname='helv', fontsize=8.5)
        x_pt = 210.0 - tw / 2.0
        y_pt = 571.92
        page.insert_text(fitz.Point(x_pt, y_pt), page_num_str, fontname='helv', fontsize=8.5, color=(0.4, 0.4, 0.4))
    return doc_clean

# ----------------------------------------------------
# 1. PAGE 53 : NOUVELLE CITATION ÉTAGE 1 (MANAGER DE PROXIMITÉ)
# ----------------------------------------------------
html_p53 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@1,400;1,500&family=Montserrat:wght@600;700&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    display: flex; flex-direction: column; justify-content: flex-end; align-items: center;
    padding: 0 45pt 90pt 45pt; position: relative; -webkit-font-smoothing: antialiased;
}
.rule { width: 80pt; height: 1.2pt; background-color: #8da4be; margin-bottom: 15pt; }
.quote {
    font-family: 'Lora', Georgia, serif; font-style: italic; font-size: 9.6pt;
    line-height: 14.5pt; text-align: center; color: #27272a; max-width: 310pt; margin-bottom: 12pt;
}
.attribution {
    font-family: 'Montserrat', sans-serif; font-size: 7.2pt; font-weight: 700;
    letter-spacing: 1.5px; text-transform: uppercase; color: #64748b; text-align: center;
}
.footer-page {
    position: absolute; bottom: 23pt; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>
<div class="rule"></div>
<div class="quote">« Le rôle d'un manager n'est pas de faire le travail à la place des autres, mais de créer les conditions pour que le travail puisse enfin être fait. »</div>
<div class="attribution">— W. EDWARDS DEMING — HORS DE LA CRISE</div>
<div class="footer-page">53</div>
</body>
</html>'''

# ----------------------------------------------------
# 1.1. PAGES 4 & 5 (SOMMET) : PROLOGUE INTÉGRAL SANS COUPURE
# ----------------------------------------------------
html_p4 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Lora:ital,wght@0,400;0,700;1,400&display=swap');
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 34.8pt 33.75pt 30pt 33.75pt;
    font-family: 'Lora', Georgia, serif; font-size: 8.9pt; line-height: 12.8pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}
.header { text-align: center; margin-bottom: 14pt; }
h1 {
    font-family: 'Montserrat', sans-serif; font-size: 11.2pt; font-weight: 800;
    text-transform: uppercase; letter-spacing: 0.5px; color: #000000;
    line-height: 14.5pt; margin-bottom: 8pt;
}
.rule { width: 100%; height: 0.75pt; background-color: #000000; margin-bottom: 12pt; }
p {
    text-align: justify; text-justify: inter-word; margin-bottom: 7.5pt;
    hyphens: auto; -webkit-hyphens: auto;
}
.footer-page {
    position: absolute; bottom: 23pt; left: 0; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>

<div class="header">
    <h1>PROLOGUE SOMMET&nbsp;: DEMAIN, LE<br>TERRAIN NE RÉPOND PLUS</h1>
    <div class="rule"></div>
</div>

<p>Quatre lieux. Quatre métiers. Le même lundi matin. Mais cette fois, personne ne monte de l'étage 0.</p>

<p><strong>Dans un théâtre, quelque part.</strong> 8h15. Le directeur de salle arrive, café en main, badge au cou. Il ouvre son ordinateur, consulte ses courriels et prépare la réunion de 10h avec le programmateur. À 9h00, il descend vers le plateau. Les portes sont ouvertes, mais les lumières restent éteintes. La console est froide, les perches immobiles, le sol non balayé. Personne. Il appelle&nbsp;: aucune réponse. Le régisseur ne viendra pas. Les techniciens, l'habilleuse et l'accessoiriste non plus. Il est 9h30. Dans une heure, trois cents personnes viendront s'asseoir dans cette salle, attendant qu'on leur raconte une histoire. Ils ont payé pour cela, certains ont économisé. Le directeur contemple le plateau désert. Il sait piloter un budget et négocier avec les institutions. Il ne sait pas allumer un projecteur. Le spectacle n'aura pas lieu.</p>

<p><strong>Dans un service hospitalier, ailleurs.</strong> 7h00. La cadre de santé arrive, rentrée de sa formation sur «&nbsp;le pilotage de la performance soignante&nbsp;». Elle dispose d'un nouveau support, d'indicateurs et d'un plan d'action. Elle franchit le sas du service&nbsp;: les couloirs sont déserts. Aucune infirmière, aucune aide-soignante, aucun brancardier. Chambre 12 (surveillance renforcée)&nbsp;: personne ne veille. Chambre 7 (perfusion à renouveler à 9h)&nbsp;: personne ne viendra. La cadre de santé possède un master en gestion hospitalière. Elle sait gérer des dotations, renseigner les tableaux de bord pour l'autorité de tutelle et rédiger des fiches de poste. Elle ne sait plus poser une perfusion. Les alarmes retentissent. L'hôpital ne fonctionne pas.</p>

<p><strong>Dans un restaurant, en centre-ville.</strong> 9h30. Le directeur régional réalise son audit de terrain. Il se présente avec sa grille d'évaluation, son stylo et son souci du détail. La porte demeure close. Ni chef en cuisine, ni commis, ni plongeur, ni serveur. Les livraisons matinales stagnent sur le seuil, les caisses chauffant au soleil. Le lot de poisson que quelqu'un aurait dû refuser commence à s'altérer. Le directeur régional sait analyser un ticket moyen, calculer un ratio matière et comparer vingt établissements sur un tableur. Il ne sait pas préparer un repas. Le restaurant n'ouvrira pas.</p>

<div class="footer-page">4</div>
</body>
</html>'''

html_p5 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Lora:ital,wght@0,400;0,700;1,400&display=swap');
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 34.8pt 33.75pt 30pt 33.75pt;
    font-family: 'Lora', Georgia, serif; font-size: 9.15pt; line-height: 13.5pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}
p {
    text-align: justify; text-justify: inter-word; margin-bottom: 9.5pt;
    hyphens: auto; -webkit-hyphens: auto;
}
.rule-separator {
    width: 100%; height: 0.75pt; background-color: #d1d5db; margin: 16pt 0;
}
.footer-page {
    position: absolute; bottom: 23pt; left: 0; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>

<p><strong>Sur un chantier, en périphérie.</strong> 7h30. Le conducteur de travaux revient de sa réunion avec le maître d'ouvrage. Tableaux financiers, pourcentages d'avancement et marges prévisionnelles sont au point. Le chantier reste pourtant silencieux&nbsp;: pas de chef d'équipe, de ferrailleur, de grutier ni de maçon. La grue ne tourne pas, le béton n'a pas été acheminé. Le conducteur de travaux sait lire un plan, planifier des étapes et négocier des avenants. Il ne sait pas couler une dalle. Le chantier ne progressera pas.</p>

<div class="rule-separator"></div>

<p>Quatre lieux. Quatre métiers. Quatre équipes opérationnelles absentes&nbsp;: l'arrêt est immédiat et absolu.</p>

<p>Une interrogation fondamentale s'impose alors à toute organisation&nbsp;: Si demain, le terrain cesse de monter&nbsp;: la structure continue-t-elle d'avancer&nbsp;? Ou tout s'arrête-t-il net&nbsp;? Et si l'activité s'arrête... où réside véritablement la création de valeur&nbsp;?</p>

<p>Ce constat n'est pas un réquisitoire, mais une grille de lecture. De l'autre côté de ce livre — en le retournant —, il y a le même lundi matin, où les chaînes de décision sont absentes tandis que le Terrain fait tourner les opérations sans le moindre accroc. Dès lors que le travail réel s'auto-régule, mais qu'aucune décision stratégique ne prend vie sans lui&nbsp;: comment penser une gouvernance enfin alignée sur le réel&nbsp;?</p>

<p>Descendons.</p>

<div class="footer-page">5</div>
</body>
</html>'''

# ----------------------------------------------------
# 2. PAGE 60 : NOUVELLE CITATION TRANSITION PARTIE II (MAX DE PREE)
# ----------------------------------------------------
html_p60 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@1,400;1,500&family=Montserrat:wght@600;700&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    display: flex; flex-direction: column; justify-content: flex-end; align-items: center;
    padding: 0 45pt 90pt 45pt; position: relative; -webkit-font-smoothing: antialiased;
}
.rule { width: 80pt; height: 1.2pt; background-color: #8da4be; margin-bottom: 15pt; }
.quote {
    font-family: 'Lora', Georgia, serif; font-style: italic; font-size: 9.6pt;
    line-height: 14.5pt; text-align: center; color: #27272a; max-width: 310pt; margin-bottom: 12pt;
}
.attribution {
    font-family: 'Montserrat', sans-serif; font-size: 7.2pt; font-weight: 700;
    letter-spacing: 1.5px; text-transform: uppercase; color: #64748b; text-align: center;
}
.footer-page {
    position: absolute; bottom: 23pt; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>
<div class="rule"></div>
<div class="quote">« Le premier devoir d'un dirigeant est de définir la réalité. Le dernier est de dire merci. Entre les deux, il doit être un serviteur. »</div>
<div class="attribution">— MAX DE PREE — LEADERSHIP IS AN ART</div>
<div class="footer-page">60</div>
</body>
</html>'''

# ----------------------------------------------------
# 2.1. PAGE 61 : NOUVEAU TITRE PARTIE II EN FORMAT OPTION A
# ----------------------------------------------------
html_p61 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;1,400&family=Montserrat:wght@700;800&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 42pt 33.75pt 30pt 33.75pt;
    font-family: 'Lora', Georgia, serif; font-size: 9.15pt; line-height: 14pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}
.partie-label {
    font-family: 'Montserrat', sans-serif; font-size: 8pt; font-weight: 700;
    letter-spacing: 2px; text-transform: uppercase; color: #71717a; text-align: center;
    margin-bottom: 8pt;
}
h1 {
    font-family: 'Montserrat', sans-serif; font-size: 15pt; font-weight: 800;
    text-transform: uppercase; letter-spacing: 0.5px; color: #000000;
    text-align: center; line-height: 18pt; margin-bottom: 11pt;
}
.rule {
    width: 352.5pt; height: 0.75pt; background-color: #000000; margin: 0 auto 12pt auto;
}
.subtitle {
    font-family: 'Lora', Georgia, serif; font-size: 10pt; font-weight: 400;
    text-align: center; color: #111111; margin-bottom: 36pt; line-height: 14pt;
}
p.intro {
    font-family: 'Lora', Georgia, serif; font-style: italic; font-size: 9.5pt;
    line-height: 15.5pt; text-align: center; color: #27272a; max-width: 310pt;
    margin: 0 auto;
}
.page-number {
    position: absolute; bottom: 23pt; left: 0; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>

<div class="partie-label">PARTIE II</div>
<h1>LES LEVIERS DU GOUVERNEMENT DU RÉEL</h1>
<div class="rule"></div>
<div class="subtitle">De la distance du pouvoir à la puissance d'agir</div>

<p class="intro">Le premier acte de ce livre vous a fait descendre neuf étages d'une tour dont vous occupez peut-être l'un des paliers. Vous avez vu, étage par étage, ce que coûte la distance entre le pouvoir et la matière. Il est temps maintenant de construire quelque chose.</p>

<div class="page-number">61</div>

</body>
</html>'''


# ----------------------------------------------------
# 3.1. PAGE 22 (SOMMET) : DÉDOUBLONNAGE PROPRE DU BILAN ÉTAGE 6
# ----------------------------------------------------
html_p22 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Montserrat:wght@600;700;800&display=swap');
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; padding: 38pt 33.8pt 45pt 33.8pt;
    font-family: 'Lora', Georgia, serif; color: #111111; background: #ffffff;
    position: relative; -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}
.section-head {
    font-family: 'Montserrat', sans-serif; font-size: 9.6pt; font-weight: 700;
    color: #000000; text-align: left;
    margin-top: 18pt; margin-bottom: 8pt;
    text-transform: uppercase; letter-spacing: 0.3px;
    display: flex; align-items: center; gap: 6pt;
}
.section-head::before {
    content: ''; display: inline-block; width: 4.8pt; height: 9.6pt;
    background-color: #111111; flex-shrink: 0;
}
p {
    font-family: 'Lora', Georgia, serif;
    font-size: 9.15pt; font-weight: 400; line-height: 13.8pt; text-align: justify;
    margin-bottom: 7pt; color: #111111;
    hyphens: auto; -webkit-hyphens: auto;
}
.callout {
    background-color: #f8f8f8; border-left: 3.5px solid #000000; padding: 10pt 12pt; margin-top: 18pt;
}
.callout-title {
    font-family: 'Montserrat', sans-serif; font-size: 8.5pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6pt; color: #000000;
}
.callout p {
    font-size: 8.9pt; font-style: italic; line-height: 1.45; margin-bottom: 0; color: #111111;
}
.footer-page {
    position: absolute; bottom: 25pt; width: 100%; left: 0; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #111111;
}
</style>
</head>
<body>
<div class="section-head" style="margin-top: 0;">▌ LE SAVIEZ-VOUS&nbsp;?</div>
<p>Les études en management international démontrent que les projets de standardisation descendante échouent massivement à générer les gains prévus, contournés systématiquement par l'ingéniosité clandestine des équipes locales pour maintenir la production.</p>

<div class="callout">
    <div class="callout-title">▌ LA QUESTION DU SOMMET</div>
    <p>«&nbsp;Vos politiques de standardisation globale laissent-elles aux équipes locales l'espace nécessaire pour s'adapter à la réalité de leur terrain, ou imposent-elles une uniformité qui détruit l'intelligence collective&nbsp;?&nbsp;»</p>
</div>

<div class="footer-page">22</div>
</body>
</html>'''
pdf_p22 = os.path.join(SCRATCH, 'new_p22.pdf')
render_html_to_pdf(html_p22, pdf_p22)

# ----------------------------------------------------
# 3.2. PAGE 83 (SOMMET) : NOUVELLE CONCLUSION POUR ÉVITER LE DOUBLON AVEC P.69
# ----------------------------------------------------
html_p83 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Montserrat:wght@600;700;800&display=swap');
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; padding: 34.8pt 33.8pt 45pt 33.8pt;
    font-family: 'Lora', Georgia, serif; color: #111111; background: #ffffff;
    position: relative; -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}
p {
    font-family: 'Lora', Georgia, serif;
    font-size: 9.15pt; font-weight: 400; line-height: 13.5pt; text-align: justify;
    margin-bottom: 7pt; color: #111111;
    hyphens: auto; -webkit-hyphens: auto;
}
.callout {
    background-color: #f8f8f8; border-left: 3.5px solid #000000; padding: 10pt 12pt; margin: 14pt 0;
}
.callout p {
    font-size: 8.9pt; font-style: italic; line-height: 1.45; margin-bottom: 0; color: #111111;
}
.conclusion-bold {
    font-weight: 700; color: #000000; margin-top: 14pt;
}
.footer-page {
    position: absolute; bottom: 25pt; width: 100%; left: 0; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #111111;
}
</style>
</head>
<body>
<p>L'inaction ne coûte rien dans l'immédiat. C'est sa caractéristique la plus dangereuse. Elle ne produit pas de facture, pas d'alerte comptable, pas de ligne rouge dans les tableaux de bord. Elle s'accumule silencieusement sous forme de capital humain érodé, de savoir-faire qui part, d'opportunités manquées, de clients perdus, de coûts de remplacement qui ne se voient pas parce qu'ils ne sont jamais nommés.</p>

<div class="callout">
    <p>«&nbsp;La pire erreur pour un dirigeant est de croire que la stabilité apparente d'un tableau de bord garantit la sécurité de son organisation. Les entreprises meurent presque toujours d'asphyxie interne, lorsque la technostructure a fini par couper tous les canaux d'oxygène qui reliaient le sommet au travail vivant.&nbsp;»</p>
</div>

<p class="conclusion-bold">L'alternative n'est plus théorique&nbsp;: choisirez-vous d'ouvrir vous-même les portes de la tour, ou attendrez-vous que la pression du sol ne vous laisse plus d'autre issue&nbsp;?</p>

<div class="footer-page">83</div>
</body>
</html>'''
pdf_p83 = os.path.join(SCRATCH, 'new_p83.pdf')
render_html_to_pdf(html_p83, pdf_p83)

# ----------------------------------------------------
# 3.3. PAGE 67 (TERRAIN) : NOUVELLE CITATION D'OUVERTURE DE PARTIE II
# ----------------------------------------------------
html_terrain_p67 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@1,400;1,500&family=Montserrat:wght@600;700&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    display: flex; flex-direction: column; justify-content: flex-end; align-items: center;
    padding: 0 45pt 90pt 45pt; position: relative; -webkit-font-smoothing: antialiased;
}
.rule { width: 80pt; height: 1.2pt; background-color: #8da4be; margin-bottom: 15pt; }
.quote {
    font-family: 'Lora', Georgia, serif; font-style: italic; font-size: 9.6pt;
    line-height: 14.5pt; text-align: center; color: #27272a; max-width: 310pt; margin-bottom: 12pt;
}
.attribution {
    font-family: 'Montserrat', sans-serif; font-size: 7.2pt; font-weight: 700;
    letter-spacing: 1.5px; text-transform: uppercase; color: #64748b; text-align: center;
}
.footer-page {
    position: absolute; bottom: 23pt; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>
<div class="rule"></div>
<div class="quote">« Quand le sommet n'écoute plus ce que le sol sait faire, la tour continue de s'élever mais ses fondations ont déjà cessé d'exister. »</div>
<div class="attribution">— LES 9 ÉTAGES DE LA TOUR —</div>
<div class="footer-page">67</div>
</body>
</html>'''
pdf_terrain_p67 = os.path.join(SCRATCH, 'new_terrain_p67.pdf')
render_html_to_pdf(html_terrain_p67, pdf_terrain_p67)

# ----------------------------------------------------
# 3.4. PAGE 125 (TERRAIN) : PAGE NETTOYÉE MONOCOUCHE
# ----------------------------------------------------
html_terrain_p125 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Montserrat:wght@600;700;800&display=swap');
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; padding: 34.8pt 33.8pt 45pt 33.8pt;
    font-family: 'Lora', Georgia, serif; color: #111111; background: #ffffff;
    position: relative; -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}
p {
    font-family: 'Lora', Georgia, serif;
    font-size: 9.15pt; font-weight: 400; line-height: 13.5pt; text-align: justify;
    margin-bottom: 6.5pt; color: #111111;
    hyphens: auto; -webkit-hyphens: auto;
}
ul {
    margin: 3pt 0 7pt 14pt; font-size: 9.15pt; line-height: 13.5pt; color: #111111;
}
li {
    margin-bottom: 4pt; text-align: justify;
}
.callout {
    background-color: #f8f8f8; border-left: 3.5px solid #000000; padding: 9pt 11pt; margin: 11pt 0;
}
.callout-title {
    font-family: 'Montserrat', sans-serif; font-size: 8pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 5pt; color: #000000;
    border-bottom: 1px solid #e5e5e5; padding-bottom: 3pt;
}
.callout p {
    font-size: 8.6pt; line-height: 1.35; margin-bottom: 5pt; color: #111111;
}
.callout ol {
    margin: 3pt 0 0 12pt; font-size: 8.5pt; line-height: 1.32;
}
.callout li {
    margin-bottom: 3.5pt; text-align: justify;
}
.section-head {
    font-family: 'Montserrat', sans-serif; font-size: 9.6pt; font-weight: 700;
    color: #000000; text-align: left;
    margin-top: 13pt; margin-bottom: 6pt;
    text-transform: uppercase; letter-spacing: 0.3px;
    display: flex; align-items: center; gap: 6pt;
}
.section-head::before {
    content: ''; display: inline-block; width: 4.8pt; height: 9.6pt;
    background-color: #111111; flex-shrink: 0;
}
.footer-page {
    position: absolute; bottom: 25pt; width: 100%; left: 0; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #111111;
}
</style>
</head>
<body>
<p><strong>Années 4-5&nbsp;: Institutionnaliser</strong> Le nouveau modèle devient la norme.</p>
<ul>
    <li>Le fonctionnement en équipes autonomes n'est plus un pilote — c'est le mode de fonctionnement standard de l'organisation.</li>
    <li>Les quelques personnes qui n'ont pas voulu s'adapter font un choix&nbsp;: évoluer ou partir. Pas par contrainte — par inadéquation. Comme dans toute organisation qui change de modèle.</li>
    <li>Les nouvelles recrues sont embauchées dans le nouveau système. Elles n'ont même pas besoin de transition — elles ne connaissent que le nouveau modèle.</li>
</ul>

<p>La tour à 9 étages n'a pas disparu. Mais elle a moins d'étages, des pièces plus grandes, et des portes ouvertes. L'ascenseur fonctionne dans les deux sens. Et surtout, les gens qui y travaillent savent pourquoi ils sont là.</p>

<div class="callout">
    <div class="callout-title">L’ÉPREUVE DE VÉRITÉ &nbsp;|&nbsp; Inaptitude, handicap et usure des corps</div>
    <p>Le piège mortel de l’autonomie est d’exiger des opérateurs à 100&nbsp;% de leurs capacités physiques. Or, le travail use les corps&nbsp;: hernies, TMS, maladies invalidantes, handicaps visibles ou invisibles. Une organisation vivante refuse l’expulsion déguisée et applique trois leviers concrets&nbsp;:</p>
    <ol>
        <li><strong>Sanctuariser les fonctions d’appui&nbsp;:</strong> Réinternaliser la préparation d’outillage, l’ordonnancement ou le contrôle amont pour les confier en priorité aux salariés en aménagement ou en situation de handicap.</li>
        <li><strong>Le statut de Référent-Transmetteur&nbsp;:</strong> L’opérateur qui ne peut plus tenir la cadence physique est détaché pour former les apprentis et transmettre sa mémoire technique. Son salaire est garanti.</li>
        <li><strong>L’ergonomie décidée par les pairs&nbsp;:</strong> L’aménagement des postes est piloté par l’équipe avec un micro-budget autonome.</li>
    </ol>
</div>

<div class="section-head">LE PREMIER PAS</div>
<p><em>Où en êtes-vous sur ce calendrier&nbsp;? À l'année 0 — l'observation&nbsp;? À l'année 1 — le premier pilote&nbsp;? Quel que soit le stade, la suite est la même&nbsp;: un pas. Un seul. Le plus petit possible. Mais dans la bonne direction.</em></p>

<div class="footer-page">125</div>
</body>
</html>'''
pdf_terrain_p125 = os.path.join(SCRATCH, 'new_terrain_p125.pdf')
render_html_to_pdf(html_terrain_p125, pdf_terrain_p125)

# ----------------------------------------------------
# 3.5. PAGE 73 : CONCLUSION & GRILLE DE DÉCISION (POURQUOI LE SYSTÈME RÉSISTE)
# ----------------------------------------------------
html_p73 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Montserrat:wght@600;700;800&display=swap');
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; padding: 34.8pt 33.8pt 45pt 33.8pt;
    font-family: 'Lora', Georgia, serif; color: #111111; background: #ffffff;
    position: relative; -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}
.section-head {
    font-family: 'Montserrat', sans-serif; font-size: 9.6pt; font-weight: 700;
    color: #000000; text-align: left;
    margin-top: 14pt; margin-bottom: 7pt;
    text-transform: uppercase; letter-spacing: 0.3px;
    display: flex; align-items: center; gap: 6pt;
}
.section-head::before {
    content: ''; display: inline-block; width: 4.8pt; height: 9.6pt;
    background-color: #111111; flex-shrink: 0;
}
p {
    font-family: 'Lora', Georgia, serif;
    font-size: 9.15pt; font-weight: 400; line-height: 13.5pt; text-align: justify;
    margin-bottom: 6.5pt; color: #111111;
    hyphens: auto; -webkit-hyphens: auto;
}
table { width: 100%; border-collapse: collapse; margin: 8pt 0 12pt 0; }
th {
    font-family: 'Montserrat', sans-serif; font-size: 7.2pt; font-weight: 700;
    text-transform: uppercase; padding: 6pt 5pt; text-align: left;
    border-top: 1.5px solid #000000; border-bottom: 1px solid #000000; color: #000000; line-height: 1.25;
}
td { padding: 6.5pt 5pt; border-bottom: 1px solid #e5e5e5; color: #111111; font-family: 'Lora', Georgia, serif; font-size: 8.3pt; line-height: 1.35; vertical-align: top; }
tr:last-child td { border-bottom: 1px solid #000000; }
.callout {
    background-color: #f8f8f8; border-left: 3.5px solid #000000; padding: 9pt 11pt; margin-top: 14pt;
}
.callout-title {
    font-family: 'Montserrat', sans-serif; font-size: 8pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 5pt; color: #000000;
}
.callout p {
    font-size: 8.8pt; font-style: italic; line-height: 1.4; margin-bottom: 0; color: #111111;
}
.footer-page {
    position: absolute; bottom: 25pt; width: 100%; left: 0; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #111111;
}
</style>
</head>
<body>
<div class="section-head" style="margin-top: 0;">L'ENSEIGNEMENT DU SOMMET</div>
<p>Ce chapitre ne vous demande pas de renverser l'organisation du jour au lendemain. Il vous invite simplement à identifier avec lucidité les chaînes invisibles qui vous retiennent.</p>
<p><strong>Nommer les freins institutionnels est la première condition pour s'en libérer.</strong></p>

<div class="section-head">GRILLE DE DÉCISION DU DIRIGEANT</div>
<table>
    <thead>
        <tr>
            <th style="width: 25%;">LE FREIN DU SYSTÈME</th>
            <th style="width: 37%;">LE RÉFLEXE DU STATU QUO</th>
            <th style="width: 38%;">LA POSTURE DE RECONNEXION</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Statut & identité</strong></td>
            <td>Défendre ses prérogatives et justifier les strates</td>
            <td>Mesurer sa légitimité à l'autonomie réelle donnée aux équipes</td>
        </tr>
        <tr>
            <td><strong>Incitations financières</strong></td>
            <td>Verrouiller les KPI court terme au détriment du fond</td>
            <td>Protéger les pilotes locaux du diktat du reporting immédiat</td>
        </tr>
        <tr>
            <td><strong>Conformisme managérial</strong></td>
            <td>S'abriter derrière le consensus mou du comité</td>
            <td>Soutenir explicitement les initiatives qui bousculent la norme</td>
        </tr>
        <tr>
            <td><strong>Illusion cosmétique</strong></td>
            <td>Multiplier les chartes, labels et séminaires</td>
            <td>Agir directement sur le pouvoir réel et les circuits de décision</td>
        </tr>
    </tbody>
</table>

<div class="callout">
    <div class="callout-title">▌ LA QUESTION DU SOMMET</div>
    <p>« Dans votre comité de direction, le consensus sert-il à bâtir l'avenir ou à protéger les positions acquises ? »</p>
</div>

<div class="footer-page">73</div>
</body>
</html>'''

pdf_p73 = os.path.join(SCRATCH, 'new_p73.pdf')
render_html_to_pdf(html_p73, pdf_p73)

# ----------------------------------------------------
# 3.6. PAGE 119 : CONCLUSION DU GUIDE TACTIQUE & VOIX DU SOMMET
# ----------------------------------------------------
html_p119 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Montserrat:wght@600;700;800&display=swap');
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; padding: 34.8pt 33.8pt 45pt 33.8pt;
    font-family: 'Lora', Georgia, serif; color: #111111; background: #ffffff;
    position: relative; -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}
.section-head {
    font-family: 'Montserrat', sans-serif; font-size: 9.6pt; font-weight: 700;
    color: #000000; text-align: left;
    margin-top: 14pt; margin-bottom: 7pt;
    text-transform: uppercase; letter-spacing: 0.3px;
    display: flex; align-items: center; gap: 6pt;
}
.section-head::before {
    content: ''; display: inline-block; width: 4.8pt; height: 9.6pt;
    background-color: #111111; flex-shrink: 0;
}
p {
    font-family: 'Lora', Georgia, serif;
    font-size: 9.15pt; font-weight: 400; line-height: 13.5pt; text-align: justify;
    margin-bottom: 6.5pt; color: #111111;
    hyphens: auto; -webkit-hyphens: auto;
}
ul {
    margin: 4pt 0 10pt 14pt; font-size: 9.15pt; line-height: 13.5pt; color: #111111;
}
li {
    margin-bottom: 4.5pt; text-align: justify;
}
.callout {
    background-color: #f8f8f8; border-left: 3.5px solid #000000; padding: 10pt 12pt; margin-top: 14pt;
}
.callout-title {
    font-family: 'Montserrat', sans-serif; font-size: 8.5pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6pt; color: #000000;
}
.callout p {
    font-size: 8.8pt; font-style: italic; line-height: 1.4; margin-bottom: 4pt; color: #111111;
}
.callout .attribution {
    font-size: 8.2pt; font-style: normal; color: #333333; margin-top: 5pt; text-align: left;
}
.footer-page {
    position: absolute; bottom: 25pt; width: 100%; left: 0; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #111111;
}
</style>
</head>
<body>
<div class="section-head" style="margin-top: 0;">SYNTHÈSE : L'HORIZON DE LA TRANSFORMATION</div>
<p>Au terme de ces douze étapes, la transformation n'apparaît plus comme un bouleversement violent ni comme un programme bureaucratique de plus. Elle est un <strong>retour au réel</strong>.</p>
<p>Traverser la tour ne consiste pas à détruire l'édifice, mais à en rouvrir les fenêtres et les circulations. Lorsque la subsidiarité devient la règle, que l'évaluation mesure la contribution réelle plutôt que l'obéissance, et que le sommet protège le travail au lieu de le saturer de contrôle, l'organisation cesse d'être une machine à contraindre&nbsp;: elle redevient une communauté productive vivante.</p>
<p>La réussite d'une transition ne se mesure pas au nombre de slides projetées en comité de direction, mais à un indicateur simple et infaillible&nbsp;: <strong>ceux qui fabriquent la valeur retrouvent la fierté et le pouvoir de bien faire leur métier.</strong></p>

<div class="section-head">LES TROIS REPÈRES CARDINAUX DU DIRIGEANT</div>
<ul>
    <li><strong>La subsidiarité absolue&nbsp;:</strong> Toute décision qui peut être prise au contact du terrain doit l'être, sans validation ascendante.</li>
    <li><strong>La protection du temps utile&nbsp;:</strong> Réduire drastiquement le bruit administratif et les réunions pour sanctuariser le temps de travail qualifié.</li>
    <li><strong>L'exemplarité de la lucidité&nbsp;:</strong> Préférer une vérité inconfortable venue du sol à un reporting rassurant mais déconnecté.</li>
</ul>

<div class="callout">
    <div class="callout-title">▌ VOIX DU SOMMET</div>
    <p>«&nbsp;Conduire une transition managériale n'est pas un acte de rébellion&nbsp;: c'est un acte de fidélité profonde à ce qui fait la grandeur de l'entreprise. En remettant le pouvoir d'agir entre les mains de ceux qui savent faire le travail, nous redonnons du sens à notre travail de dirigeants et nous construisons des organisations solides, pérennes et fières de leur utilité collective.&nbsp;»</p>
    <div class="attribution">— Directeur Général Adjoint, groupe bancaire mutualiste</div>
</div>

<div class="footer-page">119</div>
</body>
</html>'''

pdf_p119 = os.path.join(SCRATCH, 'new_p119.pdf')
render_html_to_pdf(html_p119, pdf_p119)

# ----------------------------------------------------
# 4. PAGES 84 À 87 : LES PREUVES QUE ÇA MARCHE (4 PAGES COMPLÈTES ET ENRICHIES)
# ----------------------------------------------------
css_preuves_common = '''
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Montserrat:wght@600;700;800&display=swap');
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; padding: 34.8pt 33.8pt 45pt 33.8pt;
    font-family: 'Lora', Georgia, serif; color: #111111; background: #ffffff;
    position: relative; -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}
.title-header { text-align: center; margin-bottom: 16pt; margin-top: 5pt; }
.title-header h1 {
    font-family: 'Montserrat', sans-serif; font-size: 11pt; font-weight: 700;
    letter-spacing: 0.6px; text-transform: uppercase; color: #000000; margin-bottom: 6pt;
}
.title-header .rule { width: 100%; height: 1px; background-color: #000000; margin-bottom: 8pt; }
.title-header h2 {
    font-family: 'Lora', Georgia, serif; font-size: 9.15pt; font-weight: 400;
    font-style: italic; color: #333333; line-height: 1.35;
}
p {
    font-size: 9.15pt; line-height: 13.5pt; text-align: justify; margin-bottom: 6.5pt; color: #111111;
    hyphens: auto; -webkit-hyphens: auto;
}
.section-head {
    font-family: 'Montserrat', sans-serif; font-size: 9.2pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; color: #000000;
    margin-top: 13pt; margin-bottom: 5pt;
}
table { width: 100%; border-collapse: collapse; margin: 6pt 0 10pt 0; font-size: 8.2pt; }
th {
    font-family: 'Montserrat', sans-serif; font-size: 7.2pt; font-weight: 700;
    text-transform: uppercase; padding: 6pt 5pt; text-align: left;
    border-top: 1.5px solid #000000; border-bottom: 1px solid #000000; color: #000000; line-height: 1.25;
}
td { padding: 6pt 5pt; border-bottom: 1px solid #e5e5e5; color: #111111; font-family: 'Lora', Georgia, serif; }
tr:last-child td { border-bottom: none; }
.callout {
    background-color: #f8f8f8; border-left: 3px solid #000000; padding: 8pt 10pt; margin: 10pt 0;
}
.callout-title {
    font-family: 'Montserrat', sans-serif; font-size: 7.8pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.4px; margin-bottom: 4pt; color: #000000;
}
.callout p {
    font-size: 8.5pt; font-style: italic; line-height: 1.38; margin-bottom: 0; color: #222222;
}
.footer-page {
    position: absolute; bottom: 25pt; width: 100%; left: 0; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #111111;
}
ul { margin-left: 14pt; margin-bottom: 8pt; }
li { font-size: 9pt; line-height: 13.5pt; margin-bottom: 4pt; color: #111111; font-family: 'Lora', Georgia, serif; }
li strong { font-family: 'Montserrat', sans-serif; font-size: 8pt; color: #000000; text-transform: uppercase; }
'''

html_p84 = f'''<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{css_preuves_common}</style></head>
<body>
<div class="title-header">
    <h1>LES PREUVES QUE ÇA MARCHE</h1>
    <div class="rule"></div>
    <h2>Données empiriques et retours sur investissement</h2>
</div>
<p>Ce chapitre ne relève pas d'une idéologie militante : il s'appuie sur la rigueur des bilans économiques. Les organisations qui ont fait le choix de la souveraineté locale et de la confiance ne sont pas des utopies fragiles — elles surperforment durablement leurs concurrents traditionnels.</p>
<p>Selon l'étude menée par Gary Hamel (Harvard Business Review), l'excès de reporting et les strates managériales intermédiaires pèsent en moyenne <strong>20 % du total de la masse salariale</strong> en pure friction administrative. En France, l'Institut Sapiens évalue le coût du désengagement à <strong>14 500 € par an et par salarié</strong>. Voici les preuves chiffrées analysées à travers le prisme du décideur :</p>
<div class="section-head">1. BUURTZORG — LA PERFORMANCE PAR L'AUTONOMIE</div>
<p style="margin-bottom: 1.5mm;">Réseau de soins de 15 000 soignants autonomes, sans aucun management intermédiaire :</p>
<table>
    <tr>
        <th style="width: 38%;">INDICATEUR DE PERFORMANCE</th>
        <th style="width: 32%;">MODÈLE HIÉRARCHIQUE CLASSIQUE</th>
        <th style="width: 30%;">MODÈLE BUURTZORG</th>
    </tr>
    <tr><td>Coût global par patient</td><td>Base 100 %</td><td><strong>- 40 %</strong></td></tr>
    <tr><td>Taux d'absentéisme</td><td>7 % à 10 %</td><td><strong>&lt; 3 %</strong></td></tr>
    <tr><td>Rotation des effectifs (Turnover)</td><td>15 % à 25 %</td><td><strong>&lt; 5 %</strong></td></tr>
    <tr><td>Coûts administratifs & contrôle</td><td>20 % à 25 % du budget</td><td><strong>&lt; 8 %</strong></td></tr>
</table>
<div class="callout">
    <div class="callout-title">LECTURE STRATÉGIQUE DU COMPTE DE RÉSULTATS</div>
    <p>Ce résultat provient de l'élimination pure et simple des strates bureaucratiques. L'audit indépendant mené par Ernst & Young a mesuré une économie nette de 33 % pour la sécurité sociale, tout en garantissant des soignants 100 % disponibles pour les soins réels.</p>
</div>
<div class="footer-page">84</div>
</body></html>'''

html_p85 = f'''<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{css_preuves_common}</style></head>
<body>
<div class="section-head" style="margin-top: 0;">2. W.L. GORE — LE GÉANT MONDIAL SANS CHEF</div>
<p>Multinationale industrielle de pointe de 13&nbsp;000 associés et 4,5 milliards de dollars de chiffre d'affaires, organisée depuis 1958 en structure horizontale sans hiérarchie classique :</p>
<ul>
    <li><strong>65 ans de rentabilité ininterrompue :</strong> Rentable chaque année depuis plus de six décennies, avec un portefeuille mondial de plus de 2&nbsp;000 brevets (Gore-Tex, prothèses vasculaires, câbles aérospatiaux).</li>
    <li><strong>Plafonnement à 150 personnes par unité :</strong> Dès qu'une usine dépasse le seuil de 150 personnes (nombre de Dunbar), une nouvelle unité autonome est créée pour préserver les relations directes de confiance.</li>
    <li><strong>Zéro hiérarchie imposée :</strong> Aucun titre officiel, pas de chaîne de commandement militaire. Les leaders émergent par adhésion volontaire des pairs (<em>followership</em>) et les rémunérations sont fixées par évaluation croisée à 360°.</li>
</ul>
<div class="callout">
    <div class="callout-title">CE QUE LE SOMMET DOIT RETENIR</div>
    <p>Supprimer les strates de contrôle n'affaiblit pas la rigueur : Gore démontre depuis six décennies qu'une organisation industrielle de pointe peut opérer au plus haut niveau technologique sans aucune bureaucratie pyramidale.</p>
</div>
<div class="section-head">3. LES MODÈLES COOPÉRATIFS & PARTICIPATIFS (SCOP)</div>
<p>Les données statistiques nationales démontrent que le taux de pérennité à 5 ans des structures coopératives est supérieur de <strong>plus de 20 %</strong> à celui des entreprises conventionnelles.</p>
<p>En période de récession, ces structures ne licencient pas : elles arbitrent collégialement (baisse temporaire de salaires, réaffectation interne), préservent leur savoir-faire clé et redémarrent deux fois plus vite lors de la reprise économique.</p>
<div class="footer-page">85</div>
</body></html>'''

html_p86 = f'''<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{css_preuves_common}</style></head>
<body>
<div class="section-head" style="margin-top: 0;">4. MONDRAGON — LA PREUVE DU CHANGEMENT D'ÉCHELLE</div>
<p>L'objection rituelle du sommet (<em>« Cela ne fonctionne que pour de petites PME d'atelier »</em>) est pulvérisée par les faits économiques :</p>
<ul>
    <li><strong>80 000 salariés-propriétaires :</strong> 256 entreprises coopératives fédérées dans l'industrie lourde, la banque et la grande distribution.</li>
    <li><strong>11 milliards d'euros de chiffre d'affaires :</strong> Premier groupe industriel du Pays basque espagnol, fondé en 1956 et rentable depuis sept décennies.</li>
    <li><strong>Ratio salarial strictement borné de 1 à 6 :</strong> Le directeur général gagne au maximum 6 fois le salaire du plus bas échelon (contre 1 à 400 dans le CAC 40). Ce ratio garantit qu'aucune décision ne sacrifie la base pour gonfler un bonus de direction à court terme.</li>
</ul>
<div class="section-head">5. L'OPEN SOURCE — LA COORDINATION SANS PYRAMIDE</div>
<p>Linux fait tourner <strong>90 % des serveurs cloud mondiaux</strong> et équipe la totalité des smartphones Android. Wikipedia est la plus grande encyclopédie vivante de l'humanité. Git, Apache, PostgreSQL — les fondations de l'économie numérique ont été créées sans vice-présidents, sans Town Halls millimétrés et sans comités de cadrage.</p>
<p>Cette réussite planétaire apporte une démonstration implacable : la coordination à grande échelle n'exige pas de hiérarchie pyramidale. Elle exige de la transparence, des règles d'arbitrage claires et la compétence reconnue par les pairs.</p>
<div class="footer-page">86</div>
</body></html>'''

html_p87 = f'''<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{css_preuves_common}</style></head>
<body>
<div class="section-head" style="margin-top: 0;">CE QUE L'HISTOIRE ENSEIGNE : LES PIÈGES ET LES DÉRIVES RÉELLES</div>
<p>L'honnêteté intellectuelle impose de regarder les revers avec la même rigueur que les succès. L'autonomie n'est ni magique ni immunisée contre les lois économiques. Les pionniers eux-mêmes ont traversé des crises sévères dont le dirigeant doit tirer les leçons :</p>
<ul>
    <li><strong>Le piège du départ du leader (Cas FAVI) :</strong> L'autonomie chez FAVI reposait largement sur le charisme et la protection personnelle de Jean-François Zobrist. Après son départ en retraite, la gouvernance n'ayant pas verrouillé statutairement l'organisation, les réflexes de contrôle et les tableaux de bord sont progressivement réapparus. <em>Leçon :</em> Une transformation qui repose sur un homme est fragile ; elle doit être sanctuarisée dans les statuts juridiques et les règles de gouvernance.</li>
    <li><strong>L'illusion de l'immunité au marché (Cas Mondragon) :</strong> En 2013, la faillite retentissante de Fagor Electrodomésticos (filiale historique de Mondragon) a démontré que l'autogestion ne protège ni des erreurs d'investissement industriel ni de la concurrence mondiale à bas coûts. <em>Leçon :</em> La subsidiarité optimise l'exécution et l'engagement, mais elle n'exonère jamais le sommet d'une vision stratégique lucide.</li>
    <li><strong>La tyrannie du flou et la pression des pairs :</strong> Supprimer la hiérarchie formelle sans définir de règles d'arbitrage explicites ne libère pas le terrain : cela crée une hiérarchie informelle, opaque et parfois plus brutale (culte du consensus, culpabilisation mutuelle). <em>Leçon :</em> Moins de chefs exige des règles du jeu encore plus claires.</li>
</ul>

<div class="callout" style="margin-top: 10pt;">
    <div class="callout-title">LE PRINCIPE DU SOMMET</div>
    <p>L'autonomie n'est pas l'absence de structure : c'est une structure conçue pour servir le réel plutôt que pour rassurer le siège. Les erreurs des pionniers ne condamnent pas le modèle ; elles en tracent le mode d'emploi pour les dirigeants d'aujourd'hui.</p>
</div>

<div class="footer-page">87</div>
</body></html>'''

# Render replacement / new pages
print("Rendering generated pages via Headless Chrome...")
render_html_to_pdf(html_p4, os.path.join(SCRATCH, 'new_p4.pdf'))
render_html_to_pdf(html_p5, os.path.join(SCRATCH, 'new_p5.pdf'))
render_html_to_pdf(html_p53, os.path.join(SCRATCH, 'new_p53.pdf'))
render_html_to_pdf(html_p60, os.path.join(SCRATCH, 'new_p60.pdf'))
render_html_to_pdf(html_p61, os.path.join(SCRATCH, 'new_p61.pdf'))
render_html_to_pdf(html_p84, os.path.join(SCRATCH, 'new_p84.pdf'))
render_html_to_pdf(html_p85, os.path.join(SCRATCH, 'new_p85.pdf'))
render_html_to_pdf(html_p86, os.path.join(SCRATCH, 'new_p86.pdf'))
render_html_to_pdf(html_p87, os.path.join(SCRATCH, 'new_p87.pdf'))
print("✅ Replacement pages rendered!")

# ----------------------------------------------------
# 5. ASSEMBLAGE ET SHIFT DU CÔTÉ SOMMET
# ----------------------------------------------------
src_sommet = fitz.open('/Users/basile/Desktop/Les-9-etages/sommet_clean_base.pdf')
new_sommet = fitz.open()

print("Building newly assembled Sommet PDF...")

# Pages 1..2 (Indices 0..1)
new_sommet.insert_pdf(src_sommet, from_page=0, to_page=1)

# Page 3 : Placeholder for TOC (we will insert final TOC at index 2 later)
# Let's insert a dummy page for now
dummy_toc = fitz.open(os.path.join(SCRATCH, 'new_p53.pdf'))
new_sommet.insert_pdf(dummy_toc, from_page=0, to_page=0)

# Pages 4..5 : New Complete Prologue (No abrupt cut, full Theater, Hospital, Restaurant, Chantier, Conclusion)
p4_doc = fitz.open(os.path.join(SCRATCH, 'new_p4.pdf'))
p5_doc = fitz.open(os.path.join(SCRATCH, 'new_p5.pdf'))
new_sommet.insert_pdf(p4_doc, from_page=0, to_page=0)
new_sommet.insert_pdf(p5_doc, from_page=0, to_page=0)

# Pages 6..21 from src_sommet (Indices 5..20)
new_sommet.insert_pdf(src_sommet, from_page=5, to_page=20)

# Page 22 : Clean Single-Layer Bilan Étage 6
p22_doc = fitz.open(os.path.join(SCRATCH, 'new_p22.pdf'))
new_sommet.insert_pdf(p22_doc, from_page=0, to_page=0)

# Pages 23..52 (Indices 22..51)
new_sommet.insert_pdf(src_sommet, from_page=22, to_page=51)

# Page 53 : New Quote Deming
p53_doc = fitz.open(os.path.join(SCRATCH, 'new_p53.pdf'))
new_sommet.insert_pdf(p53_doc, from_page=0, to_page=0)

# Pages 54..59 (Indices 53..58)
new_sommet.insert_pdf(src_sommet, from_page=53, to_page=58)

# Page 60 (gauche) : Infographie 3 200 milliards $ (src_sommet[61])
# Page 61 (droite) : Titre Partie II Les Leviers (src_sommet[62])
# La page de souffle (citation Max De Pree) est supprimée pour positionner directement l'infographie en page 60 et les leviers en page 61

# Page 60 (gauche) : Infographie 3 200 milliards $ (src_sommet[61])
new_sommet.insert_pdf(src_sommet, from_page=61, to_page=61)

# Page 61 (droite) : Titre Partie II Les Leviers format Option A (new_p61.pdf)
p61_doc = fitz.open(os.path.join(SCRATCH, 'new_p61.pdf'))
new_sommet.insert_pdf(p61_doc, from_page=0, to_page=0)

# Pages 62..71 from src_sommet (Indices 63..71: Ce que gouverner jusqu'à Pourquoi le système résiste)
new_sommet.insert_pdf(src_sommet, from_page=63, to_page=71)

# Page 73 : New Enriched Conclusion & Decision Grid
p73_doc = fitz.open(os.path.join(SCRATCH, 'new_p73.pdf'))
new_sommet.insert_pdf(p73_doc, from_page=0, to_page=0)

# Pages 74..82 (Indices 73..81)
new_sommet.insert_pdf(src_sommet, from_page=73, to_page=81)

# Page 83 : Clean Conclusion of Et si ? (no duplicate of p.69)
p83_doc = fitz.open(os.path.join(SCRATCH, 'new_p83.pdf'))
new_sommet.insert_pdf(p83_doc, from_page=0, to_page=0)

# Pages 84..87 : New 4-page Preuves Section
p84_doc = fitz.open(os.path.join(SCRATCH, 'new_p84.pdf'))
p85_doc = fitz.open(os.path.join(SCRATCH, 'new_p85.pdf'))
p86_doc = fitz.open(os.path.join(SCRATCH, 'new_p86.pdf'))
p87_doc = fitz.open(os.path.join(SCRATCH, 'new_p87.pdf'))

new_sommet.insert_pdf(p84_doc, from_page=0, to_page=0)
new_sommet.insert_pdf(p85_doc, from_page=0, to_page=0)
new_sommet.insert_pdf(p86_doc, from_page=0, to_page=0)
new_sommet.insert_pdf(p87_doc, from_page=0, to_page=0)

# Shift starts at index 87 (page 88)
shift_start_idx = len(new_sommet)

# Pages 86..116 from src_sommet (Indices 85..115) -> Pages 88..118
new_sommet.insert_pdf(src_sommet, from_page=85, to_page=115)

# Page 119 : New Conclusion of Guide Tactique & Voix du Sommet
p119_doc = fitz.open(os.path.join(SCRATCH, 'new_p119.pdf'))
new_sommet.insert_pdf(p119_doc, from_page=0, to_page=0)

# Pages 118..121 from src_sommet (Indices 117..120 : Grille, Calendrier 90 jours, Premier Pas 8 micro-actes)
new_sommet.insert_pdf(src_sommet, from_page=117, to_page=120)

# We omit indices 121..122 ("Le Plan de Transformation") which was an exact duplicate of "Le Premier Pas"!
# Pages 124..129 from src_sommet (Indices 123..128 : Feuille de route 18 mois, Hall central, Sources, Padlet)
new_sommet.insert_pdf(src_sommet, from_page=123, to_page=len(src_sommet)-1)

print(f"Intermediate Sommet page count: {len(new_sommet)} pages")

# Update page number footer on shifted pages (88 to 131)
for p_idx in range(shift_start_idx, len(new_sommet)):
    page_num = p_idx + 1
    page = new_sommet[p_idx]
    # Redact / cover previous page number
    # Footers are centered around x=210, y=555..585
    rect = fitz.Rect(180, 555, 240, 585)
    page.draw_rect(rect, color=None, fill=(1, 1, 1))
    # Write new page number
    # Use Helvetica font
    text = str(page_num)
    page.insert_textbox(
        rect,
        text,
        fontsize=8.5,
        fontname="helv",
        color=(0.44, 0.44, 0.48),
        align=fitz.TEXT_ALIGN_CENTER
    )

# ----------------------------------------------------
# 5.5. ENRICHISSEMENT ET HARMONISATION VISUELLE DES PAGES DE FIN D'ÉTAGE (SOMMET)
# ----------------------------------------------------
print("Enriching floor ending pages (16, 22, 28, 34, 40, 52, 58) with full-height structured layout & 'LES SIGNAUX D'ALERTE DU SOCLE'...")

enriched_pages_data = {
    16: {
        'page_num': 16,
        'traducteur_th': ('Ce que le conseil valide en séance', 'Ce que les salariés vivent dans les territoires'),
        'traducteur_rows': [
            ('«&nbsp;Amélioration du ratio d\'efficience opérationnelle.&nbsp;»', 'Moins de personnel pour absorber une charge de travail identique.'),
            ('«&nbsp;Recentrage stratégique sur le cœur de métier.&nbsp;»', 'Fermeture ou cession d\'activités historiques pourtant rentables.'),
            ('«&nbsp;Renforcement des exigences de conformité globale.&nbsp;»', 'Alourdissement des démarches administratives pour les équipes de terrain.')
        ],
        'saviez_vous': 'Selon les analyses historiques du cabinet Proxinvest, le ratio moyen entre la rémunération globale des présidents de conseils du SBF 120 et le salaire moyen de leurs salariés est passé de 1 à 15 dans les années 1980 à près de 1 à 90 aujourd\'hui.',
        'question': '«&nbsp;Dans les choix stratégiques soumis à votre arbitrage, quelle part accordez-vous à la réalité vécue par les femmes et les hommes qui font tourner l\'entreprise au quotidien, par rapport aux seules exigences du cours de bourse&nbsp;?&nbsp;»',
        'signaux': [
            ('L\'évaporation de l\'expérience métier', 'départs silencieux des techniciens et artisans indispensables, jamais répertoriés dans les indicateurs financiers du trimestre.'),
            ('La bureaucratie défensive', 'multiplication des comités de validation pour couvrir juridiquement les administrateurs au détriment de l\'agilité réelle des équipes.'),
            ('Le découplage de la gouvernance', 'des délibérations guidées par des ratios boursiers abstraits tandis que les infrastructures locales se dégradent en silence.')
        ]
    },
    22: {
        'page_num': 22,
        'traducteur_th': ('Ce que le siège mondial décide', 'Ce que les filiales locales affrontent'),
        'traducteur_rows': [
            ('«&nbsp;Déploiement d\'un système unique de gestion mondiale.&nbsp;»', 'Paralysie des livraisons due aux spécificités fiscales locales non intégrées.'),
            ('«&nbsp;Harmonisation internationale des processus d\'achat.&nbsp;»', 'Impossibilité d\'acheter des pièces détachées d\'urgence chez des fournisseurs locaux.'),
            ('«&nbsp;Alignement des politiques managériales globales.&nbsp;»', 'Bricolages informatiques clandestins des équipes terrain pour contourner les blocages.')
        ],
        'saviez_vous': 'Les études en management international démontrent que les projets de standardisation descendante échouent massivement à générer les gains prévus, contournés systématiquement par l\'ingéniosité clandestine des équipes locales pour maintenir la production.',
        'question': '«&nbsp;Vos politiques de standardisation globale laissent-elles aux équipes locales l\'espace nécessaire pour s\'adapter à la réalité de leur terrain, ou imposent-elles une uniformité qui détruit l\'intelligence collective&nbsp;?&nbsp;»',
        'signaux': [
            ('La prolifération des fichiers clandestins', 'chaque filiale recrée ses propres outils sous le manteau pour compenser les lacunes du système central.'),
            ('L\'étouffement des contextes culturels', 'application aveugle de normes conçues au siège, en contradiction frontale avec les usages commerciaux du pays.'),
            ('La fuite des compétences locales', 'les meilleurs managers régionaux démissionnent face à la perte totale d\'autonomie décisionnelle.')
        ]
    },
    28: {
        'page_num': 28,
        'traducteur_th': ('Ce que le dirigeant déclare lors du Town Hall', 'Ce que les salariés ressentent dans les services'),
        'traducteur_rows': [
            ('«&nbsp;L\'inclusion et la diversité sont au cœur de nos valeurs.&nbsp;»', '«&nbsp;Conformez-vous au moule managérial si vous voulez progresser.&nbsp;»'),
            ('«&nbsp;Nous devons faire preuve d\'agilité collective.&nbsp;»', '«&nbsp;Vous allez devoir travailler plus vite avec moins de ressources.&nbsp;»'),
            ('«&nbsp;Le dialogue direct et authentique est notre priorité.&nbsp;»', '«&nbsp;Posez uniquement des questions filtrées lors des webinaires.&nbsp;»')
        ],
        'saviez_vous': 'D\'après le Baromètre LGBT+ au travail (L\'Autre Cercle / IFOP, 2022), 1 salarié LGBT+ sur 2 déclare encore ne pas être visible au travail par crainte d\'un impact sur sa carrière ou de micro-discriminations. Dans la tour, la célébration publique de la diversité masque trop souvent une injonction feutrée au conformisme managérial absolu.',
        'question': '«&nbsp;Vos chartes d\'inclusion et de diversité célèbrent-elles la singularité humaine réelle de vos équipes, ou servent-elles de paravent éthique à une organisation qui broie toute divergence&nbsp;?&nbsp;»',
        'signaux': [
            ('Le plafond de verre du conformisme', 'l\'obligation tacite d\'adopter le même langage, les mêmes codes et la même posture pour espérer gravir les étages.'),
            ('L\'invisibilisation des singularités', 'des collaborateurs contraints de dissimuler des pans entiers de leur identité personnelle par peur de marginalisation.'),
            ('Le cynisme face aux chartes RSE', 'les grandes déclarations d\'ouverture institutionnelle ne suscitent plus que du scepticisme chez les salariés du réel.')
        ]
    },
    34: {
        'page_num': 34,
        'traducteur_th': ('Ce que le VP déclare en comité exécutif', 'Ce qui se passe concrètement sur le terrain'),
        'traducteur_rows': [
            ('«&nbsp;Nous devons optimiser nos coûts d\'achats indirects.&nbsp;»', 'Les équipes manquent d\'outillage, de gants et de consommables de base.'),
            ('«&nbsp;Nous renforçons la gouvernance globale des projets.&nbsp;»', 'Trois nouveaux formulaires de validation administrative à remplir par semaine.'),
            ('«&nbsp;Nous déployons un nouvel outil digital unifié.&nbsp;»', 'Un logiciel lourd qui impose dix clics là où une seconde suffisait.')
        ],
        'saviez_vous': 'Les recherches de la Harvard Business Review sur l\'emploi du temps des dirigeants montrent que ceux-ci passent plus de 70 % de leur temps en réunions de coordination interne, laissant moins de 3 % de leur agenda au contact direct des clients et du terrain.',
        'question': '«&nbsp;Vos comités de validation ont-ils été créés pour accélérer la performance opérationnelle, ou pour diluer la responsabilité individuelle des décideurs&nbsp;?&nbsp;»',
        'signaux': [
            ('La paralysie par la signature', 'des commandes de quelques centaines d\'euros bloquées pendant des semaines dans l\'attente de validations hiérarchiques.'),
            ('La déresponsabilisation des chefs d\'équipe', 'privés de tout pouvoir de décision financière directe pour régler un problème matériel urgent.'),
            ('La dérive bureaucratique des réunions', 'des heures entières passées à justifier des écarts de budget minimes plutôt qu\'à débloquer la production.')
        ]
    },
    40: {
        'page_num': 40,
        'traducteur_th': ('Ce que le directeur de site écrit au siège', 'Ce qui se passe réellement dans l\'usine'),
        'traducteur_rows': [
            ('«&nbsp;Les cadences de production sont conformes au plan.&nbsp;»', 'Les techniciens ont modifié les réglages machines pour éviter la surchauffe.'),
            ('«&nbsp;Le climat social sur le site est stable.&nbsp;»', 'Les salariés sont résignés et compensent la fatigue par solidarité d\'équipe.'),
            ('«&nbsp;Le plan de maintenance préventive est exécuté.&nbsp;»', 'On répare au coup par coup faute de pièces détachées disponibles en stock.')
        ],
        'saviez_vous': 'Selon l\'Enquête Conditions de Travail du Ministère du Travail (DARES), près d\'un cadre sur deux déclare être confronté régulièrement à des ordres ou des exigences contradictoires, plaçant le management intermédiaire dans un écart permanent entre le travail prescrit et le travail réel.',
        'question': '«&nbsp;Combien de dysfonctionnements chroniques sur votre site sont aujourd\'hui masqués par l\'ingéniosité clandestine de vos équipes pour ne pas dégrader vos indicateurs officiels&nbsp;?&nbsp;»',
        'signaux': [
            ('L\'usure physique et morale du collectif', 'des équipes qui tiennent les cadences au détriment de leur santé et de leur sécurité.'),
            ('Le reporting cosmétique', 'des indicateurs délibérément ajustés pour satisfaire les attentes du siège sans refléter l\'état réel du parc machine.'),
            ('L\'effondrement de la maintenance préventive', 'le report constant des arrêts techniques indispensables pour ne pas impacter les volumes du mois.')
        ]
    },
    52: {
        'page_num': 52,
        'traducteur_th': ('Ce que le chef d\'équipe dit à son responsable', 'Ce qu\'il dit ensuite à ses gars dans l\'atelier'),
        'traducteur_rows': [
            ('«&nbsp;Bien noté pour les nouveaux objectifs du trimestre.&nbsp;»', '«&nbsp;Les gars, on fait comme d\'habitude, mais on fait gaffe aux audits.&nbsp;»'),
            ('«&nbsp;Je vais sensibiliser l\'équipe à la saisie des temps.&nbsp;»', '«&nbsp;Remplissez le tableau vite fait vendredi à 16h pour qu\'ils nous lâchent.&nbsp;»'),
            ('«&nbsp;Nous participons activement à la démarche qualité.&nbsp;»', '«&nbsp;Faites ce que vous savez faire de mieux&nbsp;: du bon boulot propre.&nbsp;»')
        ],
        'saviez_vous': 'Selon les études de l\'APEC sur les aspirations des cadres, seuls 34 % d\'entre eux souhaitent aujourd\'hui exercer des responsabilités managériales, les deux tiers refusant d\'endosser ce rôle en raison de la surcharge administrative et du manque d\'autonomie opérationnelle.',
        'question': '«&nbsp;Donnez-vous à vos managers de proximité les moyens réels et l\'autonomie nécessaires pour protéger leurs équipes des absurdités administratives, ou les transformez-vous en simples exécutants du contrôle hiérarchique&nbsp;?&nbsp;»',
        'signaux': [
            ('Le refus des promotions internes', 'les ouvriers et techniciens les plus compétents refusent catégoriquement de devenir chefs d\'équipe.'),
            ('Le rôle d\'amortisseur épuisant', 'des managers de terrain pris en tenaille entre des directives inapplicables et la réalité du travail de leurs équipes.'),
            ('Le sentiment d\'abandon hiérarchique', 'l\'impression constante de devoir porter seul la responsabilité des dysfonctionnements du système.')
        ]
    },
    58: {
        'page_num': 58,
        'traducteur_th': ('Ce que le sommet pensait avant de descendre', 'Ce que le sommet découvre au niveau zéro'),
        'traducteur_rows': [
            ('«&nbsp;Les équipes appliquent les processus que nous concevons.&nbsp;»', 'Les équipes passent leur journée à contourner des processus inadaptés.'),
            ('«&nbsp;Les réunions et les reportings améliorent la qualité.&nbsp;»', 'Les réunions privent les équipes du temps nécessaire pour bien faire le travail.'),
            ('«&nbsp;L\'autorité vient du titre sur l\'organigramme.&nbsp;»', 'L\'autorité réelle se gagne par l\'écoute, le soutien et la compétence démontrée.')
        ],
        'saviez_vous': 'Selon l\'étude mondiale Gallup sur l\'engagement au travail (State of the Global Workplace, 2024), seuls 7 % des salariés français se déclarent activement engagés dans leur travail, plaçant la France au 38e rang sur 38 pays européens. La première cause citée est le sentiment d\'inutilité administrative.',
        'question': '«&nbsp;Si l\'ensemble de votre état-major prenait un mois de congé sabbatique, vos équipes opérationnelles continueraient à livrer vos clients. Mais si vos équipes de terrain s\'arrêtaient une seule journée, que resterait-il de votre organisation&nbsp;?&nbsp;»',
        'signaux': [
            ('La lucidité absolue du terrain', 'les opérationnels savent exactement comment simplifier l\'organisation, mais personne ne leur pose la question.'),
            ('La fin de l\'illusion technocratique', 'la preuve tangible que la valeur est créée au socle, et non dans l\'empilement des strates de contrôle.'),
            ('L\'urgence de la subsidiarité', 'le besoin vital de redonner le pouvoir d\'arbitrage à ceux qui font face quotidiennement aux conséquences réelles.')
        ]
    }
}

enriched_page_template = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400;1,700&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
<style>
@page {{ size: 420pt 595.92pt; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 34.8pt 33.75pt 30pt 33.75pt;
    font-family: 'Lora', Georgia, serif; font-size: 9.15pt; line-height: 13.5pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}}
.section-title {{
    font-family: 'Montserrat', sans-serif; font-size: 9.2pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; color: #000000;
    margin-bottom: 7pt; display: flex; align-items: center;
}}
.symbol {{
    display: inline-block; width: 3.8pt; height: 9.8pt; background-color: #000000;
    margin-right: 5pt; flex-shrink: 0;
}}
table {{
    width: 100%; border-collapse: collapse; margin-bottom: 11pt; font-size: 8.2pt;
}}
th {{
    font-family: 'Montserrat', sans-serif; font-size: 7pt; font-weight: 700;
    text-transform: uppercase; padding: 5pt 5pt; text-align: left;
    border-top: 1.2pt solid #000000; border-bottom: 0.8pt solid #000000; color: #000000; line-height: 1.25;
}}
td {{
    padding: 5pt 5pt; border-bottom: 0.6pt solid #e5e5e5; color: #111111;
    font-family: 'Lora', Georgia, serif; line-height: 11.8pt;
}}
tr:last-child td {{ border-bottom: none; }}
p.body-text {{
    font-size: 9.15pt; line-height: 13.5pt; text-align: justify; text-justify: inter-word;
    color: #222222; margin-bottom: 9pt;
}}
.callout {{
    width: 100%; background-color: #f8f8f8; border-left: 3.5px solid #000000;
    padding: 8pt 10pt; margin-bottom: 9pt;
}}
.callout-title {{
    font-family: 'Montserrat', sans-serif; font-size: 8.4pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.4px; margin-bottom: 4pt; color: #000000;
}}
.callout p {{
    font-size: 9.15pt; font-style: italic; line-height: 13.5pt; color: #111111;
    text-align: justify; margin: 0;
}}
.synthesis-block {{
    margin-top: 3pt;
}}
.synthesis-title {{
    font-family: 'Montserrat', sans-serif; font-size: 8.8pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; color: #000000;
    margin-bottom: 6pt; display: flex; align-items: center;
}}
ul.signals {{
    list-style: none; margin: 0; padding: 0;
}}
ul.signals li {{
    font-size: 9.15pt; line-height: 13.5pt; color: #222222; position: relative;
    padding-left: 11pt; margin-bottom: 4pt; text-align: justify;
}}
ul.signals li::before {{
    content: '•'; position: absolute; left: 0; color: #000000; font-weight: 700;
}}
.page-number {{
    position: absolute; bottom: 24pt; left: 0; width: 100%; text-align: center;
    font-family: 'Lora', Georgia, serif; font-size: 8.5pt; color: #666666;
}}
</style>
</head>
<body>

<div class="section-title"><span class="symbol"></span>LE TRADUCTEUR DU SOMMET</div>
<table>
    <thead>
        <tr>
            <th style="width: 50%;">{th0}</th>
            <th style="width: 50%;">{th1}</th>
        </tr>
    </thead>
    <tbody>
{rows_html}
    </tbody>
</table>

<div class="section-title"><span class="symbol"></span>LE SAVIEZ-VOUS&nbsp;?</div>
<p class="body-text">{saviez_vous}</p>

<div class="callout">
    <div class="callout-title">▌ LA QUESTION DU SOMMET</div>
    <p>{question}</p>
</div>

<div class="synthesis-block">
    <div class="synthesis-title"><span class="symbol"></span>LES SIGNAUX D'ALERTE DU SOCLE</div>
    <ul class="signals">
{signals_html}
    </ul>
</div>

<div class="page-number">{page_num}</div>

</body>
</html>"""

# Render each enriched page
for pno, data in enriched_pages_data.items():
    rows_html = ''
    for r0, r1 in data['traducteur_rows']:
        rows_html += f'        <tr>\n            <td>{r0}</td>\n            <td>{r1}</td>\n        </tr>\n'
    signals_html = ''
    for s_title, s_desc in data['signaux']:
        signals_html += f'        <li><strong>{s_title}</strong>&nbsp;: {s_desc}</li>\n'
    
    html = enriched_page_template.format(
        th0=data['traducteur_th'][0],
        th1=data['traducteur_th'][1],
        rows_html=rows_html.rstrip(),
        saviez_vous=data['saviez_vous'],
        question=data['question'],
        signals_html=signals_html.rstrip(),
        page_num=data['page_num']
    )
    
    html_path = os.path.join(SCRATCH, f'page_{pno}_enriched.html')
    pdf_path = os.path.join(SCRATCH, f'page_{pno}_enriched.pdf')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    subprocess.run([
        CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
        f'--print-to-pdf={pdf_path}', html_path
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Redact original page in new_sommet and replace with rendered PDF
    target_page = new_sommet[pno - 1]
    target_page.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
    target_page.apply_redactions()
    
    enriched_doc = fitz.open(pdf_path)
    target_page.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), enriched_doc, 0)
    print(f"Applied full enriched layout to Sommet page {pno}")

# For pages 10 and 46 (which have DONNÉES D'ÉTAGE at top and are already full), harmonize callout box only:
dense_callouts = {
    10: {
        "y_start": 454.0, "height": 72.0, "clean_rect": fitz.Rect(30, 448, 390, 540),
        "text": "«&nbsp;Quand avez-vous, pour la dernière fois, passé deux heures complètes à observer le travail d'une équipe opérationnelle sans que votre présence ait été annoncée et scénarisée trois semaines à l'avance&nbsp;?&nbsp;»"
    },
    46: {
        "y_start": 454.0, "height": 72.0, "clean_rect": fitz.Rect(30, 448, 390, 540),
        "text": "«&nbsp;Quelle proportion de votre temps de travail hebdomadaire est consacrée à des tâches d'auto-justification administrative plutôt qu'au soutien concret de vos équipes sur leurs priorités réelles&nbsp;?&nbsp;»"
    }
}

for pno, info in dense_callouts.items():
    page = new_sommet[pno - 1]
    page.add_redact_annot(info["clean_rect"], fill=(1, 1, 1))
    page.apply_redactions()
    h_pt = info["height"]
    html_box = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;1,400&family=Montserrat:wght@700&display=swap');
@page {{ size: 352.4pt {h_pt}pt; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
    width: 352.4pt; height: {h_pt}pt;
    font-family: 'Lora', Georgia, serif;
    background: #ffffff;
    -webkit-font-smoothing: antialiased;
}}
.callout {{
    width: 100%;
    background-color: #f8f8f8;
    border-left: 3.5px solid #000000;
    padding: 8pt 11pt;
}}
.callout-title {{
    font-family: 'Montserrat', sans-serif;
    font-size: 8.5pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4pt;
    color: #000000;
}}
.callout p {{
    font-family: 'Lora', Georgia, serif;
    font-size: 8.8pt;
    font-style: italic;
    line-height: 1.38;
    color: #111111;
    text-align: justify;
}}
</style>
</head>
<body>
<div class="callout">
    <div class="callout-title">▌ LA QUESTION DU SOMMET</div>
    <p>{info["text"]}</p>
</div>
</body>
</html>'''
    temp_html = os.path.join(SCRATCH, f'temp_box_p{pno}.html')
    box_pdf = os.path.join(SCRATCH, f'box_p{pno}.pdf')
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_box)
    subprocess.run([
        CHROME,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={box_pdf}',
        temp_html
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    box_doc = fitz.open(box_pdf)
    target_rect = fitz.Rect(33.8, info["y_start"], 33.8 + 352.4, info["y_start"] + h_pt)
    page.show_pdf_page(target_rect, box_doc, 0)

# Patch Sommet Page 50 : LA QUESTION INTERDITE -> ▌ LA QUESTION INTERDITE
p50 = new_sommet[49]
p50.add_redact_annot(fitz.Rect(30.0, 30.0, 380.0, 50.0), fill=(1, 1, 1))
p50.apply_redactions()
html_p50_title = '''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
@page { size: 340pt 20pt; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
body { width: 340pt; height: 20pt; background: #ffffff; font-family: 'Montserrat', sans-serif; font-size: 9.6pt; font-weight: 700; color: #000000; letter-spacing: 0.3px; line-height: 20pt; -webkit-font-smoothing: antialiased; }
</style></head><body>▌ LA QUESTION INTERDITE : LE DROIT DE REDESCENDRE</body></html>'''
temp_p50_title = os.path.join(SCRATCH, 'temp_p50_title.html')
pdf_p50_title = os.path.join(SCRATCH, 'title_p50.pdf')
with open(temp_p50_title, 'w', encoding='utf-8') as f:
    f.write(html_p50_title)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p50_title}', temp_p50_title
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
title_doc_p50 = fitz.open(pdf_p50_title)
p50.show_pdf_page(fitz.Rect(33.75, 30.0, 33.75 + 340.0, 50.0), title_doc_p50, 0)

# Patch Sommet Pages 70 & 71 (suite suppression page de souffle p60) : Mise en page aérée et équilibrée
# Page 70 : Sections 3 et 4 avec conclusion et belle respiration
p71 = new_sommet[69]
p71.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
p71.apply_redactions()

# Page 71 : VOIX DU SOMMET (2 encadrés) + L'ENSEIGNEMENT DU SOMMET
p72 = new_sommet[70]
p72.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
p72.apply_redactions()

html_p71_layout = '''<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400;1,700&family=Montserrat:wght@700&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 34.8pt 33.75pt 30pt 33.75pt;
    font-family: 'Lora', Georgia, serif; font-size: 9.15pt; line-height: 13.5pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}
h2 {
    font-family: 'Montserrat', sans-serif; font-size: 9.6pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; color: #000000;
    margin-bottom: 9.7pt; display: flex; align-items: center;
}
.symbol {
    display: inline-block; width: 4.8pt; height: 9.6pt; background-color: #000000;
    margin-right: 6pt; flex-shrink: 0;
}
p.body-text {
    text-align: justify; text-justify: inter-word; margin-bottom: 0;
    hyphens: auto; -webkit-hyphens: auto;
}
.rule {
    width: 100%; height: 0.75pt; background-color: #000000; margin: 18pt 0;
}
ul.bullets {
    list-style: none; margin: 9.5pt 0 11pt 13.5pt; padding: 0;
}
ul.bullets li {
    font-size: 9.15pt; line-height: 15.5pt; position: relative; padding-left: 10pt;
}
ul.bullets li::before {
    content: '•'; position: absolute; left: 0; font-size: 11pt; line-height: 14pt;
}
.page-number {
    position: absolute; bottom: 23pt; left: 0; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style></head><body>
<h2><span class="symbol"></span>3. LA PRESSION DU CONFORMISME MANAGÉRIAL</h2>
<p class="body-text">Dans les comités de direction, celui qui propose une transformation profonde et authentique reçoit immédiatement trois étiquettes&nbsp;: naïf parce qu'il sous-estimerait la complexité, dangereux parce qu'il déstabiliserait le modèle économique, politique parce qu'il chercherait à capter du pouvoir. Le consensus mou et le statu quo protecteur deviennent alors les stratégies de survie les plus rationnelles.</p>

<div class="rule"></div>

<h2><span class="symbol"></span>4. L'ILLUSION DU CHANGEMENT COSMÉTIQUE</h2>
<p class="body-text">Pour se donner bonne conscience, les grandes organisations multiplient les initiatives de surface&nbsp;:</p>

<ul class="bullets">
    <li>Séminaires de «&nbsp;sensibilisation culturelle&nbsp;»,</li>
    <li>Nomination de coordinateurs de bien-être,</li>
    <li>Hackathons ponctuels et enquêtes de climat interne.</li>
</ul>

<p class="body-text">Ces actions ont un point commun&nbsp;: <strong>elles modifient le vocabulaire mais ne touchent jamais à la répartition réelle du pouvoir. Lancer une réorganisation sans toucher à la subsidiarité revient à repeindre les murs alors qu'il y a une fuite de plomberie&nbsp;: on masque les symptômes sans jamais réparer la tuyauterie.</strong></p>

<div class="page-number">71</div>
</body></html>'''

html_p72_layout = '''<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400;1,700&family=Montserrat:wght@700&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 34.8pt 33.75pt 28pt 33.75pt;
    font-family: 'Lora', Georgia, serif; font-size: 9.0pt; line-height: 13.2pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}
h2 {
    font-family: 'Montserrat', sans-serif; font-size: 9.6pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; color: #000000;
    margin-bottom: 8pt; display: flex; align-items: center;
}
.symbol {
    display: inline-block; width: 4.8pt; height: 9.6pt; background-color: #000000;
    margin-right: 6pt; flex-shrink: 0;
}
.callout {
    background-color: #f8f8f8; border-left: 3.5px solid #000000;
    padding: 9pt 11pt; margin-bottom: 11pt;
}
.callout p.quote {
    font-size: 8.8pt; font-style: italic; line-height: 13.0pt; color: #111111;
    text-align: justify; margin-bottom: 4pt;
    hyphens: auto; -webkit-hyphens: auto;
}
.callout p.author {
    font-size: 8.2pt; font-style: italic; color: #444444; margin-bottom: 0;
}
.rule {
    width: 100%; height: 0.75pt; background-color: #000000; margin: 14pt 0;
}
p.body-text {
    text-align: justify; text-justify: inter-word; margin-bottom: 6pt; font-size: 9.0pt; line-height: 13.2pt;
    hyphens: auto; -webkit-hyphens: auto;
}
.page-number {
    position: absolute; bottom: 23pt; left: 0; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style></head><body>
<h2><span class="symbol"></span>5. LA PROTECTION INVOLONTAIRE DES PROFILS TOXIQUES</h2>
<p class="body-text">C'est le plus grand angle mort du sommet&nbsp;: <strong>la structure pyramidale protège structurellement les personnalités manipulatrices.</strong> Ces profils excellent dans l'art de séduire la hiérarchie en affichant des indicateurs impeccables, tout en exerçant une pression destructrice sur leurs subordonnés à l'abri des regards.</p>
<p class="body-text">Comme le sommet ne jure que par le résultat apparent, il qualifie trop souvent les victimes d'«&nbsp;éléments réfractaires&nbsp;». Selon le Baromètre RH / Theragora (2023), <strong>71 % des salariés victimes de harcèlement moral ne signalent jamais les faits à leur employeur</strong>, convaincus que l'organisation protégera le manager courtisan au détriment de leur parole.</p>

<div class="rule"></div>

<h2><span class="symbol"></span>VOIX DU SOMMET</h2>

<div class="callout">
    <p class="quote">«&nbsp;Nous avons mis deux ans à comprendre qu'un de nos meilleurs directeurs commerciaux — célébré en convention pour ses chiffres records — avait fait démissionner sept collaborateurs de talent. Vue d'en haut, sa rentabilité aveuglait tout le monde.&nbsp;»</p>
    <p class="author">— Membre du Comité de Direction, secteur financier</p>
</div>

<div class="callout" style="margin-bottom: 0;">
    <p class="quote">«&nbsp;Dans la tour, l'inutile et le toxique portent souvent un costume irréprochable et parlent exactement la langue que le siège a envie d'entendre.&nbsp;»</p>
    <p class="author">— Directrice des Ressources Humaines, 48 ans</p>
</div>

<div class="page-number">72</div>
</body></html>'''

temp_p71_file = os.path.join(SCRATCH, 'temp_p71_air.html')
pdf_p71_file = os.path.join(SCRATCH, 'p71_air.pdf')
with open(temp_p71_file, 'w', encoding='utf-8') as f:
    f.write(html_p71_layout)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p71_file}', temp_p71_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_p71_air = fitz.open(pdf_p71_file)
p71.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), doc_p71_air, 0)

temp_p72_file = os.path.join(SCRATCH, 'temp_p72_air.html')
pdf_p72_file = os.path.join(SCRATCH, 'p72_air.pdf')
with open(temp_p72_file, 'w', encoding='utf-8') as f:
    f.write(html_p72_layout)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p72_file}', temp_p72_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_p72_air = fitz.open(pdf_p72_file)
p72.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), doc_p72_air, 0)

# Patch Sommet Page 109 (anciennement 110) : Encadré LE SAVIEZ-VOUS institutionnel propre (Gloria Mark)
p111 = new_sommet[108]
p111.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
p111.apply_redactions()

html_p111_layout = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400;1,700&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 34.8pt 33.75pt 30pt 33.75pt;
    font-family: 'Lora', Georgia, serif; font-size: 9.15pt; line-height: 13.5pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}
.callout {
    width: 100%; background-color: #f8f8f8; border-left: 3.5px solid #000000;
    padding: 9pt 11pt; margin-bottom: 16pt;
}
.callout-title {
    font-family: 'Montserrat', sans-serif; font-size: 8.5pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 5pt; color: #000000;
}
.callout p {
    font-size: 8.8pt; font-style: italic; line-height: 13.2pt; color: #111111;
    text-align: justify; margin: 0;
}
h2 {
    font-family: 'Montserrat', sans-serif; font-size: 9.6pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; color: #000000;
    margin-bottom: 9pt; line-height: 13pt;
}
p.body-text {
    font-size: 9.15pt; line-height: 13.5pt; text-align: justify; text-justify: inter-word;
    color: #111111; margin-bottom: 8pt;
}
p.protocol-intro {
    font-size: 9.15pt; font-weight: 700; color: #111111; margin-top: 10pt; margin-bottom: 6pt;
}
ol.protocol-list {
    list-style: none; margin: 0; padding: 0;
}
ol.protocol-list li {
    font-size: 9.15pt; line-height: 13.2pt; margin-bottom: 6pt; text-align: justify;
}
ol.protocol-list li strong {
    font-weight: 700; color: #000000;
}
.page-number {
    position: absolute; bottom: 23pt; left: 0; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>

<div class="callout">
    <div class="callout-title">▌ LE SAVIEZ-VOUS&nbsp;?</div>
    <p>Selon les recherches fondatrices de Gloria Mark (Université de Californie, Irvine), un collaborateur interrompu dans son travail met en moyenne 23&nbsp;minutes et 15&nbsp;secondes pour retrouver son état de concentration initial sur sa tâche principale.</p>
</div>

<h2>ÉTAPE 4&nbsp;: L'INSTAURATION DU BUDGET D'AUTONOMIE LOCALE NON CONTRÔLÉ A PRIORI</h2>

<p class="body-text">La confiance managériale ne se décrète pas dans une charte de valeurs&nbsp;: elle se prouve par la décentralisation immédiate du pouvoir financier au plus près du terrain.</p>

<p class="body-text">Dans la majorité des entreprises, pour acheter un outillage de 80&nbsp;euros, remplacer un écran cassé ou commander une pièce détachée urgente, un chef d'équipe doit constituer une demande d'achat informatique, la faire valider par son N+1, attendre l'accord du contrôle de gestion et espérer la création d'un bon de commande par le service achats centralisé. Ce circuit coûte souvent 200&nbsp;euros de temps administratif pour un achat de 50&nbsp;euros, tout en paralysant le travail pendant dix jours.</p>

<p class="protocol-intro">Le protocole de souveraineté budgétaire&nbsp;:</p>

<ol class="protocol-list">
    <li><strong>1. L'allocation de l'enveloppe mensuelle directe&nbsp;:</strong> Confiez à chaque chef d'équipe ou responsable d'îlot une carte bancaire professionnelle plafonnée à un montant de 1&nbsp;500 à 3&nbsp;000&nbsp;euros par mois.</li>
    <li><strong>2. La règle d'or d'utilisation&nbsp;:</strong> Toute dépense directement destinée à améliorer la sécurité des personnes, la qualité du travail, la maintenance d'urgence ou le confort matériel du poste est autorisée sans validation préalable d'aucune sorte.</li>
    <li><strong>3. Le contrôle a posteriori basé sur la confiance&nbsp;:</strong> Remplacer le contrôle a priori par une revue trimestrielle informelle et collective des dépenses réalisées. Les données montrent que les équipes responsabilisées directement font preuve d'une gestion beaucoup plus économe et rigoureuse que les services d'achats distants.</li>
</ol>

<div class="page-number">109</div>

</body>
</html>'''

temp_p111_file = os.path.join(SCRATCH, 'temp_p111_formatted.html')
pdf_p111_file = os.path.join(SCRATCH, 'p111_formatted.pdf')
with open(temp_p111_file, 'w', encoding='utf-8') as f:
    f.write(html_p111_layout)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p111_file}', temp_p111_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_p111 = fitz.open(pdf_p111_file)
p111.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), doc_p111, 0)
print("Applied proper formatted LE SAVIEZ-VOUS callout on Sommet page 110")

# Patch Sommet Pages 111 & 112 (suite suppression page de souffle) : Cas documenté 3M Post-It
p113 = new_sommet[110]
p113.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
p113.apply_redactions()

html_p113_layout = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400;1,700&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 34.8pt 33.75pt 30pt 33.75pt;
    font-family: 'Lora', Georgia, serif; font-size: 9.15pt; line-height: 13.5pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}
ul.bullet-list {
    list-style: none; margin: 0 0 16pt 0; padding: 0;
}
ul.bullet-list li {
    font-size: 9.15pt; line-height: 13.5pt; margin-bottom: 6pt; text-align: justify;
    position: relative; padding-left: 12pt;
}
ul.bullet-list li::before {
    content: '•'; position: absolute; left: 0; color: #000000; font-weight: 700;
}
h2 {
    font-family: 'Montserrat', sans-serif; font-size: 9.6pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; color: #000000;
    margin-bottom: 9pt; line-height: 13pt;
}
p.body-text {
    font-size: 9.15pt; line-height: 13.5pt; text-align: justify; text-justify: inter-word;
    color: #111111; margin-bottom: 7pt;
}
p.protocol-intro {
    font-size: 9.15pt; font-weight: 700; color: #111111; margin-top: 9pt; margin-bottom: 5pt;
}
ol.protocol-list {
    list-style: none; margin: 0 0 10pt 0; padding: 0;
}
ol.protocol-list li {
    font-size: 9.15pt; line-height: 13.2pt; margin-bottom: 5.5pt; text-align: justify;
}
ol.protocol-list li strong {
    font-weight: 700; color: #000000;
}
.case-title {
    font-size: 9.15pt; font-weight: 700; color: #000000; margin-top: 8pt; margin-bottom: 4pt;
}
.page-number {
    position: absolute; bottom: 23pt; left: 0; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>

<ul class="bullet-list">
    <li><strong>Zéro recours aux agences d'intérim médical</strong> onéreuses sur l'ensemble de l'exercice budgétaire.</li>
    <li><strong>Un climat de solidarité immédiate&nbsp;:</strong> les soignants s'échangent spontanément leurs gardes sans friction ni formalisme lourd.</li>
</ul>

<h2>ÉTAPE 6&nbsp;: L'OFFICIALISATION BIENVEILLANTE DES INNOVATIONS CLANDESTINES</h2>

<p class="body-text">Dans toute organisation vivante, les salariés de terrain développent des dizaines de solutions ingénieuses pour contourner les lourdeurs du système officiel&nbsp;: gabarits sur mesure, feuilles de calcul automatisées, raccourcis de maintenance ou réorganisations spontanées d'ateliers.</p>

<p class="body-text">Trop souvent, ces innovations restent cachées par crainte des reproches des auditeurs qualité ou de la direction informatique centrale.</p>

<p class="protocol-intro">Le protocole de libération de l'ingéniosité locale&nbsp;:</p>

<ol class="protocol-list">
    <li><strong>1. L'atelier de partage sans jugement&nbsp;:</strong> Organisez une demi-journée conviviale où chaque collaborateur est invité à présenter ses astuces, ses outils artisanaux et ses méthodes personnelles de travail.</li>
    <li><strong>2. L'analyse collégiale de valeur&nbsp;:</strong> Évaluez collectivement les gains réels de temps, de sécurité et d'ergonomie apportés par chaque bricolage clandestin.</li>
    <li><strong>3. L'homologation et la valorisation publique&nbsp;:</strong> Faites valider formellement ces créations par les services techniques, intégrez-les aux standards officiels et attribuez une prime d'innovation aux salariés inventeurs.</li>
</ol>

<p class="case-title">Le cas historique de l'innovation clandestine chez 3M&nbsp;:</p>
<p class="body-text">Chez 3M, le chercheur Spencer Silver avait découvert un adhésif à faible adhérence jugé totalement «&nbsp;inutile&nbsp;» et rejeté par la direction commerciale pendant cinq ans. C'est son collègue Art Fry qui a détourné clandestinement les machines de l'usine le week-end pour enduire des chutes de papier jaune et créer les premiers prototypes de Post-it distribués sous le manteau aux secrétaires du siège.</p>

<div class="page-number">111</div>

</body>
</html>'''

temp_p113_file = os.path.join(SCRATCH, 'temp_p113_3m.html')
pdf_p113_file = os.path.join(SCRATCH, 'p113_3m.pdf')
with open(temp_p113_file, 'w', encoding='utf-8') as f:
    f.write(html_p113_layout)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p113_file}', temp_p113_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_p113 = fitz.open(pdf_p113_file)
p113.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), doc_p113, 0)

p114 = new_sommet[111]
p114.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
p114.apply_redactions()

html_p114_layout = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400;1,700&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 34.8pt 33.75pt 30pt 33.75pt;
    font-family: 'Lora', Georgia, serif; font-size: 9.15pt; line-height: 13.5pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}
p.body-text {
    font-size: 9.15pt; line-height: 13.5pt; text-align: justify; text-justify: inter-word;
    color: #111111; margin-bottom: 14pt;
}
h2 {
    font-family: 'Montserrat', sans-serif; font-size: 9.6pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; color: #000000;
    margin-bottom: 9pt; line-height: 13pt;
}
p.protocol-intro {
    font-size: 9.15pt; font-weight: 700; color: #111111; margin-top: 9pt; margin-bottom: 5pt;
}
ol.protocol-list {
    list-style: none; margin: 0 0 10pt 0; padding: 0;
}
ol.protocol-list li {
    font-size: 9.15pt; line-height: 13.2pt; margin-bottom: 5.5pt; text-align: justify;
}
ol.protocol-list li strong {
    font-weight: 700; color: #000000;
}
.callout {
    width: 100%; background-color: #f8f8f8; border-left: 3.5px solid #000000;
    padding: 8pt 10pt; margin-top: 10pt;
}
.callout-title {
    font-family: 'Montserrat', sans-serif; font-size: 8.2pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.4px; margin-bottom: 4pt; color: #000000;
}
.callout p {
    font-size: 8.8pt; font-style: italic; line-height: 13.2pt; color: #111111;
    text-align: justify; margin: 0;
}
.page-number {
    position: absolute; bottom: 23pt; left: 0; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>

<p class="body-text"><strong>L'arbitrage lucide de la direction de 3M&nbsp;:</strong> Plutôt que de sanctionner cette infraction manifeste aux plannings de fabrication, la direction générale a reconnu l'engouement immédiat des utilisateurs, industrialisé le procédé et formalisé la célèbre <em>règle des 15&nbsp;%</em> de temps libre pour tous les ingénieurs. Le Post-it est devenu l'un des produits les plus rentables de l'histoire du groupe.</p>

<h2>ÉTAPE 7&nbsp;: LE DIALOGUE DIRECT ET CONSTRUCTIF AVEC LES PARTENAIRES SOCIAUX</h2>

<p class="body-text">Les relations sociales sont trop souvent réduites à des postures juridiques crispées entre la direction et les représentants syndicaux. Pour transformer durablement une organisation, le dirigeant doit faire du travail réel le terrain d'entente privilégié&nbsp;:</p>

<p class="protocol-intro">Les clés d'un partenariat social régénéré&nbsp;:</p>

<ol class="protocol-list">
    <li><strong>1. L'invitation sur le sol du travail vivant&nbsp;:</strong> Invitez les élus du Comité Social et Économique (CSE) et les délégués syndicaux à participer à des visites de terrain conjointes non protocolaires pour constater ensemble la réalité matérielle des postes de travail.</li>
    <li><strong>2. Le partage transparent des données économiques&nbsp;:</strong> Communiquez aux élus les chiffres réels de rentabilité, les marges opérationnelles et les contraintes de trésorerie sans dissimulation ni artifice comptable.</li>
    <li><strong>3. Les accords d'expérimentation locale dérogatoire&nbsp;:</strong> Négociez des accords de méthode permettant d'expérimenter de nouvelles formes d'organisation du travail (autonomie locale, budgets souverains, horaires flexibles) pendant six à douze mois sur des sites pilotes, avec un bilan contradictoire partagé.</li>
</ol>

<div class="callout">
    <div class="callout-title">▌ LE TÉMOIGNAGE D'UN DÉLÉGUÉ SYNDICAL CENTRAL</div>
    <p>«&nbsp;Pendant vingt ans, mes réunions avec la direction consistaient à éplucher des documents juridiques de trois cents pages. Le jour où le nouveau directeur nous a emmenés dans l'atelier pour regarder ensemble comment réparer les postes de travail les plus pénibles, nous sommes passés de la guerre de tranchées au travail d'équipe pour sauver notre usine.&nbsp;»</p>
</div>

<div class="page-number">112</div>

</body>
</html>'''

temp_p114_file = os.path.join(SCRATCH, 'temp_p114_3m.html')
pdf_p114_file = os.path.join(SCRATCH, 'p114_3m.pdf')
with open(temp_p114_file, 'w', encoding='utf-8') as f:
    f.write(html_p114_layout)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p114_file}', temp_p114_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_p114 = fitz.open(pdf_p114_file)
p114.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), doc_p114, 0)
print("Applied 3M Post-it case on Sommet pages 112 and 113")

# Patch Sommet Page 86 (suite suppression page de souffle) : Remplacement du cas FAVI par Zhang Ruimin / Haier (Rendanheyi)

# Patch Sommet Page 62 : Nettoyage en-tête et application du format Option A (Ce que gouverner veut vraiment dire)
p62_sommet = new_sommet[61]
p62_sommet.add_redact_annot(fitz.Rect(30.0, 35.0, 390.0, 105.0), fill=(1, 1, 1))
p62_sommet.apply_redactions()

html_p62_header = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;1,400&family=Montserrat:wght@700;800&display=swap" rel="stylesheet">
<style>
@page { size: 352.5pt 65pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 352.5pt; height: 65pt; background: #ffffff;
    font-family: 'Lora', Georgia, serif; color: #000000;
    -webkit-font-smoothing: antialiased;
}
h1 {
    font-family: 'Montserrat', sans-serif; font-size: 13.5pt; font-weight: 800;
    text-transform: uppercase; letter-spacing: 0.5px; color: #000000;
    text-align: center; line-height: 16pt; margin-bottom: 10pt;
}
.rule {
    width: 100%; height: 0.75pt; background-color: #000000; margin-bottom: 10pt;
}
.subtitle {
    font-family: 'Lora', Georgia, serif; font-size: 10pt; font-weight: 400;
    text-align: center; color: #111111; line-height: 13pt;
}
</style>
</head>
<body>
<h1>CE QUE GOUVERNER VEUT VRAIMENT DIRE</h1>
<div class="rule"></div>
<div class="subtitle">L'équation tacite entre gouverner et contrôler</div>
</body>
</html>'''

temp_p62_header = os.path.join(SCRATCH, 'temp_p62_header.html')
pdf_p62_header = os.path.join(SCRATCH, 'header_p62.pdf')
with open(temp_p62_header, 'w', encoding='utf-8') as f:
    f.write(html_p62_header)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p62_header}', temp_p62_header
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
header_doc_p62 = fitz.open(pdf_p62_header)
p62_sommet.show_pdf_page(fitz.Rect(33.75, 41.0, 33.75 + 352.5, 41.0 + 65.0), header_doc_p62, 0)
print("Applied Option A header on Sommet page 62")

p88_sommet = new_sommet[85]
p88_sommet.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
p88_sommet.apply_redactions()

html_p88_haier = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400;1,700&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 34.8pt 33.75pt 30pt 33.75pt;
    font-family: 'Lora', Georgia, serif; font-size: 9.15pt; line-height: 13.5pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}
h1 {
    font-family: 'Montserrat', sans-serif; font-size: 13pt; font-weight: 800;
    text-transform: uppercase; letter-spacing: 0.5px; color: #000000;
    text-align: center; line-height: 16pt; margin-bottom: 9pt;
}
.rule {
    width: 352.5pt; height: 0.75pt; background-color: #000000; margin: 0 auto 9.5pt auto;
}
.subtitle {
    font-family: 'Lora', Georgia, serif; font-size: 9.8pt; font-weight: 400;
    text-align: center; color: #111111; margin-bottom: 14pt; line-height: 13pt;
}
h2 {
    font-family: 'Montserrat', sans-serif; font-size: 9.6pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; color: #000000;
    margin-top: 11pt; margin-bottom: 6pt; line-height: 13pt;
}
p {
    text-align: justify; text-justify: inter-word; margin-bottom: 6.5pt;
}
.page-number {
    position: absolute; bottom: 23pt; left: 0; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>

<h1>CEUX QUI ONT CHOISI DE FAIRE AUTREMENT</h1>
<div class="rule"></div>
<div class="subtitle">La preuve par les faits et les modèles réels</div>

<p>Il aurait été commode — et intellectuellement malhonnête — de s'arrêter au diagnostic. De documenter les dysfonctionnements, les coûts cachés et les scénarios d'implosion, puis de conclure que la transformation est nécessaire sans montrer qu'elle est possible. Ce chapitre existe précisément pour éviter ce confort-là.</p>

<p>Ce qui suit n'est pas de la prospective ni de la théorie de l'organisation. Ce sont des faits vérifiables, des entreprises qui existent ou ont existé, des bilans économiques chiffrés sur des décennies, et des hommes et des femmes qui ont pris des décisions que leurs pairs considéraient comme imprudentes ou naïves.</p>

<p>Ils avaient raison. Leurs pairs avaient tort.</p>

<h2>ZHANG RUIMIN ET LE MODÈLE RENDANHEYI (HAIER)</h2>

<p>Lorsqu'il prend la tête d'un fabricant d'électroménager au bord du dépôt de bilan, Zhang Ruimin pose un acte fondateur devenu légendaire : il fait aligner soixante-seize réfrigérateurs défectueux dans la cour de l'usine et remet des masses aux ouvriers pour qu'ils détruisent eux-mêmes leur production médiocre. Le message est gravé : la qualité et la responsabilité ne se délèguent pas.</p>

<p>Devenu le numéro un mondial de l'électroménager avec plus de 80&nbsp;000 salariés (et le rachat de GE Appliances aux États-Unis), Zhang Ruimin engage alors la métamorphose organisationnelle la plus radicale du XXI<sup>e</sup> siècle : il démantèle la totalité de la hiérarchie intermédiaire. Plus de dix mille postes de cadres et de directeurs fonctionnels sont purement et simplement abolis.</p>

<p>Le groupe est éclaté en quatre mille micro-entreprises autonomes de dix à quinze personnes. Chaque micro-entreprise choisit son propre leader par élection, gère son compte d'exploitation (P&L), embauche librement et contracte des accords internes ou externes. Chez Haier, le client direct est devenu le seul et unique patron.</p>

<div class="page-number">86</div>

</body>
</html>'''

temp_p88_file = os.path.join(SCRATCH, 'temp_p88_haier.html')
pdf_p88_file = os.path.join(SCRATCH, 'p88_haier.pdf')
with open(temp_p88_file, 'w', encoding='utf-8') as f:
    f.write(html_p88_haier)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p88_file}', temp_p88_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_p88 = fitz.open(pdf_p88_file)
p88_sommet.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), doc_p88, 0)
print("Applied Zhang Ruimin / Haier case on Sommet page 87")

# Patch Sommet Page 89 (suite suppression page de souffle) : Actualisation de la synthèse (Zhang Ruimin au lieu de Zobrist)
p91_sommet = new_sommet[88]
r_zobrist_p91 = p91_sommet.search_for("Zobrist ne savait pas que les opérateurs seraient capables de gérer leurs propres")
if r_zobrist_p91:
    r_z = r_zobrist_p91[0]
    p91_sommet.add_redact_annot(fitz.Rect(r_z.x0 - 1, r_z.y0 - 1, r_z.x0 + 60, r_z.y1 + 1), fill=(1, 1, 1))
    p91_sommet.apply_redactions()
    p91_sommet.insert_text(fitz.Point(r_z.x0, r_z.y1 - 2.2), "Zhang Ruimin", fontsize=8.95, fontname="tiro", color=(0.07, 0.07, 0.07))
    print("Updated synthesis on Sommet page 90")

# Patch Sommet Page 80 (suite suppression page de souffle) : Titre "Le coût de ne rien faire : l'urgence silencieuse" normalisé
p81_sommet = new_sommet[79]
# Redact former unstyled title and old separator line above it
p81_sommet.add_redact_annot(fitz.Rect(30.0, 440.0, 390.0, 476.0), fill=(1, 1, 1))
p81_sommet.apply_redactions()

html_p81_title = '''<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap" rel="stylesheet">
<style>
@page { size: 352.5pt 36pt; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width: 352.5pt; height: 36pt; background: #ffffff;
    font-family: 'Montserrat', sans-serif;
    -webkit-font-smoothing: antialiased;
}
.rule {
    width: 100%; height: 0.75pt; background-color: #000000; margin-bottom: 11pt;
}
h2 {
    font-size: 9.6pt; font-weight: 700; text-transform: uppercase;
    letter-spacing: 0.3px; color: #000000; display: flex; align-items: center;
    line-height: 9.6pt;
}
.symbol {
    display: inline-block; width: 4.8pt; height: 9.6pt; background-color: #000000;
    margin-right: 6pt; flex-shrink: 0;
}
</style></head><body>
<div class="rule"></div>
<h2><span class="symbol"></span>LE COÛT DE NE RIEN FAIRE : L'URGENCE SILENCIEUSE</h2>
</body></html>'''

temp_p81_title = os.path.join(SCRATCH, 'temp_p81_title.html')
pdf_p81_title = os.path.join(SCRATCH, 'p81_title.pdf')
with open(temp_p81_title, 'w', encoding='utf-8') as f:
    f.write(html_p81_title)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p81_title}', temp_p81_title
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_p81_title = fitz.open(pdf_p81_title)
p81_sommet.show_pdf_page(fitz.Rect(33.75, 440.0, 33.75 + 352.5, 440.0 + 36.0), doc_p81_title, 0)
print("Standardized unstyled title on Sommet page 81")

# Bottom-anchoring ("collé au bas") for Sommet floor opening pages with dead whitespace
sommet_openings_shift = {
    7: (40.0, fitz.Rect(30, 155, 390, 520)),
    37: (54.0, fitz.Rect(30, 155, 390, 520)),
    43: (37.0, fitz.Rect(30, 155, 390, 520)),
    49: (17.5, fitz.Rect(30, 155, 390, 520))
}
for pno, (dy, rect_src) in sommet_openings_shift.items():
    page = new_sommet[pno - 1]
    page_copy = fitz.open()
    page_copy.insert_pdf(new_sommet, from_page=pno-1, to_page=pno-1)
    page.add_redact_annot(rect_src, fill=(1, 1, 1))
    page.apply_redactions()
    rect_dst = fitz.Rect(rect_src.x0, rect_src.y0 + dy, rect_src.x1, rect_src.y1 + dy)
    page.show_pdf_page(rect_dst, page_copy, 0, clip=rect_src)
    print(f"Applied bottom-anchoring shift (dy=+{dy}pt) to Sommet page {pno}")

# ----------------------------------------------------
print("Scanning exact new chapter positions...")

def find_first_page_with(doc, term):
    for i in range(len(doc)):
        if i == 2: continue # skip TOC page
        t = doc[i].get_text().upper().replace(' ', ' ')
        if term.upper() in t:
            return i + 1
    return None

p_prologue = find_first_page_with(new_sommet, "LE LUNDI DE LA DÉCISION") or 5
p_ceo = find_first_page_with(new_sommet, "ÉTAGE 8 SUR 8") or 7
p_chairman = find_first_page_with(new_sommet, "ÉTAGE 7 SUR 8") or 13
p_pres_int = find_first_page_with(new_sommet, "ÉTAGE 6 SUR 8") or 19
p_pres_div = find_first_page_with(new_sommet, "ÉTAGE 5 SUR 8") or 25
p_vp = find_first_page_with(new_sommet, "ÉTAGE 4 SUR 8") or 31
p_dir = find_first_page_with(new_sommet, "ÉTAGE 3 SUR 8") or 37
p_resp = find_first_page_with(new_sommet, "ÉTAGE 2 SUR 8") or 43
p_mgr = find_first_page_with(new_sommet, "ÉTAGE 1 SUR 8") or 49
p_terrain = find_first_page_with(new_sommet, "ÉTAGE 0 SUR 8") or 55
p_bilan = 59
p_jonction = 60

p_gouverner = find_first_page_with(new_sommet, "CE QUE GOUVERNER VEUT VRAIMENT DIRE") or 62
p_cout = find_first_page_with(new_sommet, "LE COÛT DE NE RIEN FAIRE") or 67
p_systeme = find_first_page_with(new_sommet, "POURQUOI LE SYSTÈME RÉSISTE") or 69
p_generations = find_first_page_with(new_sommet, "DIRIGER 4 GÉNÉRATIONS") or 72
p_monde = find_first_page_with(new_sommet, "ET SI ? LE MONDE D'APRÈS") or 77
p_preuves = find_first_page_with(new_sommet, "LES PREUVES QUE ÇA MARCHE") or 82
p_choisi = find_first_page_with(new_sommet, "CEUX QUI ONT CHOISI DE FAIRE AUTREMENT") or 86
p_pionniers = find_first_page_with(new_sommet, "LES PIONNIERS DE LA TRANSFORMATION") or 90
p_angles = find_first_page_with(new_sommet, "CE QUE LA TOUR NE VOIT PAS") or 95
p_fiches = find_first_page_with(new_sommet, "LES FICHES PRATIQUES DU DIRIGEANT") or 98
p_transition = find_first_page_with(new_sommet, "LA TRANSITION VUE D'EN HAUT") or 105
p_premier = find_first_page_with(new_sommet, "LE PREMIER PAS DU DÉCIDEUR") or 120
p_feuille = find_first_page_with(new_sommet, "18 MOIS POUR BÂTIR") or 122
p_hall = find_first_page_with(new_sommet, "LE HALL CENTRAL") or 124
p_sources = find_first_page_with(new_sommet, "LISTE DES SOURCES") or 126

print(f"Scanned: CEO={p_ceo}, VP={p_vp}, Mgr={p_mgr}, Preuves={p_preuves}, Hall={p_hall}")

# ----------------------------------------------------
# 7. GENERER LA TABLE DES MATIÈRES EXACTE (PAGE 3)
# ----------------------------------------------------
p_prologue = 4

html_toc_raw = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap');
@page { size: 148mm 210mm; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 148mm; height: 210mm; padding: 10mm 13mm 11mm 13mm;
    box-sizing: border-box; background: #ffffff;
    font-family: 'Lora', Georgia, serif; color: #18181b; position: relative;
    -webkit-font-smoothing: antialiased;
}
.header { text-align: center; margin-bottom: 2.2mm; }
.header .eyebrow {
    font-family: 'Montserrat', sans-serif; font-size: 7.2pt; font-weight: 700; letter-spacing: 2.6px; text-transform: uppercase;
    color: #52525b; margin-bottom: 0.8mm;
}
.header h1 {
    font-family: 'Montserrat', sans-serif; font-size: 13.5pt; font-weight: 800; letter-spacing: 0.6px; text-transform: uppercase;
    color: #09090b; margin-bottom: 1.5mm;
}
.header .rule {
    width: 36px; height: 1.6px; background-color: #09090b; margin: 0 auto;
}
.part-title {
    font-family: 'Montserrat', sans-serif; font-size: 7.6pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;
    color: #09090b; margin-top: 2.2mm; margin-bottom: 0.8mm;
}
.part-rule {
    width: 100%; height: 1px; background-color: #18181b; margin-bottom: 1.4mm;
}
.toc-list {
    display: flex; flex-direction: column; gap: 0.75mm;
}
.toc-row {
    display: flex; align-items: baseline; font-size: 7.3pt; line-height: 1.18;
}
.toc-num {
    width: 3.8mm; font-family: 'Montserrat', sans-serif; font-size: 7.2pt; font-weight: 700; color: #09090b; flex-shrink: 0;
}
.toc-bullet {
    width: 3.8mm; color: #71717a; flex-shrink: 0; text-align: center; font-size: 6.0pt;
}
.toc-label {
    font-family: 'Lora', Georgia, serif; font-size: 7.6pt; color: #18181b; flex-shrink: 0;
}
.toc-dots {
    flex: 1; border-bottom: 1px dotted #cbd5e1; margin: 0 4px; height: 0.9em;
}
.toc-page {
    font-family: 'Montserrat', sans-serif; font-size: 7.3pt; font-weight: 600;
    color: #09090b; flex-shrink: 0; text-align: right; min-width: 5mm;
}
.footer-page {
    position: absolute; bottom: 6mm; width: 100%; left: 0; text-align: center;
    font-family: 'Montserrat', sans-serif; font-size: 8.5pt; color: #71717a;
}
</style>
</head>
<body>

<div class="header">
    <div class="eyebrow">C Ô T É   S O M M E T</div>
    <h1>TABLE DES MATIÈRES</h1>
    <div class="rule"></div>
</div>

<div class="part-title">PARTIE I — LA TOUR (DESCENTE)</div>
<div class="part-rule"></div>
<div class="toc-list">
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Prologue — Le lundi de la décision</div><div class="toc-dots"></div><div class="toc-page">{p_prologue}</div></div>
    <div class="toc-row"><div class="toc-num">8</div><div class="toc-label">Le CEO (PDG)</div><div class="toc-dots"></div><div class="toc-page">{p_ceo}</div></div>
    <div class="toc-row"><div class="toc-num">7</div><div class="toc-label">Le Chairman</div><div class="toc-dots"></div><div class="toc-page">{p_chairman}</div></div>
    <div class="toc-row"><div class="toc-num">6</div><div class="toc-label">Le Président international</div><div class="toc-dots"></div><div class="toc-page">{p_pres_int}</div></div>
    <div class="toc-row"><div class="toc-num">5</div><div class="toc-label">Le Président de division</div><div class="toc-dots"></div><div class="toc-page">{p_pres_div}</div></div>
    <div class="toc-row"><div class="toc-num">4</div><div class="toc-label">Le Vice-Président</div><div class="toc-dots"></div><div class="toc-page">{p_vp}</div></div>
    <div class="toc-row"><div class="toc-num">3</div><div class="toc-label">Le Directeur</div><div class="toc-dots"></div><div class="toc-page">{p_dir}</div></div>
    <div class="toc-row"><div class="toc-num">2</div><div class="toc-label">Le Responsable de service</div><div class="toc-dots"></div><div class="toc-page">{p_resp}</div></div>
    <div class="toc-row"><div class="toc-num">1</div><div class="toc-label">Le Manager de proximité</div><div class="toc-dots"></div><div class="toc-page">{p_mgr}</div></div>
    <div class="toc-row"><div class="toc-num">0</div><div class="toc-label">Le Terrain vu du Sommet (Le Retour au réel)</div><div class="toc-dots"></div><div class="toc-page">{p_terrain}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">La vue d'ensemble du Sommet (Bilan)</div><div class="toc-dots"></div><div class="toc-page">{p_bilan}</div></div>
</div>

<div class="part-title" style="margin-top: 2.2mm;">PARTIE II — LES LEVIERS DU GOUVERNEMENT DU RÉEL</div>
<div class="part-rule"></div>
<div class="toc-list">
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Ouverture — De la distance du pouvoir à la puissance d'agir</div><div class="toc-dots"></div><div class="toc-page">{p_ouverture}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Ce que gouverner veut vraiment dire</div><div class="toc-dots"></div><div class="toc-page">{p_gouverner}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Le coût de ne rien faire</div><div class="toc-dots"></div><div class="toc-page">{p_cout}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Pourquoi le système résiste</div><div class="toc-dots"></div><div class="toc-page">{p_systeme}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Diriger 4 générations</div><div class="toc-dots"></div><div class="toc-page">{p_generations}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Et si ? Le monde d'après</div><div class="toc-dots"></div><div class="toc-page">{p_monde}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Les preuves que ça marche</div><div class="toc-dots"></div><div class="toc-page">{p_preuves}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Ceux qui ont choisi de faire autrement</div><div class="toc-dots"></div><div class="toc-page">{p_choisi}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Les pionniers de la transformation</div><div class="toc-dots"></div><div class="toc-page">{p_pionniers}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Ce que la tour ne voit pas</div><div class="toc-dots"></div><div class="toc-page">{p_angles}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Les fiches pratiques du dirigeant</div><div class="toc-dots"></div><div class="toc-page">{p_fiches}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">La transition vue d'en haut</div><div class="toc-dots"></div><div class="toc-page">{p_transition}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Le premier pas du décideur</div><div class="toc-dots"></div><div class="toc-page">{p_premier}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">La feuille de route : 18 mois pour transformer</div><div class="toc-dots"></div><div class="toc-page">{p_feuille}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Le Hall Central</div><div class="toc-dots"></div><div class="toc-page">{p_hall}</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Sources documentaires & Références</div><div class="toc-dots"></div><div class="toc-page">{p_sources}</div></div>
</div>

<div class="footer-page">3</div>
</body>
</html>'''

p_ouverture = 61
html_toc = html_toc_raw.replace('{p_prologue}', str(p_prologue)).replace('{p_ceo}', str(p_ceo)).replace('{p_chairman}', str(p_chairman)).replace('{p_pres_int}', str(p_pres_int)).replace('{p_pres_div}', str(p_pres_div)).replace('{p_vp}', str(p_vp)).replace('{p_dir}', str(p_dir)).replace('{p_resp}', str(p_resp)).replace('{p_mgr}', str(p_mgr)).replace('{p_terrain}', str(p_terrain)).replace('{p_bilan}', str(p_bilan)).replace('{p_ouverture}', str(p_ouverture)).replace('{p_gouverner}', str(p_gouverner)).replace('{p_cout}', str(p_cout)).replace('{p_systeme}', str(p_systeme)).replace('{p_generations}', str(p_generations)).replace('{p_monde}', str(p_monde)).replace('{p_preuves}', str(p_preuves)).replace('{p_choisi}', str(p_choisi)).replace('{p_pionniers}', str(p_pionniers)).replace('{p_angles}', str(p_angles)).replace('{p_fiches}', str(p_fiches)).replace('{p_transition}', str(p_transition)).replace('{p_premier}', str(p_premier)).replace('{p_feuille}', str(p_feuille)).replace('{p_hall}', str(p_hall)).replace('{p_sources}', str(p_sources))

final_toc_pdf = os.path.join(SCRATCH, 'final_toc_p3.pdf')
render_html_to_pdf(html_toc, final_toc_pdf)

# Replace page 3 in new_sommet (Index 2)
new_sommet.delete_page(2) # remove dummy
toc_doc = fitz.open(final_toc_pdf)
new_sommet.insert_pdf(toc_doc, from_page=0, to_page=0, start_at=2)

# Standardize all footers across all numbered pages of Sommet
new_sommet = standardize_all_footers(new_sommet)

# Save final Sommet PDF in V3
out_sommet_path = os.path.join(V3_DIR, 'Les_9_Etages_Cote_Sommet.pdf')
new_sommet.save(out_sommet_path)
print(f"🎉 SUCCÈS : {out_sommet_path} généré avec {len(new_sommet)} pages !")

# ----------------------------------------------------
# ----------------------------------------------------
# 8. CÔTÉ TERRAIN : ENRICHIR PAGE 113 & TOC
# ----------------------------------------------------
src_terrain_path = '/Users/basile/Desktop/Les-9-etages/terrain_clean_base.pdf'
out_terrain_path = os.path.join(V3_DIR, 'Les_9_Etages_Cote_Terrain.pdf')
shutil.copy2(src_terrain_path, out_terrain_path)
terrain_doc = fitz.open(out_terrain_path)

# HTML for enriched Terrain Page 113
html_terrain_p113 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Montserrat:wght@600;700;800&display=swap');
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; padding: 34.8pt 33.8pt 45pt 33.8pt;
    box-sizing: border-box; background: #ffffff;
    font-family: 'Lora', Georgia, serif; color: #111111; position: relative;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}
p {
    font-size: 9.15pt; line-height: 13.5pt; text-align: justify; margin-bottom: 6.5pt; color: #111111;
    hyphens: auto; -webkit-hyphens: auto;
}
.first-intro {
    text-indent: 14pt; margin-bottom: 8pt;
}
.section-head {
    font-family: 'Montserrat', sans-serif; font-size: 9.2pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; color: #000000;
    margin-top: 10pt; margin-bottom: 6pt;
}
ul { margin-left: 14pt; margin-bottom: 8pt; }
li { font-size: 9pt; line-height: 13.5pt; margin-bottom: 5pt; color: #111111; font-family: 'Lora', Georgia, serif; }
li strong { font-family: 'Montserrat', sans-serif; font-size: 8pt; color: #000000; text-transform: uppercase; }
.callout {
    background-color: #f8f8f8; border-left: 3px solid #000000; padding: 8pt 10pt; margin-top: 10pt;
}
.callout-title {
    font-family: 'Montserrat', sans-serif; font-size: 7.8pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.4px; margin-bottom: 4pt; color: #000000;
}
.callout p {
    font-size: 8.5pt; font-style: italic; line-height: 1.38; margin-bottom: 0; color: #222222;
}
.footer-page {
    position: absolute; bottom: 25pt; width: 100%; left: 0; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #111111;
}
</style>
</head>
<body>
<p class="first-intro">Le secret des cercles concentriques, c'est qu'ils inversent la charge de la preuve. Ce n'est plus le terrain qui doit prouver que le changement est possible. C'est la direction qui doit expliquer pourquoi elle refuse d'étendre ce qui marche.</p>

<div class="section-head">LES 4 PIÈGES DE L'AUTONOMIE VÉCUS PAR LE TERRAIN</div>
<p>Quand une équipe prend son autonomie, le risque ne vient pas du travail : il vient des réflexes humains. Pour ne pas saborder votre propre liberté, voici les 4 dérives vécues sur le terrain et la manière de s'en protéger :</p>
<ul>
    <li><strong>La tyrannie des pairs (l'inquisition mutuelle) :</strong> Quand le N+1 disparaît, le risque est que chacun se mette à surveiller ses collègues. Le regard du groupe peut devenir plus inquisiteur et culpabilisant que l'ancienne hiérarchie. <em>Parade :</em> Sanctuariser le droit à l'erreur et proscrire la délation. L'autonomie, c'est la responsabilité, pas le tribunal populaire.</li>
    <li><strong>L'épuisement par le consensus (« la réunionite autogérée ») :</strong> Vouloir que tout le monde vote sur chaque détail technique ou organisationnel mène au burn-out démocratique. <em>Parade :</em> Utiliser la règle de la <em>sollicitation d'avis</em> : une personne décide seule après avoir consulté ceux qui ont l'expertise et ceux qui subiront la décision.</li>
    <li><strong>L'émergence de « chefs clandestins » :</strong> Dans un flou sans règles écrites, ce sont souvent les personnalités les plus fortes ou manipulatrices qui prennent le pouvoir sans légitimité. <em>Parade :</em> Définir des rôles de coordination clairs, révocables et tournants.</li>
    <li><strong>L'oubli de la documentation :</strong> Si vous ne mesurez pas vous-mêmes vos résultats (gains de temps, satisfaction client), un nouveau chef pourra un jour affirmer que « votre pilote ne marche pas ». <em>Parade :</em> Rendez vos indicateurs indiscutables.</li>
</ul>

<div class="callout">
    <div class="callout-title">RÈGLE D'OR DU TERRAIN</div>
    <p>L'autonomie n'est pas l'absence de chef : c'est le refus d'être infantilisé. Et pour ne pas être infantilisé, le terrain doit se montrer deux fois plus rigoureux que la bureaucratie qu'il remplace.</p>
</div>

<div class="footer-page">113</div>
</body>
</html>'''

pdf_terrain_p113 = os.path.join(SCRATCH, 'new_terrain_p113.pdf')
render_html_to_pdf(html_terrain_p113, pdf_terrain_p113)

# Replace page 113 in terrain_doc (index 112)
doc_p113 = fitz.open(pdf_terrain_p113)
terrain_doc.delete_page(112)
terrain_doc.insert_pdf(doc_p113, from_page=0, to_page=0, start_at=112)

# Replace page 67 in terrain_doc (index 66) - eliminate duplicate quote of page 9
doc_p67 = fitz.open(pdf_terrain_p67)
terrain_doc.delete_page(66)
terrain_doc.insert_pdf(doc_p67, from_page=0, to_page=0, start_at=66)

# Replace page 125 in terrain_doc (index 124) - clean single-layer layout
doc_p125 = fitz.open(pdf_terrain_p125)
terrain_doc.delete_page(124)
terrain_doc.insert_pdf(doc_p125, from_page=0, to_page=0, start_at=124)

html_toc_terrain_raw = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap');
@page { size: 148mm 210mm; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 148mm; height: 210mm; padding: 13mm 13mm 14mm 13mm;
    box-sizing: border-box; background: #ffffff;
    font-family: 'Lora', Georgia, serif; color: #18181b; position: relative;
    -webkit-font-smoothing: antialiased;
}
.header { text-align: center; margin-bottom: 3.5mm; }
.header .eyebrow {
    font-family: 'Montserrat', sans-serif; font-size: 7.5pt; font-weight: 700; letter-spacing: 2.6px; text-transform: uppercase;
    color: #52525b; margin-bottom: 1.2mm;
}
.header h1 {
    font-family: 'Montserrat', sans-serif; font-size: 14pt; font-weight: 800; letter-spacing: 0.6px; text-transform: uppercase;
    color: #09090b; margin-bottom: 1.8mm;
}
.header .rule {
    width: 36px; height: 1.8px; background-color: #09090b; margin: 0 auto;
}
.part-title {
    font-family: 'Montserrat', sans-serif; font-size: 7.8pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;
    color: #09090b; margin-top: 3.2mm; margin-bottom: 1mm;
}
.part-rule {
    width: 100%; height: 1px; background-color: #18181b; margin-bottom: 2mm;
}
.toc-list {
    display: flex; flex-direction: column; gap: 1.2mm;
}
.toc-row {
    display: flex; align-items: baseline; font-size: 7.6pt; line-height: 1.22;
}
.toc-num {
    width: 4mm; font-family: 'Montserrat', sans-serif; font-size: 7.4pt; font-weight: 700; color: #09090b; flex-shrink: 0;
}
.toc-bullet {
    width: 4mm; color: #71717a; flex-shrink: 0; text-align: center; font-size: 6.2pt;
}
.toc-label {
    font-family: 'Lora', Georgia, serif; font-size: 7.9pt; color: #18181b; flex-shrink: 0;
}
.toc-dots {
    flex: 1; border-bottom: 1px dotted #cbd5e1; margin: 0 4px; height: 0.9em;
}
.toc-page {
    font-family: 'Montserrat', sans-serif; font-size: 7.6pt; font-weight: 600;
    color: #09090b; flex-shrink: 0; text-align: right; min-width: 5mm;
}
.footer-page {
    position: absolute; bottom: 7.5mm; width: 100%; left: 0; text-align: center;
    font-family: 'Montserrat', sans-serif; font-size: 8.5pt; color: #71717a;
}
</style>
</head>
<body>

<div class="header">
    <div class="eyebrow">C Ô T É   T E R R A I N</div>
    <h1>TABLE DES MATIÈRES</h1>
    <div class="rule"></div>
</div>

<div class="part-title">PARTIE I — LA TOUR (MONTÉE)</div>
<div class="part-rule"></div>
<div class="toc-list">
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Prologue — Le lundi sans management</div><div class="toc-dots"></div><div class="toc-page">4</div></div>
    <div class="toc-row"><div class="toc-num">0</div><div class="toc-label">Le Terrain</div><div class="toc-dots"></div><div class="toc-page">5</div></div>
    <div class="toc-row"><div class="toc-num">1</div><div class="toc-label">Le Manager de proximité</div><div class="toc-dots"></div><div class="toc-page">11</div></div>
    <div class="toc-row"><div class="toc-num">2</div><div class="toc-label">Le Responsable de service</div><div class="toc-dots"></div><div class="toc-page">19</div></div>
    <div class="toc-row"><div class="toc-num">3</div><div class="toc-label">Le Directeur</div><div class="toc-dots"></div><div class="toc-page">27</div></div>
    <div class="toc-row"><div class="toc-num">4</div><div class="toc-label">Le Vice-Président</div><div class="toc-dots"></div><div class="toc-page">35</div></div>
    <div class="toc-row"><div class="toc-num">5</div><div class="toc-label">Le Président de division</div><div class="toc-dots"></div><div class="toc-page">43</div></div>
    <div class="toc-row"><div class="toc-num">6</div><div class="toc-label">Le Président international</div><div class="toc-dots"></div><div class="toc-page">51</div></div>
    <div class="toc-row"><div class="toc-num">7</div><div class="toc-label">Le Chairman</div><div class="toc-dots"></div><div class="toc-page">57</div></div>
    <div class="toc-row"><div class="toc-num">8</div><div class="toc-label">Le CEO (PDG)</div><div class="toc-dots"></div><div class="toc-page">61</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">La vue d'ensemble du Terrain (Bilan)</div><div class="toc-dots"></div><div class="toc-page">66</div></div>
</div>

<div class="part-title" style="margin-top: 4.5mm;">PARTIE II — LES ROUAGES DU SYSTÈME</div>
<div class="part-rule"></div>
<div class="toc-list">
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Qui a construit la tour ?</div><div class="toc-dots"></div><div class="toc-page">70</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Le grand départ</div><div class="toc-dots"></div><div class="toc-page">75</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Et si ? Le monde d'après</div><div class="toc-dots"></div><div class="toc-page">84</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Ceux qui ont déjà commencé</div><div class="toc-dots"></div><div class="toc-page">92</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Fiches pratiques du terrain</div><div class="toc-dots"></div><div class="toc-page">101</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">La transition réaliste</div><div class="toc-dots"></div><div class="toc-page">109</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Le plan de transformation</div><div class="toc-dots"></div><div class="toc-page">131</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Le Hall Central</div><div class="toc-dots"></div><div class="toc-page">136</div></div>
    <div class="toc-row"><div class="toc-bullet">•</div><div class="toc-label">Sources documentaires & Références</div><div class="toc-dots"></div><div class="toc-page">138</div></div>
</div>

<div class="footer-page">3</div>
</body>
</html>'''
final_toc_terrain_pdf = os.path.join(SCRATCH, 'final_toc_terrain_p3.pdf')
render_html_to_pdf(html_toc_terrain_raw, final_toc_terrain_pdf)
toc_terrain_doc = fitz.open(final_toc_terrain_pdf)
terrain_doc.delete_pages(2, 2)
terrain_doc.insert_pdf(toc_terrain_doc, from_page=0, to_page=0, start_at=2)

# ----------------------------------------------------
# 8.1 HARMONISATION DES CALLOUTS & CHARTE GRAPHIQUE CÔTÉ TERRAIN
# ----------------------------------------------------
print("Harmonizing Terrain callouts and visual charter...")

def render_terrain_callout_box(title, text, width_pt, height_pt, out_pdf, font_size="8.3pt", line_height="1.32"):
    html_box = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;1,400&family=Montserrat:wght@700&display=swap');
@page {{ size: {width_pt}pt {height_pt}pt; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
    width: {width_pt}pt; height: {height_pt}pt;
    font-family: 'Lora', Georgia, serif;
    background: #ffffff;
    -webkit-font-smoothing: antialiased;
}}
.callout {{
    width: 100%; height: {height_pt}pt;
    background-color: #f8f8f8;
    border-left: 3.5px solid #000000;
    padding: 6pt 10pt;
}}
.callout-title {{
    font-family: 'Montserrat', sans-serif;
    font-size: 7.8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 3.5pt;
    color: #000000;
}}
.callout p {{
    font-family: 'Lora', Georgia, serif;
    font-size: {font_size};
    font-style: italic;
    line-height: {line_height};
    color: #111111;
    text-align: justify;
}}
</style>
</head>
<body>
<div class="callout">
    <div class="callout-title">{title}</div>
    <p>{text}</p>
</div>
</body>
</html>'''
    temp_html = os.path.join(SCRATCH, 'temp_box_terrain.html')
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_box)
    subprocess.run([
        CHROME,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={out_pdf}',
        temp_html
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

terrain_callout_fixes = [
    {
        "page": 110,
        "clean_rect": fitz.Rect(30, 355, 390, 435),
        "target_rect": fitz.Rect(33.8, 358.0, 33.8 + 352.4, 358.0 + 72.0),
        "title": "▌ VOIX DU TERRAIN",
        "text": "«&nbsp;Mon chef nous a annoncé un lundi qu'on passait en mode agile. Le mardi, on avait des post-it partout et un \"Scrum Master\" qui ne savait pas ce qu'on fabriquait. Le mercredi, on faisait exactement comme avant, mais avec des post-it.&nbsp;» — Kévin, développeur dans une ESN, Lyon",
        "font_size": "8.2pt", "line_height": "1.28", "h": 72.0
    },
    {
        "page": 115,
        "clean_rect": fitz.Rect(30, 105, 390, 225),
        "target_rect": fitz.Rect(33.8, 108.0, 33.8 + 352.4, 108.0 + 104.0),
        "title": "▌ VOIX DU TERRAIN",
        "text": "«&nbsp;Avant, on avait la pointeuse. Les gars arrivaient à 7h59, badgeaient, allaient prendre un café de 20 minutes. Quand on a retiré la pointeuse, ceux qui bossaient bien ont continué. Ceux qui glandaient — il y en avait deux sur trente — on les a vus. Parce que quand il n'y a plus de pointeuse pour se cacher derrière, c'est l'équipe qui te regarde. Et l'équipe, elle est beaucoup plus exigeante qu'une machine.&nbsp;» — Fabrice, chef d'équipe dans une fonderie, Picardie",
        "font_size": "8.3pt", "line_height": "1.32", "h": 104.0
    },
    {
        "page": 116,
        "clean_rect": fitz.Rect(30, 178, 390, 258),
        "target_rect": fitz.Rect(33.8, 180.0, 33.8 + 352.4, 180.0 + 64.0),
        "title": "▌ LA QUESTION",
        "text": "«&nbsp;Dans votre travail, la pointeuse mesure-t-elle votre sécurité ou votre obéissance&nbsp;? Si la réponse est «&nbsp;obéissance&nbsp;» — posez-vous la question de ce que vous pourriez accomplir si l'on mesurait votre travail à ses résultats plutôt qu'à vos horaires.&nbsp;»",
        "font_size": "8.3pt", "line_height": "1.32", "h": 64.0
    },
    {
        "page": 117,
        "clean_rect": fitz.Rect(30, 348, 390, 468),
        "target_rect": fitz.Rect(33.8, 350.0, 33.8 + 352.4, 350.0 + 106.0),
        "title": "▌ VOIX DU TERRAIN",
        "text": "«&nbsp;Quand on a proposé les équipes autonomes au CSE, le délégué CGT a d'abord bloqué. Il pensait qu'on voulait supprimer les protections. On a pris le temps de lui expliquer&nbsp;: on ne touche pas aux droits, on change l'organisation. Il a fini par être le plus grand défenseur du projet. Parce qu'il a vu que pour la première fois, les ouvriers avaient vraiment leur mot à dire. C'était exactement ce pour quoi il se battait depuis trente ans.&nbsp;» — Nathalie, DRH d'une PME industrielle, Isère",
        "font_size": "8.2pt", "line_height": "1.30", "h": 106.0
    },
    {
        "page": 119,
        "clean_rect": fitz.Rect(30, 92, 390, 196),
        "target_rect": fitz.Rect(33.8, 95.0, 33.8 + 352.4, 95.0 + 90.0),
        "title": "▌ VOIX DU TERRAIN",
        "text": "«&nbsp;Mon manager était un ancien technicien brillant. Le jour où on a supprimé son poste de \"responsable d'équipe\", il a eu peur. Six mois plus tard, il était redevenu technicien — avec 30&nbsp;% de salaire en moins mais 100&nbsp;% de passion en plus. Il m'a dit&nbsp;: \"J'avais oublié que j'aimais ce métier. Le management m'avait volé ça.\"&nbsp;» — Sarah, technicienne en maintenance industrielle, Dunkerque",
        "font_size": "8.2pt", "line_height": "1.30", "h": 90.0
    },
    {
        "page": 119,
        "clean_rect": fitz.Rect(30, 202, 390, 280),
        "target_rect": fitz.Rect(33.8, 205.0, 33.8 + 352.4, 205.0 + 68.0),
        "title": "▌ LA QUESTION",
        "text": "«&nbsp;Si votre manager disparaissait demain, que se passerait-il concrètement dans votre équipe&nbsp;? Qu'est-ce qui s'arrêterait… et qu'est-ce qui continuerait exactement comme avant&nbsp;? La réponse à cette question vous dit tout ce que vous devez savoir sur l'utilité réelle de ce rôle.&nbsp;»",
        "font_size": "8.2pt", "line_height": "1.30", "h": 68.0
    },
    {
        "page": 120,
        "clean_rect": fitz.Rect(30, 224, 390, 370),
        "target_rect": fitz.Rect(33.8, 226.0, 33.8 + 352.4, 226.0 + 130.0),
        "title": "▌ VOIX DU TERRAIN",
        "text": "«&nbsp;On a lancé un projet d'équipe autonome dans notre école. Les six premiers mois ont été catastrophiques&nbsp;: conflits entre collègues, décisions qui traînaient, deux profs qui faisaient rien pendant que les autres bossaient double. On a failli tout arrêter. Et puis on a fait venir quelqu'un pour nous apprendre la facilitation. On a mis en place un tour de parole, un système de décision par consentement, et un bilan toutes les deux semaines. La deuxième année, on était l'équipe la mieux évaluée de l'académie. Il nous avait juste manqué les outils.&nbsp;» — Amina, professeure de mathématiques dans un collège REP+, Seine-Saint-Denis",
        "font_size": "8.2pt", "line_height": "1.30", "h": 130.0
    },
    {
        "page": 123,
        "clean_rect": fitz.Rect(30, 32, 390, 136),
        "target_rect": fitz.Rect(33.8, 34.0, 33.8 + 352.4, 34.0 + 92.0),
        "title": "▌ VOIX DU TERRAIN",
        "text": "«&nbsp;J'ai passé six mois à noter, dans un carnet, tout ce qui me semblait aberrant. Les mails en copie à douze personnes. Les validations à quatre signatures pour commander une cartouche d'encre. Les réunions de deux heures pour répéter ce qu'on savait déjà. Au bout de six mois, j'avais un dossier de quarante pages. C'est ce dossier qui a convaincu mon directeur de tenter le pilote.&nbsp;» — Thomas, ingénieur dans un bureau d'études, Toulouse",
        "font_size": "8.2pt", "line_height": "1.30", "h": 92.0
    },
    {
        "page": 124,
        "clean_rect": fitz.Rect(30, 196, 390, 260),
        "target_rect": fitz.Rect(33.8, 198.0, 33.8 + 352.4, 198.0 + 54.0),
        "title": "▌ VOIX DU TERRAIN",
        "text": "«&nbsp;Les meilleures initiatives viennent de ceux qui ont les mains dans la matière. Nous n'attendions pas des consignes supplémentaires, nous attendions simplement la liberté d'agir.&nbsp;» — Infirmier, service hospitalier",
        "font_size": "8.3pt", "line_height": "1.32", "h": 54.0
    },
    {
        "page": 124,
        "clean_rect": fitz.Rect(30, 264, 390, 342),
        "target_rect": fitz.Rect(33.8, 266.0, 33.8 + 352.4, 266.0 + 66.0),
        "title": "▌ VOIX DU TERRAIN",
        "text": "«&nbsp;Dès qu'on nous a fait confiance pour adapter les plannings et l'organisation du chantier sans paperasse inutile, nous avons gagné trois semaines sur les délais tout en réduisant la fatigue des équipes.&nbsp;» — Chef de chantier, secteur des travaux publics",
        "font_size": "8.3pt", "line_height": "1.32", "h": 66.0
    },
    {
        "page": 127,
        "clean_rect": fitz.Rect(30, 187, 390, 252),
        "target_rect": fitz.Rect(33.8, 189.0, 33.8 + 352.4, 189.0 + 56.0),
        "title": "▌ VOIX DU TERRAIN",
        "text": "«&nbsp;Le directeur est venu sur le chantier, a écouté nos propositions et a validé notre nouvelle organisation sans chercher à imposer ses tableurs. Il a juste dit&nbsp;: \"Continuez.\"&nbsp;» — Chef de chantier, secteur travaux publics",
        "font_size": "8.3pt", "line_height": "1.32", "h": 56.0
    },
    {
        "page": 129,
        "clean_rect": fitz.Rect(30, 246, 390, 350),
        "target_rect": fitz.Rect(33.8, 248.0, 33.8 + 352.4, 248.0 + 94.0),
        "title": "▌ VOIX DU TERRAIN",
        "text": "«&nbsp;Je suis infirmière en réa. Quand un patient décompense, je ne vais pas organiser un vote pour savoir quoi faire. Il y a un protocole, je le suis, point. Mais pour organiser nos roulements, nos formations, notre matériel&nbsp;? On est les mieux placées pour décider. On connaît notre service mieux que n'importe quel cadre de santé qui passe une fois par semaine.&nbsp;» — Céline, infirmière en réanimation, CHU de Bordeaux",
        "font_size": "8.2pt", "line_height": "1.30", "h": 94.0
    },
    {
        "page": 129,
        "clean_rect": fitz.Rect(30, 355, 390, 460),
        "target_rect": fitz.Rect(33.8, 357.0, 33.8 + 352.4, 357.0 + 94.0),
        "title": "▌ VOIX DU TERRAIN",
        "text": "«&nbsp;Sur le chantier, la sécurité c'est non négociable. Le port du casque, les lignes de vie, les procédures d'évacuation — ça, c'est hiérarchique et ça le restera. Mais pour organiser le travail du jour, dispatcher les équipes, gérer les approvisionnements&nbsp;? On n'a pas besoin qu'un conducteur de travaux qui n'a jamais touché une truelle nous dise comment faire.&nbsp;» — Stéphane, maçon et délégué du personnel, chantier de logements collectifs, Nantes",
        "font_size": "8.2pt", "line_height": "1.30", "h": 94.0
    },
    {
        "page": 130,
        "clean_rect": fitz.Rect(30, 315, 390, 392),
        "target_rect": fitz.Rect(33.8, 317.0, 33.8 + 352.4, 317.0 + 68.0),
        "title": "▌ LA QUESTION FINALE",
        "text": "«&nbsp;Si vous pouviez changer UNE seule chose dans votre organisation — une seule — laquelle choisiriez-vous&nbsp;? Ne répondez pas «&nbsp;tout&nbsp;». Répondez précisément. Concrètement. C'est par là que ça commence. Et lundi matin, faites le premier pas.&nbsp;»",
        "font_size": "8.3pt", "line_height": "1.32", "h": 68.0
    }
]

# Render title overlay PDFs for Terrain
html_trad = '''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
@page { size: 150pt 16pt; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
body { width: 150pt; height: 16pt; background: #ffffff; font-family: 'Montserrat', sans-serif; font-size: 9.2pt; font-weight: 700; color: #000000; letter-spacing: 0.3px; line-height: 16pt; -webkit-font-smoothing: antialiased; }
</style></head><body>▌ LE TRADUCTEUR</body></html>'''
pdf_trad = os.path.join(SCRATCH, 'title_trad.pdf')
with open(os.path.join(SCRATCH, 'temp_trad.html'), 'w') as f: f.write(html_trad)
subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_trad}', os.path.join(SCRATCH, 'temp_trad.html')], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_trad = fitz.open(pdf_trad)

html_p65 = '''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
@page { size: 180pt 18pt; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
body { width: 180pt; height: 18pt; background: #ffffff; font-family: 'Montserrat', sans-serif; font-size: 9.6pt; font-weight: 700; color: #000000; letter-spacing: 0.3px; line-height: 18pt; -webkit-font-smoothing: antialiased; }
</style></head><body>▌ LE SAVIEZ-VOUS ?</body></html>'''
pdf_p65 = os.path.join(SCRATCH, 'title_p65.pdf')
with open(os.path.join(SCRATCH, 'temp_p65.html'), 'w') as f: f.write(html_p65)
subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_p65}', os.path.join(SCRATCH, 'temp_p65.html')], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_p65 = fitz.open(pdf_p65)

html_saviez_box = '''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
@page { size: 110pt 16pt; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
body { width: 110pt; height: 16pt; background: #f8f8f8; font-family: 'Montserrat', sans-serif; font-size: 7.8pt; font-weight: 700; color: #000000; letter-spacing: 0.5px; line-height: 16pt; -webkit-font-smoothing: antialiased; }
</style></head><body>▌ LE SAVIEZ-VOUS ?</body></html>'''
pdf_saviez_box = os.path.join(SCRATCH, 'title_saviez_box.pdf')
with open(os.path.join(SCRATCH, 'temp_saviez_box.html'), 'w') as f: f.write(html_saviez_box)
subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_saviez_box}', os.path.join(SCRATCH, 'temp_saviez_box.html')], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_saviez_box = fitz.open(pdf_saviez_box)

for idx, fix in enumerate(terrain_callout_fixes):
    pno = fix["page"]
    page = terrain_doc[pno - 1]
    page.add_redact_annot(fix["clean_rect"], fill=(1, 1, 1))
    page.apply_redactions()
    box_pdf = os.path.join(SCRATCH, f'box_terrain_build_{pno}_{idx}.pdf')
    render_terrain_callout_box(fix["title"], fix["text"], 352.4, fix["h"], box_pdf, fix["font_size"], fix["line_height"])
    box_doc = fitz.open(box_pdf)
    page.show_pdf_page(fix["target_rect"], box_doc, 0)

# Patch Page 8 : LA QUESTION DU TERRAIN (Styled Callout)
p8 = terrain_doc[7]
p8.add_redact_annot(fitz.Rect(30, 155, 390, 228), fill=(1, 1, 1))
p8.apply_redactions()
p8_box = os.path.join(SCRATCH, 'box_terrain_p8_build.pdf')
render_terrain_callout_box("▌ LA QUESTION DU TERRAIN", "«&nbsp;Si demain matin, tous les tableaux de bord et toutes les réunions de la tour disparaissaient, votre équipe saurait-elle exactement quoi faire pour faire tourner l'activité&nbsp;? Dès lors, qui a véritablement besoin du contrôle de l'autre&nbsp;?&nbsp;»", 352.4, 66.0, p8_box, "8.5pt", "1.35")
p8.show_pdf_page(fitz.Rect(33.8, 156.0, 33.8 + 352.4, 156.0 + 66.0), fitz.open(p8_box), 0)

# Patch Page 65 : LE SAVIEZ-VOUS ? -> ▌ LE SAVIEZ-VOUS ?
p65 = terrain_doc[64]
p65.add_redact_annot(fitz.Rect(40, 105, 160, 126), fill=(1, 1, 1))
p65.apply_redactions()
p65.show_pdf_page(fitz.Rect(33.75, 107.0, 33.75 + 180, 125.0), doc_p65, 0)

# Add ▌ to LE SAVIEZ-VOUS on Pages 111, 114, 117, 121 cleanly without clipping following text
saviez_targets = {
    111: (46.4, 235.0, 131.0, 248.0, 243.0),
    114: (46.4, 418.5, 134.5, 431.5, 426.5),
    117: (46.4, 250.0, 128.0, 263.0, 258.0),
    121: (46.4, 350.5, 129.5, 363.5, 358.5)
}
for pno, (x0, y0, x1, y1, baseline) in saviez_targets.items():
    page = terrain_doc[pno - 1]
    page.add_redact_annot(fitz.Rect(x0, y0, x1, y1), fill=(0.9843, 0.9843, 0.9843))
    page.apply_redactions()
    # Draw square symbol ▌
    symbol_rect = fitz.Rect(46.5, baseline - 6.8, 46.5 + 3.2, baseline + 1.0)
    page.draw_rect(symbol_rect, color=None, fill=(0.0, 0.0, 0.0))
    # Insert text "LE SAVIEZ-VOUS ?" using Helvetica font
    page.insert_text(fitz.Point(53.0, baseline), "LE SAVIEZ-VOUS ?", fontname="helv", fontsize=7.8, color=(0.0, 0.0, 0.0))

# Add ▌ to LE TRADUCTEUR on Pages 112, 118, 124, 129
trad_bullet_coords = {
    112: 361.0,
    118: 93.0,
    124: 33.0,
    129: 33.0
}
for pno, y0 in trad_bullet_coords.items():
    page = terrain_doc[pno - 1]
    page.add_redact_annot(fitz.Rect(33.0, y0, 130.0, y0 + 15.0), fill=(1, 1, 1))
    page.apply_redactions()
    page.show_pdf_page(fitz.Rect(33.75, y0 - 1.0, 33.75 + 150.0, y0 + 15.0), doc_trad, 0)

# Harmonisation chirurgicale Page 47 (Terrain) : Callout LE CHIFFRE CLÉ institutionnel
html_p47_callout = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;1,400&family=Montserrat:wght@700&display=swap');
@page { size: 352.5pt 150pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 352.5pt; height: 150pt; background: #ffffff;
    font-family: 'Lora', Georgia, serif;
    -webkit-font-smoothing: antialiased;
}
.callout {
    width: 100%; background-color: #f8f8f8; border-left: 3.5px solid #000000;
    padding: 7pt 9pt;
}
.callout-title {
    font-family: 'Montserrat', sans-serif; font-size: 8.2pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.4px; margin-bottom: 3pt; color: #000000;
}
.callout-subtitle {
    font-family: 'Lora', Georgia, serif; font-size: 8.3pt; font-style: italic; font-weight: 700;
    color: #333333; margin-bottom: 3pt;
}
.callout p {
    font-size: 8.05pt; line-height: 11.2pt; color: #111111;
    text-align: justify; margin: 0;
}
</style>
</head>
<body>
<div class="callout">
    <div class="callout-title">▌ LE CHIFFRE CLÉ</div>
    <div class="callout-subtitle">Moins de 3 % au client et le grand écart de l'inclusion</div>
    <p>L'agenda d'un membre de comité de direction révèle une réalité paradoxale&nbsp;: moins de 3 % de son temps est passé au contact direct des clients ou du terrain. Le reste est absorbé par des négociations internes et des arbitrages politiques feutrés. C'est à cet étage que naissent les slogans institutionnels sur «&nbsp;l'inclusion et la diversité&nbsp;». Or, dans les faits, la tour exige le conformisme le plus strict&nbsp;: pour monter, il faut gommer ses aspérités et ses différences. Selon le Baromètre LGBT+ au travail (L'Autre Cercle / IFOP, 2022), <strong>1 salarié LGBT+ sur 2 reste invisible</strong> par crainte de pénaliser sa carrière. La diversité y est célébrée en vitrine mais redoutée dès qu'elle bouscule la norme managériale dominante.</p>
</div>
</body>
</html>'''
temp_p47_callout = os.path.join(SCRATCH, 'temp_p47_callout.html')
pdf_p47_callout = os.path.join(SCRATCH, 'p47_callout_run.pdf')
with open(temp_p47_callout, 'w', encoding='utf-8') as f:
    f.write(html_p47_callout)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p47_callout}', temp_p47_callout
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
p47_t = terrain_doc[46]
p47_t.add_redact_annot(fitz.Rect(30, 315, 390, 480), fill=(1, 1, 1))
p47_t.apply_redactions()
doc_callout_p47 = fitz.open(pdf_p47_callout)
p47_t.show_pdf_page(fitz.Rect(33.75, 320.0, 386.25, 320.0 + 150.0), doc_callout_p47, 0)
print("Applied enriched surgical LE CHIFFRE CLÉ callout on Terrain page 47 (inclusion & diversité)")

# Harmonisation chirurgicale Page 12 (Terrain) : Callout CE QU'ELLE A RÉELLEMENT TROUVÉ
html_p12_callout = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;1,400&family=Montserrat:wght@700&display=swap');
@page { size: 352.5pt 135pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 352.5pt; height: 135pt; background: #ffffff;
    font-family: 'Lora', Georgia, serif;
    -webkit-font-smoothing: antialiased;
}
.callout {
    width: 100%; background-color: #f8f8f8; border-left: 3.5px solid #000000;
    padding: 7pt 9pt 6pt 9pt;
}
.callout-title {
    font-family: 'Montserrat', sans-serif; font-size: 8.2pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.4px; margin-bottom: 4.5pt; color: #000000;
}
ul.bullet-list {
    margin: 0; padding-left: 11pt; list-style-type: square;
}
ul.bullet-list li {
    font-family: 'Lora', Georgia, serif; font-size: 8.2pt; line-height: 11.4pt;
    color: #222222; margin-bottom: 2.8pt;
}
ul.bullet-list li:last-child {
    margin-bottom: 0;
}
p.confrontation-conclusion {
    font-family: 'Lora', Georgia, serif; font-size: 8.1pt; font-style: italic;
    line-height: 11.4pt; color: #333333; margin-top: 4.5pt; margin-bottom: 0;
}
</style>
</head>
<body>
<div class="callout">
    <div class="callout-title">▌ CE QU'ELLE A RÉELLEMENT TROUVÉ</div>
    <ul class="bullet-list">
        <li>Des réunions, en nombre exponentiel</li>
        <li>Des tableaux de bord à remplir pour satisfaire les attentes de l'étage supérieur</li>
        <li>Un flux ininterrompu d'e-mails (dont une majorité où elle est en copie pour «&nbsp;traçabilité&nbsp;»)</li>
        <li>Des outils de planification parfois obsolètes qu'elle doit compenser par elle-même</li>
        <li>L'obligation de refuser des demandes légitimes à ses anciens collègues</li>
    </ul>
    <p class="confrontation-conclusion">Au fond d'elle-même, une question s'installe discrètement : «&nbsp;Hier, j'exerçais un métier concret. Aujourd'hui, quelle est ma véritable valeur ajoutée&nbsp;?&nbsp;»</p>
</div>
</body>
</html>'''
temp_p12_callout = os.path.join(SCRATCH, 'temp_p12_callout.html')
pdf_p12_callout = os.path.join(SCRATCH, 'p12_callout_run.pdf')
with open(temp_p12_callout, 'w', encoding='utf-8') as f:
    f.write(html_p12_callout)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p12_callout}', temp_p12_callout
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
p12_t = terrain_doc[11]
p12_t.add_redact_annot(fitz.Rect(30, 30, 390, 170), fill=(1, 1, 1))
p12_t.apply_redactions()
doc_callout_p12 = fitz.open(pdf_p12_callout)
p12_t.show_pdf_page(fitz.Rect(33.75, 34.0, 386.25, 34.0 + 135.0), doc_callout_p12, 0)
print("Applied surgical CE QU'ELLE A RÉELLEMENT TROUVÉ callout on Terrain page 12")

# Harmonisation chirurgicale Page 13 (Terrain) : LA LOTERIE DU MANAGEMENT & LES PROFILS PROTÉGÉS
html_p13_callout = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;1,400&family=Montserrat:wght@700&display=swap');
@page { size: 352.5pt 130pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 352.5pt; height: 130pt; background: #ffffff;
    font-family: 'Lora', Georgia, serif;
    -webkit-font-smoothing: antialiased;
}
.callout {
    width: 100%; background-color: #f8f8f8; border-left: 3.5px solid #000000;
    padding: 7pt 9pt;
}
.callout-title {
    font-family: 'Montserrat', sans-serif; font-size: 8.2pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.4px; margin-bottom: 3.5pt; color: #000000;
}
.callout p {
    font-size: 8.05pt; line-height: 11.2pt; color: #111111;
    text-align: justify; margin: 0;
}
</style>
</head>
<body>
<div class="callout">
    <div class="callout-title">▌ LE PIÈGE DE LA LOTERIE MANAGÉRIALE</div>
    <p>Pour le terrain, le management est une loterie aux conséquences directes sur la santé. Si certains encadrants jouent un rôle remarquable d'amortisseur, d'autres profilent une gestion par la terreur ou la manipulation feutrée. Quand un petit chef toxique «&nbsp;fait le chiffre&nbsp;», le système hiérarchique a tendance à le couvrir. C'est ce mécanisme qui explique que <strong>71 % des salariés victimes de harcèlement ne le signalent jamais à leur direction</strong> (Baromètre RH / Theragora)&nbsp;: l'institution est perçue comme protégeant ses cadres avant d'écouter ses exécutants.</p>
</div>
</body>
</html>'''
temp_p13_callout = os.path.join(SCRATCH, 'temp_p13_callout.html')
pdf_p13_callout = os.path.join(SCRATCH, 'p13_callout_run.pdf')
with open(temp_p13_callout, 'w', encoding='utf-8') as f:
    f.write(html_p13_callout)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p13_callout}', temp_p13_callout
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
p13_t = terrain_doc[12]
p13_t.add_redact_annot(fitz.Rect(30, 415, 390, 550), fill=(1, 1, 1))
p13_t.apply_redactions()
doc_callout_p13 = fitz.open(pdf_p13_callout)
p13_t.show_pdf_page(fitz.Rect(33.75, 418.0, 386.25, 418.0 + 130.0), doc_callout_p13, 0)
print("Applied surgical LA LOTERIE DU MANAGEMENT callout on Terrain page 13")

# Harmonisation complète Page 81 (Terrain) : Titre de chapitre standard + trait de séparation + calage bas
html_terrain_p81 = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Montserrat:wght@600;700;800&display=swap');
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 0 33.75pt;
    font-family: 'Lora', Georgia, serif; font-size: 9.15pt; line-height: 13.5pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
    display: flex; flex-direction: column; justify-content: flex-end;
}
.header-container {
    position: absolute; top: 43.7pt; left: 33.75pt; right: 33.75pt;
}
.chapter-title {
    font-family: 'Montserrat', sans-serif; font-size: 15.0pt; font-weight: 700;
    text-align: center; text-transform: uppercase; letter-spacing: 0.5px;
    color: #000000; margin-bottom: 9.5pt; line-height: 15.0pt;
}
.rule {
    width: 100%; height: 0.75pt; background-color: #18181b;
}
.body-container {
    margin-bottom: 70.92pt; /* 595.92 - 70.92 = 525.0pt */
}
p {
    font-size: 9.15pt; line-height: 13.5pt; text-align: justify;
    color: #111111; margin-bottom: 9pt; hyphens: auto; -webkit-hyphens: auto;
}
.ol-list {
    margin: 0; padding: 0; list-style: none; margin-bottom: 9pt;
}
.ol-item {
    font-size: 9.15pt; line-height: 13.5pt; text-align: justify;
    margin-bottom: 5.5pt; position: relative; padding-left: 13.5pt;
}
.ol-item:last-child {
    margin-bottom: 0;
}
.ol-num {
    position: absolute; left: 0; top: 0;
    font-family: 'Lora', Georgia, serif; font-weight: 700; color: #000000;
}
.ol-title {
    font-family: 'Lora', Georgia, serif; font-weight: 700; color: #000000;
}
.footer-page {
    position: absolute; bottom: 23pt; left: 0; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>

<div class="header-container">
    <div class="chapter-title">L'ILLUSION DE L'IA VUE D'EN BAS</div>
    <div class="rule"></div>
</div>

<div class="body-container">
    <p>L'arrivée de l'intelligence artificielle générative et de l'automatisation a déclenché une nouvelle vague d'anxiété — et d'incrédulité — sur le Terrain. Vue d'en bas, la promesse de l'IA ressemble étrangement à celle des vagues d'automatisation précédentes&nbsp;:</p>

    <div class="ol-list">
        <div class="ol-item">
            <span class="ol-num">1.</span> <span class="ol-title">L'IA ne comprend pas l'imprévu&nbsp;:</span> Un algorithme d'optimisation de tournée logistique ou de planning de soins raisonne sur un monde théorique où les camions ne tombent pas en panne, où les patients ne pleurent pas et où les pièces détachées arrivent à l'heure. Quand le réel déraille, c'est l'humain de Terrain qui colmate les brèches en silence, pendant que le système indique que tout est «&nbsp;sous contrôle&nbsp;».
        </div>
        <div class="ol-item">
            <span class="ol-num">2.</span> <span class="ol-title">Le paradoxe du contrôle automatisé&nbsp;:</span> L'IA est trop souvent utilisée comme un sur-flicage technologique (caméras intelligentes, analyse des temps de frappe, scoring d'appels en temps réel) qui détruit le peu d'autonomie restante.
        </div>
        <div class="ol-item">
            <span class="ol-num">3.</span> <span class="ol-title">Le scepticisme de l'artisan&nbsp;:</span> Le Terrain sait une chose que les concepteurs d'IA oublient&nbsp;: l'expertise métier réside dans les 10&nbsp;% d'exceptions que la machine ne sait pas traiter.
        </div>
    </div>

    <p>À l'Étage 6, l'Intelligence Artificielle est souvent pensée comme un outil de contrôle ou de réduction de coûts. Mais le Terrain n'est pas technophobe pour autant. Au contraire.</p>

    <p style="margin-bottom: 0;">Les équipes de première ligne savent mieux que quiconque quelles sont les tâches répétitives, purement administratives et chronophages qui vampirisent leur journée. Saisies multiples, formulaires redondants, <em>reportings</em> sans fin&nbsp;: voilà ce qu'ils aimeraient déléguer à la machine. Si l'IA était co-construite avec le Terrain, plutôt qu'imposée par le Sommet, elle rendrait enfin du temps aux gens — du temps pour l'empathie face à un client, la résolution de problèmes imprévus, et l'artisanat du métier.</p>
</div>

<div class="footer-page">81</div>

</body>
</html>'''

temp_p81_file = os.path.join(SCRATCH, 'temp_p81_terrain.html')
pdf_p81_file = os.path.join(SCRATCH, 'p81_terrain_run.pdf')
with open(temp_p81_file, 'w', encoding='utf-8') as f:
    f.write(html_terrain_p81)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p81_file}', temp_p81_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
p81_t = terrain_doc[80]
p81_t.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
p81_t.apply_redactions()
p81_t.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), fitz.open(pdf_p81_file), 0)
print("Applied chapter title and bottom-anchored layout on Terrain page 81")

# Calage au bas ("collé au bas") pour les ouvertures de chapitres côté Terrain
terrain_openings_shift = {
    5: (58.0, fitz.Rect(30, 155, 390, 520)),
    11: (28.0, fitz.Rect(30, 155, 390, 520)),
    19: (43.0, fitz.Rect(30, 155, 390, 520)),
    27: (13.5, fitz.Rect(30, 155, 390, 520)),
    35: (110.0, fitz.Rect(30, 155, 390, 520)),
    43: (60.0, fitz.Rect(30, 155, 390, 520)),
    61: (13.5, fitz.Rect(30, 155, 390, 520))
}
for pno, (dy, rect_src) in terrain_openings_shift.items():
    page = terrain_doc[pno - 1]
    page_copy = fitz.open()
    page_copy.insert_pdf(terrain_doc, from_page=pno-1, to_page=pno-1)
    page.add_redact_annot(rect_src, fill=(1, 1, 1))
    page.apply_redactions()
    rect_dst = fitz.Rect(rect_src.x0, rect_src.y0 + dy, rect_src.x1, rect_src.y1 + dy)
    page.show_pdf_page(rect_dst, page_copy, 0, clip=rect_src)
    print(f"Applied bottom-anchoring shift (dy=+{dy}pt) to Terrain page {pno}")

# ----------------------------------------------------
# 8.2 ENRICHISSEMENT & CALAGE DES PAGES 84, 85 & 101 (TERRAIN)
# ----------------------------------------------------
# Page 101 : Fiches pratiques - Répertoire aéré et équilibré
p101_terrain = terrain_doc[100]
p101_terrain.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
p101_terrain.apply_redactions()

html_p101_terrain = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 34.8pt 33.8pt 28pt 33.8pt;
    font-family: 'Lora', Georgia, serif; font-size: 9.15pt; line-height: 13.2pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}
.header {
    text-align: center; margin-bottom: 10pt;
}
h1 {
    font-family: 'Montserrat', sans-serif; font-size: 12pt; font-weight: 800;
    text-transform: uppercase; letter-spacing: 0.5px; color: #000000;
    line-height: 1.25; margin-bottom: 5pt;
}
.rule {
    width: 30pt; height: 1.4pt; background-color: #000000; margin: 0 auto 6pt auto;
}
.subtitle {
    font-family: 'Lora', Georgia, serif; font-size: 9.2pt; font-weight: 600;
    color: #222222; font-style: italic;
}
p.intro {
    text-align: justify; text-justify: inter-word; margin-bottom: 7pt; color: #111111;
}
.principle-box {
    background-color: #f8f9fa; border-left: 3px solid #000000;
    padding: 6.5pt 9pt; margin-bottom: 9pt; font-size: 8.6pt; line-height: 12.2pt;
}
.principle-box strong {
    font-family: 'Montserrat', sans-serif; font-size: 7.4pt; text-transform: uppercase; letter-spacing: 0.3px;
    display: block; margin-bottom: 2pt; color: #000000;
}
.section-title {
    font-family: 'Montserrat', sans-serif; font-size: 8.6pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.4px; color: #000000;
    margin-bottom: 5pt; display: flex; align-items: center;
}
table {
    width: 100%; border-collapse: collapse; font-size: 8.2pt; margin-bottom: 7pt;
}
th {
    font-family: 'Montserrat', sans-serif; font-size: 7pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; background-color: #f1f5f9;
    border-top: 1.2pt solid #000000; border-bottom: 1.2pt solid #000000;
    padding: 3.8pt 5pt; text-align: left; color: #000000;
}
td {
    padding: 3.5pt 5pt; border-bottom: 0.6pt solid #e5e7eb; color: #111111;
}
tr:last-child td { border-bottom: 1.2pt solid #000000; }
td.num {
    font-family: 'Montserrat', sans-serif; font-weight: 700; color: #000000; width: 22pt;
}
td.action {
    font-weight: 600; color: #000000;
}
td.target {
    color: #4b5563; font-size: 7.8pt;
}
td.horizon {
    font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 7.4pt; color: #111111; text-align: right;
}
th:last-child { text-align: right; }
.footer-note {
    font-size: 8pt; font-style: italic; color: #555555; text-align: justify; line-height: 11.5pt;
}
.page-number {
    position: absolute; bottom: 24pt; left: 0; width: 100%; text-align: center;
    font-family: 'Lora', Georgia, serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>

<div class="header">
    <h1>FICHES PRATIQUES — PAR OÙ COMMENCER</h1>
    <div class="rule"></div>
    <div class="subtitle">Sept actions concrètes pour transformer le quotidien dès lundi matin</div>
</div>

<p class="intro">Ce chapitre rassemble <strong>sept protocoles d'action autonome</strong> conçus pour être activés directement sur le terrain, sans solliciter de budget supplémentaire ni attendre une hypothétique autorisation d'étage. Chaque fiche répond à une asphyxie organisationnelle précise observée dans la tour.</p>

<div class="principle-box">
    <strong>La règle d'or du terrain</strong>
    «&nbsp;Ne demandez pas la permission de simplifier ce qui relève de votre zone d'action. Expérimentez localement, mesurez les gains d'énergie et de temps, puis laissez les résultats convaincre par capillarité.&nbsp;»
</div>

<div class="section-title">▌ RÉPERTOIRE DES 7 FICHES D'ACTION</div>

<table>
    <thead>
        <tr>
            <th style="width:8%;">N°</th>
            <th style="width:42%;">Intitulé de l'action</th>
            <th style="width:32%;">Cible prioritaire</th>
            <th style="width:18%;">Horizon</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="num">01</td>
            <td class="action">L'Audit de Réunions</td>
            <td class="target">Tout manager & équipe saturée</td>
            <td class="horizon">1 semaine</td>
        </tr>
        <tr>
            <td class="num">02</td>
            <td class="action">La Semaine Inversée</td>
            <td class="target">Cadres, directeurs & fonctions support</td>
            <td class="horizon">1 jour / mois</td>
        </tr>
        <tr>
            <td class="num">03</td>
            <td class="action">La Transparence Progressive</td>
            <td class="target">Managers de service & chefs de pôle</td>
            <td class="horizon">6 mois</td>
        </tr>
        <tr>
            <td class="num">04</td>
            <td class="action">Le Coordinateur Tournant</td>
            <td class="target">Équipes projet de 5 à 20 personnes</td>
            <td class="horizon">1 mois / cycle</td>
        </tr>
        <tr>
            <td class="num">05</td>
            <td class="action">Le Budget Décentralisé</td>
            <td class="target">Responsables de pôle opérationnel</td>
            <td class="horizon">Immédiat</td>
        </tr>
        <tr>
            <td class="num">06</td>
            <td class="action">Le REX Sans Blâme</td>
            <td class="target">Opérations, Technique & Sécurité</td>
            <td class="horizon">Après incident</td>
        </tr>
        <tr>
            <td class="num">07</td>
            <td class="action">La Décision par Consentement</td>
            <td class="target">Collectifs et équipes autonomes</td>
            <td class="horizon">Continu</td>
        </tr>
    </tbody>
</table>

<p class="footer-note">Chaque fiche détaille son objectif précis, son public cible, son protocole d'application pas à pas, son résultat mesurable et le repère clé issu du terrain.</p>

<div class="page-number">101</div>

</body>
</html>'''

temp_p101_file = os.path.join(SCRATCH, 'temp_p101_terrain.html')
pdf_p101_file = os.path.join(SCRATCH, 'p101_terrain.pdf')
with open(temp_p101_file, 'w', encoding='utf-8') as f:
    f.write(html_p101_terrain)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p101_file}', temp_p101_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
p101_terrain.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), fitz.open(pdf_p101_file), 0)
print("Applied harmonized layout on Terrain page 101 (FICHES PRATIQUES)")

# Page 84 : Et si ? Le monde d'après - Buurtzorg avec tableau d'impact
p84_terrain = terrain_doc[83]
p84_terrain.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
p84_terrain.apply_redactions()

html_p84_terrain = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 34.8pt 33.8pt 28pt 33.8pt;
    font-family: 'Lora', Georgia, serif; font-size: 9.15pt; line-height: 13.2pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}
.header {
    text-align: center; margin-bottom: 9pt;
}
h1 {
    font-family: 'Montserrat', sans-serif; font-size: 12pt; font-weight: 800;
    text-transform: uppercase; letter-spacing: 0.5px; color: #000000;
    line-height: 1.2; margin-bottom: 4pt;
}
.rule {
    width: 28pt; height: 1.4pt; background-color: #000000; margin: 0 auto 5pt auto;
}
.subtitle {
    font-family: 'Lora', Georgia, serif; font-size: 9pt; font-weight: 600;
    color: #222222; font-style: italic;
}
p {
    text-align: justify; text-justify: inter-word; margin-bottom: 5.5pt; color: #111111;
}
h2 {
    font-family: 'Montserrat', sans-serif; font-size: 8.6pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; color: #000000;
    margin-top: 8pt; margin-bottom: 2pt;
}
.date-loc {
    font-family: 'Montserrat', sans-serif; font-size: 7.2pt; font-weight: 700;
    color: #555555; text-transform: uppercase; letter-spacing: 0.3px; margin-bottom: 4pt;
}
ul.scope-list {
    margin: 3pt 0 6pt 14pt; padding: 0; font-size: 8.6pt; line-height: 12.4pt;
}
ul.scope-list li {
    margin-bottom: 1.5pt;
}
table {
    width: 100%; border-collapse: collapse; margin-top: 5pt; margin-bottom: 5pt; font-size: 7.8pt; line-height: 11pt;
}
th {
    font-family: 'Montserrat', sans-serif; font-size: 6.8pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; background-color: #f1f5f9;
    border-top: 1.2pt solid #000000; border-bottom: 1.2pt solid #000000;
    padding: 3pt 4pt; text-align: left; color: #000000;
}
td {
    border-bottom: 0.5pt solid #e5e7eb; padding: 2.5pt 4pt; text-align: left;
}
tr:last-child td { border-bottom: 1.2pt solid #000000; }
.conclusion {
    font-size: 8.3pt; font-style: italic; color: #333333; margin-top: 5pt; margin-bottom: 0; line-height: 11.8pt; text-align: justify;
}
.page-number {
    position: absolute; bottom: 24pt; left: 0; width: 100%; text-align: center;
    font-family: 'Lora', Georgia, serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>

<div class="header">
    <h1>ET SI&nbsp;? LE MONDE D'APRÈS</h1>
    <div class="rule"></div>
    <div class="subtitle">Les alternatives qui existent déjà — et que la tour refuse de voir</div>
</div>

<p>Tout ce que nous avons décrit jusqu'ici — la tour, les étages, la déconnexion, le départ des jeunes — pourrait donner envie de baisser les bras. De se résigner&nbsp;: «&nbsp;C'est comme ça. Le système est trop lourd.&nbsp;» Ce chapitre prouve le contraire.</p>

<p>Partout dans le monde, des organisations rentables et robustes fonctionnent sans tour, sans hiérarchie pyramidale et sans strates de reporting. Ce ne sont pas des utopies&nbsp;: ce sont des adresses postales.</p>

<h2>▌ 1. BUURTZORG — LES SOIGNANTS QUI SE SONT LIBÉRÉS</h2>
<div class="date-loc">Pays-Bas, 2006 • Fondé par Jos de Blok</div>

<p>Après des années dans un système de santé étouffé sous les protocoles et les réunions, Jos de Blok crée Buurtzorg («&nbsp;soins de quartier&nbsp;»). Le principe est sans appel&nbsp;: <strong>zéro manager intermédiaire</strong>. Des équipes de 10 à 12 infirmiers autonomes s'auto-organisent intégralement&nbsp;:</p>

<ul class="scope-list">
    <li>Gestion autonome des plannings et des soins aux patients</li>
    <li>Recrutement direct des pairs et gestion intégrale du budget local</li>
    <li>Résolution directe des difficultés sans arbitrage hiérarchique</li>
</ul>

<table>
    <thead>
        <tr>
            <th style="width:38%;">Indicateur clé</th>
            <th style="width:31%;">Système classique</th>
            <th style="width:31%;">Buurtzorg</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Satisfaction patients</td>
            <td>Moyenne sectorielle</td>
            <td><strong>La plus élevée du pays</strong></td>
        </tr>
        <tr>
            <td>Satisfaction employés</td>
            <td>Basse (turnover fort)</td>
            <td><strong>La plus élevée du secteur</strong></td>
        </tr>
        <tr>
            <td>Coûts de gestion / patient</td>
            <td>Élevés</td>
            <td><strong>-40 % d'économies réelles</strong></td>
        </tr>
        <tr>
            <td>Taux d'absentéisme</td>
            <td>Élevé</td>
            <td><strong>-60 % par rapport au secteur</strong></td>
        </tr>
        <tr>
            <td>Échelle opérationnelle</td>
            <td>Multiples directeurs</td>
            <td><strong>15 000 soignants sans chefs</strong></td>
        </tr>
    </tbody>
</table>

<p class="conclusion">«&nbsp;Les soignants savent ce qu'ils font. Il suffit de leur faire confiance.&nbsp;» Exactement ce que le terrain affirme depuis le début.</p>

<div class="page-number">84</div>

</body>
</html>'''

temp_p84_file = os.path.join(SCRATCH, 'temp_p84_terrain.html')
pdf_p84_file = os.path.join(SCRATCH, 'p84_terrain.pdf')
with open(temp_p84_file, 'w', encoding='utf-8') as f:
    f.write(html_p84_terrain)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p84_file}', temp_p84_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
p84_terrain.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), fitz.open(pdf_p84_file), 0)
print("Applied harmonized layout on Terrain page 84 (ET SI ? LE MONDE D'APRÈS)")

# 0.2 Terrain Page 83 : Harmonisation de la page de souffle (transition)
p83_terrain = terrain_doc[82]
p83_terrain.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
p83_terrain.apply_redactions()

html_p83_terrain_breath = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;1,400&family=Montserrat:wght@600;700&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    display: flex; flex-direction: column; justify-content: flex-end; align-items: center;
    padding: 0 45pt 82pt 45pt; position: relative; -webkit-font-smoothing: antialiased;
}
.rule { width: 80pt; height: 1.2pt; background-color: #8da4be; margin-bottom: 16pt; }
p {
    font-family: 'Lora', Georgia, serif; font-size: 11.5pt; font-style: italic; line-height: 17pt;
    text-align: center; color: #1e293b; margin: 0;
}
.callout-transition {
    font-family: 'Lora', Georgia, serif; font-style: italic; font-size: 8.8pt;
    line-height: 13pt; color: #64748b; text-align: center; margin-top: 14pt;
}
.page-number { position: absolute; bottom: 24pt; left: 0; width: 100%; text-align: center; font-family: 'Lora', Georgia, serif; font-size: 8.5pt; color: #666666; }
</style>
</head>
<body>
<div class="rule"></div>
<p>«&nbsp;Le système ne change pas parce qu'on lui demande gentiment.<br>Il change parce que la réalité finit toujours par s'imposer.&nbsp;»</p>
<div class="callout-transition">[ L'ascenseur est en panne. Plus personne n'appuie sur le bouton. ]</div>
<div class="page-number">83</div>
</body>
</html>'''

temp_p83_t_file = os.path.join(SCRATCH, 'temp_terrain_p83_breath.html')
pdf_p83_t_file = os.path.join(SCRATCH, 'p83_terrain_breath.pdf')
with open(temp_p83_t_file, 'w', encoding='utf-8') as f:
    f.write(html_p83_terrain_breath)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p83_t_file}', temp_p83_t_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_p83_t = fitz.open(pdf_p83_t_file)
p83_terrain.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), doc_p83_t, 0)
print("Applied harmonized breath page on Terrain page 83")

# 1. Terrain Page 85 : Grand cas atelier W.L. Gore (L'atelier en treillis sans petits chefs)
p85_terrain = terrain_doc[84]
p85_terrain.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
p85_terrain.apply_redactions()

html_p85_terrain_full = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 34.8pt 33.8pt 28pt 33.8pt;
    font-family: 'Lora', Georgia, serif; font-size: 9.15pt; line-height: 13.5pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}
h2 {
    font-family: 'Montserrat', sans-serif; font-size: 8.8pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.35px; color: #000000;
    margin-top: 0; margin-bottom: 3pt;
}
.date-loc {
    font-family: 'Montserrat', sans-serif; font-size: 7.2pt; font-weight: 700;
    color: #555555; text-transform: uppercase; letter-spacing: 0.3px; margin-bottom: 8pt;
}
p {
    text-align: justify; text-justify: inter-word; margin-bottom: 8pt; color: #111111;
}
.results-box {
    background-color: #f8f9fa; border-left: 3px solid #000000;
    padding: 8pt 10pt; margin: 9pt 0 10pt 0; font-size: 8.7pt; line-height: 12.8pt;
}
.results-box strong {
    font-family: 'Montserrat', sans-serif; font-size: 7.5pt; text-transform: uppercase; letter-spacing: 0.3px;
    display: block; margin-bottom: 4pt; color: #000000;
}
ul.results-list {
    margin: 0 0 0 12pt; padding: 0; font-size: 8.7pt; line-height: 12.8pt;
}
ul.results-list li {
    margin-bottom: 3pt;
}
.quote-box {
    background-color: #f1f5f9; border-left: 3.5px solid #2563eb;
    padding: 9pt 11pt; margin-top: 12pt; font-style: italic; font-size: 8.9pt; line-height: 13.2pt; color: #0f172a; text-align: justify;
}
.page-number {
    position: absolute; bottom: 24pt; left: 0; width: 100%; text-align: center;
    font-family: 'Lora', Georgia, serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>

<h2>▌ 2. W.L. GORE — L'ATELIER EN TREILLIS SANS PETITS CHEFS</h2>
<div class="date-loc">Delaware, États-Unis • Fondé en 1958 par Bill Gore</div>

<p>W.L. Gore & Associates fabrique des membranes industrielles haute performance (Gore-Tex), des implants chirurgicaux vitaux et des câbles pour l'aérospatiale. C'est de l'industrie technologique de pointe comptant plus de 13&nbsp;000 collaborateurs. Dès l'origine, Bill Gore a instauré une règle non négociable&nbsp;: <strong>aucun site ne dépasse 150 personnes</strong>. Au-delà, l'humain s'efface et la tentation bureaucratique réintroduit des chefs.</p>

<p>Chez Gore, l'organisation fonctionne selon une structure en «&nbsp;treillis&nbsp;» intégralement horizontale&nbsp;: aucun organigramme figé, aucune ligne hiérarchique verticale, aucun titre honorifique. Les équipes de fabrication s'organisent librement par projets selon les urgences du carnet de commandes. Les leaders ne sont pas nommés par un comité exécutif lointain&nbsp;: ils émergent naturellement parce que leurs pairs choisissent volontairement de travailler avec eux.</p>

<div class="results-box">
    <strong>Les performances concrètes de l'auto-organisation&nbsp;:</strong>
    <ul class="results-list">
        <li>Entreprise mondialement rentable chaque année sans interruption depuis plus de 60 ans.</li>
        <li>Plus de 2&nbsp;000 brevets technologiques majeurs déposés directement par les équipes de terrain.</li>
        <li>Absentéisme et rotation du personnel parmi les plus bas de toute l'industrie américaine.</li>
    </ul>
</div>

<p>Les opérateurs et techniciens participent directement au choix des investissements et cooptent leurs futurs collègues. La confiance n'est pas un slogan de ressources humaines&nbsp;: c'est le moteur direct de la productivité.</p>

<div class="quote-box">
    «&nbsp;La liberté d'expérimenter et la cooptation par les pairs transforment chaque associé en propriétaire attentif de son atelier.&nbsp;»
</div>

<div class="page-number">85</div>

</body>
</html>'''

temp_p85_t_file = os.path.join(SCRATCH, 'temp_terrain_p85_gore.html')
pdf_p85_t_file = os.path.join(SCRATCH, 'p85_terrain_gore.pdf')
with open(temp_p85_t_file, 'w', encoding='utf-8') as f:
    f.write(html_p85_terrain_full)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p85_t_file}', temp_p85_t_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_p85_t = fitz.open(pdf_p85_t_file)
p85_terrain.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), doc_p85_t, 0)
print("Applied W.L. Gore case on Terrain page 85")

# 1.1 Nettoyage du haut de la page 86 (suppression du reliquat de paragraphe sur Zobrist)
p86_terrain = terrain_doc[85]
p86_terrain.add_redact_annot(fitz.Rect(30, 30, 390, 80), fill=(1, 1, 1))
p86_terrain.apply_redactions()
print("Cleaned top of Terrain page 86")

# 1.2 Transformation de la Page 91 en page de souffle avec citation W.L. Gore
p91_terrain = terrain_doc[90]
p91_terrain.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
p91_terrain.apply_redactions()

html_p91_terrain_quote = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@1,400;1,500&family=Montserrat:wght@600;700&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    display: flex; flex-direction: column; justify-content: flex-end; align-items: center;
    padding: 0 45pt 82pt 45pt; position: relative; -webkit-font-smoothing: antialiased;
}
.rule { width: 80pt; height: 1.2pt; background-color: #8da4be; margin-bottom: 16pt; }
.quote {
    font-family: 'Lora', Georgia, serif; font-style: italic; font-size: 9.6pt;
    line-height: 14.5pt; text-align: center; color: #27272a; max-width: 320pt; margin-bottom: 13pt;
}
.attribution {
    font-family: 'Montserrat', sans-serif; font-size: 7.2pt; font-weight: 700;
    letter-spacing: 1.5px; text-transform: uppercase; color: #64748b; text-align: center;
}
.footer-page {
    position: absolute; bottom: 23pt; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>
<div class="rule"></div>
<div class="quote">« Les meilleures décisions naissent toujours là où la matière rencontre la main, jamais dans le bureau de celui qui n'en subit pas les conséquences. »</div>
<div class="attribution">— W.L. GORE &amp; ASSOCIATES — PRINCIPE DU TREILLIS</div>
<div class="footer-page">91</div>
</body>
</html>'''

temp_p91_t_file = os.path.join(SCRATCH, 'temp_terrain_p91_quote.html')
pdf_p91_t_file = os.path.join(SCRATCH, 'p91_terrain_quote.pdf')
with open(temp_p91_t_file, 'w', encoding='utf-8') as f:
    f.write(html_p91_terrain_quote)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p91_t_file}', temp_p91_t_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_p91_t = fitz.open(pdf_p91_t_file)
p91_terrain.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), doc_p91_t, 0)
print("Applied breath quote page on Terrain page 91")

# 2. Terrain Page 111 : Transition incrémentale W.L. Gore
p111_terrain = terrain_doc[110]
p111_terrain.add_redact_annot(fitz.Rect(0, 0, 420, 595.92), fill=(1, 1, 1))
p111_terrain.apply_redactions()

html_p111_terrain_full = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400;1,700&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
<style>
@page { size: 420pt 595.92pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 420pt; height: 595.92pt; background: #ffffff;
    padding: 34.8pt 33.8pt 30pt 33.8pt;
    font-family: 'Lora', Georgia, serif; font-size: 8.9pt; line-height: 13.2pt;
    color: #111111; -webkit-font-smoothing: antialiased; position: relative;
}
p {
    text-align: justify; text-justify: inter-word; margin-bottom: 7pt;
}
h2 {
    font-family: 'Montserrat', sans-serif; font-size: 9.3pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.3px; color: #000000;
    margin-top: 9pt; margin-bottom: 5pt; line-height: 12.5pt;
}
.callout {
    width: 100%; background-color: #f8f8f8; border-left: 3.5px solid #000000;
    padding: 7pt 10pt; margin: 8pt 0;
}
.callout-title {
    font-family: 'Montserrat', sans-serif; font-size: 7.8pt; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 3pt; color: #000000;
}
.callout p {
    font-size: 8.3pt; font-style: italic; line-height: 12.3pt; margin-bottom: 0;
}
.page-number {
    position: absolute; bottom: 23pt; left: 0; width: 100%; text-align: center;
    font-family: 'Helvetica', Arial, sans-serif; font-size: 8.5pt; color: #666666;
}
</style>
</head>
<body>

<p>Chez W.L. Gore, la référence mondiale de l'industrie sans hiérarchie, la transformation s'est bâtie sur la durée. Bill Gore n'a pas envoyé de mémo révolutionnaire. Il a commencé par une décision concrète&nbsp;: limiter chaque usine à 150 personnes pour préserver le contact humain direct. Puis il a supprimé les titres hiérarchiques et instauré le parrainage volontaire. Les ouvriers et techniciens, responsabilisés, ont pris en main leurs plannings et leurs investissements d'atelier. Étape par étape, preuve par preuve.</p>

<p>On ne démantèle pas une tour de 9 étages en un jour. On la transforme pièce par pièce, étage par étage.</p>

<p>La leçon est universelle&nbsp;: le changement qui tient est celui qui se construit par la démonstration, pas par le décret. Vous ne convaincrez jamais un directeur avec un livre (même celui-ci). Vous le convaincrez avec des résultats. Des chiffres. Des faits. Un pilote qui marche, dans un coin de l'entreprise, que personne ne peut ignorer.</p>

<div class="callout">
    <div class="callout-title">▌ LE SAVIEZ-VOUS ?</div>
    <p>Les recherches en psychologie organisationnelle (Kotter, 1996 ; Higgs &amp; Rowland, 2005) montrent que 70&nbsp;% des projets de transformation échouent — et que les causes principales sont le manque d'implication des équipes terrain, un rythme trop brutal et l'absence de victoires rapides. Le changement qui réussit est presque toujours incrémental, volontaire et mesurable.</p>
</div>

<h2>2. LA LOGIQUE DES CERCLES CONCENTRIQUES</h2>

<p>Si le Grand Soir ne marche pas, qu'est-ce qui marche&nbsp;? Un modèle simple, testé dans des dizaines d'organisations&nbsp;: les cercles concentriques. Imaginez un caillou jeté dans l'eau. Il crée un premier cercle, petit, puis un deuxième, plus grand, puis un troisième. Chaque cercle naît du précédent. La transition fonctionne exactement comme ça&nbsp;:</p>

<p><strong>Cercle 1&nbsp;: UNE équipe (3-6 mois).</strong> Tout commence par une seule équipe. Pas un département. Pas un service. Une équipe. Cinq à quinze personnes volontaires. Règle absolue&nbsp;: cette équipe doit être volontaire. Jamais désignée. Jamais forcée. Si vous devez contraindre les gens pour les rendre autonomes, votre démarche est faussée d'avance. Cette équipe pilote reçoit un cadre clair&nbsp;: des objectifs mesurables (qualité, délais, satisfaction client, climat interne).</p>

<div class="page-number">111</div>

</body>
</html>'''

temp_p111_t_file = os.path.join(SCRATCH, 'temp_terrain_p111_gore.html')
pdf_p111_t_file = os.path.join(SCRATCH, 'p111_terrain_gore.pdf')
with open(temp_p111_t_file, 'w', encoding='utf-8') as f:
    f.write(html_p111_terrain_full)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_p111_t_file}', temp_p111_t_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_p111_t = fitz.open(pdf_p111_t_file)
p111_terrain.show_pdf_page(fitz.Rect(0, 0, 420, 595.92), doc_p111_t, 0)
print("Applied W.L. Gore case on Terrain page 111")

# 3. Terrain Page 114 : Callout W.L. Gore sur l'absence de pointeuse
p114_terrain = terrain_doc[113]
p114_terrain.add_redact_annot(fitz.Rect(30, 405, 395, 525), fill=(1, 1, 1))
p114_terrain.apply_redactions()

html_box_p114_gore = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;1,400&family=Montserrat:wght@700&display=swap');
@page { size: 352.4pt 98pt; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 352.4pt; height: 98pt;
    font-family: 'Lora', Georgia, serif;
    background: #ffffff;
    -webkit-font-smoothing: antialiased;
}
.callout {
    width: 100%; height: 98pt;
    background-color: #f8f8f8;
    border-left: 3.5px solid #000000;
    padding: 7pt 10pt;
}
.callout-title {
    font-family: 'Montserrat', sans-serif;
    font-size: 7.8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4pt;
    color: #000000;
}
.callout p {
    font-family: 'Lora', Georgia, serif;
    font-size: 8.2pt;
    font-style: italic;
    line-height: 1.30;
    color: #111111;
    text-align: justify;
}
</style>
</head>
<body>
<div class="callout">
    <div class="callout-title">▌ LE SAVIEZ-VOUS ?</div>
    <p>Chez W.L. Gore, l'absence totale de pointeuses et de contrôle horaire bureaucratique n'a jamais créé d'abus : le taux d'absentéisme y est historiquement inférieur à 2 %, contre plus de 5 % dans l'industrie traditionnelle. Pourquoi ? Parce que la confiance responsabilise : quand vos pairs comptent sur vous pour livrer le projet de l'atelier, la réciprocité est un ressort infiniment plus puissant qu'un badge électronique.</p>
</div>
</body>
</html>'''

temp_box_p114_file = os.path.join(SCRATCH, 'temp_box_p114_gore.html')
pdf_box_p114_file = os.path.join(SCRATCH, 'box_p114_gore_run.pdf')
with open(temp_box_p114_file, 'w', encoding='utf-8') as f:
    f.write(html_box_p114_gore)
subprocess.run([
    CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_box_p114_file}', temp_box_p114_file
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc_box_p114 = fitz.open(pdf_box_p114_file)
p114_terrain.show_pdf_page(fitz.Rect(33.8, 412.0, 33.8 + 352.4, 412.0 + 98.0), doc_box_p114, 0)
print("Applied W.L. Gore callout on Terrain page 114")

# 4. In-place benchmark replacements on Pages 92, 109, 116, 126
# Page 92
p92_t = terrain_doc[91]
r92 = p92_t.search_for("FAVI,")[0]
p92_t.add_redact_annot(fitz.Rect(r92.x0 - 0.5, r92.y0 - 0.5, r92.x1 + 0.5, r92.y1 + 0.5), fill=(1, 1, 1))
p92_t.apply_redactions()
p92_t.insert_text(fitz.Point(r92.x0, r92.y1 - 2.2), "Gore,", fontsize=9.15, fontname="tiro", color=(0.07, 0.07, 0.07))

# Page 109
p109_t = terrain_doc[108]
r109 = p109_t.search_for("FAVI,")[0]
p109_t.add_redact_annot(fitz.Rect(r109.x0 - 0.5, r109.y0 - 0.5, r109.x1 + 0.5, r109.y1 + 0.5), fill=(1, 1, 1))
p109_t.apply_redactions()
p109_t.insert_text(fitz.Point(r109.x0, r109.y1 - 2.2), "Gore,", fontsize=9.15, fontname="tiro", color=(0.07, 0.07, 0.07))

# Page 116
p116_t = terrain_doc[115]
r116 = p116_t.search_for("FAVI,")[0]
p116_t.add_redact_annot(fitz.Rect(r116.x0 - 0.5, r116.y0 - 0.5, r116.x1 + 0.5, r116.y1 + 0.5), fill=(1, 1, 1))
p116_t.apply_redactions()
p116_t.insert_text(fitz.Point(r116.x0, r116.y1 - 2.2), "Gore,", fontsize=9.15, fontname="tiro", color=(0.07, 0.07, 0.07))

# Page 126
p126_t = terrain_doc[125]
r126_line = p126_t.search_for("Voici ce que Buurtzorg a obtenu. Voici ce que FAVI a mesuré. On")[0]
p126_t.add_redact_annot(fitz.Rect(r126_line.x0 - 0.5, r126_line.y0 - 0.5, r126_line.x1 + 0.5, r126_line.y1 + 0.5), fill=(1, 1, 1))
p126_t.apply_redactions()
p126_t.insert_text(fitz.Point(r126_line.x0, r126_line.y1 - 2.2), "Voici ce que Buurtzorg a obtenu. Voici ce que Gore a mesuré. On", fontsize=8.9, fontname="tiro", color=(0.07, 0.07, 0.07))
print("Updated all benchmark occurrences on Terrain pages 92, 109, 116, 126")

# Standardize all footers across all numbered pages of Terrain
terrain_doc = standardize_all_footers(terrain_doc)

tmp_path = out_terrain_path + '.tmp'
terrain_doc.save(tmp_path)
terrain_doc.close()
os.replace(tmp_path, out_terrain_path)
terrain_doc = fitz.open(out_terrain_path)

print(f"🎉 SUCCÈS : {out_terrain_path} ({len(terrain_doc)} pages)")

# ----------------------------------------------------
# 9. ASSEMBLAGE MANUSCRIT INTÉGRAL TÊTE-BÊCHE
# ----------------------------------------------------
print("Assembling complete tête-bêche volume...")

# Check for QR center page or generate it
qr_pdf_path = os.path.join(SCRATCH, 'qr_center.pdf')
if not os.path.exists(qr_pdf_path):
    # build clean center page
    html_qr = '''<!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&family=Merriweather:ital,wght@0,400;1,300&display=swap');
    @page { size: 148mm 210mm; margin: 0; }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
        width: 148mm; height: 210mm; display: flex; flex-direction: column;
        background: #ffffff; font-family: 'Montserrat', sans-serif;
    }
    .half-top {
        flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-end;
        padding: 8mm 12mm 6mm; transform: rotate(180deg); border-bottom: 1px solid #e2e8f0;
    }
    .half-bottom {
        flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-end;
        padding: 8mm 12mm 6mm; border-top: 1px solid #e2e8f0;
    }
    .book-title {
        font-size: 9.5pt; font-weight: 700; letter-spacing: 3px; text-transform: uppercase;
        color: #18181b; margin-bottom: 3px;
    }
    .book-subtitle {
        font-family: 'Merriweather', serif; font-style: italic; font-size: 8pt;
        color: #64748b; margin-bottom: 8px; text-align: center;
    }
    .flip-line {
        font-size: 7.5pt; letter-spacing: 2px; text-transform: uppercase;
        color: #94a3b8; font-weight: 600; margin-bottom: 3px;
    }
    .arrow-line { font-size: 11pt; color: #cbd5e1; }
    .center-band {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        padding: 8mm 14mm; gap: 3.5mm; background: #f8fafc;
        border-top: 1.5px solid #09090b; border-bottom: 1.5px solid #09090b;
    }
    .url { font-size: 11pt; font-weight: 700; letter-spacing: 1.5px; color: #09090b; text-align: center; }
    .desc {
        font-family: 'Merriweather', serif; font-size: 8.5pt; color: #475569;
        line-height: 1.5; max-width: 95mm; text-align: center; font-style: italic;
    }
    </style>
    </head>
    <body>
    <div class="half-top">
        <div class="arrow-line">↓</div>
        <div class="flip-line">Retournez le livre pour l'autre versant</div>
        <div class="book-subtitle">Les 9 Étages — Du terrain au sommet</div>
        <div class="book-title">Les 9 Étages</div>
    </div>
    <div class="center-band">
        <div class="url">padlet.com/les9etages</div>
        <div class="desc">Un espace de libre échange entre lecteurs, praticiens et observateurs des organisations.</div>
    </div>
    <div class="half-bottom">
        <div class="book-title">Les 9 Étages</div>
        <div class="book-subtitle">Du sommet au terrain — Les 9 Étages</div>
        <div class="flip-line">Retournez le livre pour l'autre versant</div>
        <div class="arrow-line">↑</div>
    </div>
    </body>
    </html>'''
    render_html_to_pdf(html_qr, qr_pdf_path)

final_complet = fitz.open()

# 1. Terrain normal
terrain_doc = fitz.open(out_terrain_path)
final_complet.insert_pdf(terrain_doc)

# 2. QR / Transition au milieu
qr_doc = fitz.open(qr_pdf_path)
final_complet.insert_pdf(qr_doc)

# 3. Sommet tête-bêche (pages inversées et tournées à 180°)
sommet_doc = fitz.open(out_sommet_path)
for pno in range(len(sommet_doc) - 1, -1, -1):
    final_complet.insert_pdf(sommet_doc, from_page=pno, to_page=pno)
    # rotate last inserted page by 180
    final_complet[-1].set_rotation(180)

out_complet_path = os.path.join(V3_DIR, 'Les_9_Etages_Livre_Complet.pdf')
final_complet.save(out_complet_path)
print(f"🎉 SUCCÈS : {out_complet_path} ({len(final_complet)} pages totales) !")
print("Terrain:", len(terrain_doc), "+ Transition: 1 + Sommet:", len(sommet_doc))

# Mirror copies to project root directory
print("Updating root desktop mirror files...")
shutil.copy2(out_sommet_path, '/Users/basile/Desktop/Les-9-etages/sommet.pdf')
shutil.copy2(out_sommet_path, '/Users/basile/Desktop/Les-9-etages/LES_9_ETAGES_SOMMET.pdf')
shutil.copy2(out_complet_path, '/Users/basile/Desktop/Les-9-etages/tete_beche.pdf')
print("✅ Root desktop mirrors updated successfully!")
