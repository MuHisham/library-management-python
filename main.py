import sys
import csv
import shared_data
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import LibrarianMain
from IntroWindow import Ui_MainWindow
from SignUpWindow import Ui_SignUpWindow
from LoginWindow import Ui_LoginWindow

# Add user data to csv file if they are already not there
def addUser(username, password, role):
    does_not_exist = True

    with open('Data/UserDatabase.csv', mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and (row[0] == username or row[1] == password):
                does_not_exist = False
                break
    message = QMessageBox()
    if does_not_exist:
        with open('Data/UserDatabase.csv', mode='a', newline="") as file:
            fwriter = csv.writer(file)
            field = [username, password, role]
            fwriter.writerow(field)
        message.setWindowTitle('Success')
        message.setText("You have created an account. You may close this page.")
    else:
        message.setWindowTitle('Error')
        message.setText("Username or Password already exists. Do you already have an account? Try logging in")
    message.exec_()


# Check user to login
def CheckUser(username, password):
    does_exist = False
    message = QMessageBox()
    message.setWindowTitle('Message')
    with open('Data/UserDatabase.csv', mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and (row[0] == username or row[1] == password):
                does_exist = True
                break

    if does_exist:
        message.setText("Logged in Successfully!")
    else:
        message.setText("Failed to log in! Create an account if you dont have one")
    message.exec_()


# Display SignUp window
class SignUpWindow(QMainWindow, Ui_SignUpWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.checkBox.stateChanged.connect(self.seePassword)
        self.pushButton.clicked.connect(self.retrieveData)

    def retrieveData(self):     # Get user data
        entered_username = self.lineEdit.text()
        entered_password = self.lineEdit_2.text()
        if self.radioButton.isChecked():
            selected_role = 'LT'
        else:
            selected_role = 'No Role'

        addUser(entered_username, entered_password, selected_role)

    def seePassword(self, state):   # See / Not see password
        if state == 2:  # 2 corresponds to the checked state
            self.lineEdit_2.setEchoMode(self.lineEdit_2.Normal)
        else:
            self.lineEdit_2.setEchoMode(self.lineEdit_2.Password)


# Display Login window
class LoginWindow(QMainWindow, Ui_LoginWindow):
    loginSuccessful = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.CheckUser)


    def CheckUser(self):
        entered_username = self.lineEdit.text()
        entered_password = self.lineEdit_2.text()

        does_exist = False
        message = QMessageBox()
        message.setWindowTitle('Message')
        with open('Data/UserDatabase.csv', mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and (row[0] == entered_username and row[1] == entered_password):
                    does_exist = True
                    break

        if does_exist:
            # LibrarianMain.show_librarian_interface()
            global g_entered_username  # Define a global variable
            g_entered_username = entered_username
            shared_data.entered_username = entered_username
            self.loginSuccessful.emit(entered_username)
        else:
            message.setText("Failed to log in! Create an account if you dont have one")
            message.exec_()


# Display Intro window
class LibraryManagement(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(LibraryManagement, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.openLoginWindow)
        self.pushButton_2.clicked.connect(self.openSignUpWindow)

    def openSignUpWindow(self):
        self.signUpWindow = SignUpWindow()  # Create an instance of the sign-up window
        self.signUpWindow.show()

    def openLoginWindow(self):
        self.loginWindow = LoginWindow()
        self.loginWindow.loginSuccessful[str].connect(self.onLoginSuccessful)
        self.loginWindow.show()

    def onLoginSuccessful(self):
        self.hide()
        LibrarianMain.show_librarian_interface()



# Creating the app
def main():
    app = QApplication(sys.argv)
    window = LibraryManagement()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
