import sys

try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except:
    sys.exit("ERROR : MODULES MISSING. PROGRAM FAILED TO LOAD.")

try:
    import serverget
    haveServer = True
except:
    haveServer = False

timerInterval = 100

def showSQLVarsDialog():
    SQLVarsDialog.show()

def showTokensDialog():
    TokensDialog.show()

def showSQLDialog():
    SQLDialog.show()

def showDialog():
    Dialog.show()

class Ui_SQLVarsDialog(object):
    def setupUi(self, SQLVarsDialog):
        SQLVarsDialog.setObjectName("SQLVarsDialog")
        SQLVarsDialog.resize(400, 300)
        self.label = QtWidgets.QLabel(SQLVarsDialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 54, 14))
        self.label.setObjectName("label")

        self.retranslateUi(SQLVarsDialog)
        QtCore.QMetaObject.connectSlotsByName(SQLVarsDialog)

    def retranslateUi(self, SQLVarsDialog):
        _translate = QtCore.QCoreApplication.translate
        SQLVarsDialog.setWindowTitle(_translate("SQLVarsDialog", "Dialog"))
        self.label.setText(_translate("SQLVarsDialog", "WIP"))

class Ui_TokensDialog(object):
    def setupUi(self, TokensDialog):
        TokensDialog.setObjectName("TokensDialog")
        TokensDialog.resize(400, 299)
        self.label = QtWidgets.QLabel(TokensDialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 121, 141))
        self.label.setObjectName("label")
        self.consumer_key_plain_text_edit = QtWidgets.QPlainTextEdit(TokensDialog)
        self.consumer_key_plain_text_edit.setGeometry(QtCore.QRect(150, 20, 241, 31))
        self.consumer_key_plain_text_edit.setObjectName("consumer_key_plain_text_edit")
        self.consumer_secret_plain_text_edit = QtWidgets.QPlainTextEdit(TokensDialog)
        self.consumer_secret_plain_text_edit.setGeometry(QtCore.QRect(150, 60, 241, 31))
        self.consumer_secret_plain_text_edit.setObjectName("consumer_secret_plain_text_edit")
        self.acess_token_plain_text_edit = QtWidgets.QPlainTextEdit(TokensDialog)
        self.acess_token_plain_text_edit.setGeometry(QtCore.QRect(150, 100, 241, 31))
        self.acess_token_plain_text_edit.setObjectName("acess_token_plain_text_edit")
        self.acess_token_secret_plain_text_edit = QtWidgets.QPlainTextEdit(TokensDialog)
        self.acess_token_secret_plain_text_edit.setGeometry(QtCore.QRect(150, 140, 241, 31))
        self.acess_token_secret_plain_text_edit.setObjectName("acess_token_secret_plain_text_edit")
        self.pushButton = QtWidgets.QPushButton(TokensDialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 260, 80, 22))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(TokensDialog)
        self.actionsUi(TokensDialog)
        QtCore.QMetaObject.connectSlotsByName(TokensDialog)

    def retranslateUi(self, TokensDialog):
        _translate = QtCore.QCoreApplication.translate
        TokensDialog.setWindowTitle(_translate("TokensDialog", "Tokens"))
        self.label.setText(_translate("TokensDialog", "<html><head/><body><p>consumer_key:<br/></p><p>consumer_secret:</p><p><br/>acess_token:</p><p><br/>acess_token_secret:</p></body></html>"))
        self.pushButton.setText(_translate("TokensDialog", "Apply"))
        self.consumer_key_plain_text_edit.setPlainText(serverget.consumer_key())
        self.consumer_secret_plain_text_edit.setPlainText(serverget.consumer_secret())
        self.acess_token_plain_text_edit.setPlainText(serverget.acess_token())
        self.acess_token_secret_plain_text_edit.setPlainText(serverget.acess_token_secret())

    def actionsUi(self, TokensDialog):
        self.pushButton.clicked.connect(lambda: self.applychanges(TokensDialog))

    def applychanges(self, TokensDialog):
        serverget.update_consumer_key(self.consumer_key_plain_text_edit.toPlainText())
        serverget.update_consumer_secret(self.consumer_secret_plain_text_edit.toPlainText())
        serverget.update_acess_token(self.acess_token_plain_text_edit.toPlainText())
        serverget.update_acess_token_secret(self.acess_token_secret_plain_text_edit.toPlainText())

