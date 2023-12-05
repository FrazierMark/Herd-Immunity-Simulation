class Logger(object):
    def __init__(self, file_name):
        # Initialize the file name and interaction logs list
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        # Open the file in 'w' mode to write metadata
        with open(self.file_name, 'w') as file:
            # Write metadata information in tab-delimited format
            file.write(f"""
            Population Size: {pop_size}
            Vaccination Percentage: {vacc_percentage}
            Virus Name: {virus_name}
            Mortality Rate: {mortality_rate}
            Basic Reproduction Number: {basic_repro_num}
            ---------------------------------------------\n\n""")
            file.close()

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        # Open the file in 'a' mode to append interaction logs
        with open(self.file_name, 'a') as file:
            # Log header
            file.write(f"""
                Step Number: {step_number}
                Interactions: {number_of_interactions}
                New Infections: {number_of_new_infections}
                       """)
            file.close()
            
    def log_final_stats(self, step_number, number_of_interactions, dead_people, total_vaccinated, total_infections, virus, pop_size, initial_infected, vacc_percentage, vaccine_saves):
        # Open the file in 'a' mode to append final stats logs
        with open(self.file_name, 'a') as file:
            # Log header line
            
            file.write(f"""
                       Final Summary
                       
                    Inputs:
                       Population Size: {pop_size}
                       Initial Vaccinated percentage: {round(vacc_percentage * 100)}%
                       Name of the virus: {virus.name}
                       Mortality rate: {virus.mortality_rate}
                       Reproductive rate of virus: {virus.repro_rate}
                       
                       Percent of population died from virus: {round(pop_size / dead_people)}%
                       
                       Total initial infected: {initial_infected}
                       Total Deaths: {total_dead}
                       Total Infections: {total_infected}
                       Total Death Percent:
                       """)
            
            # Log final stats details
            file.write(f"\t\t{total_dead}\t\t\t\t{total_infected}\t\t\t\t\t{round((population_count / total_dead), 2)}% \n")