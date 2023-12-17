from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class StudentManagementApp(App):
    def build(self):
        self.title = 'Student Management App'

        # Layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Widgets
        self.student_info_label = Label(text='Student Information')
        self.student_name_input = TextInput(hint_text='Enter student name')
        self.student_roll_input = TextInput(hint_text='Enter roll number')
        self.display_button = Button(text='Display Info', on_press=self.display_student_info)

        # Add widgets to the layout
        layout.add_widget(self.student_info_label)
        layout.add_widget(self.student_name_input)
        layout.add_widget(self.student_roll_input)
        layout.add_widget(self.display_button)

        return layout

    def display_student_info(self, instance):
        student_name = self.student_name_input.text
        student_roll = self.student_roll_input.text

        if student_name and student_roll:
            info_text = f"Student Name: {student_name}\nRoll Number: {student_roll}"
            self.student_info_label.text = info_text
        else:
            self.student_info_label.text = "Please enter both name and roll number."


if __name__ == '__main__':
    StudentManagementApp().run()