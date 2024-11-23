
import pandas as pd
import matplotlib.pyplot as plt


def graficoCasosConfirmados():
    df = pd.read_csv('covid_data.csv')

# Convertir la columna 'Fecha' a tipo datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
# Graficar los casos confirmados, recuperados, fallecidos y activos
    plt.figure(figsize=(12, 6))
    plt.plot(df['Fecha'], df['Casos Confirmados'], label='Casos Confirmados', marker='o')
    plt.plot(df['Fecha'], df['Recuperados'], label='Recuperados', marker='s')
    plt.plot(df['Fecha'], df['Fallecidos'], label='Fallecidos', marker='^')
    plt.plot(df['Fecha'], df['Activos'], label='Casos Activos', marker='x')

# Etiquetas y título
    plt.title('Tendencias del COVID-19')
    plt.xlabel('Fecha')
    plt.ylabel('Número de Personas')
    plt.legend()
    plt.grid(True)

# Guardar el gráfico como imagen PNG
    return plt.savefig('sources/images/grafico_covid.webp')    

def graficoEvolucionCasos():
    df = pd.read_csv('covid_data.csv')

# Convertir la columna 'Fecha' a tipo datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    # Gráfico de líneas
    plt.figure(figsize=(12, 6))
    plt.plot(df['Fecha'], df['Casos Confirmados'], label='Casos Confirmados', color='blue', marker='o')
    plt.plot(df['Fecha'], df['Recuperados'], label='Recuperados', color='green', marker='o')
    plt.plot(df['Fecha'], df['Fallecidos'], label='Fallecidos', color='red', marker='o')

    plt.title('Evolución de Casos Confirmados, Recuperados y Fallecidos')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)

#-------------------------------------------------------------------------------
# Guardar la imagen
    plt.savefig('sources/images/evolucion_casos.png', bbox_inches='tight')
    plt.show()

def graficoTasaMortalidad():
    df = pd.read_csv('covid_data.csv')

# Convertir la columna 'Fecha' a tipo datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    # Gráfico de líneas para la tasa de mortalidad
    plt.figure(figsize=(12, 6))
    plt.plot(df['Fecha'], df['Tasa de Mortalidad (%)'], color='purple', marker='o')

    plt.title('Tasa de Mortalidad a lo largo del tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Tasa de Mortalidad (%)')
    plt.grid(True)
    plt.xticks(rotation=45)

#-------------------------------------------------------------------------------
# Guardar la imagen
    plt.savefig('sources/images/tasa_mortalidad.png', bbox_inches='tight')
    plt.show()

def graficoCasosPorMillon():
    df = pd.read_csv('covid_data.csv')

# Convertir la columna 'Fecha' a tipo datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    # Gráfico de líneas para los casos por millón
    plt.figure(figsize=(12, 6))
    plt.plot(df['Fecha'], df['Casos por Millón'], color='orange', marker='o')

    plt.title('Casos por Millón de Habitantes')
    plt.xlabel('Fecha')
    plt.ylabel('Casos por Millón')
    plt.grid(True)
    plt.xticks(rotation=45)

# Guardar la imagen
    plt.savefig('sources/images/casos_por_millon.png', bbox_inches='tight')
    plt.show()

def graficoCasosRecuperados():
    df = pd.read_csv('covid_data.csv')

# Convertir la columna 'Fecha' a tipo datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    #---------------------------
# Proporción de casos recuperados y fallecidos
    recuperados_totales = df['Recuperados'].iloc[-1]
    fallecidos_totales = df['Fallecidos'].iloc[-1]
    proporciones = [recuperados_totales, fallecidos_totales]
    labels = ['Recuperados', 'Fallecidos']

    plt.figure(figsize=(8, 8))
    plt.pie(proporciones, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'red'])
    plt.title('Proporción de Recuperados vs Fallecidos')

# Guardar la imagen
    plt.savefig('sources/images/proporcion_recuperados_fallecidos.png', bbox_inches='tight')
    plt.show()

graficoCasosConfirmados()
graficoEvolucionCasos()
graficoTasaMortalidad()
graficoCasosPorMillon()
graficoCasosRecuperados()