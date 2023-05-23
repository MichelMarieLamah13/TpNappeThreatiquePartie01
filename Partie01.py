import pandas as pd

from DataProcessing import DataProcessing


class Partie01:
    @staticmethod
    def get_all_processed_data():
        """
        Méthode permettant d'afficher les données traitée
        :return: Le dataframe correspondant au fichier
        """
        return DataProcessing.get_all_pp()

    @staticmethod
    def get_processed_data(filename: str) -> pd.DataFrame:
        """
        Permet de retourner le dataframe relatif à un fichier traité
        :param filename: Nom du fichier
        :return: Dataframe
        """
        try:
            return DataProcessing.get_pp(filename)
        except Exception as e:
            print(f"Erreur: {e}")

    @staticmethod
    def plot_processed_data(filename: str):
        """
        Methode pour representé les données d'un fichier traité
        :param filename: nom du fichier
        :return:
        """
        DataProcessing.plot_pp(filename)

    @staticmethod
    def get_ccc_for_processed_data(filename: str, c="GWL"):
        """
        Calcul le coefficient de correlation d'une colonne d'un fichier normalisé par rapport aux autres
        :param filename: nom du fichier
        :param c: la colonne
        :return: Dataframe
        """
        ccc = DataProcessing.get_ccc_for_pp(filename, c)
        return pd.DataFrame(ccc, index=[c])

    @staticmethod
    def get_ccc_for_all_processed_data(filename: str):
        """
        Calcul le ccc pour toutes les paires de variables possibles pour un fichier traité
        :param filename: nom du fichier
        :return: Dictionnaire {'col':{'col': ccc}}
        """
        ccc = DataProcessing.get_ccc_for_all_pp(filename)
        indexes = ccc[0].keys()
        return pd.DataFrame(ccc, index=indexes)

    @staticmethod
    def get_all_normalized_data():
        """
        Méthode permettant d'avoir les données normalisées correspondant au fichier
        :return: Dictionnaire dataframe {'nom_fichier1': Dataframe, 'nom_fichier2': Dataframe}
        """
        return DataProcessing.get_all_nor()

    @staticmethod
    def get_normalized_data(filename: str) -> pd.DataFrame:
        """
        Permet de retourner le dataframe spécifique à un seul fichier normalisé
        :param filename: nom du fichier
        :return: Dataframe
        """
        try:
            return DataProcessing.get_nor(filename)
        except Exception as e:
            print(f"Erreur: {e}")

    @staticmethod
    def plot_normalized_data(filename: str):
        """
        Methode pour representé les données d'un fichier normalisé
        :param filename: nom du fichier
        :return:
        """
        DataProcessing.plot_nor(filename)

    @staticmethod
    def get_ccc_for_normalized_data(filename: str, c="GWL"):
        """
        Calcul le coefficient de correlation d'une colonne d'un fichier normalisé par rapport aux autres
        :param filename: nom du fichier
        :param c: la colonne
        :return: Un dictionnaire {'col': ccc}
        """
        ccc = DataProcessing.get_ccc_for_nor(filename, c)
        return pd.DataFrame(ccc, index=[c])

    @staticmethod
    def get_ccc_for_all_normalized_data(filename: str):
        """
        Calcul le ccc pour toutes les paires de variables possibles pour un fichier normalisé
        :param filename: nom du fichier
        :return: Dataframe
        """
        ccc = DataProcessing.get_ccc_for_all_nor(filename)
        indexes = ccc[0].keys()
        return pd.DataFrame(ccc, index=indexes)

    @staticmethod
    def get_all_original_data():
        """
        Méthode permettant d'avoir les données originales correspondant au fichier
        :return: Dictionnaire dataframe {'nom_fichier1': Dataframe, 'nom_fichier2': Dataframe}
        """
        return DataProcessing.get_all_orig()

    @staticmethod
    def get_original_data(filename: str) -> pd.DataFrame:
        """
        Permet de retourner le dataframe relatif à un fichier originale
        :param filename: Nom du fichier
        :return: Dataframe
        """
        try:
            return DataProcessing.get_orig(filename)
        except Exception as e:
            print(f"Erreur: {e}")

    @staticmethod
    def _menu():
        """
        Methode permettant d'afficher un menu pour les questions du TP
        :return: le choix entré
        """
        while True:
            try:
                print(f"================== MENU ====================")
                print(f"[1] - Affichage des données")
                print(f"[2] - Representation graphique")
                print(f"[3] - Calcul du Coefficient de Concordance")
                print(f"[4] - Quitter")
                print(f"============================================")
                choix = int(input("Votre choix: "))
                if 1 <= choix <= 4:
                    return choix
            except ValueError as e:
                print(f"ERREUR: {e}")

    @staticmethod
    def start():
        """
        Methode permettant de lancer la première partie
        :return:
        """
        while True:
            choix = Partie01._menu()
            if choix == 1:
                Partie01._menu_affichage_donnees()
            elif choix == 2:
                Partie01._menu_representation_graphique()
            elif choix == 3:
                Partie01._menu_calcul_ccc()
            else:
                print("Merci pour le test, à bientôt")
                break

    @staticmethod
    def _menu_affichage_donnees():
        """
        Permet d'afficher un menu pour l'affichage des données
        :return: le choix
        """
        while True:
            try:
                print(f"================== MENU ====================")
                print(f"[1] - Données normalisées")
                print(f"[2] - Données non normalisées")
                print(f"[3] - Données brutes")
                print(f"[4] - Retour")
                print(f"============================================")
                choix = int(input("Votre choix: "))

                if choix == 1:
                    Partie01._choix_donnees_normalisees()
                elif choix == 2:
                    Partie01._choix_donnees_traitees()
                elif choix == 3:
                    Partie01._choix_donnees_originales()
                elif choix == 4:
                    break

            except ValueError as e:
                print(f"ERREUR: {e}")

    @staticmethod
    def _choix_donnees_normalisees():
        while True:
            choix = Partie01._menu_donnees()
            if choix == 1:
                fichier = Partie01._menu_donnees_normalisees()
                df = Partie01.get_normalized_data(fichier)
                print(df)
            elif choix == 2:
                dfs = Partie01.get_all_normalized_data()
                Partie01._display_dfs(dfs)
            elif choix == 3:
                break

    @staticmethod
    def _display_dfs(dfs):
        for filename, df in dfs.items():
            print(f"File: {filename}")
            print(df)

    @staticmethod
    def _choix_donnees_traitees():
        while True:
            choix = Partie01._menu_donnees()
            if choix == 1:
                fichier = Partie01._menu_donnees_non_normalisees()
                df = Partie01.get_processed_data(fichier)
                print(df)
                break
            elif choix == 2:
                dfs = Partie01.get_all_processed_data()
                Partie01._display_dfs(dfs)
                break
            elif choix == 3:
                break

    @staticmethod
    def _choix_donnees_originales():
        while True:
            choix = Partie01._menu_donnees()
            if choix == 1:
                fichier = Partie01._menu_donnees_brutes()
                df = Partie01.get_original_data(fichier)
                print(df)
            elif choix == 2:
                dfs = Partie01.get_all_original_data()
                Partie01._display_dfs(dfs)
            elif choix == 3:
                break

    @staticmethod
    def _menu_donnees():
        while True:
            try:
                print(f"================== MENU ====================")
                print(f"[1] - Un fichier spécifique")
                print(f"[2] - Tous les fichiers")
                print(f"[3] - Retour")
                print(f"============================================")
                choix = int(input("Votre choix: "))
                if 1 <= choix <= 3:
                    return choix
            except ValueError as e:
                print(f"ERREUR: {e}")
        pass

    @staticmethod
    def _menu_donnees_normalisees():
        """
        Methode permettant de retourner le fichier à afficher
        :return: None
        """
        try:
            filenames = DataProcessing.get_all_nor_filenames()
            print("=====Fichiers normalisés===")
            while True:
                for i, filename in enumerate(filenames):
                    print(f"[{i + 1}] -> {filename}")
                print("========================")
                choix = int(input("Votre choix: "))
                if 1 <= choix <= len(filenames):
                    return filenames[choix - 1]
        except ValueError as e:
            print(f"ERREUR: {e}")

    @staticmethod
    def _menu_donnees_non_normalisees():
        """
            Methode permettant de retourner le fichier à afficher
            :return: None
        """
        try:
            filenames = DataProcessing.get_all_pp_filenames()
            print("=====Fichiers non normalisés===")
            while True:
                for i, filename in enumerate(filenames):
                    print(f"[{i + 1}] -> {filename}")
                print("========================")
                choix = int(input("Votre choix: "))
                if 1 <= choix <= len(filenames):
                    return filenames[choix - 1]
        except ValueError as e:
            print(f"ERREUR: {e}")

    @staticmethod
    def _menu_donnees_brutes():
        """
            Methode permettant de retourner le fichier à afficher
            :return: None
        """
        try:
            filenames = DataProcessing.get_all_orig_filenames()
            print("=====Fichiers bruts===")
            while True:
                for i, filename in enumerate(filenames):
                    print(f"[{i + 1}] -> {filename}")
                print("========================")
                choix = int(input("Votre choix: "))
                if 1 <= choix <= len(filenames):
                    return filenames[choix - 1]
        except ValueError as e:
            print(f"ERREUR: {e}")

    @staticmethod
    def _menu_representation_graphique():
        """
        Permet d'afficher un menu pour la representation graphique
        :return: le choix
        """
        while True:
            try:
                print(f"================== MENU ====================")
                print(f"[1] - Données normalisées")
                print(f"[2] - Données non normalisées")
                print(f"[3] - Retour")
                print(f"============================================")
                choix = int(input("Votre choix: "))

                if choix == 1:
                    fichier = Partie01._menu_donnees_normalisees()
                    Partie01.plot_normalized_data(fichier)
                elif choix == 2:
                    fichier = Partie01._menu_donnees_non_normalisees()
                    Partie01.plot_processed_data(fichier)
                elif choix == 3:
                    break

            except ValueError as e:
                print(f"ERREUR: {e}")

    @staticmethod
    def _menu_calcul_ccc():
        """
        Permet d'afficher un menu pour le calcul ccc
        :return:
        """
        while True:
            try:
                print(f"================== MENU ====================")
                print(f"[1] - Données normalisées")
                print(f"[2] - Données non normalisées")
                print(f"[3] - Retour")
                print(f"============================================")
                choix = int(input("Votre choix: "))

                if choix == 1:
                    fichier = Partie01._menu_donnees_normalisees()
                    c = Partie01._choix_ccc()
                    if c == 1:
                        ccc = Partie01.get_ccc_for_normalized_data(fichier)
                    else:
                        ccc = Partie01.get_ccc_for_all_normalized_data(fichier)
                    print(ccc)
                elif choix == 2:
                    fichier = Partie01._menu_donnees_non_normalisees()
                    if c == 1:
                        ccc = Partie01.get_ccc_for_processed_data(fichier)
                    else:
                        ccc = Partie01.get_ccc_for_all_processed_data(fichier)
                    print(ccc)
                elif choix == 3:
                    break

            except ValueError as e:
                print(f"ERREUR: {e}")

    @staticmethod
    def _choix_ccc():
        while True:
            try:
                print(f"================== MENU ====================")
                print(f"[1] - GWL")
                print(f"[2] - Tous les couples")
                print(f"============================================")
                choix = int(input("Votre choix: "))
                if 1 <= choix <= 2:
                    return choix
            except ValueError as e:
                print(f"Erreur: {e}")
