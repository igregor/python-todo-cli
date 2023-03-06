# Steps

## Init

venv

```
$ python3 -m venv ./venv
$ source venv/bin/activate
```

deps

```
python3 -m pip install typer==0.3.2 colorama==0.4.4 shellingham==1.4.0
python3 -m pip install pytest==6.2.4

# install
python3 -m pip install -r requirements.txt
```

you can execute this once you added a `__main__.py`

```
python3 -m igregor_todo --help
python3 -m igregor_todo -v
python3 -m igregor_todo
```
