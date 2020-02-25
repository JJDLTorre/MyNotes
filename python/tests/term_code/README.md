# A simple unit test example using Python on Visual Studio Code

## Goal of this example
Simple step to create tests and run them as you code.

## Create Unit Test

### Try Doc Test first

```
python3 -m doctest term_code.py
```

### Ultimatly you want to move the doc test into thier own tests
Create the tests into ___term_code_test.py___.

### Run unittest
```
$ /usr/local/bin/python3 -m unittest term_code_test.py 
```

## Using and installing PyTest

### install
```
$ /usr/local/bin/python3 -m pip install pytest
```

### Run
```
$ /usr/local/bin/python3 -m pytest
```

