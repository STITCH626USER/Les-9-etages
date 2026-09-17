const fs = require('fs');
const puppeteer = require('puppeteer');
const { PDFDocument } = require('pdf-lib');

const css = `
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&family=Merriweather:ital,wght@0,400;1,300&display=swap');
body {
    font-family: 'Montserrat', sans-serif;
    padding: 10mm 15mm;
    margin: 0;
    color: #1a1a1a;
    background: #ffffff;
    font-size: 10.5px;
    line-height: 1.4;
}
h1 {
    font-size: 14px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 20px;
    border-bottom: 1px solid #000;
    padding-bottom: 5px;
}
h3 {
    font-size: 11px;
    font-weight: 700;
    color: #444;
    margin-top: 15px;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.toc-line {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 4px;
}
.toc-text {
    background: #fff;
    padding-right: 5px;
}
.toc-dots {
    flex-grow: 1;
    border-bottom: 1px dotted #999;
    margin: 0 5px;
    position: relative;
    top: -4px;
}
.toc-page {
    background: #fff;
    padding-left: 5px;
    font-weight: 600;
}
strong { font-weight: 700; }
`;

const sommet_toc = `
<h1>TABLE DES MATIÈRES — CÔTÉ SOMMET</h1>
<div class="toc-line"><span class="toc-text"><strong>PROLOGUE : Demain, le terrain ne répond plus</strong></span><span class="toc-dots"></span><span class="toc-page">5</span></div>
<h3>PARTIE I : LA DESCENTE DE LA TOUR</h3>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 8 — Le CEO :</strong> La vue panoramique et l'isolement doré</span><span class="toc-dots"></span><span class="toc-page">7</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 7 — Le Chairman :</strong> La mémoire effacée et le glissement des loyautés</span><span class="toc-dots"></span><span class="toc-page">13</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 6 — Le Président International :</strong> L'illusion du contrôle global</span><span class="toc-dots"></span><span class="toc-page">19</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 5 — Le Président de Division :</strong> La fabrique des Town Halls</span><span class="toc-dots"></span><span class="toc-page">25</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 4 — Le Vice-Président :</strong> L'arbitrage budgétaire et les territoires</span><span class="toc-dots"></span><span class="toc-page">31</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 3 — Le Directeur de Site :</strong> L'étau entre le siège et l'émeute</span><span class="toc-dots"></span><span class="toc-page">37</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 2 — Le Responsable de Service :</strong> Le management par tableur</span><span class="toc-dots"></span><span class="toc-page">43</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 1 — Le Manager de Proximité :</strong> Le choc des deux mondes</span><span class="toc-dots"></span><span class="toc-page">49</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 0 — Le Retour au Réel :</strong> La redécouverte du travail vivant</span><span class="toc-dots"></span><span class="toc-page">55</span></div>
<h3>PARTIE II : LES LEVIERS DE LA TRANSFORMATION</h3>
<div class="toc-line"><span class="toc-text"><strong>Vue d'ensemble :</strong> La carte des pouvoirs réels & Subsidiarité</span><span class="toc-dots"></span><span class="toc-page">59</span></div>
<div class="toc-line"><span class="toc-text"><strong>Les Générations vues du Sommet :</strong> Diriger 4 générations sans clichés</span><span class="toc-dots"></span><span class="toc-page">65</span></div>
<div class="toc-line"><span class="toc-text"><strong>Les Scénarios de Rupture :</strong> Quand le modèle pyramidal craque</span><span class="toc-dots"></span><span class="toc-page">73</span></div>
<div class="toc-line"><span class="toc-text"><strong>Les Dirigeants Pionniers :</strong> Sept récits détaillés de transformation</span><span class="toc-dots"></span><span class="toc-page">83</span></div>
<div class="toc-line"><span class="toc-text"><strong>Les Managers qui ont changé :</strong> Retours d'expériences concrets</span><span class="toc-dots"></span><span class="toc-page">91</span></div>
<div class="toc-line"><span class="toc-text"><strong>Le Coût de ne rien faire :</strong> L'urgence silencieuse et l'érosion des talents</span><span class="toc-dots"></span><span class="toc-page">99</span></div>
<div class="toc-line"><span class="toc-text"><strong>Les Angles Morts du Sommet :</strong> Ce que l'architecture pyramidale invisibilise</span><span class="toc-dots"></span><span class="toc-page">103</span></div>
<div class="toc-line"><span class="toc-text"><strong>Pourquoi le Système résiste :</strong> Comprendre les freins institutionnels</span><span class="toc-dots"></span><span class="toc-page">107</span></div>
<div class="toc-line"><span class="toc-text"><strong>Les Preuves que ça marche :</strong> Données empiriques et retours sur investissement</span><span class="toc-dots"></span><span class="toc-page">111</span></div>
<div class="toc-line"><span class="toc-text"><strong>Les Fiches Pratiques du Dirigeant :</strong> Boîte à outils opérationnelle</span><span class="toc-dots"></span><span class="toc-page">115</span></div>
<div class="toc-line"><span class="toc-text"><strong>La Transition vue d'en haut :</strong> Guide tactique du manager réformateur</span><span class="toc-dots"></span><span class="toc-page">119</span></div>
<div class="toc-line"><span class="toc-text"><strong>Le Premier Pas du Décideur :</strong> Huit micro-actes d'impact immédiat</span><span class="toc-dots"></span><span class="toc-page">121</span></div>
<div class="toc-line"><span class="toc-text"><strong>Le Plan de Transformation & L'IA :</strong> Feuille de route à 18 mois</span><span class="toc-dots"></span><span class="toc-page">123</span></div>
<div class="toc-line"><span class="toc-text"><strong>LE HALL CENTRAL :</strong> Reconnecter la stratégie au réel (Conclusion)</span><span class="toc-dots"></span><span class="toc-page">125</span></div>
<div class="toc-line"><span class="toc-text"><strong>LISTE DES SOURCES :</strong> Appareil critique et références</span><span class="toc-dots"></span><span class="toc-page">127</span></div>
`;

