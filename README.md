# MadLib Game

_Author: Leo Kukharau_

---

## Description

This is a Python module that provides a number of classes to model a Band made up of different kinds of musicians like Guitarist,Bassist, and Drummer. Musician base class used to handle common functionality which particular kinds of musicians will inherit.

---

### Getting Started

Clone this repository to your local machine.

```
$ git clone [repo clone url here]
```

### To run the program from VS Code:

Select `File` -> `Open` -> `Project/Solution`

Next navigate to the location you cloned the Repository.

Double click on the `pythonic_garage_band` directory.

Then select and open `pythonic_garage_band.py`

### API

_*class Musician*_: creates instances of the musicians  
_*class Bassist(Musician)*_: creates instances of the bassists, inherits properties of Musician class  
_*class Guitarist(Musician)*_: creates instances of the guitarists, inherits properties of Musician class  
_*class Drummer(Musician)*_: creates instances of the drummers, inherits properties of Musician class  
_*class Band*_: creates instances of the band, has a staitc class that allows to create an instance from the provided text file

### Change Log

1.0: _Added basic functionality_ - 06/10/2020

[Link to PR](https://github.com/LeoKuhorev/pythonic-garage-band/pull/2)
