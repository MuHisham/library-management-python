import csv
def addStudentRecord(name, book, date_borrowed, date_returned):

    with open('Data/students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, book, date_borrowed, date_returned])


def addStudentToListView():
    data = []
    with open('Data/students.csv', 'r', newline='', encoding='utf-8') as file:
        books = csv.reader(file)
        for book in books:
            data.append(f"Student: {book[0]}\nBook: {book[1]}\nDate Borrowed: {book[2]}\nDate Returned: {book[3]}")
    data.pop(0)
    return data
