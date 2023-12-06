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

    def log_interactions(self, step_number, total_dead, number_of_interactions, total_infections):
        # Open the file in 'a' mode to append interaction logs
        with open(self.file_name, 'a') as file:
            # Log header
            file.write(f"""
                Step Number: {step_number}
                Interactions: {number_of_interactions}
                Current Infections: {total_infections}
                Current Deaths: {total_dead}
                       """)
            file.close()
            
    def log_final_stats(self, step_number, number_of_interactions, dead_people, total_vaccinated, total_infections, virus, pop_size, initial_infected, vacc_percentage, vaccine_saves, total_dead, total_infected):
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
                       Percent of population infected before burnout: {round(total_infections / pop_size)}%
                       Number of people saved by vaccine: {vaccine_saves}
                       
                       
                       Total steps: {step_number}
                       Total interactions: {number_of_interactions}
                       Total vaccinated: {total_vaccinated}
                       Total Deaths: {total_dead}
                       Total Infections: {total_infected}
                       """)
            file.close()