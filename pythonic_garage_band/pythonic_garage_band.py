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
