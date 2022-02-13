# Run with .spec file:

```console
pyinstaller my_awesome_app.spec 
```
# Build from scratch

## One-file version:

```console
pyinstaller --name="my_awesome_app" --icon=animal-dog.png --add-data="animal-dog.png:." --onefile app.py
```

## Folder-version:
```console
pyinstaller --name="my_awesome_app" --icon=animal-dog.png --add-data="animal-dog.png:." app.py
```