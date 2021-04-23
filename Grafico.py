import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects


if __name__ == "__main__":
    df_ibge = pd.read_csv("piramide petropolis ibge censo corrigido.csv", sep=";")
    df_vac1 = pd.read_csv("petropolis vacinados 1 dose.csv", sep=";")
    df_vac2 = pd.read_csv("petropolis vacinados 2 dose.csv", sep=";")

    # Truque para colocar as barras lateralmente
    df_ibge["Mulheres"] = df_ibge["Mulheres"] * -1
    df_vac1["Mulheres"] = df_vac1["Mulheres"] * -1
    df_vac2["Mulheres"] = df_vac2["Mulheres"] * -1

    fig = plt.figure(figsize=(6, 6))
    ax = plt.gca()

    sns.barplot(
        x='Homens',
        y='Grupo',
        data=df_ibge,
        ax=ax,
        color="lightblue",
        edgecolor="black",
        lw=1.5,
        label="Homens"
    )
    sns.barplot(
        x='Mulheres',
        y='Grupo',
        data=df_ibge,
        ax=ax,
        color="pink",
        edgecolor="black",
        lw=1.5,
        label="Mulheres"
    )

    sns.barplot(
        x='Homens',
        y='Grupo',
        data=df_vac1,
        ax=ax,
        color="lightgreen",
        edgecolor="black",
        lw=1.5
    )
    sns.barplot(
        x='Mulheres',
        y='Grupo',
        data=df_vac1,
        ax=ax,
        color="lightgreen",
        edgecolor="black",
        lw=1.5,
        label="Primeira Dose"
    )

    sns.barplot(
        x='Homens',
        y='Grupo',
        data=df_vac2,
        ax=ax,
        color="darkgreen",
        edgecolor="black",
        lw=1.5,
        label="Segunda Dose"
    )
    sns.barplot(
        x='Mulheres',
        y='Grupo',
        data=df_vac2,
        ax=ax,
        color="darkgreen",
        edgecolor="black",
        lw=1.5
    )

    plt.axvline(x=0, c="black")

    plt.xlabel("Mulheres        |        Homens   ")
    plt.ylabel("")

    ax.xaxis.set_major_formatter(
        lambda x, pos: abs(round(x))
    )

    plt.title("Vacinação COVID-19 Em Petrópolis\nPor Faixa Etária e Gênero - Dados de 23/04/21")

    plt.legend()
    plt.tight_layout()

    txt = ax.text(0.5, 0.167, s="@eduardopietre", fontweight='bold', size=12, color='#701111', ha='center', va="center", transform=ax.transAxes)

    txt.set_path_effects([PathEffects.withStroke(linewidth=3.0, foreground='w')])

    plt.savefig("Vacinação COVID-19 Em Petrópolis Por Faixa Etária e Gênero.png")
