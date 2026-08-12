import re

with open("web/index.html", "r", encoding="utf-8") as f:
    content = f.read()

old_css = """    .id-pass-card {
      container-type: inline-size;
      width: 100%;
      max-width: 680px;
      aspect-ratio: 1.586 / 1;
      background: #FFFFFF;
      border-radius: 4cqw;
      border: 0.1cqw solid #000000;
      box-shadow: 0 2cqw 5cqw rgba(0, 0, 0, 0.7);
      color: #0F172A;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-sizing: border-box;
      margin: 0 auto;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    .id-pass-header-banner {
      background-color: #FFC107;
      border-bottom: 0.3cqw solid #000000;
      padding: 2.5cqw 4cqw;
    }

    .id-pass-header-banner .title {
      font-size: 2.2cqw;
      font-weight: 800;
      letter-spacing: 0.02em;
      color: #0F172A;
      text-transform: uppercase;
    }
    
    .id-pass-header-banner .subtitle {
      font-size: 1.4cqw;
      font-weight: 600;
      letter-spacing: 0.05em;
      color: #0F172A;
      text-transform: uppercase;
      margin-top: 0.4cqw;
    }

    .id-pass-body {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 3.5cqw;
      flex: 1;
      padding: 3cqw 4cqw 1cqw 4cqw;
    }

    .id-pass-info {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      height: 100%;
    }

    .id-pass-info > div {
      margin-bottom: 1.5cqw;
    }

    .id-pass-label {
      font-size: 1.3cqw;
      letter-spacing: 0.08em;
      color: #0F172A;
      font-weight: 800;
      text-transform: uppercase;
      margin-bottom: 0.4cqw;
      opacity: 0.7;
    }

    .id-pass-val {
      font-size: 2.6cqw;
      font-weight: 800;
      color: #0F172A;
      line-height: 1.2;
    }

    .id-pass-badge {
      display: inline-flex;
      align-items: center;
      padding: 0.6cqw 1.8cqw;
      border-radius: 0.8cqw;
      border: 0.25cqw solid #10B981;
      background: rgba(16, 185, 129, 0.1);
      color: #10B981;
      font-size: 1.8cqw;
      font-weight: 500;
      width: fit-content;
      margin-top: 0.2cqw;
    }

    .id-pass-badge.pending {
      border-color: #F59E0B;
      background: rgba(245, 158, 11, 0.1);
      color: #F59E0B;
    }

    .id-pass-qr-frame {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 0.8cqw;
      align-self: flex-start;
      margin-top: 1cqw;
    }

    .id-pass-qr-box {
      background: #FFFFFF;
      border: 0.2cqw solid #000000;
      border-radius: 1.5cqw;
      padding: 0.8cqw;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .id-pass-qr-box canvas {
      width: 32cqw !important;
      height: 32cqw !important;
      display: block;
    }

    .id-pass-qr-label {
      font-size: 1.4cqw;
      font-weight: 800;
      color: #0F172A;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }

    .id-pass-footer {
      border-top: 0.3cqw solid #000000;
      padding: 1.5cqw 4cqw;
      font-size: 1.3cqw;
      color: #0F172A;
      font-weight: 600;
      text-align: center;
      letter-spacing: 0.05em;
      margin-bottom: 0;
      background-color: #FFFFFF;
    }"""

