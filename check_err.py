import requests, re, html
r = requests.get('https://trabajo-final-2keb.onrender.com/accounts/login/', timeout=15)
# Find exception value
m = re.search(r'<summary[^>]*>\s*Exception Value\s*</summary>\s*<pre[^>]*>(.+?)</pre>', r.text, re.DOTALL)
if m:
    val = html.unescape(m.group(1)).strip()[:500]
    print('EXCEPTION VALUE:', val)
else:
    # Try alternate pattern
    m = re.search(r'Reverse for[^<]+', r.text)
    if m:
        print('MATCH:', m.group()[:500])
    # Print context
    print('First 8000 chars:')
    print(r.text[:8000])
