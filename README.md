# Currency converter GUI with principles

MK's solution to assignment 5.

## Info

The whole solution is sensibly split into distinct components, each expressed as a seprate file in `src` module.
There are seperate files for creating GUI layout, downloading currency data or loading it from previously saved file.

There are **no** strange functions that modify the class attributes from outside of it, no references to some global variables.

## Running app
To run the application, follow some good principles and first create virtual env:
```bash
uv venv venv
```

or in a more standard way (if you don't have uv installed):
```
python -m venv venv
```

Next activate the environment and install the required packages:
```bash
uv pip intall -r requirements.txt
```

or if you prefer it slow:
```bash
pip install -r requirements.txt
```

Finally type:
```bash
python main.py
```
