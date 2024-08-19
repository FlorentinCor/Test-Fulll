import unittest
import pandas as pd
from bike_investigation import time_stats, station_stats, trip_duration_stats, user_stats

class TestBikeShareData(unittest.TestCase):

    def test_time_stats(self):
        data = {
            'Start Time': ['2017-01-01 09:07:57', '2017-01-02 09:07:57', '2017-01-03 00:07:57'],
            'End Time': ['2017-01-01 09:20:53', '2017-01-02 09:20:53', '2017-01-03 00:20:53'],     
        }

        # TO DO : create a panda DataFrame from the data dictionary

        df = pd.DataFrame(data)

        # TO DO : add more tests for the other keys in the result dictionary

        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])

        df['month'] = df['Start Time'].dt.month
        df['day'] = df['Start Time'].dt.day_name()
        
        result = time_stats(df)

        self.assertEqual(result['best_month'], 1)
        self.assertEqual(result['best_day'], 'Monday')
       
    # TO DO : base on the above test, create tests for station_stats, trip_duration_stats and user_stats function. Make sure you cover common corner cases.


    def test_station_stats(self):
        data = {
            'Start Station': ['Streeter Dr & Grand Ave', 'Green St & Madison St', 'Clark St & Armitage Ave A'],
            'End Station': ['Rush St & Cedar St', 'Streeter Dr & Grand Ave', 'Clinton St & Washington Blvd'],
        }

        df = pd.DataFrame(data)
        result = station_stats(df)

        self.assertEqual(result['best_start_station'], 'Clark St & Armitage Ave A')
        self.assertEqual(result['best_end_station'], 'Clinton St & Washington Blvd')
        self.assertEqual(result['best_start_end_station'], 'Clark St & Armitage Ave A AND Clinton St & Washington Blvd')

    def test_trip_duration_stats(self):
        data = {
            'Trip Duration': [300,1900,800,2000],
        }

        df = pd.DataFrame(data)
        result = trip_duration_stats(df)

        self.assertEqual(result['Trip Duration'], 5000)
        self.assertEqual(result['Mean Duration'], 1250)

if __name__ == '__main__':
    unittest.main()
