import random
# random.seed(42)
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated, infection = None):
        # A person has an id, is_vaccinated and possibly an infection
        
        self._id = _id  # int
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
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    # TODO Test unvaccinated_person's attributes here...
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True

    # Test an infected person. An infected person has an infection/virus
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus

    # You need to check the survival of an infected person. Since the chance
    # of survival is random you need to check a group of people. 
    # Create a list to hold 100 people. Use the loop below to make 100 people
    people = []
    for i in range(1, 100):
        person = Person(i, False, virus)
        people.append(person)
            

    # Count the people that survived and did not survive
    did_survive = 0
    did_not_survive = 0
    
    for person in people:
        if person.did_survive_infection():
            did_survive += 1
        else:
            did_not_survive += 1
            
    print("DID SURVIVE", did_survive)
    print("DID NOT SURVIVE", did_not_survive)
    print("Mortality Rate of Sample Group", round(did_survive / (did_survive + did_not_survive), 3))

    # Stretch challenge! 
    # Check the infection rate of the virus...
    
    uninfected_group = []
    
    infected_people_count = 0
    uninfected_people_count = 0
    
    for i in range(1, 100):
        person = Person(i, False)
        uninfected_group.append(person)
    
    for person in uninfected_group:
        random_number = random.random()
        if random_number < virus.repro_rate:
            person.infection = virus
            infected_people_count += 1
        else:
            uninfected_people_count += 1
    
    print("INFECTED PEOPLE COUNT", infected_people_count)
    print("UNINFECTED PEOPLE COUNT", uninfected_people_count)
    print("Infection Rate of Virus", round(infected_people_count / (infected_people_count + uninfected_people_count), 3))
