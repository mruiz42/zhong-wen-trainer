from py.setupUi.DeckNamePrompt import *
from PySide2 import QtWidgets
from py.utilities.SQLTools import *

class DeckNamePrompt(QtWidgets.QDialog):

    def __init__(self, mainWindow, parent=None):
        super(DeckNamePrompt, self).__init__(parent)
        self.DNPD  = Ui_DeckNamePromptDialog()
        self.DNPD.setupUi(self)
        self.mainWindow = mainWindow
        # ADD
        self.DNPD.buttonBox.accepted.connect(self.acceptInput)

    def acceptInput(self):
        table_name = self.DNPD.lineEdit.text()
        print("Creating table: ", table_name)
        db = SqlTools()
        db.openDatabase('../data/vocab.db')
        db.createTable(table_name)
        db.closeDatabase()
        self.mainWindow.refreshTableList()
