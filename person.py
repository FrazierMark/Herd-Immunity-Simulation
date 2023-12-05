import random
# random.seed(42)
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, id, is_vaccinated, infection = None):
        # A person has an id, is_vaccinated and possibly an infection
        
        self.id = id  # int
        self.is_vaccinated = is_vaccinated
        self.infection = infection # default to None
        self.is_alive = True # default to True
        

    def did_survive_infection(self):
        # This method checks if a person survived an infection. 
        # TODO Only called if infection attribute is not None.
        if self.infection is not None:
            random_number = random.random()
            if random_number < self.infection.mortality_rate:
                self.is_alive = False
                return False
            self.is_vaccinated = True
            return True

if __name__ == "__main__":
    # This section is incomplete finish it and use it to test your Person class
    # TODO Define a vaccinated person and check their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person.id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    # TODO Test unvaccinated_person's attributes here...
    assert unvaccinated_person.id == 2
    assert unvaccinated_person.is_alive is True

    # Test an infected person. An infected person has an infection/virus
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    assert infected_person.id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus