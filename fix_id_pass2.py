import re

with open("web/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# First, re-add dark:bg-[#1A1A1A] to bg-white everywhere.
html = re.sub(r'(?<!dark:)\bbg-white\b', 'bg-white dark:bg-[#1A1A1A]', html)

# Then, strip dark mode classes out of the printable-id-card
match = re.search(r'(<div id="printable-id-card".*?<!-- QR Code Container -->.*?</div>\s*</div>)', html, flags=re.DOTALL)
if match:
    pass_block = match.group(1)
    
    reps = {
        ' dark:bg-[#1A1A1A]': '',
        ' dark:bg-[#111111]': '',
        ' dark:text-slate-200': '',
        ' dark:text-slate-300': '',
        ' dark:text-slate-400': '',
        ' dark:text-slate-500': '',
        ' dark:text-white': '',
    }
    for k, v in reps.items():
        pass_block = pass_block.replace(k, v)
        
    html = html.replace(match.group(1), pass_block)
    print("Fixed ID pass.")
else:
    print("Could not match ID pass block.")

with open("web/index.html", "w", encoding="utf-8") as f:
    f.write(html)
