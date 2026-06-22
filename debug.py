import requests, re
s = requests.Session()
p = s.get('https://trabajo-final-2keb.onrender.com/accounts/login/', timeout=30)
m = re.search(r'csrfmiddlewaretoken" value="([^"]+)"', p.text)
resp = s.post('https://trabajo-final-2keb.onrender.com/accounts/login/', data={
    'username': 'testuser456', 'password': 'TestPass123!',
    'csrfmiddlewaretoken': m.group(1)}, allow_redirects=True)
print('Login final URL:', resp.url)

r = s.get('https://trabajo-final-2keb.onrender.com/pelicula/79/', timeout=30)
print('Status:', r.status_code)
print('URL:', r.url)

# Check for key elements
text = r.text
print('Iniciar Sesion:', 'Iniciar Sesion' in text or 'Iniciar Sesi' in text)
print('Coco:', 'Coco' in text)
print('detail-grid:', 'detail-grid' in text)
print('video-section:', 'video-section' in text)
print('player:', 'player' in text)
print('main_video:', 'main_video' in text)
print('trailer-card:', 'trailer-card' in text)

# Print first 3000 chars
print('--- HTML start ---')
print(text[:3000])
print('--- HTML end ---')
if len(text) > 3000:
    # Check near the bottom for video sections
    idx = text.find('video-section')
    if idx > 0:
        print('--- Around video-section ---')
        print(text[max(0,idx-200):idx+500])
