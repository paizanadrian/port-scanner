import streamlit as st
import socket
import pandas as pd
import time

# Dicționar cu porturi și servicii asociate (doar pentru afișare)
ports_services = {
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
    3306: "MySQL/MariaDB (Acces remote)",
    3389: "RDP (Remote Desktop Protocol - acces la Windows)",
    3478: "PlayStation Network",
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
}

def check_port(ip, port_local):
    """Verifică dacă un port este deschis pe un IP"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Timeout mai mic pentru scanare rapidă
        return s.connect_ex((ip, port_local)) == 0

# Interfață Streamlit
st.title("🔍 Scanner de Porturi")
st.title("(1024-49151)")

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

        for port in range(1024, 49152):  # Scanează porturile de la 1024 la 49151
            service = ports_services.get(port, "Necunoscut")  # Caută serviciul asociat
            status_box.write(f"🔄 Se scanează portul: **{port} ({service})**...")
            time.sleep(0.1)  # Efect vizual pentru scanare
            status = "🟢 Deschis" if check_port(ip_address, port) else "🔴 Închis"
            results.append(f"**{port} ({service})**: {status}")

        status_box.write("✅ Scanare completă!")  # Mesaj final
        df = pd.DataFrame(results, columns=["Rezultat"])
        df.index = df.index + 1
        st.table(df)
