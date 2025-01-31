import streamlit as st
import socket
import pandas as pd
import time  # Pentru efect vizual de scanare

# Dicționar cu porturi și servicii asociate
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
    1194: "OpenVPN",
    1433: "Microsoft SQL Server",
    1521: "Oracle Database",
    1701: "L2TP VPN",
    1723: "PPTP VPN",
    1863: "MSN Messenger",
    1935: "RTMP (Streaming video)",
    2030: "Panoul de administrare CWP (HTTP)",
    2031: "Panoul de administrare CWP (HTTPS)",
    2082: "Panoul de administrare (HTTP) cPanel & WHM",
    2083: "Panoul de administrare (HTTPS) cPanel & WHM",
    2086: "WHM (Web Host Manager - HTTP)",
    2087: "WHM (HTTPS)",
    2095: "Webmail (HTTP)",
    2096: "Webmail (HTTPS)",
    3074: "Xbox Live",
    3306: "MySQL/MariaDB",
    3306: "MySQL/MariaDB (Acces remote)",
    3389: "RDP (Remote Desktop Protocol - acces la Windows)",
    3478: "PlayStation Network",
    3478: "WebRTC (folosit în apeluri video)",
    3479: "PlayStation Network",
    3480: "WebRTC (folosit în apeluri video)",
    3659: "PlayStation Network",
    4500: "IPsec VPN",
    5000: "IPsec VPN",
    5222: "XMPP (Google Talk, Jabber)",
    5223: "XMPP (Google Talk, Jabber)",
    5432: "PostgreSQL",
    5632: "PCAnywhere",
    5900: "VNC (Acces grafic la servere)",
    5901: "VNC (Acces grafic la servere)",
    6379: "Redis",
    6667: "IRC (Internet Relay Chat)",
    7800: "Servicii web",
    8080: "HTTP alternativ (folosit pentru aplicații web)",
    8080: "Panoul de administrare (HTTPS)  ISPConfig",
    8081: "Alternativ pentru streaming HTTP",
    8090: "Panoul de administrare CyberPanel",
    8443: "HTTPS alternativ",
    8883: "MQTT (protocol IoT)",
    8888: "Panoul de administrare (port implicit) aaPanel",
    11211: "Memcached",
    25565: "Minecraft",
    27015: "Steam (jocuri online)",
    27050: "Steam (jocuri online)",
    51820: "WireGuard VPN"
}

def check_port(ip, port_local):
    """Verifică dacă un port este deschis pe un IP"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)  # Timeout de 2 secunde
        return s.connect_ex((ip, port_local)) == 0

# Interfață Streamlit
st.title("🔍 Scanner de Porturi")

# Input pentru IP
ip_address = st.text_input("Introduceți adresa IP:", "")

# Buton pentru scanare
if st.button("🔎 Scanează porturile"):
    st.write(f"📡 Scanare pentru IP: `{ip_address}`...")
    
    results = []
    status_box = st.empty()  # Creează un placeholder pentru actualizare dinamică

    for port, service in ports_services.items():
        status_box.write(f"🔄 Se scanează portul: **{port} ({service})**...")
        time.sleep(0.5)  # Efect vizual pentru scanare
        status = "🟢 Deschis" if check_port(ip_address, port) else "🔴 Închis"
        results.append(f"**{port} ({service})**: {status}")

    status_box.write("✅ Scanare completă!")  # Afișează mesaj final
    df = pd.DataFrame(results, columns=["Rezultat"])
    df.index = df.index + 1  # Face ca indexul să înceapă de la 1
    st.table(df)
