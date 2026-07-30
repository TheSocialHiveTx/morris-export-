const fs = require('fs');
const path = require('path');

// Read index.html content
const content = fs.readFileSync(path.join(__dirname, '../index.html'), 'utf8');

// We will extract SERVICES and renderServiceDetail and run them in a mock browser environment
// Let's create a sandbox JS code
const startServicesIdx = content.indexOf('const SERVICES = [');
const endServicesIdx = content.indexOf('];', startServicesIdx) + 2;
const servicesJs = content.substring(startServicesIdx, endServicesIdx);

const startRenderIdx = content.indexOf('function renderServiceDetail(slug) {');
const endRenderIdx = content.indexOf('<!-- Bottom CTA -->', startRenderIdx);
const renderJs = content.substring(startRenderIdx, endRenderIdx);

// Build the test runner
const sandboxCode = `
${servicesJs}
${renderJs}
// Close the function since we cut it off before the end of the template string
// Let's see: renderServiceDetail ends after the template string.
// Let's add the closing part manually:
\`;
}

// Mock other templates that might be referenced
function renderHome() { return ''; }

// Mock document/window objects
global.window = {
  location: {
    origin: 'https://www.morrisexport.com',
    pathname: '/'
  }
};
global.getBasePath = function() { return '/'; };

console.log('Testing SERVICES slugs...');
SERVICES.forEach(s => {
  try {
    const html = renderServiceDetail(s.slug);
    if (html.includes('Service not found')) {
      console.log('FAIL: slug not found in SERVICES:', s.slug);
    } else {
      console.log('SUCCESS: rendered', s.slug, 'Length:', html.length);
    }
  } catch (err) {
    console.error('ERROR rendering slug:', s.slug, err);
  }
});
`;

const runnerPath = path.join(__dirname, '../temp_test_runner.js');
fs.writeFileSync(runnerPath, sandboxCode);
console.log('Test runner written. Running...');
try {
  require(runnerPath);
} catch (e) {
  console.error('Runner failed:', e);
} finally {
  // Clean up
  try { fs.unlinkSync(runnerPath); } catch (err) {}
}
