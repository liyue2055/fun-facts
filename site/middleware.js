// HTTP Basic Auth gate for the private Tokyo trip page.
// Credentials come from Vercel env vars (TOKYO_AUTH_USER / TOKYO_AUTH_PASS),
// never hardcoded — the repo is public.
export function middleware(request) {
  const user = process.env.TOKYO_AUTH_USER;
  const pass = process.env.TOKYO_AUTH_PASS;
  let ok = false;
  if (user && pass) {
    const expected = 'Basic ' + btoa(user + ':' + pass);
    ok = request.headers.get('authorization') === expected;
  }
  if (!ok) {
    return new Response('Authentication required.', {
      status: 401,
      headers: { 'WWW-Authenticate': 'Basic realm="Tokyo Trip"' },
    });
  }
}

export const config = {
  matcher: '/tokyo-trip/:path*',
};