const terrain_toc = `
<h1>TABLE DES MATIÈRES — CÔTÉ TERRAIN</h1>
<div class="toc-line"><span class="toc-text"><strong>PROLOGUE : Le Lundi sans Management</strong></span><span class="toc-dots"></span><span class="toc-page">5</span></div>
<h3>PARTIE I : L'ASCENSION DE LA TOUR</h3>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 0 — Le Terrain :</strong> Le point de contact et la création de valeur</span><span class="toc-dots"></span><span class="toc-page">7</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 1 — Le Manager de Proximité :</strong> L'amortisseur des injonctions</span><span class="toc-dots"></span><span class="toc-page">13</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 2 — Le Responsable de Service :</strong> L'illusion de la transmission</span><span class="toc-dots"></span><span class="toc-page">19</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 3 — Le Directeur de Site :</strong> L'application aveugle</span><span class="toc-dots"></span><span class="toc-page">25</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 4 — Le Vice-Président :</strong> La guerre des territoires</span><span class="toc-dots"></span><span class="toc-page">31</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 5 — Le Président de Division :</strong> Le monde des KPIs</span><span class="toc-dots"></span><span class="toc-page">37</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 6 — Le Président International :</strong> La perte de contact</span><span class="toc-dots"></span><span class="toc-page">43</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 7 — Le Chairman :</strong> Le temps figé</span><span class="toc-dots"></span><span class="toc-page">49</span></div>
<div class="toc-line"><span class="toc-text"><strong>ÉTAGE 8 — Le CEO :</strong> Le vide d'air</span><span class="toc-dots"></span><span class="toc-page">61</span></div>
<h3>PARTIE II : CEUX QUI RÉINVENTENT LE MODÈLE</h3>
<div class="toc-line"><span class="toc-text"><strong>Vue d'ensemble :</strong> La réalité perçue depuis la base</span><span class="toc-dots"></span><span class="toc-page">66</span></div>
<div class="toc-line"><span class="toc-text"><strong>Qui a construit la tour ? :</strong> Histoire et obsolescence de la hiérarchie</span><span class="toc-dots"></span><span class="toc-page">70</span></div>
<div class="toc-line"><span class="toc-text"><strong>Le Grand Départ (Quiet Quitting) :</strong> Le désengagement silencieux</span><span class="toc-dots"></span><span class="toc-page">76</span></div>
<div class="toc-line"><span class="toc-text"><strong>Et si ? Le monde d'après :</strong> Nouveaux paradigmes organisationnels</span><span class="toc-dots"></span><span class="toc-page">82</span></div>
<div class="toc-line"><span class="toc-text"><strong>Ceux qui ont déjà commencé :</strong> Entreprises pionnières</span><span class="toc-dots"></span><span class="toc-page">88</span></div>
<div class="toc-line"><span class="toc-text"><strong>Fiches pratiques du terrain :</strong> Outils pour réagir au quotidien</span><span class="toc-dots"></span><span class="toc-page">94</span></div>
<div class="toc-line"><span class="toc-text"><strong>La Transition réaliste :</strong> Gérer l'existant tout en changeant de modèle</span><span class="toc-dots"></span><span class="toc-page">110</span></div>
<div class="toc-line"><span class="toc-text"><strong>Le Plan de Transformation :</strong> Comment reprendre la main</span><span class="toc-dots"></span><span class="toc-page">120</span></div>
<div class="toc-line"><span class="toc-text"><strong>LE HALL CENTRAL :</strong> Reconnecter la stratégie au réel (Conclusion)</span><span class="toc-dots"></span><span class="toc-page">137</span></div>
<div class="toc-line"><span class="toc-text"><strong>LISTE DES SOURCES :</strong> Références et inspirations</span><span class="toc-dots"></span><span class="toc-page">139</span></div>
`;

