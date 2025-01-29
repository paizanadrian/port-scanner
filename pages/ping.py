import streamlit as st
import subprocess


# Funcție pentru a face ping unui domeniu/IP și a capta întreaga ieșire
def ping_domeniu(domeniu):
    # Execută comanda ping și captează ieșirea
    result = subprocess.run(["ping", "-n", "4", domeniu], capture_output=True, text=True)  # '-c 4' pentru Linux, folosește '-n 4' pe Windows

    # Verifică dacă ping-ul a avut succes
    if result.returncode == 0:
        return result.stdout  # Returnează ieșirea completă (stdout)
    else:
        return f"Ping-ul către {domeniu} a eșuat.\n{result.stderr}"

# Interfață Streamlit
st.title("🌐 Verificare Ping")  # Titlu aplicației

# Introducere domeniu
domeniu_input = st.text_input("Adaugă domeniul pentru ping:", "website.com")

# Verifică dacă s-a dat click pe butonul de Ping
if st.button('Verifică Ping'):
    if domeniu_input:
        ping_result = ping_domeniu(domeniu_input)
        st.write("### Rezultate Ping:")
        st.text_area('', ping_result, height=300)
    else:
        st.warning("Te rugăm să introduci un domeniu valid.")
