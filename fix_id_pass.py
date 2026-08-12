import re

with open("web/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Extract ID pass card
match = re.search(r'(<div id="printable-id-card".*?<!-- ID Pass Card End -->)', html, flags=re.DOTALL)
if not match:
    # Just try to find the end div manually if comment is missing
    match = re.search(r'(<div id="printable-id-card".*?</div>\s*</div>\s*</div>\s*</div>)', html, flags=re.DOTALL)

if match:
    pass_html = match.group(1)
    
    # Strip out the dark classes that were added
    reps = {
        ' dark:bg-[#111111]': '',
        ' dark:bg-[#1A1A1A]': '',
        ' dark:text-slate-200': '',
        ' dark:text-slate-300': '',
        ' dark:text-slate-400': '',
        ' dark:text-slate-500': '',
        ' dark:text-white': '',
        ' dark:bg-[#222222]': '',
        ' dark:bg-[#333333]': '',
        ' dark:border-neutral-800': '',
        ' dark:border-neutral-700': ''
    }
    for k, v in reps.items():
        pass_html = pass_html.replace(k, v)
        
    html = html.replace(match.group(1), pass_html)
    print("Fixed ID pass dark mode classes.")
else:
    print("Still couldn't find ID pass block.")

with open("web/index.html", "w", encoding="utf-8") as f:
    f.write(html)
