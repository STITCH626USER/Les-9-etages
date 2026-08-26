const fs = require('fs');
const puppeteer = require('puppeteer');
const { marked } = require('marked');
const { PDFDocument, rgb, StandardFonts } = require('pdf-lib');
const QRCode = require('qrcode');

async function renderSectionToPdf(browser, html, css, isStatPage = false) {
    const page = await browser.newPage();
    const fullHtml = `<!DOCTYPE html><html><head><meta charset="UTF-8"><style>${css}</style></head><body>${html}</body></html>`;
    await page.setContent(fullHtml, { waitUntil: 'networkidle0' });
    
    // We will draw the page numbers later using pdf-lib to ensure continuous numbering
    const buf = await page.pdf({
        format: 'A5',
        printBackground: true,
        displayHeaderFooter: false,
        margin: { top: '12mm', right: '12mm', bottom: '18mm', left: '12mm' }
    });
    await page.close();
    return buf;
}

async function buildBookSide(browser, side) {
    const isSommet = (side === 'sommet');
    const generatorFile = isSommet ? './generate_pdf_puppeteer_sommet.js' : './generate_pdf_puppeteer.js';
    const code = fs.readFileSync(generatorFile, 'utf-8');
    
    
    let css = code.match(/<style>([\s\S]*?)<\/style>/)[1];

    const statsMatch = code.match(/const chapterStats = {([\s\S]*?)};/);
    const chapterStats = eval('({' + statsMatch[1] + '})');

    function getStatPageHtml(floorNum) {
        const s = chapterStats[floorNum];
        if (!s) return '';
        let inner = '';
        if (s.type === 'stat') {
            inner = `
                <div class="stat-eyebrow">ÉTAGE ${floorNum} — CHIFFRE CLÉ</div>
                <div class="stat-number">${s.stat}</div>
                <div class="stat-label">${s.label}</div>
                <div class="stat-source">${s.source}</div>`;
        } else if (s.type === 'quote') {
            inner = `
                <div class="stat-eyebrow">ÉTAGE ${floorNum} — POUR RÉFLÉCHIR</div>
                <div class="stat-quote-mark">«</div>
                <div class="stat-quote">${s.quote}</div>
                <div class="stat-attribution">${s.attribution}</div>`;
        } else if (s.type === 'fact') {
            inner = `
                <div class="stat-eyebrow">ÉTAGE ${floorNum} — À SAVOIR</div>
                <div class="stat-fact-bar"></div>
                <div class="stat-fact">${s.fact}</div>
                <div class="stat-source">${s.source}</div>`;
        }
        return `<div class="stat-page"><div>${inner}</div></div>`;
    }

    function getElevatorHtml(floorNum) {
        let squaresHtml = '';
        for (let i = 0; i <= 9; i++) {
            const color = (i === floorNum) ? '#000000' : '#737373';
            squaresHtml += `<div style="width: 14px; height: 14px; background-color: ${color};"></div>`;
        }
        return `
            <div class="elevator-container">
                <div class="squares-row">${squaresHtml}</div>
                <div class="elevator-label">ÉTAGE ${floorNum} SUR 9</div>
            </div>
        `;
    }

    const brainDir = "/Users/basile/.gemini/antigravity-ide/brain/e76ab0a9-1a14-4ef3-b1fe-0bb770d213f0";
                const files = isSommet ? [
        `${brainDir}/rewrite_sommet_copyright.md`,
        `${brainDir}/rewrite_sommet_titre.md`,
        `${brainDir}/rewrite_sommet_prologue.md`,
        `${brainDir}/rewrite_sommet_table_des_matieres.md`,
        `${brainDir}/rewrite_sommet_chap8.md`,
        `${brainDir}/rewrite_sommet_chap7.md`,
        `${brainDir}/rewrite_sommet_chap6.md`,
        `${brainDir}/rewrite_sommet_chap5.md`,
        `${brainDir}/rewrite_sommet_chap4.md`,
        `${brainDir}/rewrite_sommet_chap3.md`,
        `${brainDir}/rewrite_sommet_chap2.md`,
        `${brainDir}/rewrite_sommet_chap1.md`,
        `${brainDir}/rewrite_sommet_chap0.md`,
        `${brainDir}/rewrite_sommet_vue_ensemble.md`,
        `${brainDir}/rewrite_sommet_generations.md`,
        `${brainDir}/rewrite_sommet_et_si.md`,
        `${brainDir}/rewrite_sommet_ceux_qui_ont_commence.md`,
        `${brainDir}/rewrite_sommet_les_managers_qui_ont_change.md`,
        `${brainDir}/rewrite_sommet_cout_de_ne_rien_faire.md`,
        `${brainDir}/rewrite_sommet_angles_morts.md`,
        `${brainDir}/rewrite_sommet_pourquoi_ne_pas_changer.md`,
        `${brainDir}/rewrite_sommet_les_preuves_que_ca_marche.md`,
        `${brainDir}/rewrite_sommet_le_premier_pas.md`,
        `${brainDir}/rewrite_sommet_fiches_pratiques.md`,
        `${brainDir}/rewrite_sommet_guide_manager.md`,
        `${brainDir}/rewrite_sommet_plan_transformation.md`,
        `${brainDir}/rewrite_sommet_miroir_croise.md`,
        `${brainDir}/rewrite_sources.md`
    ] : [
        `${brainDir}/rewrite_terrain_copyright.md`,
        `${brainDir}/rewrite_terrain_prologue.md`,
        `${brainDir}/rewrite_terrain_table_des_matieres.md`,
        `${brainDir}/rewrite_terrain_chap0.md`,
        `${brainDir}/rewrite_terrain_chap1.md`,
        `${brainDir}/rewrite_terrain_chap2.md`,
        `${brainDir}/rewrite_terrain_chap3.md`,
        `${brainDir}/rewrite_terrain_chap4.md`,
        `${brainDir}/rewrite_terrain_chap5.md`,
        `${brainDir}/rewrite_terrain_chap6.md`,
        `${brainDir}/rewrite_terrain_chap7.md`,
        `${brainDir}/rewrite_terrain_chap8.md`,
        `${brainDir}/rewrite_terrain_vue_ensemble.md`,
        `${brainDir}/rewrite_terrain_generations.md`,
        `${brainDir}/rewrite_terrain_et_si.md`,
        `${brainDir}/rewrite_terrain_ceux_qui_ont_commence.md`,
        `${brainDir}/rewrite_terrain_fiches_pratiques.md`,
        `${brainDir}/rewrite_terrain_la_transition.md`,
        `${brainDir}/rewrite_terrain_plan_transformation.md`,
        `${brainDir}/rewrite_hall_central_miroir.md`,
        `${brainDir}/rewrite_sources.md`
    ];

    const finalDoc = await PDFDocument.create();

    async function appendPdfBytes(buf) {
        const doc = await PDFDocument.load(buf);
        const pages = await finalDoc.copyPages(doc, doc.getPageIndices());
        for (const p of pages) {
            finalDoc.addPage(p);
        }
        return doc.getPageCount();
    }

    async function addBlankPage() {
        const blankBuf = await renderSectionToPdf(browser, '<div style="height: 100vh;">&nbsp;</div>', css, true);
        await appendPdfBytes(blankBuf);
    }

    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        if (!fs.existsSync(file)) continue;
        let content = fs.readFileSync(file, 'utf-8');
        if (content.trim() === '') continue; // Skip empty files

        if (file.includes('mot_auteur')) {
            content = '<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 85vh;">\n\n' + content + '\n\n</div>';
        }
        
        let wrapperClass = '';
        if (file.includes('sommet_titre') || file.includes('terrain_prologue')) {
            wrapperClass = 'titre-page-compact';
        } else if (file.includes('prologue')) {
            wrapperClass = 'prologue-compact';
        }

        content = content.replace(/ ([;:!?»])/g, '&nbsp;$1');
        content = content.replace(/(«) /g, '$1&nbsp;');
        content = content.replace(/&nbsp;:---/g, ' :---');

        let parsedHtml = marked.parse(content);
        if (wrapperClass) {
            parsedHtml = `<div class="${wrapperClass}">${parsedHtml}</div>`;
        }

        const floorMatch = file.match(/chap(\d+)\.md/);
        
        if (floorMatch) {
            const floorNum = parseInt(floorMatch[1]);
            let currentTotalPages = finalDoc.getPageCount();

            // Nouvelle Règle de pagination :
            // Si le chapitre précédent se termine sur une page paire (gauche),
            // on supprime l'infographie pour éviter une page blanche. Le nouveau chapitre démarre directement à droite (impaire).
            // Si le chapitre précédent se termine sur une page impaire (droite),
            // on garde l'infographie, qui s'imprime à gauche (paire), et le chapitre démarre à droite.
            if (currentTotalPages % 2 !== 0) {
                // 1. Infographie (page paire / gauche)
                const statHtml = getStatPageHtml(floorNum);
                const statBuf = await renderSectionToPdf(browser, statHtml, css, true);
                await appendPdfBytes(statBuf);
            }

            // 2. Titre et contenu du chapitre (page impaire / droite)
            parsedHtml = parsedHtml.replace(/<h1>ÉTAGE (\d+)(.*?)<\/h1>/g, (m, fStr, r) => {
                return `<div>${getElevatorHtml(floorNum)}<h1>ÉTAGE ${floorNum}${r}</h1></div>`;
            });

            parsedHtml = parsedHtml.replace(/(\d+)\s+(%|&nbsp;%|€|\s*km\b|\s*h\b)/g, '$1\u00a0$2');

            const chapBuf = await renderSectionToPdf(browser, parsedHtml, css, false);
            await appendPdfBytes(chapBuf);

        } else {
            parsedHtml = parsedHtml.replace(/(\d+)\s+(%|&nbsp;%|€|\s*km\b|\s*h\b)/g, '$1\u00a0$2');

            const docBuf = await renderSectionToPdf(browser, parsedHtml, css, false);
            await appendPdfBytes(docBuf);
        }
    }
    const font = await finalDoc.embedFont(StandardFonts.Helvetica);
    const pages = finalDoc.getPages();
    for (let i = 0; i < pages.length; i++) {
        const page = pages[i];
        const { width } = page.getSize();
        const text = String(i + 1);
        const textWidth = font.widthOfTextAtSize(text, 9);
        // Do not add page numbers to the first 2 pages (cover, copyright usually)
        // or actually, the original code had it on all pages since displayHeaderFooter was true except for stat pages.
        // Wait, the user's "isStatPage" parameter disabled headers/footers for stat pages!
        // We need to skip numbering for stat pages? The old code set displayFooter = !isStatPage.
        // But continuous page numbering usually counts every page, even if it doesn't print the number on some.
        // Actually, if we want to mimic the old behaviour but with continuous numbers, we shouldn't draw on stat pages.
        // How to know if it's a stat page here? It's hard. Let's just put it on all pages, or skip based on something.
        // A printed book usually has page numbers on almost every page. Let's just put it on every page except maybe page 0.
        if (i > 1) { // Skip title and copyright
            page.drawText(text, {
                x: width / 2 - textWidth / 2,
                y: 28,
                size: 9,
                font: font,
                color: rgb(0.4, 0.4, 0.4)
            });
        }
    }

    const finalPdfBytes = await finalDoc.save();
    const finalPdfPath = isSommet ? '/Users/basile/Desktop/Projet_Manuscrit_TeteBeche/LES_9_ETAGES_SOMMET.pdf' : '/Users/basile/Desktop/Projet_Manuscrit_TeteBeche/LES_9_ETAGES_TERRAIN.pdf';
    fs.writeFileSync(finalPdfPath, finalPdfBytes);
    console.log(`✅ [${side}] PDF généré avec succès (${finalDoc.getPageCount()} pages) -> ${finalPdfPath}`);
    return finalPdfPath;
}

