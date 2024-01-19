import streamlit as st
import pandas as pd
import plotly.express as px

df_car=pd.read_csv("./data/vehicles_us.csv")

# Page configuration
st.set_page_config(
    page_title="Car Sales",
    page_icon=":blue_car:",
    initial_sidebar_state="expanded"
)


st.title("Car sales app")
st.header("Data viewer",divider='rainbow')
dataframe_toggle = st.toggle("Hide/Show Dataframe", value=True)
if dataframe_toggle:
    st.dataframe(df_car.head(15))

st.text_area(
    "Creación de gráficos",
    "En el siguiente apartado podras observar una web creada con streamlit para el análisis de datos "
    "con la finalidad de que podrás visualizar diferentes gráficos referentes a las diferentes industrias manufactureras."
    )

#---------------------------------------------------------------------------------
                                         #Gráfico de barras
#---------------------------------------------------------------------------------

st.header('Visualización de gráficos de :blue[Barras] :gb: :car:', divider="blue")

bar_button = st.button('Construir gráficos de barras')
if bar_button:
    st.subheader('_Model & Price_', divider="gray")
    st.write("Creación de un gráfico de barras del modelo y precio")
    fig = px.bar(df_car, x="model", y="price",title="Modelo y Precio")
    st.plotly_chart(fig, use_container_width=True)
    st.subheader('_Model & Price & Type_', divider="gray")


if bar_button:
    st.write("Creación de un grafico de barras del modelo y precio por el tipo de vehículo")
    fig = px.bar(df_car, x="model", color="type", title="Long-Form Input")

    st.plotly_chart(fig, use_container_width=True)

#---------------------------------------------------------------------------------
                                     #Histograma
#---------------------------------------------------------------------------------
st.header('Visualización de un :green[Histograma] :flag-ht: :car:', divider="green")
hist_button = st.button('Construir histogramas') # crear un botón
        
if hist_button: # al hacer clic en el botón
            st.subheader('_"Condition & Model"_', divider="gray")
            # escribir un mensaje
            st.write('Creación de un histograma sobre modelo del año y su condición ')            
            # crear un histograma
            fig = px.histogram(df_car, x="model_year", color="condition", title="Condition & Model")       
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True) 
            st.subheader('_"Odometer"_', divider="gray")
            
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(df_car, x="odometer",title="Odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True) 

#---------------------------------------------------------------------------------
                                     #Gráfico de dispersión
#---------------------------------------------------------------------------------
st.header('Visualización de un gráfico :orange[Dispersión] :de: :car:', divider="orange")

hist_button = st.button('Construir gráficos de dispersión') # crear un botón
        
if hist_button: # al hacer clic en el botón
            st.subheader('_"Ometer & Price"_', divider="gray")
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')           
            # crear un histograma
            fig = px.scatter(df_car, x="odometer", y="price")        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True) 
            


if hist_button: # al hacer clic en el botón
             st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches por el tipo de vehículo')
             fig = px.scatter(df_car, x="odometer", y="price", color="type")
             st.plotly_chart(fig, use_container_width=True) 





#---------------------------------------------------------------------------------
                                     #Gráfico de Violín
#---------------------------------------------------------------------------------
st.header('Visualización de un gráfico :violet[Violín] :flag-vi: :car:', divider="violet") 

bar_button_bar = st.button('Construir gráfico Violín')
if bar_button_bar:
    st.subheader('_"model_year & condition"_', divider="gray")
    st.write("Creación de un grafico de barras del modelo y precio")
    fig = px.violin(df_car, x="model_year", color="condition", title="Model_year & condition",labels="a")

    st.plotly_chart(fig, use_container_width=True)





#---------------------------------------------------------------------------------
                                     #Seleccion de grafico
#---------------------------------------------------------------------------------
st.header('Comparación de modelos con la condicion de cada vehículo :oncoming_police_car:', divider="red") 

option = st.selectbox(
    'Selecciona el primer modelo',
    (df_car["model"].unique()))

st.write('You selected:', option)

option2 = st.selectbox(
    'Selecciona el segundo modelo',
    (df_car["model"].unique()))

st.write('You selected:', option2)

#mostrar el df filtrado
st.subheader('_"Puedes mostrar el Data Frame Filtrado"_', divider="gray")
df_filtered=df_car.query("@option in model or @option2 in model")
dataframe_toggle = st.toggle("Hide/Show Dataframe2", value=False)
if dataframe_toggle:
    st.dataframe(df_filtered.head(15))


#Creación de el grafico
st.header('Construir Gráfico :heavy_check_mark:', divider="red")
bar_button_bar = st.checkbox('Constuir gráfico seleccionado')
if bar_button_bar:
    st.write("Creación de un grafico de barras del modelo y precio")
    fig = px.histogram(df_filtered, x="price",y="condition",color="model" , title="Condition & Model")

    st.plotly_chart(fig, use_container_width=True)

    