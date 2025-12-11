import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        actors_df = pd.json_normalize(actors)
        st.write('Lista de Atores/Atrizes:')

        AgGrid(data=actors_df, reload_data=True, key='actors_grid')
    else:
        st.warning('Nenhum ator encontrado ')

    st.title('Cadastrar novo ator: ')

    name = st.text_input('Nome do ator: ')
    birthday = st.date_input(
        label='Data de nascimento',
        value=datetime.today(),
        min_value=datetime(1600, 1, 1),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationality_dropdown = ['BRAZIL', 'USA']
    nationality = st.selectbox(options=nationality_dropdown, label='Nacionalidade')

    if st.button('Cadastar'):
        new_actor = actor_service.create_actor(name=name, birthday=birthday, nationality=nationality,)
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar. Verifique os campos!')
