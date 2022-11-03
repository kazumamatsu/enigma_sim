# enigma_simulater

## Overview

This is 3 rotors enigma simulater
３ローターのエニグマシミュレータです。  

## Quickstart

### Installation
```python
python -m pip install git+https://github.com/kazumamatsu/enigma_sim.git
```

### Using enigma_simulater in a Python script
#### Import module
```python
import enigma
```
#### Setting config 
```python
config = list("AAA")
```

#### Encryption
```python
E = enigma.enigma(config[0], config[1], config[2], seed = 100)
text = list(str.upper("AAA"))
code = []
for t in text:
  print(E.typing(t),　end=' , ')
```
output:
```python
>>> 
```

#### Decoding
```python
E = enigma.enigma(config[0], config[1], config[2], seed = 100)
decode = []
for t in text:
  print(E.typing(t),　end=' , ')
```

output:
```python

```
