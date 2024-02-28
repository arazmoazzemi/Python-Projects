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

```
| Num-Cam KDT | Location                     | Stream Link                                                |
| ----------- | ---------------------------- | ---------------------------------------------------------- |
| Cam-001     | انبار دانه                   | rtsp://admin:mrns@192.168.86.16:554/mode=real&idc=1&ids=1  |
| Cam-002     | پارکینگ مهمانسرا             | rtsp://admin:mrns@192.168.86.12:554/mode=real&idc=1&ids=1  |
| Cam-003     | انبار دانه - تخلیه           | rtsp://admin:mrns@192.168.86.13:554/mode=real&idc=1&ids=1  |
| Cam-004     | ورودی انبار  دانه            | rtsp://admin:mrns@192.168.86.14:554/mode=real&idc=1&ids=1  |
| Cam-005     | باسکول روغن به پلیت          | rtsp://admin:mrns@192.168.86.15:554/mode=real&idc=1&ids=1  |
| Cam-006     | بارگیری فول فت               | rtsp://admin:mrns@192.168.86.67:554/mode=real&idc=1&ids=1  |
| Cam-007     | انبار دانه به ضلع جنوب       | rtsp://admin:mrns@192.168.86.17:554/mode=real&idc=1&ids=1  |
| Cam-008     | دیوار برق به باسکول          | rtsp://admin:mrns@192.168.86.18:554/mode=real&idc=1&ids=1  |
| Cam-009     | خودپرداز به انتظامات         | rtsp://admin:mrns@192.168.86.19:554/mode=real&idc=1&ids=1  |
| Cam-010     | محوطه خدمات                  | rtsp://admin:mrns@192.168.86.20:554/mode=real&idc=1&ids=1  |
| Cam-011     | ورودی انتظامات               | rtsp://admin:mrns@192.168.86.21:554/mode=real&idc=1&ids=1  |
| Cam-012     | پارکینگ رانندگان             | rtsp://admin:mrns@192.168.86.22:554/mode=real&idc=1&ids=1  |
| Cam-013     | محوطه آزمایشگاه به انبار فنی | rtsp://admin:mrns@192.168.86.23:554/mode=real&idc=1&ids=1  |
| Cam-014     | پلیت                         | rtsp://admin:mrns@192.168.86.24:554/mode=real&idc=1&ids=1  |
| Cam-015     | باسکول روغن                  | rtsp://admin:mrns@192.168.86.25:554/mode=real&idc=1&ids=1  |
| Cam-016     | انبار کنجاله - پروژه         | rtsp://admin:mrns@192.168.86.26:554/mode=real&idc=1&ids=1  |
| Cam-017     | پشت دستگاه خودپرداز          | rtsp://admin:mrns@192.168.86.27:554/mode=real&idc=1&ids=1  |
| Cam-018     | دیوار شمال شرق به غرب        | rtsp://admin:mrns@192.168.86.28:554/mode=real&idc=1&ids=1  |
| Cam-019     | کنترل اتاق بار رانندگان      | rtsp://admin:mrns@192.168.86.29:554/mode=real&idc=1&ids=1  |
| Cam-020     | تاسیسات                      | rtsp://admin:mrns@192.168.86.30:554/mode=real&idc=1&ids=1  |
| Cam-021     | دیوار برق به محوطه اصلی      | rtsp://admin:mrns@192.168.86.31:554/mode=real&idc=1&ids=1  |
| Cam-022     | آزمایشگاه به ضایعات          | rtsp://admin:mrns@192.168.86.32:554/mode=real&idc=1&ids=1  |
| Cam-023     | مانیتورینگ به ورودی باسکول   | rtsp://admin:mrns@192.168.86.33:554/mode=real&idc=1&ids=1  |
| Cam-024     | راهروی تاسیسات به تولید      | rtsp://admin:mrns@192.168.86.34:554/mode=real&idc=1&ids=1  |
| Cam-025     | پارکینگ پرسنل                | rtsp://admin:mrns@192.168.86.35:554/mode=real&idc=1&ids=1  |
| Cam-026     | دیوار شمال شرق به پروژه      | rtsp://admin:mrns@192.168.86.36:554/mode=real&idc=1&ids=1  |
| Cam-027     | انبار دانه داخلی             | rtsp://admin:mrns@192.168.86.37:554/mode=real&idc=1&ids=1  |
| Cam-028     | مانیتورینگ به باسکول         | rtsp://admin:mrns@192.168.86.38:554/mode=real&idc=1&ids=1  |
| Cam-029     | دیوار غرب به شمال            | rtsp://admin:mrns@192.168.86.39:554/mode=real&idc=1&ids=1  |
| Cam-030     | اکسترکشن فاز یک              | rtsp://admin:mrns@192.168.86.40:554/mode=real&idc=1&ids=1  |
| Cam-031     | انتظامات به محوطه            | rtsp://admin:mrns@192.168.86.41:554/mode=real&idc=1&ids=1  |
| Cam-032     | انبار دانه به ضایعات         | rtsp://admin:mrns@192.168.86.42:554/mode=real&idc=1&ids=1  |
| Cam-033     | تعمیرات                      | rtsp://admin:mrns@192.168.86.43:554/mode=real&idc=1&ids=1  |
| Cam-034     | مالی                         | rtsp://admin:mrns@192.168.86.44:554/mode=real&idc=1&ids=1  |
| Cam-035     | آزمایشگاه                    | rtsp://admin:mrns@192.168.86.45:554/mode=real&idc=1&ids=1  |
| Cam-036     | لسیتین                       | rtsp://admin:mrns@192.168.86.46:554/mode=real&idc=1&ids=1  |
| Cam-037     | مقدمات فاز یک                | rtsp://admin:mrns@192.168.86.47:554/mode=real&idc=1&ids=1  |
| Cam-038     | مقدمات فاز دو                | rtsp://admin:mrns@192.168.86.48:554/mode=real&idc=1&ids=1  |
| Cam-039     | رستوران                      | rtsp://admin:mrns@192.168.86.49:554/mode=real&idc=1&ids=1  |
| Cam-040     | اکسترکشن فاز یک              | rtsp://admin:mrns@192.168.86.50:554/mode=real&idc=1&ids=1  |
| Cam-041     | انتظامات                     | rtsp://admin:mrns@192.168.86.51:554/mode=real&idc=1&ids=1  |
| Cam-042     | خروج حواله                   | rtsp://admin:mrns@192.168.86.52:554/mode=real&idc=1&ids=1  |
| Cam-043     | اکسترکشن فاز دو - داخل       | rtsp://admin:mrns@192.168.86.53:554/mode=real&idc=1&ids=1  |
| Cam-044     | پست برق - داخل 1             | rtsp://admin:mrns@192.168.86.54:554/mode=real&idc=1&ids=1  |
| Cam-045     | صدور حواله                   | rtsp://admin:mrns@192.168.86.55:554/mode=real&idc=1&ids=1  |
| Cam-046     | رختکن پرسنل تولید            | rtsp://admin:mrns@192.168.86.77:554/mode=real&idc=1&ids=1  |
| Cam-047     | مسئول دفتر                   | rtsp://admin:mrns@192.168.86.57:554/mode=real&idc=1&ids=1  |
| Cam-048     | باسکول به محوطه پارکینگ      | rtsp://admin:mrns@192.168.86.58:554/mode=real&idc=1&ids=1  |
| Cam-049     | پست برق - داخل 2             | rtsp://admin:mrns@192.168.86.59:554/mode=real&idc=1&ids=1  |
| Cam-050     | سالن اداری                   | rtsp://admin:mrns@192.168.86.60:554/mode=real&idc=1&ids=1  |
| Cam-051     | سرور آزمایشکاه               | rtsp://admin:mrns@192.168.86.61:554/mode=real&idc=1&ids=1  |
| Cam-052     | انبار دانه به پروژه          | rtsp://admin:mrns@192.168.86.111:554/mode=real&idc=1&ids=1 |
| Cam-053     | اکسترکشن فازیک  داخلی        | rtsp://admin:mrns@192.168.86.63:554/mode=real&idc=1&ids=1  |
| Cam-054     | ضلع غرب به پشت انبار فنی     | rtsp://admin:mrns@192.168.86.64:554/mode=real&idc=1&ids=1  |
| Cam-055     | برجک جنوب                    | rtsp://admin:mrns@192.168.86.65:554/mode=real&idc=1&ids=1  |
| Cam-056     | برجک جنوب به شمال            | rtsp://admin:mrns@192.168.86.66:554/mode=real&idc=1&ids=1  |
| Cam-057     | انبار دانه به پروژه          | rtsp://admin:mrns@192.168.86.110:554/mode=real&idc=1&ids=1 |
| Cam-058     | باسکول یک داخلی              | rtsp://admin:mrns@192.168.86.68:554/mode=real&idc=1&ids=1  |
| Cam-059     | انبار کنجاله - بارگیری       | rtsp://admin:mrns@192.168.86.69:554/mode=real&idc=1&ids=1  |
| Cam-060     | محوطه تولید                  | rtsp://admin:mrns@192.168.86.70:554/mode=real&idc=1&ids=1  |
| Cam-061     | اکسترکشن فاز 2 به پلیت       | rtsp://admin:mrns@192.168.86.71:554/mode=real&idc=1&ids=1  |
| Cam-062     | خدمات شرق به غرب انبار       | rtsp://admin:mrns@192.168.86.72:554/mode=real&idc=1&ids=1  |
| Cam-063     | رستوران به محوطه             | rtsp://admin:mrns@192.168.86.73:554/mode=real&idc=1&ids=1  |
| Cam-064     | داخل انبار کنجاله            | rtsp://admin:mrns@192.168.86.74:554/mode=real&idc=1&ids=1  |
| Cam-065     | کنفرانس اداری                | rtsp://admin:mrns@192.168.86.62:554/mode=real&idc=1&ids=1  |
| Cam-066     | سالن غذا خوری                | rtsp://admin:mrns@192.168.86.56:554/mode=real&idc=1&ids=1  |
| Cam-067     | دیوار غرب به جنوب            | rtsp://admin:mrns@192.168.86.11:554/mode=real&idc=1&ids=1  |
```


