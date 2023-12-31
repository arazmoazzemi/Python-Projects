## Project Documentation With Markdown

_MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. 
Documentation source files are written in Markdown, and configured with a single YAML configuration file. 
Start by reading the introductory tutorial, then check the User Guide for more information._

---
  > Reference: _**<https://www.mkdocs.org/>**_

---
* Install on python:

```python
>>> pip install mkdocs
```
```bash
$ mkdocs --help
```

* Cretae a new project:
```python
>>> mkdocs new hello-pkg
```

```bash
$ cd hello-pkg
```

* After install, Configure **yml** file:

```
# Open mkdocs.yml and set below config:

site_name: MkLorum
site_url: https://example.com/
nav:
  - Home: index.md
  - About: about.md
```

* Write your markdown code, Into the index.md file,
* For Example:
```
## Hello-Pkgs

### Getting Started

### Installation
```bash
pip install hello-pkg
```

* Run the server:
```
mkdocs serve --dev-addr 127.0.0.1:8001

# default: '127.0.0.1:8000'
# Open your program on <127.0.0.1:8000> address
```



