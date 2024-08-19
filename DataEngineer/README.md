# Test Data Fulll

    Def get_filters(): 

Utilisation de la boucle while True pour effectuer une boucle avec une condition de sortie via break. Ajout de la saisie utilisateur (input) pour s'assurer que le texte corresponde bien au nom d'un fichier Excel ; sinon, afficher "donnée invalide".

Pour les mois et les jours, même principe, mais tout est stocké dans une variable qui sera appelée dans la boucle while True.


    Def load_data(city, month, day):

Lecture du fichier CSV en fonction de la ville choisie ainsi que conversion de la colonne Start Time.
Ajout de errors='coerce' pour gérer les données invalides ou mal formatées.

On extrait les colonnes mois et jour de la colonne Start Time.
On ajoute des boucles pour le mois et les jours afin de les assigner correctement et pouvoir filtrer. Si l'utilisateur choisit 'All', aucun filtre n'est appliqué.


    Def time_stats(df):

Ajout d'une boucle pour vérifier s'il n'y a aucune donnée afin d'informer l'utilisateur.
Utilisation de la fonction mode() pour afficher les valeurs les plus fréquentes.
Pour l'heure la plus fréquente, on ajoute la colonne 'hour' dans le DataFrame.

Le "return" sera intégré plus loin (ainsi que pour la station et le temps).


    Def station_stats(df):

Même principe pour les stations les plus fréquentes.
Pour obtenir la combinaison des deux stations les plus utilisées, on ajoute une nouvelle colonne contenant les deux éléments combinés, puis on utilise la fonction mode().


    Def trip_duration_stats(df):

Pour calculer le temps total et la moyenne, on utilise les fonctions sum() et mean(). Les données étant en secondes, on les affiche en minutes et en heures pour plus de lisibilité.
On ajoute :.2f pour afficher les résultats avec deux décimales.


    Def user_stats(df):

Utilisation de la fonction df[].unique() pour vérifier les valeurs dans les colonnes.
On utilise une boucle pour vérifier si une colonne est introuvable ; dans ce cas, on affiche "Pas de données". Sinon, on compte le nombre de fois où le texte apparaît et on fait la somme.
Utilisation des fonctions min() et max() pour afficher l'année la plus récente et la plus ancienne.


TestBikeShareData(unittest.TestCase):

    Def test_time_stats(self):

Ajout d'une fonction return dans def time_stats(df) pour récupérer les valeurs du test et les utiliser.
Création du DataFrame et ajout des colonnes Start Time et End Time, conversion en datetime, et extraction des mois et des jours.

Avec la fonction self.assertEqual, on vérifie que les valeurs sont identiques aux résultats du fichier initial.

On réitère les tests avec les stations et les statistiques de voyage.
