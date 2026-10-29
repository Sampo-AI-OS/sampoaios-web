import re

path = r'D:\Sampo AI OS V2\sampo_os\dist_web\research.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update JSON-LD for EITN
old_eitn_json = '''      {
        "@type": "TechArticle",
        "@id": "https://sampoaios.com/research.html#mining-esg",
        "headline": "EITN Mining ESG Monitor: Cryptographically Audited IoT Telemetry, Tailings Dam Predictive Integrity, and Autonomous Regulatory Compliance for Extractive Industries",
        "identifier": "EITN-TR-2026-V1.0",
        "author": { "@id": "https://sampoaios.com/#architect" },'''

new_eitn_json = '''      {
        "@type": "TechArticle",
        "@id": "https://sampoaios.com/research.html#mining-esg",
        "headline": "EITN Mining ESG Monitor: Cryptographically Audited IoT Telemetry, Tailings Dam Predictive Integrity, and Autonomous Regulatory Compliance for Extractive Industries",
        "identifier": "EITN-TR-2026-V1.0",
        "sameAs": "https://doi.org/10.5281/zenodo.23753914",
        "author": { "@id": "https://sampoaios.com/#architect" },'''

content = content.replace(old_eitn_json, new_eitn_json)

# 2. Update JSON-LD for Quantum Identity
old_qs_json = '''      {
        "@type": "TechArticle",
        "@id": "https://sampoaios.com/research.html#quantum-identity",
        "headline": "Quantum-Safe Blockchain Identity Protocol: Post-Quantum Lattice Cryptography, Zero-Knowledge Selective Disclosure, and Decentralized Sovereign Attestation",
        "identifier": "QS-TR-2026-V1.0",
        "author": { "@id": "https://sampoaios.com/#architect" },'''

new_qs_json = '''      {
        "@type": "TechArticle",
        "@id": "https://sampoaios.com/research.html#quantum-identity",
        "headline": "Quantum-Safe Blockchain Identity Protocol: Post-Quantum Lattice Cryptography, Zero-Knowledge Selective Disclosure, and Decentralized Sovereign Attestation",
        "identifier": "QS-TR-2026-V1.0",
        "sameAs": "https://doi.org/10.5281/zenodo.23754131",
        "author": { "@id": "https://sampoaios.com/#architect" },'''

content = content.replace(old_qs_json, new_qs_json)

# 3. Update EITN Card Header
old_eitn_header = '''      <!-- PAPER 10: EITN Mining ESG Monitor (OCTOBER 2026) -->
      <article class="paper-card" data-cat="water" id="mining-esg">
        <div class="paper-header-meta">
          <span class="doc-id-pill">ID: EITN-TR-2026-V1.0</span>
          <span class="category-badge badge-blue">Mining ESG &amp; Structural Integrity • October 2026</span>
        </div>'''

new_eitn_header = '''      <!-- PAPER 10: EITN Mining ESG Monitor (OCTOBER 2026) -->
      <article class="paper-card" data-cat="water" id="mining-esg">
        <div class="paper-header-meta">
          <span class="doc-id-pill">ID: EITN-TR-2026-V1.0</span>
          <a href="https://doi.org/10.5281/zenodo.23753914" target="_blank" class="doi-badge-link"><span style="background: #10B981; color: white; padding: 1px 5px; border-radius: 3px; font-size: 0.68rem; font-weight: 700;">ZENODO DOI</span> 10.5281/zenodo.23753914</a>
          <span class="category-badge badge-blue">Mining ESG &amp; Structural Integrity • October 2026</span>
        </div>'''

content = content.replace(old_eitn_header, new_eitn_header)

# 4. Update EITN Actions & BibTeX
old_eitn_actions = '''        <div class="paper-actions">
          <a href="EITN_Mining_ESG_Monitor_Technical_Whitepaper_2026.pdf" target="_blank" class="btn-paper btn-paper-primary">
            📄 Download Technical Whitepaper PDF (356 KB)
          </a>
          <a href="EITN_Mining_ESG_Monitor_Technical_Whitepaper_2026.html" target="_blank" class="btn-paper btn-paper-secondary">
            🌐 Read Online (HTML Edition)
          </a>
          <button class="btn-paper btn-paper-cite" onclick="toggleCitation('cite-eitn')">
            📋 Copy BibTeX Citation
          </button>
        </div>

        <div id="cite-eitn" class="citation-drawer">
          <span class="copy-confirm-badge" id="badge-eitn">Copied!</span>
          <pre>@techreport{lanzett2026miningesg,
  title={EITN Mining ESG Monitor: Cryptographically Audited IoT Telemetry, Tailings Dam Predictive Integrity, and Autonomous Regulatory Compliance for Extractive Industries},
  author={Lanzett, Harri},
  institution={Sampo AI Research Laboratory and Lansec Oy},
  year={2026},
  month={October},
  number={EITN-TR-2026-V1.0},
  url={https://sampoaios.com/EITN_Mining_ESG_Monitor_Technical_Whitepaper_2026.pdf}
}</pre>
        </div>'''

