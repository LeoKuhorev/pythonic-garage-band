from pythonic_garage_band.pythonic_garage_band import Musician


class TestMusician:
    musician = Musician('TestMusician')

    def test_str(self):
        assert self.musician.name == 'TestMusician'

    def test_get_instrument(self):
        assert self.musician.instrument == 'Instrument'

    def test_play_solo(self):
        assert self.musician.play_solo() == 'Plays Instrument'
