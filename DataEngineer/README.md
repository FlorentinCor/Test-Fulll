# Test Data Fulll

    Def get_filters(): 

Utilisation de la fonction While True pour effectuer une boucle avec une condition de sortie "Break" et ajout de l'input pour aiguiller à ce que le texte corresponde bien au nom d'un Excel, sinon donnée invalide

Pour les mois et les jours, même principe mais on stock tout dans une variable qu'on appellera en suivant dans le While True


    Def load_data(city, month, day):

Lecture du csv en fonction de la ville choisie ainsi que la conversion de la colonne Start Time
Ajout de "errors='coerce'" pour gérer les données invalides ou mal formatées.

On extrait les colonnes mois et jour de la colonne start time
On ajoute des boucles sur le mois et les jours pour leur donner une valeur et pouvoir filtrer sauf si l'utilisateur choisi 'All', on ne filtre pas


    Def time_stats(df):

On ajoute une boucke si aucune donnée pour informer l'utilisateur
On utilise la fonction mode() pour afficher les valeurs les plus fréquentes

Pour l'heure la plus fréqente, on ajoute la colonne 'hour' dans le Dataframe


    Def station_stats(df):

Même principe pour les stations les pus fréquentes
Pour avoir la combinaison des deux, on ajoute une nouvelle colonne avec les 2 éléments et on réutilise la foncion mode()


    Def trip_duration_stats(df):

Pour calculer le temps total et la moyenne on utilise les fonctions sum() et mean(), les données sont en secondes, on les affichent en minute et en heure pour plus de lisibilité
On ajoute :.2f pour avoir les résultats avec 2 décimales


    Def user_stats(df):

Utilisation de la fonction "df[].unique()" pour vérifier les valeurs dans les colonnes
On utilise une boucle si colonne introuvable alors "Pas de données", sinon on compte le nombre de fois où le texte apparait et on le somme
Utilisation les fonction min et max pour l'année la plus récente et ancienne


TestBikeShareData(unittest.TestCase):

    Def test_time_stats(self):

Ajout d'une fonction "return" dans "def time_stats(df)" pour récupérer les valeurs du test et ainsi les utiliser
Création du DataFrame et ajout des colonnes "Start Time" et "End Time", on les converti en datetime et on extrait le mois et le jour

Avec la fontion self.assertEqual, on vérifie que les valeurs soient les mêmes que les résultats du premier fichier

On réitère les tests avec les stations et stats du voyage


