#!/usr/bin/env python
import os, sys
sys.path.append(os.path.abspath('.'))
import pqaut.server as pqaut

import PyQt5.Qt as Qt


class Root(Qt.QWidget):

    def __init__(self):
        super(Qt.QWidget, self).__init__()
        widget = Qt.QWidget(self)
        widget.automation_id = "custom_widget"
        widget.setGeometry(0,0,400,100)
        self.show()


pqaut.start_automation_server()
app = Qt.QApplication(sys.argv)
root = Root()
sys.exit(app.exec_())
