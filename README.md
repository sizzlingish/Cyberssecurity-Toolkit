# 🛡️ CyberSec Toolkit

A modular Python **defensive-security dashboard** built with Streamlit: OSINT, web security, network analysis,
digital forensics, defensive tooling, a honeypot dashboard and scored HTML/JSON reports.

> ⚠️ Only test systems you own or have written permission to assess. Uploaded files are analysed statically in memory and never executed.

## Features
| Section | Tools |
|---|---|
| 🔎 OSINT | DNS records, SPF/DMARC/DKIM/DNSSEC/CAA checks, username presence, file metadata (EXIF/PDF/Office) |
| 🌐 Web | Security headers, TLS protocols & certificate, cookie flags, technology detection |
| 📡 Network | Rate-limited port scanner, PCAP analyzer (pcap/pcapng), host info |
| 🕵️ Forensics | Multi-hash, Shannon entropy, strings, file-type & PE header analysis |
| 🛡️ Defense | File integrity (ZIP baselines), log analyzer (SSH/web logs, brute-force detection), server audit, process monitor |
| 🍯 Honeypot | Cowrie JSON-lines dashboard (+ synthetic demo data) |
| 📊 Reports | Severity-scored findings → `security_report.html` / `.json` |

## Deploy on Streamlit Community Cloud
1. Create a GitHub repo and push this folder (`git init && git add . && git commit -m "init" && git push`).
2. Go to <https://share.streamlit.io> → **New app** → pick the repo.
3. Set **Main file path** to `app.py` → **Deploy**. Every `git push` redeploys automatically.

## Architecture
```
pages/ (Streamlit UI)  →  modules/ (analysis logic)  →  core/findings (Finding + Severity)  →  reports/
```
Pages only handle input/output; all logic lives in `modules/` and returns structured `Finding` objects.

## Safety design (important for a public deployment)
- **SSRF protection:** every URL/host (including redirect hops) must resolve to a *public* IP; localhost, LAN and cloud-metadata addresses are blocked.
- Port scanner limited to **100 ports**, short timeouts, authorisation checkbox required.
- Upload cap 50 MB, ZIP-bomb protection in integrity checker, no file execution.
- Server-side tools (System Audit, Process Monitor) inspect the **hosting container**, not the visitor's PC.

## Local lab mode
```bash
pip install -r requirements.txt
CYBERSEC_LOCAL_MODE=1 streamlit run app.py   # enables private/LAN targets, up to 1024 ports
```

## Tests
```bash
pytest
```

## Roadmap
Forensic timeline, service fingerprinting, PDF reports, threat-intel API integrations, Dockerfile.

## License
MIT
