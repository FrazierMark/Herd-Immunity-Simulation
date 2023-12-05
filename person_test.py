import unittest
from person import Person
from virus import Virus
import random

class TestPerson(unittest.TestCase):
    def setUp(self):
        # Create instances of the Virus class for testing
        self.virus_a = Virus("VirusA", 0.5, 0.1)
        self.virus_b = Virus("VirusB", 0.8, 0.2)

    def test_person_initialization(self):
        person = Person(1, True)
        self.assertEqual(person.id, 1)
        self.assertTrue(person.is_vaccinated)
        self.assertIsNone(person.infection)
        self.assertTrue(person.is_alive)

    def test_did_survive_infection(self):
        # Test the case when a person is not infected
        person = Person(2, True)
        self.assertIsNone(person.infection)
        self.assertTrue(person.is_alive)
        self.assertTrue(person.is_vaccinated)
        self.assertIsNone(person.did_survive_infection())  # Should return None for uninfected person

        # Test the case when a person is infected
        person = Person(3, False, self.virus_a)
        self.assertEqual(person.infection, self.virus_a)
        self.assertTrue(person.is_alive)
        self.assertFalse(person.is_vaccinated)  # Person is not vaccinated before infection
        
        random.seed(42)  # Setting seed for reproducibility
        survived = person.did_survive_infection()
        if survived:
            self.assertTrue(person.is_vaccinated)
        else:
            self.assertFalse(person.is_alive)

if __name__ == '__main__':
    unittest.main()