import unittest
import pandas as pd
from io import StringIO
from Task import load_and_process_data

class TestLoadAndProcessData(unittest.TestCase):

    def setUp(self):
        # Set up sample CSV data for testing
        #Looked up StringIO syntax
        self.data = StringIO(
            """General,number_of_battles,WAR,aWAR
General A,5,3.0,0.9
General B,3,2.5,0.8
General C,4,4.0,1.0
General D,6,3.5,1.2
General E,2,1.5,0.4"""
        )

        #Expected data if Task runs correctly
        self.expected_data = pd.DataFrame({
            "General": ["General D", "General C", "General A"],
            "number_of_battles": [6, 4, 5],
            "WAR": [3.5, 4.0, 3.0],
            "aWAR": [1.2, 1.0, 0.9]
        })

    def test_load_and_process_data(self):
        #Run Task on created data
        df_sorted = load_and_process_data(self.data)
        
        #Checking that all expected outcomes are true
        self.assertEqual(len(df_sorted), 3)
        self.assertTrue((df_sorted["number_of_battles"] >= 4).all())
        sorted_aWAR = df_sorted["aWAR"].values
        self.assertTrue(all(sorted_aWAR[i] >= sorted_aWAR[i + 1] for i in range(len(sorted_aWAR) - 1)))

        # Final double check that outcome matches the expected outcome
        pd.testing.assert_frame_equal(df_sorted.reset_index(drop=True), self.expected_data)
#For Command Line Tool
def main():
    #explicit loading for tests added because for some reason command line was not picking up the test originally
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLoadAndProcessData)
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == '__main__':
    main()
