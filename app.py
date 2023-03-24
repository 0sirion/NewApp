import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.title("test s01")

df = pd.DataFrame(np.random.randn(10,2),
                  columns=['x','y'])
st.line_chart(df)
 


# Ti è piaciuto il grafico

x = st.radio(
    "Ti piace il grafichetto?",
    ('mah', 'no.', 'Anche no'))

if x == 'mah':
    st.write('cioe?')
else:
    st.write("eh vabè")


     # Insert comment


if st.button('test ballons'):
   st.balloons()
st.write("**Lascia un commento:**")
form = st.form("commento")
name = form.text_input("Nome")
comment = form.text_area("Commento")
if form.form_submit_button("Invia"):
   st.write()
   

else :
  date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#   if "just_posted" not in st.session_state:
#       st.session_state["just_posted"] = True
#   st.experimental_rerun()
