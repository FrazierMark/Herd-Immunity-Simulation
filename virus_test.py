import unittest
from virus import Virus

class TestVirus(unittest.TestCase):
    def test_virus_initialization(self):
        virus = Virus("TestVirus", 0.7, 0.15)
        self.assertEqual(virus.name, "TestVirus")
        self.assertEqual(virus.repro_rate, 0.7)
        self.assertEqual(virus.mortality_rate, 0.15)
        
        virus2 = Virus("TestVirus2", 5.7, 0.25)
        self.assertEqual(virus2.name, "TestVirus2")
        self.assertEqual(virus2.repro_rate, 5.7)
        self.assertEqual(virus2.mortality_rate, 0.25)
        
        virus3 = Virus("TestVirus3", 1.8, 0.45)
        self.assertEqual(virus3.name, "TestVirus3")
        self.assertEqual(virus3.repro_rate, 1.8)
        self.assertEqual(virus3.mortality_rate, 0.45)

if __name__ == '__main__':
    unittest.main()