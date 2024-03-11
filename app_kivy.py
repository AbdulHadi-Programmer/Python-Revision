from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import sqlite3

class ExpenseTrackerApp(App):
    def build(self):
        # UI components
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Income Section
        income_layout = BoxLayout(orientation='horizontal', spacing=10)
        income_text = TextInput(hint_text='Enter Income', multiline=False)
        add_income_button = Button(text='Add Income', on_press=self.add_income)
        income_layout.add_widget(income_text)
        income_layout.add_widget(add_income_button)

        # Expenses Section
        expenses_layout = BoxLayout(orientation='vertical', spacing=10)
        expenses_text = TextInput(hint_text='Enter Expense', multiline=False)
        expenses_price_text = TextInput(hint_text='Enter Price', multiline=False)
        add_expense_button = Button(text='Add Expense', on_press=self.add_expense)
        expenses_layout.add_widget(expenses_text)
        expenses_layout.add_widget(expenses_price_text)
        expenses_layout.add_widget(add_expense_button)

        # Savings Section
        savings_layout = BoxLayout(orientation='horizontal', spacing=10)
        savings_text = TextInput(hint_text='Enter Saving', multiline=False)
        add_saving_button = Button(text='Add Saving', on_press=self.add_saving)
        savings_layout.add_widget(savings_text)
        savings_layout.add_widget(add_saving_button)

        # Display Section
        display_layout = BoxLayout(orientation='vertical', spacing=10)
        display_button = Button(text='Show Data', on_press=self.show_data)
        display_layout.add_widget(display_button)

        # Add all components to the main layout
        layout.add_widget(income_layout)
        layout.add_widget(expenses_layout)
        layout.add_widget(savings_layout)
        layout.add_widget(display_layout)

        return layout

    def add_income(self, instance):
        self.save_to_database('Income', instance.text)

    def add_expense(self, instance):
        expense_name = instance.parent.children[0].text
        expense_price = instance.parent.children[1].text
        self.save_to_database('Expenses', f"{expense_name}: {expense_price}")

    def add_saving(self, instance):
        self.save_to_database('Savings', instance.text)

    def show_data(self, instance):
        conn = sqlite3.connect('expense_tracker.db')
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM Records")
            data = cursor.fetchall()
            print(data)
        except sqlite3.Error as e:
            print(f"Error: {e}")

        conn.close()

    def save_to_database(self, category, data):
        conn = sqlite3.connect('expense_tracker.db')
        cursor = conn.cursor()

        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS Records (Category TEXT, Data TEXT)")
            cursor.execute("INSERT INTO Records (Category, Data) VALUES (?, ?)", (category, data))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")

        conn.close()

if __name__ == '__main__':
    ExpenseTrackerApp().run()