async function generateCenterQrPage() {
    const qrText = 'https://padlet.com/les9etages/les-9-etages-de-la-tour-espace-libre-9fs1vfnbejnrbzvl';
    const qrDataUrl = await QRCode.toDataURL(qrText, {
        width: 300,
        margin: 2,
        color: { dark: '#000000', light: '#ffffff' }
    });

    const browser = await puppeteer.launch();
    const page = await browser.newPage();

       const html = `
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&family=Merriweather:ital,wght@0,400;1,300&display=swap');
            @page { size: A5; margin: 0; }
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body {
                width: 148mm; height: 210mm;
                display: flex; flex-direction: column;
                background: #ffffff;
                font-family: 'Montserrat', sans-serif;
            }

            /* ── TOP HALF (for Sommet reader — rotated 180°) ── */
            .half-top {
                flex: 1;
                display: flex; flex-direction: column;
                align-items: center; justify-content: flex-end;
                padding: 8mm 12mm 6mm;
                transform: rotate(180deg);
                border-bottom: 1px solid #e0e0e0;
            }

            /* ── BOTTOM HALF (for Terrain reader — normal) ── */
            .half-bottom {
                flex: 1;
                display: flex; flex-direction: column;
                align-items: center; justify-content: flex-end;
                padding: 8mm 12mm 6mm;
                border-top: 1px solid #e0e0e0;
            }

            .book-title {
                font-size: 9px; font-weight: 700; letter-spacing: 3px;
                text-transform: uppercase; color: #1a1a1a; margin-bottom: 4px;
            }
            .book-subtitle {
                font-family: 'Merriweather', serif; font-style: italic;
                font-size: 8.5px; color: #888888; margin-bottom: 10px; text-align: center;
            }
            .flip-line {
                font-size: 7.5px; letter-spacing: 2px; text-transform: uppercase;
                color: #aaaaaa; font-weight: 600; margin-bottom: 4px;
            }
            .arrow-line {
                font-size: 11px; color: #cccccc; letter-spacing: 6px;
            }

            /* ── CENTER BAND (QR + URL) ── */
            .center-band {
                display: flex; flex-direction: column;
                align-items: center; justify-content: center;
                padding: 5mm 14mm;
                gap: 4mm;
                background: #fafafa;
                border-top: 1px solid #e0e0e0;
                border-bottom: 1px solid #e0e0e0;
            }
            .qr-wrapper {
                border: 1px solid #d4d4d4;
                padding: 7px;
                background: #fff;
                display: inline-block;
            }
            .qr-wrapper img { width: 110px; height: 110px; display: block; }
            .url {
                font-size: 12px; font-weight: 700; letter-spacing: 1.5px;
                color: #1a1a1a; text-align: center;
            }
            .desc {
                font-family: 'Merriweather', serif; font-size: 9px;
                color: #777777; line-height: 1.6; max-width: 90mm; text-align: center;
            }
        </style>
    </head>
    <body>
        <!-- TOP HALF: rotated for Sommet reader -->
        <div class="half-top">
            <div class="arrow-line">↓</div>
            <div class="flip-line">Retournez le livre pour l'autre versant</div>
            <div class="book-subtitle">Les 9 Étages — Du terrain au sommet</div>
            <div class="book-title">Les 9 Étages</div>
        </div>

        <!-- CENTER: QR code + URL (visible from both sides) -->
        <div class="center-band">
            <div class="qr-wrapper"><img src="${qrDataUrl}" alt="QR Code" /></div>
            <div class="url">padlet.com/les9etages</div>
            <div class="desc">Un espace de libre échange entre lecteurs, praticiens et observateurs des organisations.</div>
        </div>

        <!-- BOTTOM HALF: normal orientation for Terrain reader -->
        <div class="half-bottom">
            <div class="book-title">Les 9 Étages</div>
            <div class="book-subtitle">Du sommet au terrain — Les 9 Étages</div>
            <div class="flip-line">Retournez le livre pour l'autre versant</div>
            <div class="arrow-line">↑</div>
        </div>
    </body>
    </html>`;

    await page.setContent(html, { waitUntil: 'networkidle0' });
    const qrPdfPath = '/Users/basile/Desktop/Projet_Manuscrit_TeteBeche/QR_CENTER_PAGE.pdf';
    await page.pdf({
        path: qrPdfPath,
        format: 'A5',
        printBackground: true,
        margin: { top: '0mm', right: '0mm', bottom: '0mm', left: '0mm' }
    });
    await browser.close();
    console.log(`✅ Page QR Centre générée -> ${qrPdfPath}`);
    return qrPdfPath;
}