async function renderTOC(browser, html, outFile) {
    const page = await browser.newPage();
    const fullHtml = `<!DOCTYPE html><html><head><meta charset="UTF-8"><style>${css}</style></head><body>${html}</body></html>`;
    await page.setContent(fullHtml, { waitUntil: 'networkidle0' });
    const buf = await page.pdf({
        format: 'A5',
        printBackground: true,
        displayHeaderFooter: false,
        margin: { top: '12mm', right: '12mm', bottom: '18mm', left: '12mm' }
    });
    fs.writeFileSync(outFile, buf);
    await page.close();
    console.log("Généré :", outFile);
}

async function injectTOC(pdfPath, tocPath) {
    const docBytes = fs.readFileSync(pdfPath);
    const tocBytes = fs.readFileSync(tocPath);
    
    const doc = await PDFDocument.load(docBytes);
    const tocDoc = await PDFDocument.load(tocBytes);
    
    // Replace page 3 (index 2) with the new TOC
    doc.removePage(2); // Page 1 is Comment, Page 2 is Avertissement. Page 3 (index 2) is TOC.
    const [tocPage] = await doc.copyPages(tocDoc, [0]);
    doc.insertPage(2, tocPage);
    
    fs.writeFileSync(pdfPath, await doc.save());
    console.log("TOC Injecté dans :", pdfPath);
}

(async () => {
    const browser = await puppeteer.launch();
    await renderTOC(browser, sommet_toc, 'TOC_Sommet.pdf');
    await renderTOC(browser, terrain_toc, 'TOC_Terrain.pdf');
    await browser.close();
    
    await injectTOC('/Users/basile/.gemini/antigravity-ide/scratch/Les-9-etages/V3/Les_9_Etages_Cote_Sommet.pdf', 'TOC_Sommet.pdf');
    await injectTOC('/Users/basile/.gemini/antigravity-ide/scratch/Les-9-etages/V3/Les_9_Etages_Cote_Terrain.pdf', 'TOC_Terrain.pdf');
    
    // Build final merged book
    const terrainPath = '/Users/basile/.gemini/antigravity-ide/scratch/Les-9-etages/V3/Les_9_Etages_Cote_Terrain.pdf';
    const sommetPath = '/Users/basile/.gemini/antigravity-ide/scratch/Les-9-etages/V3/Les_9_Etages_Cote_Sommet.pdf';
    const qrPath = '/Users/basile/.gemini/antigravity-ide/scratch/Les-9-etages/QR_CENTER_PAGE.pdf'; // Needs to exist or we just build it
    const finalOutputPath = '/Users/basile/.gemini/antigravity-ide/scratch/Les-9-etages/V3/Les_9_Etages_Livre_Complet.pdf';

    const mergedDoc = await PDFDocument.create();
    
    // Terrain
    const terrainDoc = await PDFDocument.load(fs.readFileSync(terrainPath));
    const tPages = await mergedDoc.copyPages(terrainDoc, terrainDoc.getPageIndices());
    tPages.forEach(p => mergedDoc.addPage(p));
    
    // QR
    if (fs.existsSync(qrPath)) {
        const qrDoc = await PDFDocument.load(fs.readFileSync(qrPath));
        const qPages = await mergedDoc.copyPages(qrDoc, qrDoc.getPageIndices());
        qPages.forEach(p => mergedDoc.addPage(p));
    }
    
    // Sommet inverted
    const sommetDoc = await PDFDocument.load(fs.readFileSync(sommetPath));
    const sPages = await mergedDoc.copyPages(sommetDoc, sommetDoc.getPageIndices());
    for (let i = sPages.length - 1; i >= 0; i--) {
        const page = sPages[i];
        page.setRotation({ type: 'degrees', angle: (page.getRotation().angle + 180) % 360 });
        mergedDoc.addPage(page);
    }
    
    fs.writeFileSync(finalOutputPath, await mergedDoc.save());
    console.log("Livre complet regénéré :", finalOutputPath);
})();
