import unittest
from logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Logger class for testing
        self.logger = Logger("test_log.txt")

    def test_write_metadata(self):
        self.logger.write_metadata(100, 0.3, "TestVirus", 0.1, 1.5)

        # Read the contents of the file to check if metadata is written correctly
        with open("test_log.txt", 'r') as file:
            content = file.read()

        expected_content = "Population Size\tVaccination Percentage\tVirus Name\tMortality Rate\tBasic Reproduction Number\n"
        expected_content += "100\t\t\t\t0.3\t\t\t\t\tTestVirus\t\t0.1\t\t\t1.5\n\n"

        self.assertEqual(content, expected_content)

    def test_log_interactions(self):
        self.logger.log_interactions(1, 50, 10)

        # Read the contents of the file to check if interaction logs are written correctly
        with open("test_log.txt", 'r') as file:
            content = file.read()

        expected_content = "Step Number\tInteractions\tNew Infections\n"
        expected_content += "1\t\t\t50\t\t\t\t10\n"

        self.assertIn(expected_content, content)

    def test_log_infection_survival(self):
        self.logger.log_infection_survival(2, 80, 5)

        # Read the contents of the file to check if infection survival logs are written correctly
        with open("test_log.txt", 'r') as file:
            content = file.read()

        expected_content = "Step Number\tPopulation Count\tNew Fatalities\n"
        expected_content += "2\t\t\t80\t\t\t\t\t5\n\n"

        self.assertIn(expected_content, content)

    def test_log_time_step(self):
        self.logger.log_time_step(3)

        # Read the contents of the file to check if time step logs are written correctly
        with open("test_log.txt", 'r') as file:
            content = file.read()

        expected_content = "\nTime Step Number\n"
        expected_content += "3\n"

        self.assertIn(expected_content, content)

    def test_log_final_stats(self):
        self.logger.log_final_stats(20, 50, 100)

        # Read the contents of the file to check if final stats logs are written correctly
        with open("test_log.txt", 'r') as file:
            content = file.read()

        expected_content = "\n\n\nFinal Summary\n \t Total Deaths \t Total Infections \t Total Death Percent\n"
        expected_content += "\t\t20\t\t\t\t50\t\t\t\t\t5.0% \n"

        self.assertIn(expected_content, content)

if __name__ == '__main__':
    unittest.main()