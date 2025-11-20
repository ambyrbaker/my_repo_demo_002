class Student:

    def __init__(self, fname, lname, id, energy_level):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = energy_level

    def __str__(self):
        return f"lname: id {id}"

    def __greeting__(self):
        return f"{self.fname} says 'Hello!' "

    def __take_exam__(self, energy_level):
        energy_level -= 1

    def __get_energy_level__(self, energy_level):
        return self.energy_level


