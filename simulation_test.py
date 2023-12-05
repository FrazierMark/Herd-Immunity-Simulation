import unittest
from virus import Virus
from logger import Logger
from simulation import Simulation

class TestSimulation(unittest.TestCase):
    def setUp(self):
        
        virus = Virus("TestVirus", 0.7, 0.15)
        self.simulation = Simulation(virus, 100, 0.3, 5)

    def test_simulation_initialization(self):
        self.assertEqual(self.simulation.pop_size, 100)
        self.assertEqual(self.simulation.vacc_percentage, 0.3)
        self.assertEqual(self.simulation.initial_infected, 5)
        self.assertIsInstance(self.simulation.logger, Logger)
        self.assertIsInstance(self.simulation.virus, Virus)
        self.assertEqual(len(self.simulation.population), 100)

    def test_simulation_should_continue(self):
        self.assertTrue(self.simulation._simulation_should_continue())

        # Set all persons to be vaccinated
        for person in self.simulation.population:
            person.is_vaccinated = True

        self.assertFalse(self.simulation._simulation_should_continue())

if __name__ == '__main__':
    unittest.main()