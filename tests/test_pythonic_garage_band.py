from pythonic_garage_band.pythonic_garage_band import (Band, Bassist, Drummer,
                                                       Guitarist, Musician)


class TestMusician:
    musician = Musician('John')

    def test_name(self):
        assert self.musician.name == 'John'

    def test_get_instrument(self):
        assert self.musician.get_instrument() == 'Music instrument'

    def test_play_solo(self):
        assert self.musician.play_solo() == 'John plays solo on Music instrument'

    def test_play_repr(self):
        assert repr(self.musician) == 'Musician(John)'

    def test_play_str(self):
        assert str(self.musician) == 'Name: John, Plays: Music instrument'


class TestGuitarist:

    guitarist = Guitarist('John')

    def test_name(self):
        assert self.guitarist.name == 'John'

    def test_get_instrument(self):
        assert self.guitarist.get_instrument() == 'Guitar'

    def test_play_solo(self):
        assert self.guitarist.play_solo() == 'John plays solo on Guitar'

    def test_play_repr(self):
        assert repr(self.guitarist) == 'Guitarist(John)'

    def test_play_str(self):
        assert str(self.guitarist) == 'Name: John, Plays: Guitar'


class TestBassist:

    bassist = Bassist('John')

    def test_name(self):
        assert self.bassist.name == 'John'

    def test_get_instrument(self):
        assert self.bassist.get_instrument() == 'Bass'

    def test_play_solo(self):
        assert self.bassist.play_solo() == 'John plays solo on Bass'

    def test_play_repr(self):
        assert repr(self.bassist) == 'Bassist(John)'

    def test_play_str(self):
        assert str(self.bassist) == 'Name: John, Plays: Bass'


class TestDrummer:

    drummer = Drummer('John')

    def test_name(self):
        assert self.drummer.name == 'John'

    def test_get_instrument(self):
        assert self.drummer.get_instrument() == 'Drums'

    def test_play_solo(self):
        assert self.drummer.play_solo() == 'John plays solo on Drums'

    def test_play_repr(self):
        assert repr(self.drummer) == 'Drummer(John)'

    def test_play_str(self):
        assert str(self.drummer) == 'Name: John, Plays: Drums'


class TestBand:

    g = Guitarist('John')
    b = Bassist('Jake')
    d = Drummer('Jane')

    band = Band('Test Band', g, b, d)
    band_1 = Band('Test Band 1', b)

    def test_name(self):
        assert self.band.name == 'Test Band'

    def test_members_1(self):
        assert type(self.band.members) == list

    def test_members_2(self):
        assert self.band.members == [self.g, self.b, self.d]

    def test_play_solos(self):
        assert self.band.play_solos(
        ) == 'John plays solo on Guitar\nJake plays solo on Bass\nJane plays solo on Drums'

    def test_repr(self):
        assert repr(
            self.band) == f'Band(Test Band, Guitarist(John), Bassist(Jake), Drummer(Jane))'

    def test_str(self):
        assert str(
            self.band) == 'Band name: Test Band, Band members: John (Guitar), Jake (Bass), Jane (Drums)'

    def test_to_list_1(self):
        assert type(self.band.to_list()) == list

    def test_to_list_2(self):
        assert self.band.to_list() == [self.band, self.band_1]
