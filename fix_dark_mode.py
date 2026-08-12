import re

with open("web/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add toggleDarkMode JS
js_func = """
    function toggleDarkMode() {
      const doc = document.documentElement;
      if (doc.classList.contains('dark')) {
        doc.classList.remove('dark');
        localStorage.theme = 'light';
      } else {
        doc.classList.add('dark');
        localStorage.theme = 'dark';
      }
    }
    window.toggleDarkMode = toggleDarkMode;
"""
if "function toggleDarkMode" not in html:
    html = html.replace('function switchLoginMode', js_func + '\n    function switchLoginMode')

# 2. Re-insert Toggle Button into Login Screen (after max-w-md div)
login_btn = """      <button onclick="toggleDarkMode()" class="absolute top-5 right-5 w-9 h-9 rounded-full bg-slate-100 dark:bg-[#222] flex items-center justify-center text-slate-600 dark:text-yellow-400 hover:scale-105 transition">
        <i class="fa-solid fa-moon dark:hidden"></i>
        <i class="fa-solid fa-sun hidden dark:block"></i>
      </button>"""
if "fa-moon" not in html:
    # Login screen injection
    html = html.replace('relative overflow-hidden">\n', 'relative overflow-hidden">\n' + login_btn + '\n')
    
    # Navbar injection
    nav_target = '          <!-- Settings Button -->'
    nav_btn = """          <!-- Dark Mode Toggle -->
          <button onclick="toggleDarkMode()" class="w-9 h-9 rounded-xl bg-black dark:bg-[#222] hover:bg-neutral-800 border border-neutral-700 text-yellow-300 flex items-center justify-center transition" title="Toggle Theme">
            <i class="fa-solid fa-moon dark:hidden"></i>
            <i class="fa-solid fa-sun hidden dark:block"></i>
          </button>\n"""
    html = html.replace(nav_target, nav_btn + '\n' + nav_target)

# 3. Apply dark classes using string replacement, but avoid breaking ID pass.
# First, let's temporarily protect ID Pass card contents by extracting it.
import uuid
pass_match = re.search(r'(<div id="pass-card".*?<!-- ID Pass Card End -->)', html, flags=re.DOTALL)
if pass_match:
    pass_html = pass_match.group(1)
    placeholder = f"__PASS_{uuid.uuid4().hex}__"
    html = html.replace(pass_html, placeholder)
else:
    print("Could not find ID Pass card!")

# Now do generic replacements
reps = {
    'bg-[#FAFAFA]': 'bg-[#FAFAFA] dark:bg-[#111111]',
    'bg-white': 'bg-white dark:bg-[#1A1A1A]',
    'text-slate-800': 'text-slate-800 dark:text-slate-200',
    'text-slate-700': 'text-slate-700 dark:text-slate-300',
    'text-slate-600': 'text-slate-600 dark:text-slate-400',
    'text-slate-500': 'text-slate-500 dark:text-slate-400',
    'text-slate-400': 'text-slate-400 dark:text-slate-500',
    'text-black': 'text-black dark:text-white',
    'bg-slate-50': 'bg-slate-50 dark:bg-[#222222]',
    'bg-slate-100': 'bg-slate-100 dark:bg-[#222222]',
    'bg-slate-200': 'bg-slate-200 dark:bg-[#333333]',
    'border-slate-200': 'border-slate-200 dark:border-neutral-800',
    'border-slate-300': 'border-slate-300 dark:border-neutral-700'
}

for k, v in reps.items():
    # Only replace if not already replaced
    if v not in html:
        # Use regex to replace exact class word, preventing double replacement
        html = re.sub(r'(?<!dark:)\b' + re.escape(k) + r'\b', v, html)

# Restore ID Pass
if pass_match:
    html = html.replace(placeholder, pass_html)

# Add Orange Accents to ID pass.
# The user wants "add orange accords to the id pass"
# Let's change the bottom border of the header banner to orange, or add an orange block.
html = html.replace('border-bottom: 3px solid #000000;', 'border-bottom: 4px solid #EA580C;')
html = html.replace('border: 3px solid #10B981;', 'border: 3px solid #EA580C;') # VALID badge border
html = html.replace('background: rgba(16, 185, 129, 0.1);', 'background: rgba(234, 88, 12, 0.1);') # VALID badge bg
html = html.replace('color: #10B981;', 'color: #EA580C;') # VALID badge text

with open("web/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done!")
