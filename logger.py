class Logger(object):
    def __init__(self, file_name):
        # Initialize the file name and interaction logs list
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        # Open the file in 'w' mode to write metadata
        with open(self.file_name, 'w') as file:
            # Write metadata information in tab-delimited format
            file.write(f"Population Size\tVaccination Percentage\tVirus Name\tMortality Rate\tBasic Reproduction Number\n")
            file.write(f"{pop_size}\t\t\t\t{vacc_percentage}\t\t\t\t\t{virus_name}\t\t{mortality_rate}\t\t\t{basic_repro_num}\n")

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        # Open the file in 'a' mode to append interaction logs
        with open(self.file_name, 'a') as file:
            # Log header
            file.write(f"\nStep Number\tInteractions\tNew Infections\n")
            
            # Log interaction details
            file.write(f"{step_number}\t\t\t{number_of_interactions}\t\t\t\t{number_of_new_infections}\n")

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        # Open the file in 'a' mode to append infection survival logs
        with open(self.file_name, 'a') as file:
            # Log header line
            file.write(f"Step Number\tPopulation Count\tNew Fatalities\n")
            
            # Log infection survival details
            file.write(f"{step_number}\t\t\t{population_count}\t\t\t\t{number_of_new_fatalities}\n\n")

    def log_time_step(self, time_step_number):
        # Open the file in 'a' mode to append time step logs
        with open(self.file_name, 'a') as file:
            # Log header line
            file.write(f"Time Step Number\n")
            
            # Log time step details
            file.write(f"{time_step_number}\n")