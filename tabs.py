import flet as ft
# Algorithm layout to create a family tree and adjust the size of the tree to fit the window
# Create a class for a "Person" node, which includes properties for the person's name, relationship to the parent node, and position on the tree.

# Create a function for displaying a "Person" node, which takes in the person's name, relationship to the parent node, and position on the tree as arguments. This function should have a default size for the displayed node.

# Create a function for adding a new "Person" node to the tree. This function should take in the person's name, relationship to the parent node, and position on the tree as arguments. It should then call the display function for the new node, positioning it adjacent to the existing siblings.

# Create a function for resizing and moving nodes in the tree, to ensure that all nodes fit within the window when more people are added. This function should be called every time a new node is added.

# Create a main function which creates the root node and calls the add function with the initial family members.

# Call the main function to display the entire family tree.

class Person(ft.UserControl):
    def __init__(self, first_name, last_name, gender):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    
    def build(self):
        # self.display_person = ft.Text(self.first_name)
        self.display_person = ft.Text("WHERE AM I????")
        self.full_name = self.first_name + " " + self.last_name
        
        
        self.display_view = ft.Row(
            controls=[
                ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.PERSON),
                            title=ft.Text(self.full_name),
                            subtitle=ft.Text(self.gender),
                        ),
                        ft.Row(
                            [ft.TextButton("EDIT BUTTON MAYBE?"), ft.TextButton("SOMETHING ELSE")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
            ]
        )
        return ft.Column(controls=[self.display_view])
class Class1(ft.UserControl):


    def build(self):
        self.new_first_name = ft.TextField(label="First Name", hint_text="First Name")
        self.new_last_name = ft.TextField(label="Last Name", hint_text="Last Name")
        self.new_gender = ft.RadioGroup(content=ft.Row([
            ft.Radio(value="male", label="M", fill_color="blue"),
            ft.Radio(value="female", label="F", fill_color="pink")]))
        self.new_person_button = ft.FloatingActionButton(ft.icons.ADD, on_click=self.add_clicked)
        self.people = ft.Column()

        name_row=ft.Column(
            controls=[
                ft.Row(
                controls=[self.new_first_name, self.new_last_name,self.new_gender, self.new_person_button],
            ),
            self.people,
            ],
        )
        return name_row

    def add_clicked(self, e):
        if (not self.new_first_name.value and self.new_last_name.value):
            self.new_first_name.error_text = "First name is required"
            self.new_first_name.focus()
            self.new_last_name.error_text = ""
            self.update()
        elif (not self.new_last_name.value and self.new_first_name.value):
            self.new_last_name.error_text = "Last name is required"
            self.new_last_name.focus()
            self.new_first_name.error_text = ""
            self.update()
        elif (not self.new_first_name.value and not self.new_last_name.value):
            self.new_first_name.error_text = "First name is required"
            self.new_last_name.error_text = "Last name is required" 
            self.new_first_name.focus()
            self.update()
        elif (self.new_first_name.value and self.new_last_name.value):
            person = Person(self.new_first_name.value, self.new_last_name.value,self.new_gender.value)
            self.people.controls.append(person)
            self.new_first_name.error_text = ""
            self.new_last_name.error_text = ""
            self.new_first_name.value = ""
            self.new_last_name.value = ""
            self.new_gender.value = ""
            self.update()
        
    def tabs(self):
        # pass
        t = ft.Tabs(
            selected_index=1,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="Tab 1",
                    content=ft.ResponsiveRow(
                        [
                        ft.Card(
                                content=ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.ListTile(
                                                leading=ft.Icon(ft.icons.ALBUM),
                                                title=ft.Text("The Enchanted Nightingale"),
                                                subtitle=ft.Text(
                                                    "Music by Julie Gable. Lyrics by Sidney Stein."
                                                ),
                                            ),
                                            ft.Row(
                                                [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                                                alignment=ft.MainAxisAlignment.END,
                                            ),
                                        ]
                                    ),
                                    width=400,
                                    padding=10,
                                )
                            ),
                        ft.Text("This is Tab 1"),
                    ],
                    ),
                ),
                ft.Tab(
                    text="Tab 2",
                    icon=ft.icons.SETTINGS,

                    content=ft.ResponsiveRow(
                        [
                        ft.TextField(label="Date of Birth", hint_text="DOB"),
                        ft.TextField(label="Gender", hint_text="Gender"),

                        ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("First name")),
                                ft.DataColumn(ft.Text("Last name")),
                                ft.DataColumn(ft.Text("Age"), numeric=True),
                                ft.DataColumn(ft.Text("Gender")),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text(" ")),
                                        ft.DataCell(ft.Text(" ")),
                                        ft.DataCell(ft.Text(" ")),
                                        ft.DataCell(ft.Text(" ")),
                                    ],
                            )
                                ],
                            ),
                        
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.ListTile(
                                            leading=ft.Icon(ft.icons.ALBUM),
                                            title=ft.Text("The Enchanted Nightingale"),
                                            subtitle=ft.Text(
                                                "Music by Julie Gable. Lyrics by Sidney Stein."
                                            ),
                                        ),
                                        ft.Row(
                                            [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                                            alignment=ft.MainAxisAlignment.END,
                                        ),
                                    ]
                                ),
                                width=400,
                                padding=10,
                            )
                        ), 
                    
                        ],),  
                ),
            ],
            expand=1,
    )



def main(page: ft.Page):
    page.title = "Add A New Person"
    page.scroll = "auto"
    

    #Center window on open and set window size
    page.window_center()
    page.window_width = 900
    page.window_height = 900


    app = Class1()
    page.add(app)

ft.app(target=main)