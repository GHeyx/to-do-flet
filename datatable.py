import flet as ft

def main(page: ft.Page):
    #Center window on open and set window size
    page.window_center()
    page.window_height = 1000
    page.window_width = 1000
    page.scroll = "adaptive"

    def add_person(e):
        family_table.columns.append(ft.DataRow(cells = [ft.DataCell(ft.Text(new_person.value))]))
        new_person.value = ""
        try:
            view.update() 
            table_view.update()
        except:
            pass

    family_table = ft.DataTable(
        columns=[
            # Person Attributes: First, Last, DOB, Gender, etc.
            ft.DataColumn(ft.Text("First name"))
        ],
        rows=[
            ft.DataRow(cells = [ft.DataCell(ft.Text("John"))]),
        ]
    )

    new_person = ft.TextField(hint_text="First Name", expand=True)
    new_person_button = ft.ElevatedButton(text="Add", on_click=add_person, icon=ft.icons.ADD)


    table_view=ft.Column(
            controls=[
                family_table
            ]
    )
    view = ft.Column(
        spacing=50,
        tight=True,
        controls=[
            ft.Row(
                controls=[
                    new_person,
                    new_person_button
                ],
            ),
            family_table
        ],
        
    )

    page.add(view)



ft.app(target=main)