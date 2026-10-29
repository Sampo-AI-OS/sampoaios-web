# -*- coding: utf-8 -*-
target_file = r'D:\Sampo AI OS V2\sampo_os\dist_web\research.html'

with open(target_file, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update EITN Mining ESG (DOI 10.5281/zenodo.23753914)
old_eitn_hdr = '<article class="paper-card" data-cat="water" id="mining-esg">\n        <div class="paper-header-meta">\n          <span class="doc-id-pill">ID: EITN-TR-2026-V1.0</span>'
new_eitn_hdr = '''<article class="paper-card" data-cat="water" id="mining-esg">
        <div class="paper-header-meta">
          <span class="doc-id-pill">ID: EITN-TR-2026-V1.0</span>
          <a href="https://doi.org/10.5281/zenodo.23753914" target="_blank" class="doi-badge-link">
            <span style="background: #10B981; color: white; padding: 1px 5px; border-radius: 3px; font-size: 0.68rem; font-weight: 700;">ZENODO DOI</span>
            10.5281/zenodo.23753914
          </a>'''
text = text.replace(old_eitn_hdr, new_eitn_hdr, 1)

old_eitn_act = '<a href="EITN_Mining_ESG_Monitor_Technical_Whitepaper_2026.pdf" target="_blank" class="btn-paper btn-paper-primary">\n            📄 Download Technical Whitepaper PDF (356 KB)\n          </a>'
new_eitn_act = '''<a href="EITN_Mining_ESG_Monitor_Technical_Whitepaper_2026.pdf" target="_blank" class="btn-paper btn-paper-primary">
            📄 Download Technical Whitepaper PDF (356 KB)
          </a>
          <a href="https://doi.org/10.5281/zenodo.23753914" target="_blank" class="btn-paper btn-paper-zenodo">
            🌐 Open on Zenodo (CERN)
          </a>'''
text = text.replace(old_eitn_act, new_eitn_act, 1)

old_eitn_bib = '''  number={EITN-TR-2026-V1.0},
  url={https://sampoaios.com/EITN_Mining_ESG_Monitor_Technical_Whitepaper_2026.pdf}'''
new_eitn_bib = '''  number={EITN-TR-2026-V1.0},
  doi={10.5281/zenodo.23753914},
  url={https://doi.org/10.5281/zenodo.23753914}'''
text = text.replace(old_eitn_bib, new_eitn_bib, 1)

text = text.replace('"identifier": "EITN-TR-2026-V1.0"', '"identifier": "EITN-TR-2026-V1.0",\n        "sameAs": "https://doi.org/10.5281/zenodo.23753914"', 1)

# 2. Update Quantum-Safe Identity (DOI 10.5281/zenodo.23754131)
old_qs_hdr = '<article class="paper-card" data-cat="security" id="quantum-identity">\n        <div class="paper-header-meta">\n          <span class="doc-id-pill">ID: QS-TR-2026-V1.0</span>'
new_qs_hdr = '''<article class="paper-card" data-cat="security" id="quantum-identity">
        <div class="paper-header-meta">
          <span class="doc-id-pill">ID: QS-TR-2026-V1.0</span>
          <a href="https://doi.org/10.5281/zenodo.23754131" target="_blank" class="doi-badge-link">
            <span style="background: #10B981; color: white; padding: 1px 5px; border-radius: 3px; font-size: 0.68rem; font-weight: 700;">ZENODO DOI</span>
            10.5281/zenodo.23754131
          </a>'''
text = text.replace(old_qs_hdr, new_qs_hdr, 1)

old_qs_act = '<a href="Quantum_Identity_Protocol_Technical_Whitepaper_2026.pdf" target="_blank" class="btn-paper btn-paper-primary">\n            📄 Download Technical Whitepaper PDF (362 KB)\n          </a>'
new_qs_act = '''<a href="Quantum_Identity_Protocol_Technical_Whitepaper_2026.pdf" target="_blank" class="btn-paper btn-paper-primary">
            📄 Download Technical Whitepaper PDF (362 KB)
          </a>
          <a href="https://doi.org/10.5281/zenodo.23754131" target="_blank" class="btn-paper btn-paper-zenodo">
            🌐 Open on Zenodo (CERN)
          </a>'''
text = text.replace(old_qs_act, new_qs_act, 1)

old_qs_bib = '''  number={QS-TR-2026-V1.0},
  url={https://sampoaios.com/Quantum_Identity_Protocol_Technical_Whitepaper_2026.pdf}'''
new_qs_bib = '''  number={QS-TR-2026-V1.0},
  doi={10.5281/zenodo.23754131},
  url={https://doi.org/10.5281/zenodo.23754131}'''
text = text.replace(old_qs_bib, new_qs_bib, 1)

text = text.replace('"identifier": "QS-TR-2026-V1.0"', '"identifier": "QS-TR-2026-V1.0",\n        "sameAs": "https://doi.org/10.5281/zenodo.23754131"', 1)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(text)

print("Both EITN and Quantum Identity DOIs applied successfully!")