new_eitn_actions = '''        <div class="paper-actions">
          <a href="EITN_Mining_ESG_Monitor_Technical_Whitepaper_2026.pdf" target="_blank" class="btn-paper btn-paper-primary">
            📄 Download Technical Whitepaper PDF (356 KB)
          </a>
          <a href="https://doi.org/10.5281/zenodo.23753914" target="_blank" class="btn-paper btn-paper-zenodo">
            🌐 Open on Zenodo (CERN)
          </a>
          <a href="EITN_Mining_ESG_Monitor_Technical_Whitepaper_2026.html" target="_blank" class="btn-paper btn-paper-secondary">
            🌐 Read Online (HTML Edition)
          </a>
          <button class="btn-paper btn-paper-cite" onclick="toggleCitation('cite-eitn')">
            📋 Copy BibTeX Citation
          </button>
        </div>

        <div id="cite-eitn" class="citation-drawer">
          <span class="copy-confirm-badge" id="badge-eitn">Copied!</span>
          <pre>@techreport{lanzett2026miningesg,
  title={EITN Mining ESG Monitor: Cryptographically Audited IoT Telemetry, Tailings Dam Predictive Integrity, and Autonomous Regulatory Compliance for Extractive Industries},
  author={Lanzett, Harri},
  institution={Sampo AI Research Laboratory and Lansec Oy},
  year={2026},
  month={October},
  number={EITN-TR-2026-V1.0},
  doi={10.5281/zenodo.23753914},
  url={https://doi.org/10.5281/zenodo.23753914}
}</pre>
        </div>'''

content = content.replace(old_eitn_actions, new_eitn_actions)

# 5. Update Quantum Identity Card Header
old_qs_header = '''      <!-- PAPER 11: Quantum-Safe Blockchain Identity Protocol (OCTOBER 2026) -->
      <article class="paper-card" data-cat="security" id="quantum-identity">
        <div class="paper-header-meta">
          <span class="doc-id-pill">ID: QS-TR-2026-V1.0</span>
          <span class="category-badge badge-teal">Post-Quantum Cryptography • October 2026</span>
        </div>'''

new_qs_header = '''      <!-- PAPER 11: Quantum-Safe Blockchain Identity Protocol (OCTOBER 2026) -->
      <article class="paper-card" data-cat="security" id="quantum-identity">
        <div class="paper-header-meta">
          <span class="doc-id-pill">ID: QS-TR-2026-V1.0</span>
          <a href="https://doi.org/10.5281/zenodo.23754131" target="_blank" class="doi-badge-link"><span style="background: #10B981; color: white; padding: 1px 5px; border-radius: 3px; font-size: 0.68rem; font-weight: 700;">ZENODO DOI</span> 10.5281/zenodo.23754131</a>
          <span class="category-badge badge-teal">Post-Quantum Cryptography • October 2026</span>
        </div>'''

content = content.replace(old_qs_header, new_qs_header)

# 6. Update Quantum Identity Actions & BibTeX
old_qs_actions = '''        <div class="paper-actions">
          <a href="Quantum_Identity_Protocol_Technical_Whitepaper_2026.pdf" target="_blank" class="btn-paper btn-paper-primary">
            📄 Download Technical Whitepaper PDF (362 KB)
          </a>
          <a href="https://youtu.be/8VBGdZmdQ2k" target="_blank" class="btn-paper btn-paper-video">
            📺 Watch Vodcast (Ep. 5)
          </a>
          <a href="Quantum_Identity_Protocol_Technical_Whitepaper_2026.html" target="_blank" class="btn-paper btn-paper-secondary">
            🌐 Read Online (HTML Edition)
          </a>
          <button class="btn-paper btn-paper-cite" onclick="toggleCitation('cite-qs')">
            📋 Copy BibTeX Citation
          </button>
        </div>

        <div id="cite-qs" class="citation-drawer">
          <span class="copy-confirm-badge" id="badge-qs">Copied!</span>
          <pre>@techreport{lanzett2026quantumidentity,
  title={Quantum-Safe Blockchain Identity Protocol: Post-Quantum Lattice Cryptography, Zero-Knowledge Selective Disclosure, and Decentralized Sovereign Attestation},
  author={Lanzett, Harri},
  institution={Sampo AI Research Laboratory and Lansec Oy},
  year={2026},
  month={October},
  number={QS-TR-2026-V1.0},
  url={https://sampoaios.com/Quantum_Identity_Protocol_Technical_Whitepaper_2026.pdf}
}</pre>
        </div>'''

new_qs_actions = '''        <div class="paper-actions">
          <a href="Quantum_Identity_Protocol_Technical_Whitepaper_2026.pdf" target="_blank" class="btn-paper btn-paper-primary">
            📄 Download Technical Whitepaper PDF (362 KB)
          </a>
          <a href="https://doi.org/10.5281/zenodo.23754131" target="_blank" class="btn-paper btn-paper-zenodo">
            🌐 Open on Zenodo (CERN)
          </a>
          <a href="https://youtu.be/8VBGdZmdQ2k" target="_blank" class="btn-paper btn-paper-video">
            📺 Watch Vodcast (Ep. 5)
          </a>
          <a href="Quantum_Identity_Protocol_Technical_Whitepaper_2026.html" target="_blank" class="btn-paper btn-paper-secondary">
            🌐 Read Online (HTML Edition)
          </a>
          <button class="btn-paper btn-paper-cite" onclick="toggleCitation('cite-qs')">
            📋 Copy BibTeX Citation
          </button>
        </div>

        <div id="cite-qs" class="citation-drawer">
          <span class="copy-confirm-badge" id="badge-qs">Copied!</span>
          <pre>@techreport{lanzett2026quantumidentity,
  title={Quantum-Safe Blockchain Identity Protocol: Post-Quantum Lattice Cryptography, Zero-Knowledge Selective Disclosure, and Decentralized Sovereign Attestation},
  author={Lanzett, Harri},
  institution={Sampo AI Research Laboratory and Lansec Oy},
  year={2026},
  month={October},
  number={QS-TR-2026-V1.0},
  doi={10.5281/zenodo.23754131},
  url={https://doi.org/10.5281/zenodo.23754131}
}</pre>
        </div>'''

content = content.replace(old_qs_actions, new_qs_actions)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated research.html with EITN and Quantum-Safe DOIs!")
