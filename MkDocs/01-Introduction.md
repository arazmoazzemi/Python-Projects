# Project documentation with Markdown

_MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. 
Documentation source files are written in Markdown, and configured with a single YAML configuration file. 
Start by reading the introductory tutorial, then check the User Guide for more information._

---
  > Reference: _**<https://www.mkdocs.org/>**_

---
* Install on python:

```python
pip install mkdocs
mkdocs --help
```

* After install, Configure **yml** file:

```
mkdocs new hello-pkg
cd hello-pkg

# Open mkdocs.yml and set below config:

site_name: MkLorum
site_url: https://example.com/
nav:
  - Home: index.md
  - About: about.md



```


