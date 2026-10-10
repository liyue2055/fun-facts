// HTTP Basic Auth gate for the private Tokyo trip page.
// Served at /tokyo-trip via vercel.json rewrite. Credentials come from
// Vercel env vars (TOKYO_AUTH_USER / TOKYO_AUTH_PASS) — never in the repo.
const fs = require('fs');
const path = require('path');

module.exports = (req, res) => {
  const user = process.env.TOKYO_AUTH_USER;
  const pass = process.env.TOKYO_AUTH_PASS;
  let ok = false;
  if (user && pass) {
    const expected = 'Basic ' + Buffer.from(user + ':' + pass).toString('base64');
    ok = req.headers.authorization === expected;
  }
  if (!ok) {
    res.setHeader('WWW-Authenticate', 'Basic realm="Tokyo Trip"');
    return res.status(401).send('Authentication required.');
  }
  const html = fs.readFileSync(path.join(__dirname, '..', 'tokyo-trip.html'), 'utf8');
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.setHeader('Cache-Control', 'private, no-store');
  return res.status(200).send(html);
};
