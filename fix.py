with open('C:\\Users\\subash\\Desktop\\WAAY2TECH_Project\\html_files\\touchbutton.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change title
content = content.replace('<title>BOUNCE · Eye & Hand Cursor Trap | Waay2Tech</title>', '<title>BOUNCE · Eye & Hand Cursor Trap | WAAY2TECH</title>')

# Change twitter:title
content = content.replace('<meta name="twitter:title" content="BOUNCE · Eye & Hand Cursor Trap">', '<meta name="twitter:title" content="BOUNCE · Eye & Hand Cursor Trap | WAAY2TECH">')

# Change JSON-LD name
content = content.replace('"name": "BOUNCE — Eye & Hand Cursor Trap"', '"name": "BOUNCE — Eye & Hand Cursor Trap | WAAY2TECH"')

# Add wordmark to header - add WAAY2TECH after BOUNCE in the wordmark
content = content.replace('<a class="wordmark" href="#"><span class="blob" aria-hidden="true"></span> BOUNCE</a>', '<a class="wordmark" href="#"><span class="blob" aria-hidden="true"></span> BOUNCE<span class="wordmark">WAAY2TECH</span></a>')

with open('C:\\Users\\subash\\Desktop\\WAAY2TECH_Project\\html_files\\touchbutton.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')