new_css = """    .id-pass-wrapper {
      width: 100%;
      overflow-x: auto;
      display: flex;
      justify-content: flex-start;
      padding-bottom: 1rem;
    }
    
    @media (min-width: 1050px) {
      .id-pass-wrapper { justify-content: center; }
    }
    
    .id-pass-card {
      min-width: 1013px;
      width: 1013px;
      height: 638px;
      background: #FFFFFF;
      border-radius: 40px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
      color: #0F172A;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-sizing: border-box;
      margin: 0 auto;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      transform-origin: top left;
    }
    
    /* Responsive scaling for mobile preview */
    @media (max-width: 1050px) {
      .id-pass-card { transform: scale(0.8); margin-bottom: -127px; }
    }
    @media (max-width: 850px) {
      .id-pass-card { transform: scale(0.65); margin-bottom: -223px; }
    }
    @media (max-width: 650px) {
      .id-pass-card { transform: scale(0.5); margin-bottom: -319px; }
    }
    @media (max-width: 500px) {
      .id-pass-card { transform: scale(0.35); margin-bottom: -414px; }
    }
    @media (max-width: 380px) {
      .id-pass-card { transform: scale(0.28); margin-bottom: -459px; }
    }

    .id-pass-header-banner {
      background-color: #FFC107;
      border-bottom: 3px solid #000000;
      padding: 25px 40px;
    }

    .id-pass-header-banner .title {
      font-size: 22px;
      font-weight: 800;
      letter-spacing: 0.02em;
      color: #0F172A;
      text-transform: uppercase;
    }
    
    .id-pass-header-banner .subtitle {
      font-size: 14px;
      font-weight: 600;
      letter-spacing: 0.05em;
      color: #0F172A;
      text-transform: uppercase;
      margin-top: 4px;
    }

    .id-pass-body {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 35px;
      flex: 1;
      padding: 30px 40px 10px 40px;
    }

    .id-pass-info {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      height: 100%;
    }

    .id-pass-info > div {
      margin-bottom: 15px;
    }

    .id-pass-label {
      font-size: 13px;
      letter-spacing: 0.08em;
      color: #0F172A;
      font-weight: 800;
      text-transform: uppercase;
      margin-bottom: 4px;
      opacity: 0.7;
    }

    .id-pass-val {
      font-size: 26px;
      font-weight: 800;
      color: #0F172A;
      line-height: 1.2;
    }

    .id-pass-badge {
      display: inline-flex;
      align-items: center;
      padding: 6px 18px;
      border-radius: 8px;
      border: 3px solid #10B981;
      background: rgba(16, 185, 129, 0.1);
      color: #10B981;
      font-size: 18px;
      font-weight: 500;
      width: fit-content;
      margin-top: 2px;
    }

    .id-pass-badge.pending {
      border-color: #F59E0B;
      background: rgba(245, 158, 11, 0.1);
      color: #F59E0B;
    }

    .id-pass-qr-frame {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 8px;
      align-self: flex-start;
      margin-top: 10px;
    }

    .id-pass-qr-box {
      background: #FFFFFF;
      border: 2px solid #000000;
      border-radius: 15px;
      padding: 8px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .id-pass-qr-box canvas {
      width: 324px !important;
      height: 324px !important;
      display: block;
    }

    .id-pass-qr-label {
      font-size: 14px;
      font-weight: 800;
      color: #0F172A;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }

    .id-pass-footer {
      border-top: 3px solid #000000;
      padding: 15px 40px;
      font-size: 13px;
      color: #0F172A;
      font-weight: 600;
      text-align: center;
      letter-spacing: 0.05em;
      margin-bottom: 0;
      background-color: #FFFFFF;
    }"""

content = content.replace(old_css, new_css)

# Update HTML wrapper
old_html = """      <!-- EXACT REPLICA ID PASS CARD MATCHING REFERENCE IMAGE 3 -->
      <div id="printable-id-card" class="id-pass-card">"""
new_html = """      <!-- EXACT REPLICA ID PASS CARD MATCHING REFERENCE IMAGE 3 -->
      <div class="id-pass-wrapper custom-scrollbar">
        <div id="printable-id-card" class="id-pass-card">"""
content = content.replace(old_html, new_html)

# Close wrapper
old_close = """        <!-- Footer Bar -->
        <div class="id-pass-footer">
          Junior Marketing Association of the Philippines - PUP Santa Rosa
        </div>
      </div>

      <!-- Action Buttons -->"""
new_close = """        <!-- Footer Bar -->
        <div class="id-pass-footer">
          Junior Marketing Association of the Philippines - PUP Santa Rosa
        </div>
        </div>
      </div>

      <!-- Action Buttons -->"""
content = content.replace(old_close, new_close)

# Change JMAP QR Text font size
old_jmap_text = """<span class="font-extrabold text-[#0F172A]" style="font-size: 2cqw;">JMAP</span>"""
new_jmap_text = """<span class="font-extrabold text-[#0F172A]" style="font-size: 20px;">JMAP</span>"""
content = content.replace(old_jmap_text, new_jmap_text)

# Enforce html-to-image exact dimensions without scale
old_save_local = """            const dataUrl = await htmlToImage.toJpeg(card, { quality: 0.95, pixelRatio: 2 });"""
new_save_local = """            const dataUrl = await htmlToImage.toJpeg(card, { 
                quality: 1.0, 
                pixelRatio: 1, 
                width: 1013, 
                height: 638,
                style: { transform: 'none', transformOrigin: 'top left', margin: '0' }
            });"""
content = content.replace(old_save_local, new_save_local)

old_save_drive = """                const dataUrl = await htmlToImage.toJpeg(card, { quality: 0.95, pixelRatio: 2 });"""
new_save_drive = """                const dataUrl = await htmlToImage.toJpeg(card, { 
                    quality: 1.0, 
                    pixelRatio: 1, 
                    width: 1013, 
                    height: 638,
                    style: { transform: 'none', transformOrigin: 'top left', margin: '0' }
                });"""
content = content.replace(old_save_drive, new_save_drive)

with open("web/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Pixel dimensions fixed.")
