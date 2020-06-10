class Musician:

    members = []

    def __init__(self, name: str):
        self.name = name
        self.instrument = 'Instrument'
        self.members.append(self)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'name: {self.name}, instrument: {self.instrument}'

    def get_instrument(self):
        return f'{self.instrument}'

    def play_solo(self):
        return f'{self.name} plays {self.instrument}'

    @property
    def get_members(self):
        return members


class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name)
        self.instrument = 'Guitar'


class Bassist(Musician):

    def __init__(self, name):
        super().__init__(name)
        self.instrument = 'Bass'


class Drummer(Musician):

    def __init__(self, name):
        super().__init__(name)
        self.instrument = 'Drums'


class Band:

    prev = []

    def __init__(self, name, *args):
        self.name = name
        self.members = args
        self.prev.append(self)

    def play_solos(self):
        return '\n'.join(m.play_solo() for m in self.members)

    def to_list(self):
        return self.prev

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()


g = Guitarist('jonh')
d = Drummer('Jack')
b = Bassist('Jane')
a = Guitarist('Dan')

band = Band('zzz', d, g)
band2 = Band('www', b, a)

print('all', d.members, '\n')
print('band', band.members, '\n')
print('band2', band2.members, '\n')

print(band.play_solos())

print(band.prev)
