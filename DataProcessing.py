import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class DataProcessing:

    @staticmethod
    def load_data():
        """
        Methode permettant de charger les données
        :return:
        """
        dfs = DataProcessing.get_all_orig()
        DataProcessing._add_datetime(dfs)

    @staticmethod
    def _get_filenames(path):
        """
        Methodes permettant de recupérer tous les fichiers de données
        :return:
        """
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return files

    @staticmethod
    def _add_datetime(dfs):
        """
        Methode permettant d'ajouter une colonne de timestamp aux données
        :return:
        """
        sc = ["2610-28.csv", "2874-28.csv", "4144-19.csv", "724-20.csv", "747-27.csv", "804-28bis.csv"]
        for filename, df in dfs.items():
            fname, fext = os.path.splitext(filename)
            df.dropna(inplace=True)
            if filename in sc:
                df['date_obj'] = pd.to_datetime(df['date'], format="%d/%m/%Y")
            else:
                df['date_obj'] = pd.to_datetime(df['date'], format="%Y-%m-%d")

            df['date'] = df["date_obj"].apply(lambda x: int(x.timestamp()))
            df.drop("date_obj", axis=1, inplace=True)
            df_normalized = df.apply(lambda x: (x - x.mean()) / x.std())
            DataProcessing._df_to_csv_file(df, "pp", fname)
            DataProcessing._df_to_csv_file(df_normalized, "nor", fname)

    @staticmethod
    def _df_to_csv_file(df, dirname, fname):
        """
        Methode permettant de sauvegarder les données transformées dans des fichiers
        :param df: la dataframe contenant les données
        :param dirname: le nom du repertoire
        :param fname: le nom du fichier
        :return:
        """
        path = f"data/{dirname}"
        if not os.path.exists(path):
            # Create the directory
            os.makedirs(path)
        df.to_csv(f"{path}/{fname}.csv", index=False)

    @staticmethod
    def get_all_pp():
        """
        Methode pour charger les données traitées
        :return:Dictionnaire de dataframe {'nom_fichier': Dataframe, ..}
        """
        path = "data/pp"
        dfs = {}
        filenames = DataProcessing._get_filenames(path)
        for filename in filenames:
            dfs[filename] = DataProcessing.get_pp(filename)

        return dfs

    @staticmethod
    def get_all_nor_filenames():
        """
        Methode permettant d'avoir tous les noms de fichiers normalisés
        :return: liste des fichiers normalisés
        """
        path = "data/nor"
        return DataProcessing._get_filenames(path)

    @staticmethod
    def get_all_orig_filenames():
        """
        Methode permettant d'avoir tous les noms de fichiers bruts
        :return: liste des fichiers bruts
        """
        path = "data/original"
        return DataProcessing._get_filenames(path)

    @staticmethod
    def get_all_pp_filenames():
        """
        Methode permettant d'avoir tous les noms de fichiers traités
        :return: liste des fichiers traités
        """
        path = "data/pp"
        return DataProcessing._get_filenames(path)

    @staticmethod
    def get_pp(filename: str):
        path = "data/pp"
        return pd.read_csv(f"{path}/{filename}")

    @staticmethod
    def plot_pp(filename: str):
        """
        Methode pour representer les données traitées
        :param filename: nom du fichier
        :return: None
        """
        df = DataProcessing.get_pp(filename)
        columns = df.columns
        nRows = 3
        nCols = 2
        fig, axs = plt.subplots(nRows, nCols, figsize=(6, 6))
        fig.suptitle(f"Données non normalisées : {filename}")
        for i in range(nRows):
            for j in range(nCols):
                column = columns[i * nCols + j]
                axs[i, j].plot(df[column])
                axs[i, j].set_ylabel(column)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def get_ccc_for_pp(filename: str, c="GWL"):
        """
        Pour calculer le coefficient de correlation d'une colonne par rapport aux autres
        :param filename: nom du fichier
        :param c: la colonne
        :return: un dictionnaire {'column': ccc}
        """
        df = DataProcessing.get_pp(filename)
        columns = df.columns
        result = {}
        x = df[c]
        for column in columns:
            y = df[column]
            result[f"{column}"] = DataProcessing._ccc(x, y)
        return result

    @staticmethod
    def get_ccc_for_all_pp(filename: str):
        """
        Calcul le ccc pour toutes les paires de variables possibles pour un fichier traité
        :param filename: nom du fichier
        :return: Dictionnaire {'col':{'col': ccc}}
        """
        df = DataProcessing.get_pp(filename)
        columns = df.columns
        result = []
        for column in columns:
            result.append(DataProcessing.get_ccc_for_pp(filename, column))

        return result

    @staticmethod
    def get_all_nor():
        """
        Méthode pour charger les données normalisées
        :return:Dictionnaire de dataframe {'nom_fichier': Dataframe, ..}
        """
        path = "data/nor"
        filenames = DataProcessing._get_filenames(path)
        dfs = {}
        for filename in filenames:
            dfs[filename] = DataProcessing.get_nor(filename)

        return dfs

    @staticmethod
    def get_nor(filename: str):
        path = "data/nor"
        return pd.read_csv(f"{path}/{filename}")

    @staticmethod
    def plot_nor(filename: str):
        """
        Methode pour representer les données normalisées
        :param filename: nom du fichier
        :return: None
        """
        df = DataProcessing.get_nor(filename)
        columns = df.columns
        nRows = 3
        nCols = 2
        fig, axs = plt.subplots(nRows, nCols, figsize=(6, 6))
        fig.suptitle(f"Données normalisées : {filename}")
        for i in range(nRows):
            for j in range(nCols):
                column = columns[i * nCols + j]
                axs[i, j].plot(df[column])
                axs[i, j].set_ylabel(column)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def get_ccc_for_nor(filename: str, c="GWL"):
        """
        Pour calculer le coefficient de correlation d'une colonne par rapport aux autres
        :param filename: nom du fichier
        :param c: la colonne
        :return: un dictionnaire {'column': ccc}
        """
        df = DataProcessing.get_nor(filename)
        columns = df.columns
        result = {}
        x = df[c]
        for column in columns:
            y = df[column]
            result[f"{column}"] = DataProcessing._ccc(x, y)
        return result

    @staticmethod
    def get_ccc_for_all_nor(filename: str):
        """
        Calcul le ccc pour toutes les paires de variables possibles pour un fichier normalisé
        :param filename: nom du fichier
        :return: Dictionnaire {'col':{'col': ccc}}
        """
        df = DataProcessing.get_nor(filename)
        columns = df.columns
        result = []
        for column in columns:
            result.append(DataProcessing.get_ccc_for_nor(filename, column))

        return result

    @staticmethod
    def get_all_orig():
        """
        Méthode pour charger les données originales
        :return: Dictionnaire de dataframe {'nom_fichier': Dataframe, ..}
        """
        path = "data/original"
        filenames = DataProcessing._get_filenames(path)
        dfs = {}
        for filename in filenames:
            dfs[filename] = DataProcessing.get_orig(filename)

        return dfs

    @staticmethod
    def get_orig(filename: str):
        path = "data/original"
        fname, fext = os.path.splitext(filename)
        if fext == ".csv":
            return pd.read_csv(f"{path}/{filename}")
        elif fext == ".xlsx":
            return pd.read_excel(f"{path}/{filename}")

    @staticmethod
    def display_dataframes(dfs):
        """
        Méthode paur afficher les dataframes
        :param dfs:
        :return:
        """
        for fname, df in dfs.items():
            print(f"File: {fname}")
            print(df)

    @staticmethod
    def _ccc(x, y):
        """
        Methode pour calculer le CCC (Coefficient de Corrélation de Concondance) entre 2 variables
        :param x: Première variable
        :param y: 2ème variable
        :return:
        """
        sxy = np.sum((x - x.mean())*(y - y.mean())) / x.shape[0]
        rhoc = 2*sxy / (np.var(x) + np.var(y) + (x.mean() - y.mean())**2)
        return rhoc
