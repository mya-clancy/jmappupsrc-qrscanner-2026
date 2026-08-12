import re

with open("web/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove dark mode classes
content = re.sub(r'\s*dark:([a-zA-Z0-9/-]+(\[[^\]]+\])?)', '', content)

# Remove toggle mode button HTML completely
toggle_btn = r'<button onclick="toggleDarkMode\(\)".*?</button>'
content = re.sub(toggle_btn, '', content, flags=re.DOTALL)

# Remove toggleDarkMode JS function
toggle_func = r'\s*function toggleDarkMode\(\) \{.*?\n    \}'
content = re.sub(toggle_func, '', content, flags=re.DOTALL)

# Remove window.toggleDarkMode = toggleDarkMode
content = content.replace("window.toggleDarkMode = toggleDarkMode;", "")

# Replace bg-slate-100 (which was the light bg) with white or a very light orange/gray? The image is white.
content = content.replace('bg-slate-100', 'bg-white')
content = content.replace('bg-white', 'bg-[#FAFAFA]', 1) # Maybe leave body as #FAFAFA, but others as white? Actually just let it be white.
content = content.replace('bg-slate-100 text-slate-800 min-h-screen', 'bg-white text-black min-h-screen')

# The login screen bg should be white
content = content.replace('bg-slate-100', 'bg-white')

with open("web/index.html", "w", encoding="utf-8") as f:
    f.write(content)
