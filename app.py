import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from flask import Flask,render_template

# importacion de datos
datos = pd.read_csv("SampleSuperstore.csv")





def graph_city_price_distribution(datos):
    datos = datos.tail(20)
    plt.figure(figsize=(14, 6))  
    # Graficar las ondas de distribución para cada ciudad
    sns.kdeplot(data=datos, x="Sales", hue="City", fill=True, common_norm=False, palette="tab20", linewidth=2)
    # Títulos y etiquetas
    plt.title("Distribución de Ventas por Ciudad", fontsize=16)
    plt.xlabel("Ventas", fontsize=12)
    plt.ylabel("Densidad de Distribución", fontsize=12)
    plt.tight_layout()
    plt.savefig('static/images/graph_city_price_distribution.webp', format="WEBP")
    plt.close()
graph_city_price_distribution(datos)


def total_sales():
    
    pivot_data = datos.pivot_table(
        index="Category",
        columns="Segment",
        values="Sales",
        aggfunc="sum",
        fill_value=0
    )
    # estilo del grafico
    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 8))
    heatmap = sns.heatmap(
        pivot_data,
        annot=True,
        cmap="YlGnBu",
        fmt=".0f",
        linewidths=.5,
        cbar_kws={"label": "Ventas Totales ($)"},  
    )
    # Personalizar el gráfico
    plt.title("Ventas Totales por Categoría y Segmento", fontsize=16)
    plt.xlabel("Segmento", fontsize=12)
    plt.ylabel("Categoría", fontsize=12)

    # Mostrar el gráfico
    plt.tight_layout()
    plt.savefig(os.path.join("static/images/total_sales.webp"),format="WEBP")
total_sales()


def save_city_sales_chart(data, output_path="static/images/city_sales.webp"):
    # Crear la carpeta si no existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Agrupar los datos por ciudad y sumar las ventas
    city_sales = data.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10)

    # Configurar el estilo de Seaborn
    sns.set(style="whitegrid")

    # Crear el gráfico de barras
    plt.figure(figsize=(12, 6))
    sns.barplot(x=city_sales.values, y=city_sales.index, palette="viridis")

    # Personalizar el gráfico
    plt.title("Top 10 Ciudades con Mayor Gasto (Ventas Totales)", fontsize=16)
    plt.xlabel("Ventas Totales ($)", fontsize=12)
    plt.ylabel("Ciudad", fontsize=12)
    plt.tight_layout()

    # Guardar el gráfico en la ruta especificada
    plt.savefig(output_path,format="WEBP",dpi=200)
    
    # Cerrar la figura
    plt.close()
save_city_sales_chart(datos)













app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)