import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt


if __name__ == "__main__":
    estimativa_populacao = 306678  # 2020

    # de https://censo2010.ibge.gov.br/sinopse/webservice/frm_piramide.php?ano=2010&codigo=330390
    # No formato: Grupo,Homens,Mulheres (apenas os números brutos, sem porcentagem).
    df_orig = pd.read_csv("piramide petropolis ibge censo 2010.csv")
    orig_total_homems = df_orig["Homens"].sum()
    orig_total_mulheres = df_orig["Mulheres"].sum()
    orig_total = orig_total_homems + orig_total_mulheres
    print("Total censo:", orig_total)

    multiplicador = estimativa_populacao / orig_total
    print("Multiplicador:", multiplicador)

    # estimativa
    df_est = df_orig.copy()
    df_est["Homens"] = df_est["Homens"] * multiplicador
    df_est["Mulheres"] = df_est["Mulheres"] * multiplicador

    df_est.to_csv("piramide petropolis ibge censo corrigido.csv", index=False, sep=";")
