import streamlit as st

from core import config

st.set_page_config(page_title=config.APP_NAME, page_icon="🛡️", layout="wide")

st.title("🛡️ CyberSec Toolkit")
st.caption("Defensive Security Dashboard · OSINT · Web · Network · Forensics · Defense · Reports")

st.warning("**Use responsibly.** Only test systems you own or have written permission to assess. "
           "Uploaded files are analysed in memory and are never executed.")

cols = st.columns(3)
cards = [
    ("pages/01_OSINT.py", "🔎", "OSINT & Recon", "DNS, email security (SPF/DMARC/DKIM), username presence, file metadata."),
    ("pages/02_Web_Security.py", "🌐", "Web Security", "Security headers, TLS/certificate, cookies, technology detection."),
    ("pages/03_Network.py", "📡", "Network", "Limited port scanner, PCAP analyzer, host information."),
    ("pages/04_Forensics.py", "🕵️", "Forensics", "Hashes, entropy, strings, file-type & PE analysis."),
    ("pages/05_Defense.py", "🛡️", "Defense", "File integrity, log analyzer, server audit, process monitor."),
    ("pages/06_Honeypot.py", "🍯", "Honeypot", "Cowrie log dashboard (with demo data)."),
]
for i, (path, icon, title, desc) in enumerate(cards):
    with cols[i % 3]:
        with st.container(border=True):
            st.subheader(f"{icon} {title}")
            st.write(desc)
            st.page_link(path, label=f"Open {title}")

with st.container(border=True):
    st.subheader("📊 Reports")
    st.write("Every tool stores structured findings (🔴 HIGH · 🟠 MEDIUM · 🟡 LOW · 🔵 INFO). "
             "Combine them into a scored HTML/JSON report.")
    st.page_link("pages/07_Reports.py", label="Open Reports")

mode = "Local lab mode" if config.LOCAL_MODE else "Public cloud mode (internal/private targets blocked)"
st.sidebar.info(f"**Mode:** {mode}\n\nVersion {config.VERSION}")
