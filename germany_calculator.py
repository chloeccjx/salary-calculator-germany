# salary_calculator_germany.py
import streamlit as st
import os
st.set_page_config(page_title="Germany Network Engineer Salary Calculator", layout="centered")

import os
print(os.getcwd())

from PIL import Image
import base64

def fmt(amount):
    return f"€{amount:,.0f}".replace(",", ".")

# --- background part ---
def add_bg_from_local(image_file):
    file_path = os.path.join(os.path.dirname(__file__), image_file)
    with open(file_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("bg5.png") 

st.image("hb_logo.png", width=250)

# --- Salary data (role -> location -> (min, max)) ---
salary_data = {
    "IP-Netzwerkingenieur": {
        "Berlin": (81100, 115500),
        "Frankfurt": (88500, 126000),
        "Hamburg": (81100, 115500),
        "Munich": (92200, 131300),
        "Regional (rest of Germany)": (70000, 99700),
    },
    "NOC-Ingenieur": {
        "Berlin": (46800, 63100),
        "Frankfurt": (51000, 68800),
        "Hamburg": (46800, 63100),
        "Munich": (53100, 71700),
        "Regional (rest of Germany)": (40400, 54500),
    },
    "Netzwerkadministrator": {
        "Berlin": (46800, 63100),
        "Frankfurt": (51000, 68800),
        "Hamburg": (46800, 63100),
        "Munich": (53100, 71700),
        "Regional (rest of Germany)": (40400, 54500),
    },
    "Netzwerkarchitekt": {
        "Berlin": (92100, 132000),
        "Frankfurt": (100500, 144000),
        "Hamburg": (92100, 132000),
        "Munich": (104700, 150000),
        "Regional (rest of Germany)": (79600, 114000),
    },
    "Netzwerkingenieur": {
        "Berlin": (66000, 90800),
        "Frankfurt": (72000, 99000),
        "Hamburg": (66000, 90800),
        "Munich": (75000, 103100),
        "Regional (rest of Germany)": (57000, 78400),
    },
    "Netzwerkmanager": {
        "Berlin": (97600, 145800),
        "Frankfurt": (106500, 159000),
        "Hamburg": (97600, 145800),
        "Munich": (111000, 165600),
        "Regional (rest of Germany)": (84300, 125900),
    },
    "Netzwerksicherheitsingenieur": {
        "Berlin": (92100, 134800),
        "Frankfurt": (100500, 147000),
        "Hamburg": (92100, 134800),
        "Munich": (104700, 153100),
        "Regional (rest of Germany)": (79600, 116400),
    },
    "Netzwerk-Supportingenieur": {
        "Berlin": (54400, 74000),
        "Frankfurt": (59400, 80700),
        "Hamburg": (54400, 74000),
        "Munich": (61900, 84000),
        "Regional (rest of Germany)": (47000, 63900),
    },
    "Pre-Sales-Ingenieur": {
        "Berlin": (83900, 134800),
        "Frankfurt": (91500, 147000),
        "Hamburg": (83900, 134800),
        "Munich": (95300, 153100),
        "Regional (rest of Germany)": (72400, 116400),
    },
    "Senior-Netzwerkingenieur": {
        "Berlin": (85200, 121000),
        "Frankfurt": (93000, 132000),
        "Hamburg": (85200, 121000),
        "Munich": (96900, 137500),
        "Regional (rest of Germany)": (73600, 104500),
    },
}

# seniority percentiles: the percentile inside the range to show as an estimated salary
seniority_percentiles = {
    "Junior": 0.25,
    "Intermediate": 0.50,
    "Senior": 0.75,
    "Managerial": 0.90
}

# --- Dropdown data ---
roles = list(salary_data.keys())
locations = ["Berlin", "Frankfurt", "Hamburg", "Munich", "Regional (rest of Germany)"]
levels = ["Junior", "Intermediate", "Senior", "Managerial"]

# --- UI ---
st.title("Finde heraus, wie viel du als Network Engineer in Deutschland verdienen könntest!")
st.write("---")
st.write("Wähle Rolle, Standort und Erfahrungsstufe aus, um eine geschätzte Gehaltsspanne zu sehen. (Nur zur Orientierung.)")

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    role = st.selectbox("Rolle", roles)
with col2:
    location = st.selectbox("Standort", locations)
with col3:
    level = st.selectbox("Erfahrungsstufe", levels)

# button below dropdowns
st.write("")
show = st.button("Schätzung anzeigen", use_container_width=True)

st.write("---")

if show:
    if role in salary_data and location in salary_data[role]:
        min_sal, max_sal = salary_data[role][location]
        suggested = int(min_sal + (max_sal - min_sal) * seniority_percentiles[level])

        st.subheader(f"{level} {role} Gehalt in {location}")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f"**Geschätzte Gehaltsspanne:**<br><span style='font-size:22px; color:#15803d; font-weight:bold;'>{fmt(min_sal)} – {fmt(max_sal)}</span>",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"**Geschätztes Gehalt für diese Erfahrungsstufe:**<br><span style='font-size:22px; color:#15803d; font-weight:bold;'>{fmt(suggested)}</span>",
                unsafe_allow_html=True
            )

        st.info(
            "Dies ist eine Schätzung basierend auf Marktdaten. "
            "Das tatsächliche Gehalt kann je nach Fähigkeiten, Zertifizierungen und Unternehmen variieren."
        )
    else:
        st.error("Ungültige Auswahl. Bitte überprüfe deine Eingabe.")

st.markdown("[Relevante Jobs entdecken →](https://www.hamilton-barnes.com/candidates/job-search/?)")
st.caption("Datenquelle: interne Marktdaten. Nur zur Orientierung.")