async function assembleTeteBeche() {
    const terrainPath = '/Users/basile/Desktop/Projet_Manuscrit_TeteBeche/LES_9_ETAGES_TERRAIN.pdf';
    const sommetPath = '/Users/basile/Desktop/Projet_Manuscrit_TeteBeche/LES_9_ETAGES_SOMMET.pdf';
    const qrPath = '/Users/basile/Desktop/Projet_Manuscrit_TeteBeche/QR_CENTER_PAGE.pdf';
    const finalOutputPath = '/Users/basile/Desktop/Projet_Manuscrit_TeteBeche/LES_9_ETAGES_FINAL.pdf';

    const terrainBytes = fs.readFileSync(terrainPath);
    const sommetBytes = fs.readFileSync(sommetPath);
    const qrBytes = fs.readFileSync(qrPath);

    const terrainDoc = await PDFDocument.load(terrainBytes);
    const sommetDoc = await PDFDocument.load(sommetBytes);
    const qrDoc = await PDFDocument.load(qrBytes);

    const mergedDoc = await PDFDocument.create();

    // 1. Ajouter Terrain à l'endroit
    const terrainPages = await mergedDoc.copyPages(terrainDoc, terrainDoc.getPageIndices());
    for (const p of terrainPages) mergedDoc.addPage(p);

    // 2. Ajouter page QR au centre
    const qrPages = await mergedDoc.copyPages(qrDoc, qrDoc.getPageIndices());
    for (const p of qrPages) mergedDoc.addPage(p);

    // 3. Ajouter Sommet inversé (tête-bêche : ordre inverse de lecture et rotation 180°)
    const sommetIndices = sommetDoc.getPageIndices();
    const sommetPages = await mergedDoc.copyPages(sommetDoc, sommetIndices);
    for (let i = sommetPages.length - 1; i >= 0; i--) {
        const page = sommetPages[i];
        page.setRotation({ type: 'degrees', angle: (page.getRotation().angle + 180) % 360 });
        mergedDoc.addPage(page);
    }

    const mergedBytes = await mergedDoc.save();
    fs.writeFileSync(finalOutputPath, mergedBytes);
    console.log(`\n🎉 MANUSCRIT TÊTE-BÊCHE INTÉGRAL FINALISÉ : ${finalOutputPath}`);
    console.log(`📊 Pages totales : ${mergedDoc.getPageCount()} (Terrain: ${terrainDoc.getPageCount()}p + QR: 1p + Sommet: ${sommetDoc.getPageCount()}p)`);
}

async function main() {
    console.log("🚀 Lancement du pipeline complet de génération 100% calibré...");
    const browser = await puppeteer.launch();
    await buildBookSide(browser, 'terrain');
    await buildBookSide(browser, 'sommet');
    await browser.close();
    await generateCenterQrPage();
    await assembleTeteBeche();
}

main().catch(console.error);
