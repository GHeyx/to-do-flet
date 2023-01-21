import flet as ft





def main(page):
    #Center window on open and set window size
    page.window_center()
    page.window_height = 1000
    page.window_width = 1000
    page.scroll = "adaptive"
    page.title = "Card Example"
    # 
    # Card Content: Selected Person Name, Image, Age
    # 


    a1_card=ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Image(src=f"assets\img\pfp.png",
                            fit=ft.ImageFit.CONTAIN),
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
        )
    page.add(a1_card)

ft.app(target=main, assets_dir="assets")