class Ui_SQLDialog(object):
    def setupUi(self, SQLDialog):
        SQLDialog.setObjectName("SQLDialog")
        SQLDialog.resize(400, 300)
        self.label = QtWidgets.QLabel(SQLDialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 54, 14))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(SQLDialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 10, 121, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(SQLDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 54, 14))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(SQLDialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(90, 50, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton = QtWidgets.QPushButton(SQLDialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 260, 80, 22))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(SQLDialog)
        self.actionsUi(SQLDialog)
        QtCore.QMetaObject.connectSlotsByName(SQLDialog)

    def retranslateUi(self, SQLDialog):
        _translate = QtCore.QCoreApplication.translate
        SQLDialog.setWindowTitle(_translate("SQLDialog", "Editing SQL User"))
        self.label.setText(_translate("SQLDialog", "SQL User:"))
        self.plainTextEdit.setPlainText(_translate("SQLDialog", serverget.sql_user()))
        self.label_2.setText(_translate("SQLDialog", "SQL Pass:"))
        self.plainTextEdit_2.setPlainText(_translate("SQLDialog", serverget.sql_pswd()))
        self.pushButton.setText(_translate("SQLDialog", "Apply"))

    def actionsUi(self, SQLDialog):
        self.pushButton.clicked.connect(lambda: self.applychanges(SQLDialog))

    def applychanges(self, SQLDialog):
        serverget.update_sql_user(self.plainTextEdit.toPlainText())
        serverget.update_sql_pswd(self.plainTextEdit_2.toPlainText())

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 205)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 10, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 321, 141))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("About", "About"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">About</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>Twitter Bot Manager made by hiperbolt </p><p>(github.com/hiperbolt)</p><p><br/></p><p>Made with &lt;3 para a +dd</p><p>Qt 5.12.3, PyQt5, Python 3.7.3 - Frozen on Arch Linux</p></body></html>"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("")
        self.timer = QtCore.QTimer()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 240, 240))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(5)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 70, 80, 22))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 30, 81, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 61, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 131, 111))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 110, 71, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 140, 71, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 170, 71, 22))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(460, 60, 111, 61))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 10, 171, 41))
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 280, 240, 240))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(5)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(90, 20, 54, 14))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 40, 201, 151))
        self.label_6.setObjectName("label_6")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(290, 280, 481, 240))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(5)
        self.frame_3.setObjectName("frame_3")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(30, 20, 101, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(30, 70, 111, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(110, 10, 331, 41))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(110, 60, 331, 41))
        self.label_17.setObjectName("label_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionsUi(MainWindow)
        self.updateWindow(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "Start Bot"))
        self.label.setText(_translate("MainWindow", "Server Status:"))
        self.label_2.setText(_translate("MainWindow", str(serverget.ServerStatus())))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>SQL User:</p><p>Tokens:</p><p>SQL Vars:</p><p><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Edit"))
        self.pushButton_3.setText(_translate("MainWindow", "Edit"))
        self.pushButton_4.setText(_translate("MainWindow", "Edit"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\"># of Tweets Made:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Output:"))
        self.label_6.setText(_translate("MainWindow", ""))
        self.label_14.setText(_translate("MainWindow", "Latest Tweet:"))
        self.label_15.setText(_translate("MainWindow", "Next Tweet:"))
        self.label_16.setText(_translate("MainWindow", "placeholder"))
        self.label_17.setText(_translate("MainWindow", "placeholder"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def actionsUi(self, MainWindow):
        self.pushButton.clicked.connect(lambda: serverget.toggleStatus())
        self.pushButton_2.clicked.connect(showSQLDialog)
        self.pushButton_3.clicked.connect(showTokensDialog)
        self.pushButton_4.clicked.connect(showSQLVarsDialog)
        self.actionQuit.triggered.connect(quit)
        self.actionAbout.triggered.connect(showDialog)
        self.timer.timeout.connect(lambda: self.updateWindow(MainWindow))
        self.timer.start(timerInterval)

    def updateWindow(self, MainWindow):
        if haveServer == True:
            self.label_2.setText(serverget.ServerStatus())
            self.label_6.setText(serverget.errOutput())
            self.label_16.setText(serverget.latestTweet())
            self.label_17.setText(serverget.nextTweet())
        else:
            self.label_6.setText('<html><head/><body><p><span style=" font-size:14pt; color:#ff0000;">Error! No connection</span></p><p><span style=" font-size:14pt; color:#ff0000;"> to server!</span></p></body></html>')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    SQLDialog = QtWidgets.QDialog()
    ui = Ui_SQLDialog()
    ui.setupUi(SQLDialog)
    TokensDialog = QtWidgets.QDialog()
    ui = Ui_TokensDialog()
    ui.setupUi(TokensDialog)
    SQLVarsDialog = QtWidgets.QDialog()
    ui = Ui_SQLVarsDialog()
    ui.setupUi(SQLVarsDialog)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
