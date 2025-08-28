from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QStackedWidget, QLineEdit, QTextEdit, QListWidget, QMessageBox, QDateTimeEdit, 
    QTableWidget, QTableWidgetItem,QHeaderView
)
from PyQt6.QtCore import Qt, QDateTime, QTime, QDate
import sys
import sqlite3
from datetime import datetime
import os


dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(dir, 'alarm_clock.db')
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

class Alarm:
    @staticmethod
    def create_table():
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ALARMS(
                alarm_id INTEGER PRIMARY KEY AUTOINCREMENT,
                alarm_date_time TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT
            )
        ''')
        connection.commit()

    @staticmethod
    def add(time, title, desc):
        cursor.execute('INSERT INTO ALARMS (alarm_date_time, title, description) VALUES (?, ?, ?)', (time, title, desc))
        connection.commit()

    @staticmethod
    def get_all():
        cursor.execute("SELECT * FROM ALARMS ORDER BY alarm_id")
        return cursor.fetchall()

    @staticmethod
    def get_by_id(alarm_id):
        cursor.execute("SELECT * FROM ALARMS WHERE alarm_id=?", (alarm_id,))
        return cursor.fetchone()

    @staticmethod
    def update(alarm_id, time, title, desc):
        cursor.execute('''
            UPDATE ALARMS SET alarm_date_time = ?, title = ?, description = ?
            WHERE alarm_id = ?
        ''', (time, title, desc, alarm_id))
        connection.commit()

    @staticmethod
    def delete(alarm_id):
        cursor.execute('DELETE FROM ALARMS WHERE alarm_id = ?', (alarm_id,))
        connection.commit()

class SmartAlarmApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" Smart Alarm ")
        self.setGeometry(300, 300, 600, 400)

        Alarm.create_table()

        self.layout = QVBoxLayout()
        self.stacked = QStackedWidget()
        self.layout.addWidget(self.stacked)
        self.setLayout(self.layout)

        self.options_page()
        self.create_page()
        self.edit_page()
        self.delete_page()
        self.print_page()

        self.stacked.setCurrentWidget(self.options_screen)

    def options_page(self):
        self.options_screen = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Select an option:")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)

        btn_create = QPushButton("Create Alarm")
        btn_edit = QPushButton("Edit Alarm")
        btn_delete = QPushButton("Delete Alarm")
        btn_print = QPushButton("Print All Alarms")

        btn_create.clicked.connect(lambda: self.stacked.setCurrentWidget(self.create_screen))
        btn_edit.clicked.connect(lambda: self.refresh_edit_list() or self.stacked.setCurrentWidget(self.edit_screen))
        btn_delete.clicked.connect(lambda: self.refresh_delete_list() or self.stacked.setCurrentWidget(self.delete_screen))
        btn_print.clicked.connect(lambda: self.refresh_print_text() or self.stacked.setCurrentWidget(self.print_screen))

        for btn in [btn_create, btn_edit, btn_delete, btn_print]:
            layout.addWidget(btn)

        self.options_screen.setLayout(layout)
        self.stacked.addWidget(self.options_screen)

    def create_page(self):
        self.create_screen = QWidget()
        layout = QVBoxLayout()

        self.create_datetime = QDateTimeEdit()
        self.create_datetime.setCalendarPopup(True)
        self.create_datetime.setDisplayFormat("yyyy-MM-dd HH:mm")
        initial_dt = QDateTime(QDate(1900, 1, 1), QTime(0, 0))
        self.create_datetime.setDateTime(initial_dt)

        self.create_title = QLineEdit()
        self.create_title.setPlaceholderText("Title")

        self.create_desc = QTextEdit()
        self.create_desc.setPlaceholderText("Description")

        btn_add = QPushButton("Add Alarm")
        btn_back = QPushButton("Back")

        btn_add.clicked.connect(self.add_alarm)
        btn_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.options_screen))

        for widget in [self.create_datetime, self.create_title, self.create_desc, btn_add, btn_back]:
            layout.addWidget(widget)

        self.create_screen.setLayout(layout)
        self.stacked.addWidget(self.create_screen)

    def add_alarm(self):
        dt = self.create_datetime.dateTime()
        alarm_str = dt.toString("yyyy-MM-dd HH:mm:ss")
        title = self.create_title.text()
        desc = self.create_desc.toPlainText()

        if not title:
            QMessageBox.warning(self, "Error", "Title cannot be empty")
            return

        Alarm.add(alarm_str, title, desc)

        QMessageBox.information(self, "Success", "Alarm added successfully!")

        self.create_datetime.setDateTime(QDateTime(QDate(1900, 1, 1), QTime(0, 0)))
        self.create_title.clear()
        self.create_desc.clear()

        self.stacked.setCurrentWidget(self.options_screen)

    def edit_page(self):
        self.edit_screen = QWidget()
        layout = QVBoxLayout()

        self.edit_list = QTableWidget()
        self.edit_list.setColumnCount(4)
        self.edit_list.setHorizontalHeaderLabels(["Alarm Id", "Date - Time", "Title", "Description"])
        self.edit_list.verticalHeader().hide()
        self.edit_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.edit_id_line = QLineEdit()
        self.edit_id_line.setPlaceholderText("Enter Alarm ID to edit")

        self.edit_datetime = QDateTimeEdit()
        self.edit_datetime.setCalendarPopup(True)
        self.edit_datetime.setDisplayFormat("yyyy-MM-dd HH:mm")
        empty_dt = QDateTime(QDate(1900, 1, 1), QTime(0, 0))
        self.edit_datetime.setDateTime(empty_dt)

        self.edit_title = QLineEdit()
        self.edit_title.setPlaceholderText("New Title (leave empty to keep original)")

        self.edit_desc = QTextEdit()
        self.edit_desc.setPlaceholderText("New Description (leave empty to keep original)")

        btn_edit = QPushButton("Edit Alarm")
        btn_back = QPushButton("Back")

        btn_edit.clicked.connect(self.edit_alarm_action)
        btn_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.options_screen))

        layout.addWidget(self.edit_list)
        layout.addWidget(self.edit_id_line)
        layout.addWidget(self.edit_datetime)
        layout.addWidget(self.edit_title)
        layout.addWidget(self.edit_desc)
        layout.addWidget(btn_edit)
        layout.addWidget(btn_back)

        self.edit_screen.setLayout(layout)
        self.stacked.addWidget(self.edit_screen)

    def refresh_edit_list(self):
        alarms = Alarm.get_all()
        self.edit_list.setRowCount(0) 

        for row, alarm in enumerate(alarms):
            self.edit_list.insertRow(row)
            for col, data in enumerate(alarm):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.edit_list.setItem(row, col, item)

    def edit_alarm_action(self):
        try:
            alarm_id = int(self.edit_id_line.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Enter valid numeric ID")
            return

        empty_dt = QDateTime(QDate(1900, 1, 1), QTime(0, 0))
        selected_dt = self.edit_datetime.dateTime()

        alarm_record = Alarm.get_by_id(alarm_id)
        if not alarm_record:
            QMessageBox.warning(self, "Error", "Alarm ID not found")
            return

        new_title = self.edit_title.text() or alarm_record[2]
        new_desc = self.edit_desc.toPlainText() or alarm_record[3]

        if selected_dt == empty_dt:
            new_dt_str = alarm_record[1]
        else:
            new_dt_str = selected_dt.toString("yyyy-MM-dd HH:mm:ss")

        Alarm.update(alarm_id, new_dt_str, new_title, new_desc)

        QMessageBox.information(self, "Success", f"Alarm ID {alarm_id} edited.")
        self.stacked.setCurrentWidget(self.options_screen)

    from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView

    def delete_page(self):
        self.delete_screen = QWidget()
        layout = QVBoxLayout()

        self.delete_list = QTableWidget() 
        self.delete_list.setColumnCount(4)
        self.delete_list.setHorizontalHeaderLabels(["Alarm Id", "Date - Time", "Title", "Description"])
        self.delete_list.verticalHeader().hide()
        self.delete_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.delete_id_line = QLineEdit()
        self.delete_id_line.setPlaceholderText("Enter Alarm ID to delete")

        btn_delete = QPushButton("Delete Alarm")
        btn_back = QPushButton("Back")

        btn_delete.clicked.connect(self.delete_alarm_action)
        btn_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.options_screen))

        layout.addWidget(self.delete_list)
        layout.addWidget(self.delete_id_line)
        layout.addWidget(btn_delete)
        layout.addWidget(btn_back)

        self.delete_screen.setLayout(layout)
        self.stacked.addWidget(self.delete_screen)

    def refresh_delete_list(self):
        alarms = Alarm.get_all()

        self.delete_list.setRowCount(0) 

        for row, alarm in enumerate(alarms):
            self.delete_list.insertRow(row)
            for col, data in enumerate(alarm):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.delete_list.setItem(row, col, item)

    def delete_alarm_action(self):
        try:
            alarm_id = int(self.delete_id_line.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Enter valid numeric ID")
            return

        alarm_record = Alarm.get_by_id(alarm_id)
        if not alarm_record:
            QMessageBox.warning(self, "Error", "Alarm ID not found")
            return

        Alarm.delete(alarm_id)
        QMessageBox.information(self, "Success", f"Alarm ID {alarm_id} deleted.")
        self.stacked.setCurrentWidget(self.options_screen)

    def print_page(self):
        self.print_screen = QWidget()
        layout = QVBoxLayout()

        self.print_table = QTableWidget()
        self.print_table.setColumnCount(4)
        self.print_table.setHorizontalHeaderLabels(["Alarm Id", "Date - Time", "Title", "Description"])

        self.print_table.verticalHeader().hide()

        #self.print_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layout.addWidget(self.print_table)

        btn_back = QPushButton("Back")
        btn_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.options_screen))

        layout.addWidget(self.print_table)
        layout.addWidget(btn_back)

        self.print_screen.setLayout(layout)
        self.stacked.addWidget(self.print_screen)

    def refresh_print_text(self):
        alarms = Alarm.get_all()
        self.print_table.setRowCount(len(alarms))

        for row, alarm in enumerate(alarms):
            for col, data in enumerate(alarm):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.print_table.setItem(row, col, item)

        self.print_table.resizeColumnsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SmartAlarmApp()
    window.show()
    sys.exit(app.exec())
