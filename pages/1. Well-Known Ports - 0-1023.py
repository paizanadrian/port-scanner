import streamlit as st
import socket
import pandas as pd
import time  

# Dicționar cu porturi și servicii asociate (doar pentru afișare)
ports_services = {
    20: "FTP (Transfer de fișiere - date)",
    21: "FTP (Control de conexiune)",
    22: "SSH (Secure Shell - acces securizat la server)",
    23: "Telnet (Protocol vechi de acces la servere, nesecurizat)",
    25: "SMTP (Trimitere e-mail)",
    53: "DNS (Rezolvarea numelor de domenii)",
    67: "DHCP (Atribuire automată a IP-urilor)",
    68: "DHCP (Atribuire automată a IP-urilor)",
    69: "TFTP (Trivial File Transfer Protocol - variantă simplificată de FTP)",
    80: "HTTP (Acces la pagini web)",
    110: "POP3 (Preluare e-mail)",
    115: "SFTP",
    119: "NNTP (Usenet newsgroups)",
    123: "NTP (Network Time Protocol - sincronizare timp)",
    135: "RPC",
    137: "NetBIOS (Partajare fișiere Windows)",
    139: "NetBIOS (Partajare fișiere Windows)",
    143: "IMAP (Preluare e-mail cu acces la server)",
    161: "SNMP (Monitorizare rețele)",
    162: "SNMP (Monitorizare rețele)",
    194: "IRC",
    389: "LDAP (Acces la directoare)",
    443: "HTTPS (Acces securizat la pagini web)",
    445: "SMB (Partajare fișiere și imprimante Windows)",
    465: "SMTPS (SMTP securizat)",
    514: "Syslog (Trimitere loguri de sistem)",
    554: "RTSP (Real-Time Streaming Protocol)",
    587: "SMTP",
    636: "LDAPS (LDAP securizat)",
    888: "Acces securizat (SSL) aaPanel",
    993: "IMAPS (IMAP securizat)",
    995: "POP3S (POP3 securizat)",
}

def check_port(ip, port_local):
    """Verifică dacă un port este deschis pe un IP"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Timeout mai mic pentru scanare rapidă
        return s.connect_ex((ip, port_local)) == 0

# Interfață Streamlit
st.title("🔍 Scanner de Porturi")
st.title("(0-1023)")

# Input pentru IP
ip_address = st.text_input("Introduceți adresa IP:", "")

# Buton pentru scanare
if st.button("🔎 Scanează porturile"):
    if not ip_address:
        st.warning("⚠️ Introduceți o adresă IP validă!")
    else:
        st.write(f"📡 Scanare pentru IP: `{ip_address}`...")

        results = []
        status_box = st.empty()  # Placeholder pentru actualizare dinamică

        for port in range(1, 1024):  # Scanează porturile de la 1 la 1023
            service = ports_services.get(port, "Necunoscut")  # Caută serviciul asociat
            status_box.write(f"🔄 Se scanează portul: **{port} ({service})**...")
            time.sleep(0.1)  # Efect vizual pentru scanare
            status = "🟢 Deschis" if check_port(ip_address, port) else "🔴 Închis"
            results.append(f"**{port} ({service})**: {status}")

        status_box.write("✅ Scanare completă!")  # Mesaj final
        df = pd.DataFrame(results, columns=["Rezultat"])
        df.index = df.index + 1  
        st.table(df)
