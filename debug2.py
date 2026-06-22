import requests, re

s = requests.Session()

# Step 1: Register
reg_page = s.get('https://trabajo-final-2keb.onrender.com/accounts/register/', timeout=30)
m = re.search(r'csrfmiddlewaretoken" value="([^"]+)"', reg_page.text)
if not m:
    print("No CSRF on register")
    exit()
reg = s.post('https://trabajo-final-2keb.onrender.com/accounts/register/', data={
    'username': 'testuser999',
    'password1': 'TestPass123!',
    'password2': 'TestPass123!',
    'csrfmiddlewaretoken': m.group(1),
}, headers={'Referer': 'https://trabajo-final-2keb.onrender.com/accounts/register/'}, allow_redirects=True)
print('Register final URL:', reg.url)

# Step 2: Login
login_page = s.get('https://trabajo-final-2keb.onrender.com/accounts/login/', timeout=30)
m2 = re.search(r'csrfmiddlewaretoken" value="([^"]+)"', login_page.text)
if not m2:
    print("No CSRF on login")
    exit()
log = s.post('https://trabajo-final-2keb.onrender.com/accounts/login/', data={
    'username': 'testuser999',
    'password': 'TestPass123!',
    'csrfmiddlewaretoken': m2.group(1),
}, headers={'Referer': 'https://trabajo-final-2keb.onrender.com/accounts/login/'}, allow_redirects=False)
print('Login status:', log.status_code)

# Step 3: Check movie
r = s.get('https://trabajo-final-2keb.onrender.com/pelicula/79/', timeout=30, allow_redirects=False)
print('Movie status:', r.status_code)
print('Movie URL:', r.url)

if r.status_code == 200:
    print('Coco in text:', 'Coco' in r.text)
    print('video-section in text:', 'video-section' in r.text)
    print('player in text:', 'player' in r.text)
    print('youtube.com/embed in text:', 'youtube.com/embed' in r.text)
    # Extract relevant snippet
    for kw in ['video-section', 'iframe', 'youtube', 'player']:
        idx = r.text.find(kw)
        if idx >= 0:
            print(f'Found "{kw}" at pos {idx}: ...{r.text[max(0,idx-50):idx+100]}...')
else:
    print('Not logged in - redirect detected')
    print('Has Entrar:', 'Entrar' in r.text)
