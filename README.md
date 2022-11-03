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
1. Import module
```python
import enigma
```
1. 


1. Setting config
1.  
```python
config = list("AAA")
```

. Encryption
```python
E = enigma.enigma(config[0], config[1], config[2], seed = 100)
text = list(str.upper("AAA"))
print(text)
code = []
for t in text:
  code.append(E.typing(t))
  E.print(ptype = 0)
print(code)
```
output:
```python
```

4. Decoding
```python
E = enigma.enigma(config[0], config[1], config[2], seed = 100)
decode = []
for t in code:
  decode.append(E.typing(t))
  E.print(ptype = 0)
print(decode)
```
