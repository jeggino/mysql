import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

conn = st.connection("gsheets", type=GSheetsConnection)
df_1 = conn.read(ttl=0,worksheet="Appointments")
df_2 = conn.read(ttl=0,worksheet="Sheet4")
df_1
df_2
#--- NEW ---
buurt_choice = ['Bijlmer-West', 'Bijlmer-Centrum', 'Bijlmer-Oost', 'Bos en Lommer',
       'Oud-Zuid', 'Osdorp', 'Indische Buurt, Oostelijk Havengebied',
       'Centrum-West', 'Noord-West', 'Gaasperdam',
       'Sloterdijk Nieuw-West', 'De Aker, Sloten, Nieuw-Sloten',
       'Centrum-Oost', 'IJburg, Zeeburgereiland',
       'Geuzenveld, Slotermeer', 'Oud-Oost', 'Westerpark',
       'Buitenveldert, Zuidas', 'Weesp, Driemond', 'Noord-Oost',
       'Oud-West, De Baarsjes', 'De Pijp, Rivierenbuurt', 'Oud-Noord',
       'Slotervaart', 'Watergraafsmeer']

expertise_choice = ['Geen','Laag','Gemiddeld','Ervaren']

type_bikes = ["Terugtraprem", "Racefiets","Versnellingen buiten","Versnellingen binnen","Vouwfiets","Kinderfiets",
             "Driewieler","Backfiets - Stuur een foto aub","E-bike - Stuur een foto aub","mijn fiets staat er niet op"]

name = st.text_input("Naam*", placeholder="Vul hier uw naam in ...")
e_mail = st.text_input("E-mail*", placeholder="Voer hier uw e-mailadres in ...")
number = st.text_input("Telefoonnummer*", placeholder="Voer hier uw nummer in ...")
buurt = st.selectbox("Uit welke buurt komt u? (voor statistieken doeleinden)", buurt_choice)
expertise = st.selectbox("Welke ervaring heeft u met fietsen?", expertise_choice )
type_bike = st.selectbox("Wat voor fiets wilt u repareren?", type_bikes)

new_data = pd.DataFrame([{
                   "Name": name, "e_mail": e_mail, "Phone number": number,
                   "Neighborhood": buurt, "Expertise": expertise, "Type of bike": type_bike,
}])

data = [{
                   "Name": name, "e_mail": e_mail, "Phone number": number,
                   "Neighborhood": buurt, "Expertise": expertise, "Type of bike": type_bike,
}]


if st.button(":red[**Create**]"):
       conn.create(worksheet="new",data=new_data)
       st.write("YOU create!!")

if st.button(":red[**update**]"):
       updated_df = pd.concat([df_1,new_data],ignore_index=True)
       conn.update(data=updated_df)
       st.write("YOU update!!")
