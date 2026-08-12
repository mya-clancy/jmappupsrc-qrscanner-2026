import re

with open("web/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# --- 1. Global Color Replacements ---
# Replace Tailwind configuration maroon
content = content.replace("maroon: '#800000'", "maroon: '#000000'")
content = content.replace("maroonDark: '#4A0000'", "maroonDark: '#111111'")
content = content.replace("maroonDeep: '#280202'", "maroonDeep: '#222222'")

# Replace class usages
content = content.replace("bg-pup-maroon", "bg-black")
content = content.replace("text-pup-maroon", "text-black")
content = content.replace("border-pup-maroon", "border-black")

# Login screen header line (from-red to from-orange)
content = content.replace("from-red-900 to-red-600", "from-orange-500 to-yellow-400")

# Other red buttons -> orange or black
content = content.replace("hover:bg-red-900", "hover:bg-neutral-800")
content = content.replace("bg-red-950", "bg-neutral-900")
content = content.replace("border-red-900/50", "border-black/20")
content = content.replace("border-red-800", "border-neutral-700")
content = content.replace("bg-red-100", "bg-orange-100")
content = content.replace("text-red-800", "text-orange-800")
content = content.replace("border-red-400", "border-orange-400")
content = content.replace("border-red-500", "border-orange-500")
content = content.replace("bg-red-50/50", "bg-orange-50/50")
content = content.replace("dark:bg-red-950/40", "dark:bg-orange-950/40")

# Admin Portal login form text changes
# Admin button
content = content.replace('<button type="submit" class="w-full bg-pup-maroon', '<button type="submit" class="w-full bg-black')
content = content.replace('bg-pup-gold hover:bg-yellow-500 text-pup-maroon', 'bg-pup-gold hover:bg-yellow-500 text-black')

# --- 2. Partner Cashier to Business Partners (Form Updates) ---
# Check existing form
old_partner_form = """      <form id="form-partner" onsubmit="handlePartnerLogin(event)" class="space-y-4 hidden">
        <div>
          <label class="block text-xs font-bold text-slate-600 dark:text-slate-300 mb-1 uppercase tracking-wider">Select Partner Business</label>
          <select id="partner-select" required class="w-full px-4 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700/40 bg-white dark:bg-pup-darkCard text-sm focus:outline-none focus:ring-2 focus:ring-pup-gold">
            <option value="">Select a Partner Store...</option>
          </select>
        </div>"""
new_partner_form = """      <form id="form-partner" onsubmit="handlePartnerLogin(event)" class="space-y-4 hidden">
        <div>
          <label class="block text-xs font-bold text-slate-600 dark:text-slate-300 mb-1 uppercase tracking-wider">Business Partner Username</label>
          <input type="text" id="partner-username" required placeholder="Enter username" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700/40 bg-white dark:bg-pup-darkCard text-sm focus:outline-none focus:ring-2 focus:ring-pup-gold">
        </div>"""
content = content.replace(old_partner_form, new_partner_form)

# Modal form for adding store
old_store_modal = """        <div>
          <label class="block mb-1 text-slate-600 dark:text-slate-300">Store Name</label>
          <input type="text" id="store-name" required value="" placeholder="Partner Store Name" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700/40 bg-slate-50 dark:bg-pup-darkCard text-sm focus:outline-none">
        </div>"""
new_store_modal = """        <div>
          <label class="block mb-1 text-slate-600 dark:text-slate-300">Store Username</label>
          <input type="text" id="store-name" required value="" placeholder="Partner Username" class="w-full p-2.5 rounded-xl border border-slate-300 dark:border-slate-700/40 bg-slate-50 dark:bg-pup-darkCard text-sm focus:outline-none">
        </div>"""
content = content.replace(old_store_modal, new_store_modal)

# JS logic update for partner login
old_partner_js = """    async function handlePartnerLogin(e) {
      e.preventDefault();
      const sel = document.getElementById('partner-select');
      const pin = document.getElementById('partner-pin').value;
      if (sel.selectedIndex <= 0) return alert('Select a partner');

      const storeId = sel.options[sel.selectedIndex].value;
      const storeName = sel.options[sel.selectedIndex].innerText;
      const actualPin = sel.options[sel.selectedIndex].getAttribute('data-pin');

      if (pin !== actualPin) {
        const err = document.getElementById('partner-error');
        err.innerText = "Invalid Access PIN";
        err.classList.remove('hidden');
        return;
      }"""
new_partner_js = """    async function handlePartnerLogin(e) {
      e.preventDefault();
      const usernameInput = document.getElementById('partner-username').value.trim();
      const pin = document.getElementById('partner-pin').value;
      
      const err = document.getElementById('partner-error');
      err.classList.add('hidden');
      
      if (!usernameInput) return alert('Enter a username');

      // Find the store by username (saved in the name field)
      const store = window.appState.stores.find(s => s.name.toLowerCase() === usernameInput.toLowerCase());
      
      if (!store) {
        err.innerText = "Username not found";
        err.classList.remove('hidden');
        return;
      }

      if (pin !== store.pin) {
        err.innerText = "Invalid Access PIN";
        err.classList.remove('hidden');
        return;
      }
      
      const storeId = store.docId;
      const storeName = store.name;"""
content = content.replace(old_partner_js, new_partner_js)

# Remove populateStores code that added to select dropdown
old_pop = """    function populateStores() {
      const sel = document.getElementById('partner-select');
      if(sel) {
        sel.innerHTML = '<option value="">Select a Partner Store...</option>';
        window.appState.stores.forEach(s => {
          sel.innerHTML += `<option value="${s.docId}" data-pin="${s.pin}">${s.name}</option>`;
        });
      }
    }"""
new_pop = """    function populateStores() {
      // Dropdown removed, using username login instead.
    }"""
content = content.replace(old_pop, new_pop)


# --- 3. QR Code JMAP image ---
old_jmap = """<span class="font-extrabold text-[#0F172A]" style="font-size: 20px;">JMAP</span>"""
new_jmap = """<img src="assets/jmap_kappa.png" alt="JMAP Kappa" class="w-full h-full object-contain" />"""
content = content.replace(old_jmap, new_jmap)


# Write back
with open("web/index.html", "w", encoding="utf-8") as f:
    f.write(content)

