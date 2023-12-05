import random, sys, math
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
       
        self.logger = Logger("answers.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        
        self.newly_infected = []
        self.newly_dead = []
        
        self.total_infected = 0
        self.total_dead = 0
        
        self.time_step_counter = 0
        self.should_continue = True
        
        self.population = self._create_population(self.pop_size)
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)
        
    def _create_population(self, population_size):
        population = []
        already_vaccinated = math.floor(population_size * self.vacc_percentage)
        
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
            self.time_step_counter += 1
            self.time_step()
            self.should_continue = self._simulation_should_continue()
        
        self.logger.log_time_step(self.time_step_counter)
        self.logger.log_final_stats(self.total_dead, self.total_infected, self.pop_size)

    def time_step(self):
        self._infect_newly_infected()
        self.logger.log_infection_survival(self.time_step_counter, (len(self.population) - self.total_dead), len(self.newly_dead))

        # Ensure that newly_infected and newly_dead lists are reset at the beginning
        self.newly_infected = []
        self.newly_dead = []

        selected_individuals = set()

        for person in self.population:
            if person.is_alive and person.infection is not None:
                i = 0
                while i < 100:
                    # Filter out individuals that are dead, vaccinated, or already selected
                    available_individuals = [p for p in self.population if p.is_alive and not p.is_vaccinated and p not in selected_individuals]
                    
                    if not available_individuals:
                        break  # Break the loop if we have already interacted with all available individuals

                    random_person = random.choice(available_individuals)
                    self.interaction(person, random_person, selected_individuals,)
                    
                    # Add the selected individual to the set
                    selected_individuals.add(random_person)

                    i += 1
                    
        self.logger.log_interactions(self.time_step_counter, len(selected_individuals), len(self.newly_infected))        

    def interaction(self, infected_person, random_person, selected_individuals,):
        if random.random() < self.virus.repro_rate:
            self.newly_infected.append(random_person)     


    def _infect_newly_infected(self):
        """Infect each person from the infected list and update their attributes"""
        for person in self.newly_infected:
            person.infection = self.virus
            self.total_infected += 1
            
            person.is_alive = person.did_survive_infection()
            
            if person.is_alive:
                person.is_vaccinated = True
            
            elif not person.is_alive:
                self.newly_dead.append(person)
                self.total_dead += 1
            
            # reintroduce person back into population
            self._update_person_with_id(self.population, person.id, person.__dict__)
        
    
    def _update_person_with_id(self, population, target_id, new_attributes):
        "Introduce infected person back into the population"
        for i, person in enumerate(population):
            if person.id == target_id:
                # Update specific attributes of the person with the target ID
                for key, value in new_attributes.items():
                    setattr(person, key, value)
                break  # Break the loop once the person is found and updated


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    # virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10
    

    # Make a new instance of the Simulation
    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()
