import random, sys, math
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
       
        self.logger = Logger("results.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        
        self.newly_infected = []
        self.newly_dead = []
        
        self.total_infected = 0
        self.total_dead = 0
        self.vaccine_saves = 0
        
        self.total_vaccinated = 0
        self.current_infected = 0
        self.total_interactions = 0
        
        self.time_step_counter = 0
        self.should_continue = True
        
        self.population = self._create_population(self.pop_size)
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)
        
    def _create_population(self, population_size):
        population = []
        already_vaccinated = math.floor(population_size * self.vacc_percentage)
        print(already_vaccinated)
        self.total_infected = self.initial_infected
        
        for i in range(population_size):
            if i < self.initial_infected:
                person = Person(i, False, self.virus)
                population.append(person)
            else:
                person = Person(i, False, None)
                population.append(person)
        
        # Vaccinate the population based on the vacc_percentage
        while already_vaccinated > 0:
            random_person = random.choice(population)
            if random_person.infection:
                continue
            else:
                random_person.is_vaccinated = True
                already_vaccinated -= 1        
        return population
        

    def _simulation_should_continue(self):        
        for person in self.population:
            if person.is_alive and not person.is_vaccinated:
                return True
        return False
    

    def run(self):
        while self.should_continue:
            self.time_step()
            self.should_continue = self._simulation_should_continue()
            self.time_step_counter += 1
            
            self.logger.log_interactions(self.time_step_counter, self.total_dead, self.total_interactions, self.current_infected)
        
            if not self.should_continue:
                self.logger.log_final_stats(self.time_step_counter, self.total_interactions, self.total_dead, self.total_vaccinated, self.current_infected, self.virus, self.pop_size, self.initial_infected, self.vacc_percentage, self.vaccine_saves, self.total_dead, self.total_infected)
        
        print("TIME STEPS: ", self.time_step_counter)

    def time_step(self):

        for person in self.population:
            if person.infection and person.is_alive:
                for i in range(100):
                    random_person = self.get_random_person()
                    self.interaction(random_person)
                    
                if person.did_survive_infection():
                    self.current_infected -= 1
                    person.is_vaccinated = True
                    self.total_vaccinated += 1

                else:
                    person.is_alive = False
                    self.total_dead += 1
                    self.current_infected -= 1
                    
        self._infect_newly_infected()
        
    def interaction(self, random_person):
        self.total_interactions += 1
        if random_person.is_vaccinated:
            self.vaccine_saves += 1
        elif random_person.infection is None and random_person.is_alive:
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person)
                self.population.remove(random_person)


    def get_random_person(self):
        random_person = random.choice(self.population)
        while random_person is None and random_person.is_alive is False and not random_person.is_vaccinated:
            random_person = random.choice(self.population)
        return random_person

    def _infect_newly_infected(self):
        """Infect each person from the infected list and update their attributes"""
        for person in self.newly_infected:
            person.infection = self.virus
            self.total_infected += 1
            self.current_infected += 1
            self.population.append(person)
            
        self.newly_infected = []
            
            

if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    # virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.12
    initial_infected = 10
    

    # Make a new instance of the Simulation
    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()
