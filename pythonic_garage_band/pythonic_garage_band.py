class Musician:

    def __init__(self, name: str):
        self.name = name
        self.instrument = 'Instrument'

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return {'name': self.name}

    def get_instrument(self):
        return f'{self.instrument}'

    def play_solo(self):
        return f'Plays {self.instrument}'
