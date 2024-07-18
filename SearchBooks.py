import csv
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QStyledItemDelegate


class CustomItemDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        painter.save()

        # Set background color based on item's index
        if index.row() % 2 == 0:
            background_color = QColor(166, 177, 225)  # Light gray
        else:
            background_color = QColor(220, 214, 247)  # White

        painter.fillRect(option.rect, background_color)

        # Add padding
        padding = 5  # Adjust the padding value as needed
        text_rect = option.rect.adjusted(padding, padding, -padding, -padding)

        # Set text alignment
        text_alignment = Qt.AlignLeft | Qt.AlignVCenter

        # Draw the text with padding
        text = index.data()
        painter.drawText(text_rect, text_alignment, text)

        painter.restore()


def addBooks():
    data = []
    with open('Data/books.csv', 'r', newline='', encoding='utf-8') as file:
        books = csv.reader(file)
        for book in books:
            data.append(f"{book[0]}\nAuthor: {book[1]}\nISBN: {book[2]}")
    data.pop(0)
    return data



