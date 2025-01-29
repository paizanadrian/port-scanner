import streamlit as st
from ping3 import ping
from ping3 import verbose_ping

# Funcție pentru a face ping unui domeniu/IP și a capta întreaga ieșire
def ping_domeniu(domeniu):
    try:
        # Folosește verbose_ping pentru a trimite mai multe pachete
        result = []
        for reply in verbose_ping(domeniu, count=4):  # Trimite 4 pachete
            result.append(str(reply))  # Salvează fiecare răspuns
        return "\n".join(result)
    except Exception as e:
        return f"A apărut o eroare la ping: {e}"

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
