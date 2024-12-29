# Python setup

## Python Virtual Environment

### Create Virtual Environment under a Folder
```
python3 -m pip install tutorial_env
```

### Create Virtual Environment in same location .
```
python3 -m pip install .
```


### Overwrite Pip url for virutal env
create ''pip.conf'' file in same location and add the content

[pip_Link](https://packaging.python.org/en/latest/tutorials/installing-packages/)
[pip_Link](https://pip.pypa.io/en/stable/topics/configuration/)

```
[global]
index-url = https://pypi.org/simple
timeout = 60
```

### To install a package using single line command

```
pip install PyYAML --index-url https://pypi.org/simple
```