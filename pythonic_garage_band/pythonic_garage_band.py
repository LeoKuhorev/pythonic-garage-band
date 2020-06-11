import sys


def str_to_class(classname: str) -> object:
    """Parses passed in classname from string
    CREDIT: https://stackoverflow.com/questions/1176136/convert-string-to-python-class-object

    Args:
        classname (str): Class Name

    Returns:
        object: Class
    """
    return getattr(sys.modules[__name__], classname)


class Musician:
    """Class Musician"""

    members = []

    def __init__(self, name: str, instrument: str = 'Music instrument') -> None:
        """Class constructor

        Args:
            name (str): Musician name
            instrument (str, optional): The instrument this musician plays on. Defaults to 'Music instrument'.
        """
        self.name = name
        self.instrument = instrument
        self.__class__.members.append(self)

    def get_instrument(self) -> str:
        """Returns what instrument musician plays on

        Returns:
            str: Instrument that this musician plays on
        """
        return f'{self.instrument}'

    def play_solo(self) -> str:
        """Returns message containing the name of the musician and the instrument they play on

        Returns:
            str: Name of the musician and the instrument they play on
        """
        return f'{self.name} plays solo on {self.instrument}'

    def __repr__(self) -> str:
        """How this class will be represented when inspected in the console or inside of repr() method

        Returns:
            str: Shows the way how the object can be recreated in Python
        """
        return f'{self.__class__.__name__}({self.name})'

    def __str__(self):
        """How this class will be represented when printed or inside of str() method

        Returns:
            str: Human readable class representation
        """
        return f'Name: {self.name}, Plays: {self.instrument}'


class Guitarist(Musician):
    """Guitarist class (extended after Musician)"""

    def __init__(self, name: str) -> None:
        """Class constructor. Sets Guitar as a default instrument

        Args:
            name (str): Guitarist name
        """
        super().__init__(name)
        self.instrument = 'Guitar'


class Bassist(Musician):
    """Bassist class (extended after Musician)"""

    def __init__(self, name):
        """Class constructor. Sets Bass as a default instrument

        Args:
            name (str): Bassist name
        """
        super().__init__(name)
        self.instrument = 'Bass'


class Drummer(Musician):
    """Drummer class (extended after Musician)"""

    def __init__(self, name):
        """Class constructor. Sets Drum as a default instrument

        Args:
            name (str): Drummer name
        """
        super().__init__(name)
        self.instrument = 'Drums'


class Band:
    """Band class"""

    all_bands = []

    def __init__(self, name: str, *args: dict) -> None:
        """Class constructor

        Args:
            name (str): Band name
            args (dict, optional): Musician instances
        """
        self.name = name
        self.members = list(args)
        self.__class__.all_bands.append(self)

    def play_solos(self) -> str:
        """Displays message that represents solo for each band member

        Returns:
            str: Message that represents solo for each band member
        """
        return '\n'.join(m.play_solo() for m in self.members)

    def to_list(self) -> list:
        """Returns a list of all previously created Band class instances

        Returns:
            list: List of all previously created Band class instances
        """
        return self.all_bands

    def __repr__(self):
        """How this class will be represented when inspected in the console or inside of repr() method

        Returns:
            str: Shows the way how the object can be recreated in Python
        """
        names = ', '.join(repr(m) for m in self.members)
        return f'{self.__class__.__name__}({self.name}, {names})'

    def __str__(self):
        """How this class will be represented when printed or inside of str() method

        Returns:
            str: Human readable class representation
        """
        names = ', '.join(f'{m.name} ({m.instrument})' for m in self.members)
        return f'Band name: {self.name}, Band members: {names}'

    @staticmethod
    def create_from_data(filepath: str) -> object:
        """Creates a new Band instance from the provided file.
        Expeted file structure:
        1st line - Name of the band
        2nd..nth lines - MusicianClass, musician_name (e.g. Guitarist, Julie)


        Args:
            filepath (str): file to read a new band from

        Returns:
            object: New instance of Band class
        """
        try:
            with open(filepath, 'r') as f:
                name = f.readline().strip('\n')
                new_band = Band(name)

                member = f.readline()
                while member:
                    try:
                        member = member.split(', ')
                        class_name = str_to_class(member[0])
                        member_name = member[1].strip('\n')
                        new_band.members.append(class_name(member_name))
                        member = f.readline()
                    except Exception as err:
                        print(
                            f'There\'s been an error while processing your request. \nDetails: {err}')

            return new_band
        except IOError as err:
            print(f'File {filepath} couldn\'t be read: {err}')

