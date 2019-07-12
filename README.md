# Joke getter

This python package allows to get a joke. It uses [JokeAPI](https://sv443.net/jokeapi).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the package.

```bash
pip install jokegetter
```

Or install the package [from a CVS url](https://pip.pypa.io/en/stable/reference/pip_install/#git).

```bash
pip install git+https://github.com/afaucon/jokegetter.git@v1.0.0
```

## Usage

As a module:

```python
from jokegetter import jokegetter

joke = jokegetter.get_joke()
print(joke)
```

or

```bash
>>> from jokegetter import jokegetter
>>> jokegetter.get_joke()
"- What is a dying programmer's last program?\n- Goodbye, world!"
>>> jokegetter.get_joke()
"- Why do Java programmers hate communism?\n- They don't want to live in a classless society."
```

As a command line:

```bash
$ python -m jokegetter
```
