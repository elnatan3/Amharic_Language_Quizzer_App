import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QProgressBar, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class AmharicLanguageLearningApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        # Set up the GUI
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle("Amharic Language Learning App")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet("background-color: white;")
        self.vbox_layout = QVBoxLayout(self.central_widget)
        self.hbox_layout = QHBoxLayout()
        self.question_label = QLabel()
        self.answer_field = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.feedback_label = QLabel()
        self.progress_bar = QProgressBar()
        self.correct_answer_label = QLabel()
        self.image_label = QLabel()
        self.answer_field.setStyleSheet("font-size: 20px; border: 10px solid black;")
        self.submit_button.setStyleSheet("font-size: 20px; border: 10px solid black;")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.question_label.setStyleSheet("font-size: 20px;")
        self.answer_field.setStyleSheet("font-size: 20px;")
        self.submit_button.setStyleSheet("font-size: 20px;")
        self.feedback_label.setStyleSheet("font-size: 20px;")
        self.progress_bar.setStyleSheet("font-size: 20px;")
        self.correct_answer_label.setStyleSheet("font-size: 20px;")

        self.questions = ["What is the Amharic word for 'hello'?", "What is the Amharic word for 'bye'?", "What is the Amharic word for 'thank you'?", "What is the Amharic word for 'please'?", "What is the Amharic word for 'yes'?", "What is the Amharic word for 'no'?"]
        self.answers = ["selam", "chaw", "ameseginalehu", "i'bakwon", "eshi", "embi"]
        self.images = ["hello.png", "goodbye.png", "thankyou.png", "please.png", "yes.png", "no.png"]
        self.current_question_index = 0
        self.correct_answers = 0
        self.question_label.setText(self.questions[self.current_question_index])
        self.submit_button.clicked.connect(self.submit_answer)
        self.progress_bar.setRange(0, len(self.questions))
        self.vbox_layout.addWidget(self.question_label)
        self.vbox_layout.addWidget(self.answer_field)
        self.vbox_layout.addWidget(self.submit_button)
        self.vbox_layout.addWidget(self.feedback_label)
        self.vbox_layout.addWidget(self.progress_bar)
        self.vbox_layout.addWidget(self.correct_answer_label)
        self.vbox_layout.addWidget(self.image_label)
        self.hbox_layout.addLayout(self.vbox_layout)
        self.central_widget.setLayout(self.hbox_layout)
        self.show()
        
    def submit_answer(self):
        # Check the answer and update the feedback
        answer = self.answer_field.text()
        if answer == self.answers[self.current_question_index]:
            self.feedback_label.setText("Correct!")
            self.feedback_label.setStyleSheet("color: green")
            self.correct_answers += 1
        else:
            self.feedback_label.setText("Incorrect.")
            self.feedback_label.setStyleSheet("color: red; background-color: lightyellow; font-weight: bold; padding: 5px;")
            self.correct_answer_label.setText("Correct answer: " + self.answers[self.current_question_index])
            self.image_label.setPixmap(QPixmap(self.images[self.current_question_index]))
        self.progress_bar.setValue(self.current_question_index + 1)
        # Go to the next question or end the quiz
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.question_label.setText(self.questions[self.current_question_index])
            self.answer_field.setText("")
        else:
            score = self.correct_answers
            total_questions = len(self.questions)
            score_percent = (score / total_questions) * 100
            score_message = f"Score: {score}/{total_questions} ({score_percent:.1f}%)"
            QMessageBox.information(self, "Quiz Completed", f"Congratulations, you have completed the quiz!\n\n{score_message}", QMessageBox.Ok, QMessageBox.Ok)
            self.close()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AmharicLanguageLearningApp()
    sys.exit(app.exec_())
