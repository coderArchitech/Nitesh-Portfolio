// Print resume.html to an A4 PDF with Chromium. Usage: node print.js <dir> <base>
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = path.resolve(process.argv[2]);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(dir, process.argv[3] + '.html'), { waitUntil: 'load' });
  await p.pdf({ path: path.join(dir, process.argv[3] + '.pdf'), format: 'A4', preferCSSPageSize: true, printBackground: true });
  await b.close();
})();
