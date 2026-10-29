# -*- coding: utf-8 -*-
target_file = r'D:\Sampo AI OS V2\sampo_os\dist_web\research.html'

with open(target_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Update header
old_hdr = '<article class="paper-card" data-cat="water" id="mining-esg">\n        <div class="paper-header-meta">\n          <span class="doc-id-pill">ID: EITN-TR-2026-V1.0</span>'
new_hdr = '''<article class="paper-card" data-cat="water" id="mining-esg">
        <div class="paper-header-meta">
          <span class="doc-id-pill">ID: EITN-TR-2026-V1.0</span>
          <a href="https://doi.org/10.5281/zenodo.23753914" target="_blank" class="doi-badge-link">
            <span style="background: #10B981; color: white; padding: 1px 5px; border-radius: 3px; font-size: 0.68rem; font-weight: 700;">ZENODO DOI</span>
            10.5281/zenodo.23753914
          </a>'''
text = text.replace(old_hdr, new_hdr, 1)

# Update actions
old_act = '<a href="EITN_Mining_ESG_Monitor_Technical_Whitepaper_2026.pdf" target="_blank" class="btn-paper btn-paper-primary">\n            📄 Download Technical Whitepaper PDF (356 KB)\n          </a>'
new_act = '''<a href="EITN_Mining_ESG_Monitor_Technical_Whitepaper_2026.pdf" target="_blank" class="btn-paper btn-paper-primary">
            📄 Download Technical Whitepaper PDF (356 KB)
          </a>
          <a href="https://doi.org/10.5281/zenodo.23753914" target="_blank" class="btn-paper btn-paper-zenodo">
            🌐 Open on Zenodo (CERN)
          </a>'''
text = text.replace(old_act, new_act, 1)

# Update BibTeX
old_bib = '''  number={EITN-TR-2026-V1.0},
  url={https://sampoaios.com/EITN_Mining_ESG_Monitor_Technical_Whitepaper_2026.pdf}'''
new_bib = '''  number={EITN-TR-2026-V1.0},
  doi={10.5281/zenodo.23753914},
  url={https://doi.org/10.5281/zenodo.23753914}'''
text = text.replace(old_bib, new_bib, 1)

# Update JSON-LD
text = text.replace('"identifier": "EITN-TR-2026-V1.0"', '"identifier": "EITN-TR-2026-V1.0",\n        "sameAs": "https://doi.org/10.5281/zenodo.23753914"', 1)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(text)

print("EITN Mining ESG updated with DOI successfully!")
