import pandas as pd


def export_csv(df, dose, csv_file):
    df_vac_pet = df[df["estabelecimento_municipio_nome"] == "PETROPOLIS"]

    df_vac_pet = df_vac_pet[[
        'document_id',
        'paciente_id', 
        'paciente_idade',
        'paciente_enumSexoBiologico',
        'paciente_endereco_nmMunicipio',
        'estabelecimento_municipio_nome',
        'vacina_descricao_dose'
    ]]

    df_vac_pet = df_vac_pet[
        df_vac_pet["paciente_endereco_nmMunicipio"] == df_vac_pet["estabelecimento_municipio_nome"]
    ]
    df_vac_pet = df_vac_pet[df_vac_pet["vacina_descricao_dose"] == f"\xa0\xa0\xa0\xa0{dose}ª\xa0Dose"]
    
    grupos = [
        'Mais de 100 anos',
        '95 a 99 anos',
        '90 a 94 anos',
        '85 a 89 anos',
        '80 a 84 anos',
        '75 a 79 anos',
        '70 a 74 anos',
        '65 a 69 anos',
        '60 a 64 anos',
        '55 a 59 anos',
        '50 a 54 anos',
        '45 a 49 anos',
        '40 a 44 anos',
        '35 a 39 anos',
        '30 a 34 anos',
        '25 a 29 anos',
        '20 a 24 anos',
        '15 a 19 anos',
        '10 a 14 anos',
        '5 a 9 anos',
        '0 a 4 anos'
    ]

    y_homens = [0] * len(grupos)
    y_mulheres = [0] * len(grupos)


    for i, grupo in enumerate(grupos):
        gender = {}

        parse = grupo.replace(" anos", "")
        if "Mais de " in parse:
            parse = parse.replace("Mais de ", "")
            age = int(parse)
            gender = (
                df_vac_pet[df_vac_pet["paciente_idade"] >= age]
                ["paciente_enumSexoBiologico"]
            ).value_counts()
        else:
            parse = parse.split(" a ")
            age1 = int(parse[0])
            age2 = int(parse[1])

            gender = (
                df_vac_pet[(
                    (df_vac_pet["paciente_idade"] >= age1)
                    &
                    (df_vac_pet["paciente_idade"] <= age2)
                )]
                ["paciente_enumSexoBiologico"]
            ).value_counts()

        if "M" in gender:
            y_homens[i] += gender["M"]
        if "F" in gender:
            y_mulheres[i] += gender["F"]

    df_vacinados = pd.DataFrame([grupos, y_homens, y_mulheres]).T
    df_vacinados.columns = ["Grupo", "Homens", "Mulheres"]

    df_vacinados.to_csv(csv_file, index=False, sep=";")


if __name__ == "__main__":
    df_vac_rj = pd.read_csv(
        # baixar de https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao e alterar
        "Registros de Vacinação COVID19 RJ ate 23 04 21.csv",
        sep=";",
        #warn_bad_lines=True, 
        #error_bad_lines=False,
    )

    export_csv(df_vac_rj, "1", "petropolis vacinados 1 dose.csv")
    export_csv(df_vac_rj, "2", "petropolis vacinados 2 dose.csv")
