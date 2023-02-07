import flet as ft

def main(page: ft.Page):
# Landing page for the app, this is the first page the user sees with controls like login, register, quit, login with google, etc.
    page.title="Landing Page"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Function for when a button is clicked, it does nothing
    def nothing_happens_when_clicked(e):
        pass
    
    # When register is clicked, a form appears below the button which asks for an email and a password
    # Check if username already exists, check if password is strong enough
    def register_clicked(e):
        email_field = ft.TextField(label="Email",width=400)
        password_field = ft.TextField(label="Password",width=400)
        register_ok_button = ft.ElevatedButton(text="Register", on_click=nothing_happens_when_clicked,width=200)
        register_cancel_button = ft.ElevatedButton(text="Cancel", on_click=register_cancel_clicked,width=200)
        ok_cancel_buttons = ft.Row([register_cancel_button,register_ok_button], alignment=ft.MainAxisAlignment.CENTER)
        register_fields = ft.Row([email_field,password_field], alignment=ft.MainAxisAlignment.CENTER)
        form_divider = ft.Divider()
        register_text_label = ft.Row([ft.Text("Registration", size=30,color="blue")],alignment=ft.MainAxisAlignment.CENTER)
        register_container = ft.Column(
            [form_divider,register_text_label,register_fields, ok_cancel_buttons,form_divider],
            alignment=ft.MainAxisAlignment.CENTER,)
        page.overlay.append(register_container)
        page.update()
        
    def register_ok_clicked(e):
        pass
    def register_cancel_clicked(e):
        page.overlay.clear()
        page.update()


    # Function for closing the application
    def quit_app(e):
        page.window_close()

    # Label for the title of the app labeled "Welcome to the Family"
    welcome_label = ft.Text("Welcome to the Family", text_align="center",size=50)
    
    # Button for logging in with google labeled "Login with Google"
    google_login = ft.ElevatedButton(text="Login with Google", on_click=nothing_happens_when_clicked)

    # Button for logging in with Username and Password labeled "Username Login"
    username_login = ft.ElevatedButton(text="Username Login", on_click=nothing_happens_when_clicked)

    # Button for registering a new account labeled "Register"
    register_new_account = ft.ElevatedButton(text="Register New Account", on_click=register_clicked)

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