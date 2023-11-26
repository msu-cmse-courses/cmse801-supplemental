import datetime

class Animal():
    '''
        This is an Animal class, used to store information about animals in the ZOO.
        Or for characters in the Madagascar movies.
    '''
    def __init__(self, kind, name, to_zoo='', area=100, staff=1):
        ''' Initialize the object Building. '''
        self.kind = kind
        self.name = name
        self.brought_to_zoo = to_zoo
        self.required_area = area       # required area [m2]
        # required number of staff members per animal; can be fraction, e.g. 0.2 means one
        # zookeeper can take care of 5 animals
        self.required_staff = staff
        return

    def set_name(self, name):
        ''' Set animal's name. '''
        self.name = name
        return

    def set_kind(self, kind):
        ''' Set animal's kind. '''
        self.kind = kind
        return

    def set_arrive_to_zoo(self, to_zoo):
        ''' Set animal's date delivered to the ZOO. '''
        self.brought_to_zoo = to_zoo
        return

    def set_required_area(self, area):
        ''' Set average required area by single a animal. '''
        self.required_area = area
        return

    def set_number_keepers(self, num):
        ''' Set the number of ZOO keepers required by a single animal. '''
        self.required_staff = num
        return

    def get_name(self):
        ''' Return animal's nick name. '''
        return self.name

    def get_kind(self):
        ''' Return animal's kind. '''
        return self.kind

    def get_arrive_to_zoo(self):
        ''' Return animal's date delivered to the ZOO. '''
        return self.brought_to_zoo

    def get_required_area(self):
        ''' Return average required area by single animal. '''
        return self.required_area

    def get_number_keepers(self):
        ''' Return the number of ZOO keepers required by a single animal. '''
        return self.required_staff

    def days_in_zoo(self):
        '''
            Return the number of days the animal is in the zoo.
        '''
        if self.brought_to_zoo == '':
            print("ERROR: the date when {0} arrived to ZOO is empty. Set the date.".format(self.name))
            return -1

        try:
            # convert string 'YYYY-MM-DD' into three strings, that are used do create a date
            # object when animal arrived to the zoo
            y, m, d = self.brought_to_zoo.split("-")
            brought_in = datetime.date(int(y), int(m), int(d))
        except ValueError:
            print("ERROR: current date {0} is in wrong format. The correct format is YYYY-MM-DD.".format(self.brought_to_zoo))
            return -1

        # finally all is OK and we can compute number of days
        today = datetime.date.today()
        # this gives us 'timedelta' object
        days_in_zoo = today - brought_in

        return days_in_zoo.days
    
class Zebra(Animal):
    def __init__(self, name):
        ''' Initialize Zebra class. All we need now is the animal nick name. '''
        # fill in missing code
        # this calls initialization of Animal class and setting the animal to given 'name'
        super().__init__(self, name)
        # in lines below we defined attribute values for lions
        self.kind = 'zebra'
        self.required_area = 100
        self.required_staff = 1
        return

class Penguin(Animal):
    def __init__(self, name):
        ''' Initialize Zebra class. All we need now is the animal nick name. '''
        # fill in missing code
        # this calls initialization of Animal class and setting the animal to given 'name'
        super().__init__(self, name)
        # in lines below we defined attribute values for lions
        self.kind = 'penguin'
        self.required_area = 300
        self.required_staff = 0.5
        return

class Lion(Animal):
    '''
        This is a Lion class, used to store information about lions.
    '''
    def __init__(self, name):
        ''' Initialize Lion class. All we need now is the animal nick name. '''
        # this calls initialization of Animal class and setting the animal to given 'name'
        super().__init__(self, name)
        # in lines below we defined attribute values for lions
        self.kind = 'lion'              # this class is only for lions, so we can define animal 'kind' as lion
        # default required area: ENTER VALUE (arbitrary one or one you used in Day 19 in-class assignment)
        self.required_area = 600
        # set default number of ZOO keepers for lions: ENTER VALUE (arbitrary one or one you used in Day 19 in-class assignment)
        self.required_staff = 2
        return
