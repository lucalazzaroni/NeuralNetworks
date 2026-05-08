#!/usr/bin/env python3
"""
Genera il token di accesso per STEdgeAI Developer Cloud.
Esegui una volta nel terminale del tuo PC (non su Colab):

    python3 get_stm32ai_token.py

Poi copia il token stampato nella variabile STM32AI_TOKEN del notebook.
"""
import html, re, getpass, json, sys
import requests
from urllib.parse import urlparse, parse_qs, urljoin

username = input('Email MyST account: ').strip()
password = getpass.getpass('Password: ')

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'

print('Connessione a sso.st.com...', end=' ', flush=True)
r = s.get(
    'https://sso.st.com/as/authorization.oauth2',
    params={
        'response_type': 'code',
        'client_id':     'oidc_prod_client_app_stm32ai',
        'scope':         'openid',
        'redirect_uri':  'https://stedgeai-dc.st.com/callback',
        'response_mode': 'query',
    },
    allow_redirects=True,
    timeout=20,
)

try:
    form_action = html.unescape(
        re.search(r'<form\s+.*?\s+action="(.*?)"', r.text, re.DOTALL).group(1))
    lt_value = html.unescape(
        re.search(r'value="(.*?)"',
                  re.search(r'<input.*?name="lt".*?/>', r.text).group(0)).group(1))
except AttributeError:
    print('\n❌ Struttura della pagina SSO cambiata. Usa il metodo F12.')
    sys.exit(1)

parsed   = urlparse(r.url)
login_url = urljoin(f'{parsed.scheme}://{parsed.netloc}', form_action)

print('login...', end=' ', flush=True)
r2 = s.post(login_url, data={
    'username': username, 'password': password,
    '_eventId': 'Login', 'lt': lt_value,
}, allow_redirects=False, timeout=20)

if r2.status_code == 200:
    if re.search(r'wrong password', r2.text, re.IGNORECASE):
        print('\n❌ Credenziali errate.')
        sys.exit(1)

redirect = r2.headers.get('Location', '')
print(f'\nPrimo redirect: {redirect[:120]}')
hop = 0
while redirect and 'stedgeai-dc.st.com/callback' not in redirect:
    hop += 1
    r3 = s.get(redirect, allow_redirects=False, timeout=20)
    redirect = r3.headers.get('Location', '')
    print(f'  hop {hop}: HTTP {r3.status_code}  →  {redirect[:120]}')
    if hop > 10:
        print('❌ Troppi redirect, interrompo.')
        sys.exit(1)

code = parse_qs(urlparse(redirect).query).get('code', [None])[0]
if not code:
    print('\n❌ OAuth code non trovato nel redirect.')
    sys.exit(1)

r4 = requests.post(
    'https://stedgeai-dc.st.com/api/user_service/login/callback',
    data={'redirect_url': 'https://stedgeai-dc.st.com/callback', 'code': code},
    timeout=20,
)
token_data = r4.json()
token = token_data.get('access_token')

if token:
    print('OK\n')
    print('=' * 72)
    print(token)
    print('=' * 72)
else:
    print('\n❌ Risposta inattesa:')
    print(json.dumps(token_data, indent=2))
    sys.exit(1)
