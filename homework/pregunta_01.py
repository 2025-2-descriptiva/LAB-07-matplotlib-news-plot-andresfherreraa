"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os
import matplotlib.pyplot as plt
import pandas as pd


def pregunta_01():
    df = pd.read_csv("files/input/news.csv", index_col=0)

    colores = {
        "Newspaper": "grey",
        "Television": "dimgray",
        "Radio": "lightgrey",
        "Internet": "tab:blue",
    }

    niveles = {
        "Internet": 3,
        "Television": 2,
        "Newspaper": 2,
        "Radio": 1,
    }

    grosor = {
        "Internet": 4,
        "Television": 2,
        "Newspaper": 2,
        "Radio": 2,
    }

    plt.figure(figsize=(8, 4))

    for medio in df.columns:
        plt.plot(
            df.index,
            df[medio],
            color=colores[medio],
            linewidth=grosor[medio],
            zorder=niveles[medio],
            label=medio,
        )

    ax = plt.gca()
    ax.set_title("How people get their news", fontsize=16)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.get_yaxis().set_visible(False)

    inicio, fin = df.index[0], df.index[-1]

    for medio in df.columns:
        v0 = df.loc[inicio, medio]
        v1 = df.loc[fin, medio]

        plt.scatter(inicio, v0, color=colores[medio], zorder=niveles[medio])
        plt.text(inicio - 0.2, v0, f"{medio} {v0}%", ha="right", va="center",
                 fontsize=8, color=colores[medio], zorder=niveles[medio])

        plt.scatter(fin, v1, color=colores[medio], zorder=niveles[medio])
        plt.text(fin + 0.2, v1, f"{v1}%", ha="left", va="center",
                 fontsize=8, color=colores[medio], zorder=niveles[medio])

    plt.xticks(df.index, df.index)
    plt.tight_layout()

    os.makedirs("files/plots", exist_ok=True)
    plt.savefig("files/plots/news.png")
    plt.close()
