import csv
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QStringListModel
from PyQt5.QtCore import QPropertyAnimation
from LibrarianWindow import Ui_LibrarianWindow
from StudentRecord import addStudentRecord, addStudentToListView
from SearchBooks import addBooks, CustomItemDelegate
import pandas as pd
import shared_data

book_count = 0
student_count = 0
with open('Data/books.csv', 'r', newline='', encoding='utf-8') as file:
    books = csv.reader(file)
    for book in books:
        book_count += 1
with open('Data/students.csv', 'r', newline='', encoding='utf-8') as file:
    students = csv.reader(file)
    for student in students:
        student_count += 1


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LibrarianWindow()
        self.ui.setupUi(self)
        username = shared_data.entered_username
        self.ui.UserName.setText(username)
        self.ui.label_8.setText(str(student_count - 1))
        self.ui.label_9.setText(str(book_count - 1))
        self.ui.Btn_toggle.clicked.connect(lambda: self.toggleMenu(250, True))
        self.initializeBookList()
        self.initializeStudentList()

        # Show Pages on button click
        self.ui.Btn_menu_1.clicked.connect(lambda: self.ui.Pages_widget.setCurrentWidget(self.ui.page_1))
        self.ui.Btn_menu_2.clicked.connect(lambda: self.ui.Pages_widget.setCurrentWidget(self.ui.page_2))
        self.ui.Btn_menu_3.clicked.connect(lambda: self.ui.Pages_widget.setCurrentWidget(self.ui.page_3))
        self.ui.Btn_menu_4.clicked.connect(lambda: self.ui.Pages_widget.setCurrentWidget(self.ui.page_4))

        self.ui.lineEdit.textChanged.connect(self.filterBooks)
        self.ui.search_btn.clicked.connect(self.findBook)

        self.ui.Search_Student.textChanged.connect(self.filterStudents)
        self.ui.search_btn_2.clicked.connect(self.findStudent)

        self.ui.Btn_add.clicked.connect(self.addBooksToDatabase)
        self.ui.Btn_remove.clicked.connect(self.removeBooksFromDatabase)

        self.ui.Add_Student_Btn.clicked.connect(self.addStudentToDatabase)
        self.ui.Remove_Student_Btn.clicked.connect(self.removeStudentFromDatabase)

        self.show()


    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def initializeBookList(self):
        data = addBooks()
        self.addListWidget(data)

    def initializeStudentList(self):
        data = addStudentToListView()
        self.addListWidget2(data)

    def addListWidget(self, items):     # Book List
        model = QStringListModel(items)
        self.ui.listView.setModel(model)
        delegate = CustomItemDelegate()
        self.ui.listView.setItemDelegate(delegate)

    def addListWidget2(self, items):    # Student List
        model = QStringListModel(items)
        self.ui.listView_2.setModel(model)
        delegate = CustomItemDelegate()
        self.ui.listView_2.setItemDelegate(delegate)

    def filterBooks(self):
        filtered_books = []
        books = addBooks()
        text_to_check = self.ui.lineEdit.text()
        for book in books:
            if text_to_check.lower() in book.lower():
                filtered_books.append(book)
        model = QStringListModel(filtered_books)
        self.ui.listView.setModel(model)
        delegate = CustomItemDelegate()
        self.ui.listView.setItemDelegate(delegate)

    def findBook(self):
        text_to_check = self.ui.lineEdit.text()
        books = addBooks()
        message = QMessageBox()
        for book in books:
            if text_to_check.lower() in book.lower():
                message.setText("Book is there!")
                break
            else:
                message.setText("Book Not Found!")
        message.exec_()

    def addBooksToDatabase(self):
        title = self.ui.lineEdit_2.text()
        author = self.ui.lineEdit_3.text()
        isbn = self.ui.lineEdit_4.text()

        with open("Data/books.csv", "a", newline="") as file:
            fwriter = csv.writer(file)
            fwriter.writerow([title, author, isbn])

        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()

    def removeBooksFromDatabase(self):
        title = self.ui.lineEdit_2.text().lower()
        df = pd.read_csv('Data/books.csv')
        try:
            row_to_remove = df[df['title'].str.lower() == title.lower()]
        except Exception as e:
            message = QMessageBox()
            message.setText(e)
            message.exec_()
        df = df.drop(row_to_remove.index)
        df.to_csv('Data/books.csv', index=False)
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()

    def addStudentToDatabase(self):
        name = self.ui.Student_Name.text()
        book = self.ui.Book_Name.text()
        date_borrowed = self.ui.Date_Borrowed.text()
        date_returned = self.ui.Date_Returned.text()
        addStudentRecord(name, book, date_borrowed, date_returned)
        self.ui.Student_Name.clear()
        self.ui.Book_Name.clear()
        self.ui.Date_Borrowed.clear()
        self.ui.Date_Returned.clear()

    def filterStudents(self):
        filtered_students = []
        students = addStudentToListView()
        text_to_check = self.ui.Search_Student.text()
        for student in students:
            if text_to_check.lower() in student.lower():
                filtered_students.append(student)
        model = QStringListModel(filtered_students)
        self.ui.listView_2.setModel(model)
        delegate = CustomItemDelegate()
        self.ui.listView_2.setItemDelegate(delegate)

    def findStudent(self):
        text_to_check = self.ui.Search_Student.text()
        students = addStudentToListView()
        message = QMessageBox()
        if len(students) != 0:
            for student in students:
                if text_to_check.lower() in student.lower():
                    message.setText("Record Found!")
                    break
                else:
                    message.setText("Record Not Found!")
        else:
            message.setText("No Student Records Found!")
        message.exec_()

    def removeStudentFromDatabase(self):
        name = self.ui.Student_Name.text().lower()
        df = pd.read_csv('Data/students.csv')
        try:
            row_to_remove = df[df['Name'].str.lower() == name.lower()]
        except Exception as e:
            message = QMessageBox()
            message.setText(e)
            message.exec_()
        df = df.drop(row_to_remove.index)
        df.to_csv('Data/students.csv', index=False)
        self.ui.Student_Name.clear()
        self.ui.Book_Name.clear()
        self.ui.Date_Borrowed.clear()
        self.ui.Date_Returned.clear()


def show_librarian_interface():
    app = QApplication.instance()  # Get the existing QApplication instance
    if not app:  # If no instance exists, create a new one (for safety)
        app = QApplication([])
    librarian_window = MainWindow()
    librarian_window.show()
    app.exec_()


if __name__ == "__main__":
    show_librarian_interface()
