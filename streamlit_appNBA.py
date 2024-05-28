import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Jogadores NBA",
    page_icon="🏀",
    layout="wide",
    initial_sidebar_state="expanded")


with open('style.css', 'r') as fp:
    st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)

df = pd.read_csv('data/all_seasons.csv')
df2 = pd.read_csv('data/nba2k-full.csv')



season_list = sorted(df['season'].unique())

with st.sidebar:
    st.title('🏀 Jogadores NBA')
    selected_season = st.selectbox('Selecione o ano', season_list)
    
    

    df_filtered = df[df['season'] == selected_season]
    
    
    player_list = sorted(df_filtered['player_name'].unique())
    

    selected_player = st.selectbox('Selecione o jogador', player_list)
    
draft_year = df[df['player_name'] == selected_player]['draft_year'].iloc[0]

# Filtrar o DataFrame para incluir apenas jogadores que foram draftados no mesmo ano
same_draft_year_df = df[df['draft_year'] == draft_year]

# Agrupar os dados filtrados por jogador e calcular a média de pontos
average_points_per_player = same_draft_year_df.groupby('player_name')['pts'].mean()

# Ordenar os dados pela média de pontos
average_points_per_player = average_points_per_player.sort_values()

# Criar um gráfico de barras com os jogadores no eixo x e a média de pontos no eixo y
plt.figure(figsize=(8, 12))
plt.barh(average_points_per_player.index, average_points_per_player.values)
plt.xlabel('Média de Pontos')
plt.title(f'Média de Pontos por Jogador (Draft de {draft_year})')
plt.grid(True)

# Destacar o jogador selecionado
plt.barh(selected_player, average_points_per_player[selected_player], color='red')

# Exibir o gráfico
st.pyplot(plt.gcf())
player_data = df[df['player_name'] == selected_player]

average_points = player_data['pts'].mean()

# Exibir o texto com a média de pontos
st.markdown(f"**Média de pontos de {selected_player} ao longo de todas as temporadas: {average_points:.2f}**")

points_per_season = player_data.groupby('season')['pts'].sum()

st.line_chart(points_per_season)





def plot1(input1, input2, input3):
    return 

def plot2(input1, input2, input3):
    return 

def plot3(input1, input2, input3):
    return
def plot_player_development(df, player_name):
    
    player_data = df[df['player_name'] == player_name]
    player_data = player_data.sort_values('season')
    fig = px.line(player_data, x='season', y='pts', title=f'Desenvolvimento de {player_name} ao longo das temporadas')
    
    return fig

import plotly.graph_objects as go

def plot_player_stats(df, player_name):
    player_data = df[df['player_name'] == player_name]
    player_data = player_data.sort_values('season')

    fig = go.Figure()
    fig.add_trace(go.Bar(x=player_data['season'], y=player_data['pts'], name='Pontos'))
    fig.add_trace(go.Bar(x=player_data['season'], y=player_data['ast'], name='Assistências'))
    fig.add_trace(go.Bar(x=player_data['season'], y=player_data['reb'], name='Rebotes'))

    fig.update_layout(barmode='group', title_text=f'Estatísticas de {player_name} ao longo das temporadas')

    return fig

player_stats_plot = plot_player_stats(df, selected_player)

st.plotly_chart(player_stats_plot)

player_plot = plot_player_development(df, selected_player)

st.plotly_chart(player_plot)


col = st.columns((45, 1), gap='medium')
st.table(player_data)






