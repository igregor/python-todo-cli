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

running tests:

```
python3 -m pytest tests/
```

add todo

```
(venv) $ python3 -m rptodo add Get some milk -p 1
to-do: "Get some milk." was added with priority: 1

(venv) $ python3 -m rptodo add Clean the house --priority 3
to-do: "Clean the house." was added with priority: 3

(venv) $ python3 -m rptodo add Wash the car
to-do: "Wash the car." was added with priority: 2

(venv) $ python3 -m rptodo add Go for a walk -p 5
Usage: rptodo add [OPTIONS] DESCRIPTION...
Try 'rptodo add --help' for help.

Error: Invalid value for '--priority' / '-p': 5 is not in the valid range...
```
