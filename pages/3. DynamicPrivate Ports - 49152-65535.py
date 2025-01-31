import streamlit as st
import socket
import pandas as pd
import time

# Dicționar cu porturi și servicii asociate (doar pentru afișare)
ports_services = {
    51820: "WireGuard VPN"
}

def check_port(ip, port_local):
    """Verifică dacă un port este deschis pe un IP"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Timeout mai mic pentru scanare rapidă
        return s.connect_ex((ip, port_local)) == 0

# Interfață Streamlit
st.title("🔍 Scanner de Porturi")
st.title("(49152-65535)")

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

        for port in range(49152, 65536):  # Scanează porturile de la 49152 la 65535
            service = ports_services.get(port, "Necunoscut")  # Caută serviciul asociat
            status_box.write(f"🔄 Se scanează portul: **{port} ({service})**...")
            time.sleep(0.1)  # Efect vizual pentru scanare
            status = "🟢 Deschis" if check_port(ip_address, port) else "🔴 Închis"
            results.append(f"**{port} ({service})**: {status}")

        status_box.write("✅ Scanare completă!")  # Mesaj final
        df = pd.DataFrame(results, columns=["Rezultat"])
        df.index = df.index + 1
        st.table(df)
