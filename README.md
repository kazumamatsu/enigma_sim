# enigma_simulater
## Description
３ローターのエニグマシミュレータです。  
This is 3 rotors enigma simulater


## Quickstart
### Installation
```python
python -m pip install git+https://github.com/kazumamatsu/enigma_sim.git
```

### Using enigma_simulater in a Python script
```python
import enigma
```

```python
setting = list("AAA")
E = enigma.enigma(setting[0], setting[1], setting[2])
text = list(str.upper("AAA"))
print(text)
code = []
for t in text:
  code.append(E.typing(t))
  E.print(ptype = 0)
print(code)
```
