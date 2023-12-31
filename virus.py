class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        # Define the attributes of virus
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate
        
# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    print(virus.name)
    print(virus.repro_rate)
    print(virus.mortality_rate)
        
    # Will throw an error without the following properties:    
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3
