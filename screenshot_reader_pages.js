const puppeteer = require('puppeteer');

async function test() {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({ width: 1400, height: 900, deviceScaleFactor: 2 });
    
    // Test port 8000
    try {
        await page.goto('http://localhost:8000/#mode=spread&side=sommet&page=7', { waitUntil: 'networkidle0', timeout: 5000 });
        await new Promise(r => setTimeout(r, 2000));
        await page.screenshot({ path: '/Users/basile/.gemini/antigravity-ide/brain/c9bc8ad0-dc63-4406-b351-c07aa43ad831/sommet_spread_p7.png' });
        console.log("Screenshot Sommet p7-8 pris avec succès !");
        
        await page.goto('http://localhost:8000/#mode=spread&side=terrain&page=7', { waitUntil: 'networkidle0', timeout: 5000 });
        await new Promise(r => setTimeout(r, 2000));
        await page.screenshot({ path: '/Users/basile/.gemini/antigravity-ide/brain/c9bc8ad0-dc63-4406-b351-c07aa43ad831/terrain_spread_p7.png' });
        console.log("Screenshot Terrain p7-8 pris avec succès !");
    } catch(e) {
        console.log("Erreur:", e.message);
    }
    await browser.close();
}
test();
