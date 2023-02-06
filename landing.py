import flet as ft

def main(page: ft.Page):
# Landing page for the app, this is the first page the user sees with controls like login, register, quit, login with google, etc.
    page.title="Landing Page"

    # Function for when a button is clicked, it does nothing
    def nothing_happens_when_clicked(e):
        pass

    # Function for closing the application
    def quit_app(e):
        page.window_close()

    # Label for the title of the app labeled "Welcome to the Family"
    welcome_label = ft.Text("Welcome to the Family", text_align=ft.TextAlign.CENTER, size=50)
    
    # Button for logging in with google labeled "Login with Google"
    google_login = ft.ElevatedButton(text="Login with Google", on_click=nothing_happens_when_clicked)

    # Button for logging in with Username and Password labeled "Username Login"
    username_login = ft.ElevatedButton(text="Username Login", on_click=nothing_happens_when_clicked)

    # Button for registering a new account labeled "Register"
    register_new_account = ft.ElevatedButton(text="Register New Account", on_click=nothing_happens_when_clicked)

    # Button to quit the app labeled "Quit"
    quit_button = ft.ElevatedButton(text="Quit", on_click=quit_app)

    # Set the scroll to auto so the page can scroll
    page.scroll = "auto"
    

    #Center window on open and set window size
    page.window_center()
    page.window_width = 900
    page.window_height = 900

    # Add the buttons to the page
    page.add(welcome_label,google_login, username_login, register_new_account, quit_button)

ft.app(target=main)