import re

with open("web/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# I'll just use string replacement
old = """    function handlePartnerLogin(e) {
      e.preventDefault();
      const sel = document.getElementById('partner-select');
      const pin = document.getElementById('partner-pin').value.trim();
      const err = document.getElementById('partner-error');

      if (sel.selectedIndex <= 0) {
        err.innerText = "Please select a partner store";
        err.classList.remove('hidden');
        return;
      }

      const opt = sel.options[sel.selectedIndex];
      const realPin = opt.getAttribute('data-pin');

      if (pin === realPin) {
        window.appState.userRole = 'partner';
        window.appState.partnerData = { id: opt.value, name: opt.innerText };
        if (document.getElementById('partner-remember').checked) {
          localStorage.setItem('jmap_session_role', 'partner');
          localStorage.setItem('jmap_session_partner_id', opt.value);
          localStorage.setItem('jmap_session_partner_name', opt.innerText);
        }
        startSession();
      } else {
        err.innerText = "Incorrect 4-digit PIN!";
        err.classList.remove('hidden');
      }
    }"""

new = """    function handlePartnerLogin(e) {
      e.preventDefault();
      const usernameInput = document.getElementById('partner-username').value.trim();
      const pin = document.getElementById('partner-pin').value.trim();
      const err = document.getElementById('partner-error');
      err.classList.add('hidden');
      
      if (!usernameInput) {
        err.innerText = "Please enter a username";
        err.classList.remove('hidden');
        return;
      }

      // Find the store by username (saved in the name field)
      const store = window.appState.stores.find(s => s.name.toLowerCase() === usernameInput.toLowerCase());
      
      if (!store) {
        err.innerText = "Username not found";
        err.classList.remove('hidden');
        return;
      }

      if (pin === store.pin) {
        window.appState.userRole = 'partner';
        window.appState.partnerData = { id: store.id || store.docId, name: store.name };
        if (document.getElementById('partner-remember').checked) {
          localStorage.setItem('jmap_session_role', 'partner');
          localStorage.setItem('jmap_session_partner_id', store.id || store.docId);
          localStorage.setItem('jmap_session_partner_name', store.name);
        }
        startSession();
      } else {
        err.innerText = "Incorrect 4-digit PIN!";
        err.classList.remove('hidden');
      }
    }"""

content = content.replace(old, new)

with open("web/index.html", "w", encoding="utf-8") as f:
    f.write(content)
