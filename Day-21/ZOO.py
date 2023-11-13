
class ZOO():
    '''
        Class for ZOO object.
    '''
    def __init__(self, name):
        ''' Initialize the ZOO object. '''
        # name of the ZOO
        self.name = name
        # we are using dictionaries for animals and personnel
        self.animals = {}
        self.zookeepers = {}
        return

    def add_animal(self, animal):
        ''' Adds an animal to the zoo. '''
        # we use animal's name as a key in the dictionary
        name = animal.get_name()
        self.animals[name] = animal
        return 

    def add(self, animal):
        ''' Shorter name of function to add animals to the ZOO. '''
        self.add_animal(animal)
        return

    def get_animals(self):
        ''' Return all animals in the zoo.'''
        return self.animals

    def remove(self, name):
        ''' Remove animal from the ZOO for given name. If the name does not exist, error is printed. '''
        if name in self.animals:
            # yes, animal with given name is in the ZOO
            del self.animals[name]
        else:
            print("Animal with given name is not in", self.name, "ZOO.")
        
        return

    def get_animal_names(self, sort=False):
        ''' Return animal names in the ZOO. Return sorted names if parameters sorted==True'''
        names = []
        
        for key in self.animals.keys():
            # get animal names and store them into list
            names.append(self.animals[key].get_name())

        if sort == True:
            # we have to return sorted names; so sort the names
            names = sorted(names)

        return names

    def number_animals(self):
        ''' Return number of animals in the ZOO.'''
        return len(self.animals)

    def total_area(self):
        ''' Return the total ZOO area to host all animals defined in the object. '''
        area = 0

        for key in self.animals:
            # get area for all animals in the zoo
            area += self.animals[key].get_required_area()

        return area

    def add_person(self, person):
        ''' Adds a person to the zoo. '''
        # we use person's name as a key in the dictionary
        name = person.get_name()
        self.zookeepers[name] = person
        return

    def number_zookeepers(self):
        ''' Return number of zookeepers in the zoo.'''
        return len(self.zookeepers)

    def get_zookeepers(self):
        ''' Return zookeepers in the zoo.'''
        return self.zookeepers

    def get_person_names(self, sort=False):
        ''' Return personnel names in the ZOO. Return sorted names if parameters sorted==True'''
        names = []
        
        for key in self.zookeepers.keys():
            # get persons names and store them into list
            names.append(self.zookeepers[key].get_name())

        if sort == True:
            # we have to return sorted names; so sort the names
            names = sorted(names)

        return names
