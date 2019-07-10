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

```python
from jokegetter import jokegetter

jokegetter.get_joke()
```
