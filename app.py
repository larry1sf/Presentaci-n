import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from flask import Flask,render_template,redirect,url_for

# importacion de datos
datos = pd.read_csv("SampleSuperstore.csv")


def graph_city_price_distribution(datos):
    datos = datos.tail(20)
    plt.figure(figsize=(14, 6))  
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
    city_sales = data.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10)

    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 6))
    sns.barplot(x=city_sales.values, y=city_sales.index, palette="viridis")

    # Personalizar el gráfico
    plt.title("Top 10 Ciudades con Mayor Gasto (Ventas Totales)", fontsize=16)
    plt.xlabel("Ventas Totales ($)", fontsize=12)
    plt.ylabel("Ciudad", fontsize=12)
    plt.tight_layout()

    # Cerrar la figura
    plt.savefig(output_path,format="WEBP",dpi=200)
    plt.close()
save_city_sales_chart(datos)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/covid')
def covid():
    return render_template("covid.html")


@app.errorhandler(404)
def not_found(e):
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
    app.handle_url_build_error(404,not_found)