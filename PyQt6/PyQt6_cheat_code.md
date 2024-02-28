---
### PyQt6 Cheat Codes
---

### *[Download QT Designer](https://build-system.fman.io/qt-designer-download)*

### Install
```
pip install pyqt6
```

### Simple window
```
from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.show()

sys.exit(app.exec())
```



