import flet as ft

def main(page: ft.Page):

    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Tab 1",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Tab 2",
                icon=ft.icons.SETTINGS,

                content=ft.ResponsiveRow(
                    [
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
                                    ft.DataCell(ft.Text("John")),
                                    ft.DataCell(ft.Text("Smith")),
                                    ft.DataCell(ft.Text("43")),
                                    ft.DataCell(ft.Text("M")),
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

    #Center window on open and set window size
    page.window_center()
    page.window_width = 800
    page.window_height = 800
    page.add(t)

ft.app(target=main)