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
        "Berlin":     {"entry": 55100, "medior": 83600,  "senior": 112500},
        "Munich":     {"entry": 57580, "medior": 87362,  "senior": 117563},
        "Hamburg":    {"entry": 57442, "medior": 87153,  "senior": 117281},
        "Frankfurt":  {"entry": 56753, "medior": 86108,  "senior": 115875},
        "Stuttgart":  {"entry": 56478, "medior": 85690,  "senior": 115313},
        "Cologne":    {"entry": 56202, "medior": 85272,  "senior": 114750},
        "Leipzig":    {"entry": 53585, "medior": 81301,  "senior": 109406},
    },
    "NOC-Ingenieur": {
        "Berlin":     {"entry": 46800, "medior": 54700, "senior": 63100},
        "Munich":     {"entry": 48906, "medior": 57162, "senior": 65940},
        "Hamburg":    {"entry": 48789, "medior": 57025, "senior": 65782},
        "Frankfurt":  {"entry": 48204, "medior": 56341, "senior": 64993},
        "Stuttgart":  {"entry": 47970, "medior": 56068, "senior": 64678},
        "Cologne":    {"entry": 47736, "medior": 55794, "senior": 64362},
        "Leipzig":    {"entry": 45513, "medior": 53196, "senior": 61365},
    },
    "Netzwerkadministrator": {
        "Berlin":     {"entry": 46800, "medior": 54700, "senior": 63100},
        "Munich":     {"entry": 48906, "medior": 57162, "senior": 65940},
        "Hamburg":    {"entry": 48789, "medior": 57025, "senior": 65782},
        "Frankfurt":  {"entry": 48204, "medior": 56341, "senior": 64993},
        "Stuttgart":  {"entry": 47970, "medior": 56068, "senior": 64678},
        "Cologne":    {"entry": 47736, "medior": 55794, "senior": 64362},
        "Leipzig":    {"entry": 45513, "medior": 53196, "senior": 61365},
    },
    "Netzwerkarchitekt": {
        "Berlin":     {"entry": 89100, "medior": 101000, "senior": 127000},
        "Munich":     {"entry": 93110, "medior": 105545, "senior": 132715},
        "Hamburg":    {"entry": 92887, "medior": 105293, "senior": 132398},
        "Frankfurt":  {"entry": 91773, "medior": 104030, "senior": 130810},
        "Stuttgart":  {"entry": 91328, "medior": 103525, "senior": 130175},
        "Cologne":    {"entry": 90882, "medior": 103020, "senior": 129540},
        "Leipzig":    {"entry": 86650, "medior": 98223,  "senior": 123508},
    },
    "Netzwerkingenieur": {
        "Berlin":     {"entry": 66000, "medior": 79800, "senior": 87800},
        "Munich":     {"entry": 68970, "medior": 83391, "senior": 91751},
        "Hamburg":    {"entry": 68805, "medior": 83192, "senior": 91532},
        "Frankfurt":  {"entry": 67980, "medior": 82194, "senior": 90434},
        "Stuttgart":  {"entry": 67650, "medior": 81795, "senior": 89995},
        "Cologne":    {"entry": 67320, "medior": 81396, "senior": 89556},
        "Leipzig":    {"entry": 64185, "medior": 77606, "senior": 85386},
    },
    "Netzwerkmanager": {
        "Berlin":     {"entry": 97600, "medior": 122400, "senior": 145800},
        "Munich":     {"entry": 101992, "medior": 127908, "senior": 152361},
        "Hamburg":    {"entry": 101748, "medior": 127602, "senior": 151997},
        "Frankfurt":  {"entry": 100528, "medior": 126072, "senior": 150174},
        "Stuttgart":  {"entry": 100040, "medior": 125460, "senior": 149445},
        "Cologne":    {"entry": 99552, "medior": 124848, "senior": 148716},
        "Leipzig":    {"entry": 94916, "medior": 119034, "senior": 141791},
    },
    "Netzwerksicherheitsingenieur": {
        "Berlin":     {"entry": 64100, "medior": 79900, "senior": 113800},
        "Munich":     {"entry": 66985, "medior": 83496, "senior": 118921},
        "Hamburg":    {"entry": 66824, "medior": 83296, "senior": 118637},
        "Frankfurt":  {"entry": 66023, "medior": 82297, "senior": 117214},
        "Stuttgart":  {"entry": 65703, "medior": 81898, "senior": 116645},
        "Cologne":    {"entry": 65382, "medior": 81498, "senior": 116076},
        "Leipzig":    {"entry": 62337, "medior": 77703, "senior": 110671},
    },
    "Netzwerk-Supportingenieur": {
        "Berlin":     {"entry": 42550, "medior": 48200, "senior": 63420},
        "Munich":     {"entry": 44465, "medior": 50369, "senior": 66274},
        "Hamburg":    {"entry": 44358, "medior": 50249, "senior": 66115},
        "Frankfurt":  {"entry": 43827, "medior": 49646, "senior": 65323},
        "Stuttgart":  {"entry": 43614, "medior": 49405, "senior": 65006},
        "Cologne":    {"entry": 43401, "medior": 49164, "senior": 64688},
        "Leipzig":    {"entry": 41380, "medior": 46875, "senior": 61676},
    },
    "Pre-Sales-Ingenieur (OTE)": {
        "Berlin":     {"entry": 83900, "medior": 104500, "senior": 140800},
        "Munich":     {"entry": 87676, "medior": 109203, "senior": 147136},
        "Hamburg":    {"entry": 87466, "medior": 108941, "senior": 146784},
        "Frankfurt":  {"entry": 86417, "medior": 107635, "senior": 145024},
        "Stuttgart":  {"entry": 85998, "medior": 107113, "senior": 144320},
        "Cologne":    {"entry": 85578, "medior": 106590, "senior": 143616},
        "Leipzig":    {"entry": 81593, "medior": 101626, "senior": 136928},
    },
    "Senior-Netzwerkingenieur": {
        "Berlin":     {"entry": 85200, "medior": 101800, "senior": 121000},
        "Munich":     {"entry": 89034, "medior": 106381, "senior": 126445},
        "Hamburg":    {"entry": 88821, "medior": 106127, "senior": 126143},
        "Frankfurt":  {"entry": 87756, "medior": 104854, "senior": 124630},
        "Stuttgart":  {"entry": 87330, "medior": 104345, "senior": 124025},
        "Cologne":    {"entry": 86904, "medior": 103836, "senior": 123420},
        "Leipzig":    {"entry": 82857, "medior": 99001,  "senior": 117673},
    },

    "Bauleiter": {
        "Berlin":     {"entry": 55500, "medior": 65000, "senior": 75000},
        "Frankfurt":  {"entry": 55500, "medior": 65000, "senior": 75000},
        "Hamburg":    {"entry": 55500, "medior": 65000, "senior": 75000},
        "Munich":     {"entry": 55500, "medior": 65000, "senior": 75000},
        "Regional (rest of Germany)": {"entry": 55500, "medior": 65000, "senior": 75000},
    },
    "Glasfasermonteur": {
        "Berlin":     {"entry": 42000, "medior": 45000, "senior": 50650},
        "Frankfurt":  {"entry": 42000, "medior": 45000, "senior": 50650},
        "Hamburg":    {"entry": 42000, "medior": 45000, "senior": 50650},
        "Munich":     {"entry": 42000, "medior": 45000, "senior": 50650},
        "Regional (rest of Germany)": {"entry": 42000, "medior": 45000, "senior": 50650},
    },
    "Projektleiter": {
        "Berlin":     {"entry": 65000, "medior": 75100, "senior": 90000},
        "Frankfurt":  {"entry": 65000, "medior": 75100, "senior": 90000},
        "Hamburg":    {"entry": 65000, "medior": 75100, "senior": 90000},
        "Munich":     {"entry": 65000, "medior": 75100, "senior": 90000},
        "Regional (rest of Germany)": {"entry": 65000, "medior": 75100, "senior": 90000},
    },
    "Netzplaner": {
        "Berlin":     {"entry": 49500, "medior": 61000, "senior": 65000},
        "Frankfurt":  {"entry": 49500, "medior": 61000, "senior": 65000},
        "Hamburg":    {"entry": 49500, "medior": 61000, "senior": 65000},
        "Munich":     {"entry": 49500, "medior": 61000, "senior": 65000},
        "Regional (rest of Germany)": {"entry": 49500, "medior": 61000, "senior": 65000},
    },
    "Senior Projektleiter": {
        "Berlin":     {"entry": 85000, "medior": 92000, "senior": 100000},
        "Frankfurt":  {"entry": 85000, "medior": 92000, "senior": 100000},
        "Hamburg":    {"entry": 85000, "medior": 92000, "senior": 100000},
        "Munich":     {"entry": 85000, "medior": 92000, "senior": 100000},
        "Regional (rest of Germany)": {"entry": 85000, "medior": 92000, "senior": 100000},
    },
    "Head of Deployment": {
        "Berlin":     {"entry": 100000, "medior": 110500, "senior": 120000},
        "Frankfurt":  {"entry": 100000, "medior": 110500, "senior": 120000},
        "Hamburg":    {"entry": 100000, "medior": 110500, "senior": 120000},
        "Munich":     {"entry": 100000, "medior": 110500, "senior": 120000},
        "Regional (rest of Germany)": {"entry": 100000, "medior": 110500, "senior": 120000},
    },
    "Oberbauleiter": {
        "Berlin":     {"entry": 80500, "medior": 85000, "senior": 95000},
        "Frankfurt":  {"entry": 80500, "medior": 85000, "senior": 95000},
        "Hamburg":    {"entry": 80500, "medior": 85000, "senior": 95000},
        "Munich":     {"entry": 80500, "medior": 85000, "senior": 95000},
        "Regional (rest of Germany)": {"entry": 80500, "medior": 85000, "senior": 95000},
    },
    "Projektassistentin": {
        "Berlin":     {"entry": 45500, "medior": 50000, "senior": 55000},
        "Frankfurt":  {"entry": 45500, "medior": 50000, "senior": 55000},
        "Hamburg":    {"entry": 45500, "medior": 50000, "senior": 55000},
        "Munich":     {"entry": 45500, "medior": 50000, "senior": 55000},
        "Regional (rest of Germany)": {"entry": 45500, "medior": 50000, "senior": 55000},
    },
    "Genehmigungsplaner": {
        "Berlin":     {"entry": 42100, "medior": 45000, "senior": 50000},
        "Frankfurt":  {"entry": 42100, "medior": 45000, "senior": 50000},
        "Hamburg":    {"entry": 42100, "medior": 45000, "senior": 50000},
        "Munich":     {"entry": 42100, "medior": 45000, "senior": 50000},
        "Regional (rest of Germany)": {"entry": 42100, "medior": 45000, "senior": 50000},
    },
}

