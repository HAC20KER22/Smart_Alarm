from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QFrame
from PyQt6.QtCore import Qt
from datetime import datetime
import sqlite3
import os
import sys

class AlarmActivationWindow(QWidget):
    def __init__(self, alarms):
        super().__init__()
        self.setWindowTitle("Active Alarms")
        self.resize(500, 400)
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        layout.addWidget(self.scroll_area)
        
        self.container = QWidget()
        self.container_layout = QVBoxLayout()
        self.container.setLayout(self.container_layout)
        self.scroll_area.setWidget(self.container)

        self.load_and_display_alarms(alarms)

        btn_close = QPushButton("Close")
        btn_close.clicked.connect(self.close)
        layout.addWidget(btn_close)

    def load_and_display_alarms(self, alarms):
        for i, alarm in enumerate(alarms):
            title = alarm[2]
            datetime_str = alarm[1]

            dt_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            formatted_dt = dt_obj.strftime('%d/%m/%Y %H:%M')

            alarm_html = f"""
            <div>
              <h2 style="margin:2px; color:#FFFFFF;">{title}</h2>
              <p style="margin:0; font-weight:bold;">Date and Time: {formatted_dt}</p>
              <p style="margin:5px 0 10px 0;">{alarm[3]}</p>
            </div>
            """
            alarm_label = QLabel()
            alarm_label.setTextFormat(Qt.TextFormat.RichText)
            alarm_label.setWordWrap(True)
            alarm_label.setText(alarm_html)

            self.container_layout.addWidget(alarm_label)

            if i < len(alarms) - 1:
                line = QFrame()
                line.setFrameShape(QFrame.Shape.HLine)
                line.setFrameShadow(QFrame.Shadow.Sunken)
                self.container_layout.addWidget(line)

def main():
    dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(dir, 'alarm_clock.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('SELECT * FROM ALARMS WHERE alarm_date_time <= ?', (now,))
    alarms_due = cursor.fetchall()

    if not alarms_due:
        # No alarms, exit silently
        return

    # Remove activated alarms from DB
    cursor.execute('DELETE FROM ALARMS WHERE alarm_date_time <= ?', (now,))
    connection.commit()
    connection.close()

    app = QApplication(sys.argv)
    window = AlarmActivationWindow(alarms_due)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
