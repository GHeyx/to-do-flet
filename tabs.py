import flet as ft

class class1(ft.UserControl):

    def build(self):
        self.TextField=ft.TextField(label="First Name", hint_text="First Name")
        self.new_person_button= ft.FloatingActionButton(ft.icons.ADD, on_click=self.new_person)
        self.people = ft.Column()

        name_row=ft.Column(
            controls=[
            ft.Row(
                controls=[self.TextField, self.new_person_button],
            ),
            self.people,
            ],
        ),
        self.update()
        return name_row

    
    # first_name=ft.TextField(label="First Name", hint_text="First Name")

    def new_person(self, e):
        pass
    
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
    page.title = "Tabs Example"
    

    #Center window on open and set window size
    page.window_center()
    page.window_width = 900
    page.window_height = 900
    page.add(t)


    app = class1()
    page.add(app)

ft.app(target=main)