# --- Dropdown data ---
roles = list(salary_data.keys())
locations = ["Berlin", "Frankfurt", "Hamburg", "Munich", "Regional (rest of Germany)"]
levels = ["Entry", "Medior", "Senior"]

# --- UI ---
st.title("Finde heraus, wie viel du als Network Engineer in Deutschland verdienen könntest!")
st.write("---")
st.write("Wähle Rolle und Standort aus, um eine geschätzte Gehaltsspanne zu sehen. (Nur zur Orientierung.)")

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    role = st.selectbox("Rolle", roles)
with col2:
    levels = st.selectbox("Berufserfahrung", levels)
with col3:
    location = st.selectbox("Standort", locations)

# button below dropdowns
st.write("")
show = st.button("Schätzung anzeigen", use_container_width=True)

st.write("---")

if show:
    if role in salary_data and location in salary_data[role]:
        min_sal, max_sal = salary_data[role][location]

        st.markdown(
    f"""
    <div style="
        text-align:center;
        margin-top:30px;
        margin-bottom:30px;
        width:100%;
    ">
        <h2 style="font-weight:600; color:#222;">{role} Gehalt in {location}</h2>
        <p style="font-size:18px; color:#333; margin-bottom:5px;">Geschätzte Gehaltsspanne:</p>
        <p style="font-size:26px; font-weight:800; color:#15803d; margin:0;">
            {fmt(min_sal)} – {fmt(max_sal)}
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

        st.info(
            "Dies ist eine Schätzung basierend auf Marktdaten. "
            "Das tatsächliche Gehalt kann je nach Fähigkeiten, Zertifizierungen und Unternehmen variieren."
        )
    else:
        st.error("Ungültige Auswahl. Bitte überprüfe deine Eingabe.")

st.caption("Datenquelle: interne Marktdaten. Nur zur Orientierung.")

# --- Simple Button Section ---
st.markdown("---")

st.markdown("""
<style>
.explore-btn {
    display: inline-block;
    border: 1px solid rgba(255, 255, 255, 0.8); /* thinner + softer */
    color: white;
    background-color: transparent;
    padding: 10px 20px;
    border-radius: 10px;
    margin: 8px;
    text-decoration: none; /* removes underline */
    font-weight: 500;
    font-size: 15px;
    letter-spacing: 0.5px;
    transition: all 0.25s ease;
}
.explore-btn:hover {
    background-color: rgba(255, 255, 255, 0.9);
    color: black;
}
</style>
""", unsafe_allow_html=True)

buttons = [
    ("Homepage", "https://www.hamilton-barnes.com/"),
    ("Rollen erkunden", "https://www.hamilton-barnes.com/jobs"),
    ("Bewerber", "https://www.hamilton-barnes.com/candidates"),
    ("Kunden", "https://www.hamilton-barnes.com/clients"),
    ("Absolventen", "https://www.empowering-future-network-engineers.com/")
]

btn_html = '<div style="text-align:center;">'
for label, link in buttons:
    btn_html += f'<a href="{link}" target="_blank" class="explore-btn">{label}</a>'
btn_html += '</div>'

st.markdown(btn_html, unsafe_allow_html=True)