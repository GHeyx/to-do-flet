import flet as ft
from flet import *
# 3 sections
#     Section 1: Family Tree View or Data Table View
#     Section 2: On Click, show the details of the person in famiily as card view 
#     Section 3: Relationship View of source and target


# Section 1 ----------------TOP SECTION-----------------------------------
# treeview tab
# from data generate family tree
    # familyid = fatherfirstname + motherfirstname + lastname
    # family color palette

# dataview tab
#   addmember.py
#     add, edit, delete





# Section 2 -----------------MIDDLE SECTION------------------------------------
# treeview tab
#   Card for selected family member
# dataview tab
#   Highlight in datatable seclected family member







# Section 3 -----------------BOTTOM SECTION-------------------------------------
# treeview tab
#   Select family tree node for source
#   Select family tree node for target
#   Relationship view

class person(ft.UserControl):
    def __init__(self, first_name):
        super().__init__()
        self.first_name = first_name

    def build(self):
        self.display_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("First name")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                    ],
                ),
            ],
        )
        return ft.DataTable()

class tree(ft.UserControl):
    def __init__(self):
        super().__init__()
        image = ft.Image("https://www.w3schools.com/howto/img_avatar.png")

    def build(self):
        return super().build() 


class ELK(ft.UserControl):
    def build(self):
        self.view = ft.Tabs(
            selected_index=0,
            animation_duration=185,
            tabs=[
                ft.Tab(
                    text="Tree",
                    icon=ft.icons.NATURE,
                    # tooltip="View Family Tree" #throws error
                    content=ft.Container(
                        content=ft.Text("This is Tab 1"), 
                        alignment=ft.alignment.center
                    ),
                ),
                ft.Tab(
                    text="Data",
                    icon=ft.icons.TABLE_VIEW,
                    # tooltip="View and Edit Family Data", #throws error
                    content=ft.Container(
                        content=ft.Text("This is Tab 2"),
                        alignment=ft.alignment.center,
                        ),
                ),
                
            ],
            expand=1,
        )

        return self.view
    
    def update(self):
        # status = self.view.tabs[self.view.selected_index].text
        super().update()

    def tabs_changed(self, e):
        self.update()
    #     page.add(t)


def main(page: Page):
    #Center window on open and set window size
    page.window_center()
    page.window_width = 800
    page.window_height = 800

    page.title = "Family Tree"
    page.update()

    # create application instance
    app = ELK()


    # add application's root control to the page
    page.add(app)


ft.app(target=main)