import streamlit as st
import socket
import pandas as pd
import time  # Pentru efect vizual de scanare

# Dicționar cu porturi și servicii asociate
ports_services = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    115: "SFTP",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    194: "IRC",
    443: "SSL",
    445: "SMB",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "Remote Desktop",
    5632: "PCAnywhere",
    5900: "VNC",
    25565: "Minecraft"
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
