from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LibrarianWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 300))
        MainWindow.setStyleSheet("background-color: rgb(244, 238, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TopBar = QtWidgets.QFrame(self.centralwidget)
        self.TopBar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.TopBar.setStyleSheet("background-color: rgb(66, 72, 116);")
        self.TopBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TopBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TopBar.setObjectName("TopBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.TopBar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.TopBar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 50))
        self.frame_toggle.setStyleSheet("background-color: rgb(166, 177, 225);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_toggle.sizePolicy().hasHeightForWidth())
        self.Btn_toggle.setSizePolicy(sizePolicy)
        self.Btn_toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid\n"
"")
        self.Btn_toggle.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/toggle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_toggle.setIcon(icon)
        self.Btn_toggle.setIconSize(QtCore.QSize(30, 30))
        self.Btn_toggle.setObjectName("Btn_toggle")
        self.verticalLayout_2.addWidget(self.Btn_toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.TopBar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.TopBar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(18, 18, 18);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menu = QtWidgets.QFrame(self.frame_left_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_top_menu.sizePolicy().hasHeightForWidth())
        self.frame_top_menu.setSizePolicy(sizePolicy)
        self.frame_top_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menu.setObjectName("frame_top_menu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menu)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Btn_menu_1 = QtWidgets.QPushButton(self.frame_top_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_menu_1.sizePolicy().hasHeightForWidth())
        self.Btn_menu_1.setSizePolicy(sizePolicy)
        self.Btn_menu_1.setMinimumSize(QtCore.QSize(70, 70))
        self.Btn_menu_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(220, 214, 247);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(166, 177, 225);\n"
"}")
        self.Btn_menu_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_menu_1.setIcon(icon1)
        self.Btn_menu_1.setIconSize(QtCore.QSize(30, 30))
        self.Btn_menu_1.setFlat(False)
        self.Btn_menu_1.setObjectName("Btn_menu_1")
        self.verticalLayout_4.addWidget(self.Btn_menu_1)
        self.Btn_menu_2 = QtWidgets.QPushButton(self.frame_top_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_menu_2.sizePolicy().hasHeightForWidth())
        self.Btn_menu_2.setSizePolicy(sizePolicy)
        self.Btn_menu_2.setMinimumSize(QtCore.QSize(0, 70))
        self.Btn_menu_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(220, 214, 247);\n"
"    border: 0px solid\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(166, 177, 225);\n"
"}")
        self.Btn_menu_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/research.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_menu_2.setIcon(icon2)
        self.Btn_menu_2.setIconSize(QtCore.QSize(30, 30))
        self.Btn_menu_2.setObjectName("Btn_menu_2")
        self.verticalLayout_4.addWidget(self.Btn_menu_2)
        self.Btn_menu_3 = QtWidgets.QPushButton(self.frame_top_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_menu_3.sizePolicy().hasHeightForWidth())
        self.Btn_menu_3.setSizePolicy(sizePolicy)
        self.Btn_menu_3.setMinimumSize(QtCore.QSize(0, 70))
        self.Btn_menu_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(220, 214, 247);\n"
"    border: 0px solid\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(166, 177, 225);\n"
"}")
        self.Btn_menu_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_menu_3.setIcon(icon3)
        self.Btn_menu_3.setIconSize(QtCore.QSize(30, 30))
        self.Btn_menu_3.setObjectName("Btn_menu_3")
        self.verticalLayout_4.addWidget(self.Btn_menu_3)
        self.Btn_menu_4 = QtWidgets.QPushButton(self.frame_top_menu)
        self.Btn_menu_4.setMinimumSize(QtCore.QSize(0, 70))
        self.Btn_menu_4.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(220, 214, 247);\n"
"    border: 0px solid\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(166, 177, 225);\n"
"}")
        self.Btn_menu_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/borrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_menu_4.setIcon(icon4)
        self.Btn_menu_4.setIconSize(QtCore.QSize(30, 30))
        self.Btn_menu_4.setObjectName("Btn_menu_4")
        self.verticalLayout_4.addWidget(self.Btn_menu_4)
        self.Btn_menu_2.raise_()
        self.Btn_menu_3.raise_()
        self.Btn_menu_4.raise_()
        self.Btn_menu_1.raise_()
        self.verticalLayout_3.addWidget(self.frame_top_menu)
        self.horizontalLayout_2.addWidget(self.frame_left_menu, 0, QtCore.Qt.AlignTop)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Pages_widget = QtWidgets.QStackedWidget(self.frame_pages)
        self.Pages_widget.setObjectName("Pages_widget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.Welcome = QtWidgets.QLabel(self.page_1)
        self.Welcome.setGeometry(QtCore.QRect(40, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.Welcome.setFont(font)
        self.Welcome.setStyleSheet("color: rgb(166, 177, 225);")
        self.Welcome.setObjectName("Welcome")
        self.UserName = QtWidgets.QLabel(self.page_1)
        self.UserName.setGeometry(QtCore.QRect(40, 60, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.UserName.setFont(font)
        self.UserName.setStyleSheet("color: rgb(66, 72, 116);")
        self.UserName.setObjectName("UserName")
        self.label = QtWidgets.QLabel(self.page_1)
        self.label.setGeometry(QtCore.QRect(160, 270, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.page_1)
        self.label_5.setGeometry(QtCore.QRect(160, 300, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(66, 72, 116);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_1)
        self.label_6.setGeometry(QtCore.QRect(450, 270, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_1)
        self.label_7.setGeometry(QtCore.QRect(450, 300, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(66, 72, 116);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_1)
        self.label_8.setGeometry(QtCore.QRect(150, 180, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_1)
        self.label_9.setGeometry(QtCore.QRect(440, 180, 151, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.Pages_widget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.Search_label = QtWidgets.QLabel(self.page_2)
        self.Search_label.setGeometry(QtCore.QRect(20, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Search_label.setFont(font)
        self.Search_label.setStyleSheet("color: rgb(66, 72, 116);")
        self.Search_label.setObjectName("Search_label")
        self.Search_bar = QtWidgets.QFrame(self.page_2)
        self.Search_bar.setGeometry(QtCore.QRect(20, 70, 725, 47))
        self.Search_bar.setMinimumSize(QtCore.QSize(725, 0))
        self.Search_bar.setStyleSheet("background-color: rgb(166, 177, 225);")
        self.Search_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Search_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Search_bar.setObjectName("Search_bar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Search_bar)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.Search_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"QLineEdit {\n"
"    border: 0px solid\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.search_btn = QtWidgets.QPushButton(self.Search_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy)
        self.search_btn.setMinimumSize(QtCore.QSize(60, 0))
        self.search_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.search_btn.setStyleSheet("QPushButton {\n"
"    border: 0px solid\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(66, 72, 116);\n"
"}")
        self.search_btn.setText("")
        self.search_btn.setIcon(icon2)
        self.search_btn.setIconSize(QtCore.QSize(25, 25))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_3.addWidget(self.search_btn)
        self.Second_main = QtWidgets.QFrame(self.page_2)
        self.Second_main.setGeometry(QtCore.QRect(20, 150, 725, 330))
        self.Second_main.setMinimumSize(QtCore.QSize(725, 330))
        self.Second_main.setStyleSheet("background-color: rgb(166, 177, 225);")
        self.Second_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Second_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Second_main.setObjectName("Second_main")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Second_main)
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.Second_main)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 701, 306))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listView = QtWidgets.QListView(self.scrollAreaWidgetContents)
        self.listView.setGeometry(QtCore.QRect(0, 0, 701, 311))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.listView.setFont(font)
        self.listView.setStyleSheet("")
        self.listView.setObjectName("listView")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        self.Pages_widget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(66, 72, 116);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(110, 120, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(110, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(110, 220, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 120, 331, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid #000;\n"
"border-radius: 10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 170, 331, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid #000;\n"
"border-radius: 10px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 220, 331, 41))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid #000;\n"
"border-radius: 10px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.Btn_add = QtWidgets.QPushButton(self.page_3)
        self.Btn_add.setGeometry(QtCore.QRect(200, 340, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_add.setFont(font)
        self.Btn_add.setStyleSheet("border: 0px solid;\n"
"background-color: rgb(145, 199, 136);\n"
"border-radius: 15px;")
        self.Btn_add.setObjectName("Btn_add")
        self.Btn_remove = QtWidgets.QPushButton(self.page_3)
        self.Btn_remove.setGeometry(QtCore.QRect(390, 340, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_remove.setFont(font)
        self.Btn_remove.setStyleSheet("border: 0px solid;\n"
"border-radius: 15px;\n"
"background-color: rgb(234, 84, 85);")
        self.Btn_remove.setObjectName("Btn_remove")
        self.Pages_widget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(66, 72, 116);")
        self.label_4.setObjectName("label_4")
        self.Student_Name_Label = QtWidgets.QLabel(self.page_4)
        self.Student_Name_Label.setGeometry(QtCore.QRect(40, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Student_Name_Label.setFont(font)
        self.Student_Name_Label.setObjectName("Student_Name_Label")
        self.Book_Name_Label = QtWidgets.QLabel(self.page_4)
        self.Book_Name_Label.setGeometry(QtCore.QRect(40, 120, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Book_Name_Label.setFont(font)
        self.Book_Name_Label.setObjectName("Book_Name_Label")
        self.Student_Name = QtWidgets.QLineEdit(self.page_4)
        self.Student_Name.setGeometry(QtCore.QRect(190, 80, 201, 31))
        self.Student_Name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Student_Name.setObjectName("Student_Name")
        self.Book_Name = QtWidgets.QLineEdit(self.page_4)
        self.Book_Name.setGeometry(QtCore.QRect(190, 120, 201, 31))
        self.Book_Name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Book_Name.setObjectName("Book_Name")
        self.Date_Borrowed_Label = QtWidgets.QLabel(self.page_4)
        self.Date_Borrowed_Label.setGeometry(QtCore.QRect(430, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Date_Borrowed_Label.setFont(font)
        self.Date_Borrowed_Label.setObjectName("Date_Borrowed_Label")
        self.Date_Returned_Label = QtWidgets.QLabel(self.page_4)
        self.Date_Returned_Label.setGeometry(QtCore.QRect(430, 120, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Date_Returned_Label.setFont(font)
        self.Date_Returned_Label.setObjectName("Date_Returned_Label")
        self.Date_Returned = QtWidgets.QDateEdit(self.page_4)
        self.Date_Returned.setGeometry(QtCore.QRect(580, 120, 131, 31))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        self.Date_Returned.setFont(font)
        self.Date_Returned.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Date_Returned.setObjectName("Date_Returned")
        self.Date_Borrowed = QtWidgets.QDateEdit(self.page_4)
        self.Date_Borrowed.setGeometry(QtCore.QRect(580, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        self.Date_Borrowed.setFont(font)
        self.Date_Borrowed.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Date_Borrowed.setObjectName("Date_Borrowed")
        self.Search_Student = QtWidgets.QLineEdit(self.page_4)
        self.Search_Student.setGeometry(QtCore.QRect(40, 240, 611, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Search_Student.sizePolicy().hasHeightForWidth())
        self.Search_Student.setSizePolicy(sizePolicy)
        self.Search_Student.setMinimumSize(QtCore.QSize(0, 0))
        self.Search_Student.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"QLineEdit {\n"
"    border: 0px solid\n"
"}")
        self.Search_Student.setObjectName("Search_Student")
        self.search_btn_2 = QtWidgets.QPushButton(self.page_4)
        self.search_btn_2.setGeometry(QtCore.QRect(650, 240, 60, 47))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn_2.sizePolicy().hasHeightForWidth())
        self.search_btn_2.setSizePolicy(sizePolicy)
        self.search_btn_2.setMinimumSize(QtCore.QSize(60, 0))
        self.search_btn_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.search_btn_2.setStyleSheet("QPushButton {\n"
"    border: 0px solid\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(66, 72, 116);\n"
"}")
        self.search_btn_2.setText("")
        self.search_btn_2.setIcon(icon2)
        self.search_btn_2.setIconSize(QtCore.QSize(25, 25))
        self.search_btn_2.setObjectName("search_btn_2")
        self.Add_Student_Btn = QtWidgets.QPushButton(self.page_4)
        self.Add_Student_Btn.setGeometry(QtCore.QRect(40, 170, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.Add_Student_Btn.setFont(font)
        self.Add_Student_Btn.setStyleSheet("QPushButton {\n"
"    border: 2px solid #fff;\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(66, 72, 116);\n"
"}")
        self.Add_Student_Btn.setObjectName("Add_Student_Btn")
        self.Fourth_Main = QtWidgets.QFrame(self.page_4)
        self.Fourth_Main.setGeometry(QtCore.QRect(40, 300, 670, 190))
        self.Fourth_Main.setMinimumSize(QtCore.QSize(670, 190))
        self.Fourth_Main.setStyleSheet("background-color: rgb(166, 177, 225);")
        self.Fourth_Main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Fourth_Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Fourth_Main.setObjectName("Fourth_Main")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Fourth_Main)
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Fourth_Main)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 646, 166))
        self.scrollAreaWidgetContents_2.setStyleSheet("")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.listView_2 = QtWidgets.QListView(self.scrollAreaWidgetContents_2)
        self.listView_2.setGeometry(QtCore.QRect(0, 0, 701, 311))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.listView_2.setFont(font)
        self.listView_2.setStyleSheet("")
        self.listView_2.setObjectName("listView_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_5.addWidget(self.scrollArea_2)
        self.Remove_Student_Btn = QtWidgets.QPushButton(self.page_4)
        self.Remove_Student_Btn.setGeometry(QtCore.QRect(400, 170, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.Remove_Student_Btn.setFont(font)
        self.Remove_Student_Btn.setStyleSheet("QPushButton {\n"
"    border: 2px solid #fff;\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(66, 72, 116);\n"
"}")
        self.Remove_Student_Btn.setObjectName("Remove_Student_Btn")
        self.Pages_widget.addWidget(self.page_4)
        self.verticalLayout_5.addWidget(self.Pages_widget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pages_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Welcome.setText(_translate("MainWindow", "Welcome"))
        self.UserName.setText(_translate("MainWindow", "FirstName LastName"))
        self.label.setText(_translate("MainWindow", "Book(s)"))
        self.label_5.setText(_translate("MainWindow", "Borrowed"))
        self.label_6.setText(_translate("MainWindow", "Total Number"))
        self.label_7.setText(_translate("MainWindow", "of Books"))
        self.label_8.setText(_translate("MainWindow", "50%"))
        self.label_9.setText(_translate("MainWindow", "100"))
        self.Search_label.setText(_translate("MainWindow", "SEARCH BOOKS"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search books..."))
        self.label_3.setText(_translate("MainWindow", "MANAGE BOOKS"))
        self.label_2.setText(_translate("MainWindow", "Book Name:"))
        self.label_10.setText(_translate("MainWindow", "Author:"))
        self.label_11.setText(_translate("MainWindow", "ISBN:"))
        self.Btn_add.setText(_translate("MainWindow", "Add"))
        self.Btn_remove.setText(_translate("MainWindow", "Remove"))
        self.label_4.setText(_translate("MainWindow", "STUDENT RECORDS"))
        self.Student_Name_Label.setText(_translate("MainWindow", "Student Name"))
        self.Book_Name_Label.setText(_translate("MainWindow", "Book Name"))
        self.Date_Borrowed_Label.setText(_translate("MainWindow", "Date Borrowed"))
        self.Date_Returned_Label.setText(_translate("MainWindow", "Date Returned"))
        self.Search_Student.setPlaceholderText(_translate("MainWindow", "Search Student..."))
        self.Add_Student_Btn.setText(_translate("MainWindow", "Add Student Record"))
        self.Remove_Student_Btn.setText(_translate("MainWindow", "Remove Student Record"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LibrarianWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())