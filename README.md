# enigma_simulater

## Overview

This is 3 rotors enigma simulater
３ローターのエニグマシミュレータです。  

## Quickstart

### Installation
In Python:
```python
python -m pip install git+https://github.com/kazumamatsu/enigma_sim.git
```
In IPython:
```python
!pip install git+https://github.com/kazumamatsu/enigma_sim.git
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
text = list(str.upper(input()))
code = []
for t in text:
  code.append(E.typing(t))
print(text)
print(code)
```
input:
```python
AAA
```

output:
```python
>>> ['A', 'A', 'A']
>>> ['Y', 'U', 'I']
```

#### Decoding
```python
E = enigma.enigma(config[0], config[1], config[2], seed = 100)
decode = []
for t in code:
  decode.append(E.typing(t))
print(decode)
```

output:
```python
>>> ['A', 'A', 'A']
```
