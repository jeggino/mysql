import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd



conn = st.connection("gsheets", type=GSheetsConnection)
df_old = conn.read(ttl=100,worksheet="old_data")

df_old


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

# ---APP---

name = st.text_input("Naam*", placeholder="Vul hier uw naam in ...")
e_mail = st.text_input("E-mail*", placeholder="Voer hier uw e-mailadres in ...")




if st.button(":red[**Update df**]"):
       data = [{"Name": name, "e_mail": e_mail}]
       df_new = pd.DataFrame(data)
       # conn.update(worksheet='old_data',data=df_old )
       df_updated = pd.concat([df_old,df_new],ignore_index=True)
       conn.update(worksheet='new_data',data=df_updated)
       st.rerun()
