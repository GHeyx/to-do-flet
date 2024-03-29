import flet as ft

def main(page: ft.Page):
    button_width = 300
# Landing page for the app, this is the first page the user sees with controls like login, register, quit, login with google, etc.
    page.title="Landing Page"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Function for when a button is clicked, it does nothing
    def nothing_happens_when_clicked(e):
        pass
    
    # When register is clicked, a form appears below the button which asks for an email and a password
    # Check if username already exists, check if password is strong enough
    def register_clicked(e):
        register_new_account.disabled = True
        username_login.disabled = True
        # google login disabled google_login.disabled = True
        email_field = ft.TextField(label="Email",width=400)
        password_field = ft.TextField(label="Password",width=400,password=True,on_submit=register_ok_clicked)
        register_ok_button = ft.ElevatedButton(text="Register", on_click=nothing_happens_when_clicked,width=200)
        register_cancel_button = ft.ElevatedButton(text="Cancel", on_click=register_cancel_clicked,width=200, color="red")
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
        # Check if username already exists, check if password is strong enough
        pass
    def register_cancel_clicked(e):
        register_new_account.disabled = False
        username_login.disabled = False
        page.overlay.clear()
        page.update()

    def login_with_user_pass_clicked(e):
        username_login.disabled = True
        register_new_account.disabled = True
        email_field = ft.TextField(label="Email",width=400)
        password_field = ft.TextField(label="Password",width=400,password=True,on_submit=login_ok_clicked)
        login_ok_button = ft.ElevatedButton(text="Go", on_click=nothing_happens_when_clicked,width=200)
        login_cancel_button = ft.ElevatedButton(text="Cancel", on_click=login_cancel_clicked,width=200, color="red")
        ok_cancel_buttons = ft.Row([login_cancel_button,login_ok_button], alignment=ft.MainAxisAlignment.CENTER)
        login_fields = ft.Row([email_field,password_field], alignment=ft.MainAxisAlignment.CENTER)
        form_divider = ft.Divider()
        login_text_label = ft.Row([ft.Text("Login", size=30,color="blue")],alignment=ft.MainAxisAlignment.CENTER)
        login_container = ft.Column(
            [form_divider,login_text_label,login_fields, ok_cancel_buttons,form_divider],
            alignment=ft.MainAxisAlignment.CENTER,)
        page.overlay.append(login_container)
        page.update()

    def login_ok_clicked(e):
        # Check if username and password are filled out, check if username and password are correct
        pass
    def login_cancel_clicked(e):
        username_login.disabled = False
        register_new_account.disabled = False
        page.overlay.clear()
        page.update()

    # Function for closing the application
    def quit_app(e):
        page.window_close()

    # Label for the title of the app labeled "Welcome to the Family"
    welcome_label = ft.Text("Welcome to the Family", text_align="center",size=50,no_wrap=True)
    
    # Button for logging in with google labeled "Login with Google"
    google_login = ft.ElevatedButton(text="Login with Google", on_click=nothing_happens_when_clicked,width=button_width)

    # Button for logging in with Username and Password labeled "Username Login"
    username_login = ft.ElevatedButton(text="Username Login", on_click=login_with_user_pass_clicked,width=button_width)

    # Button for registering a new account labeled "Register"
    register_new_account = ft.ElevatedButton(text="Register New Account", on_click=register_clicked,width=button_width)

    # Button to quit the app labeled "Quit"
    quit_button = ft.ElevatedButton(text="Quit", on_click=quit_app,width=button_width-100, color="red")

    # Set the scroll to auto so the page can scroll
    page.scroll = "auto"
    

    #Center window on open and set window size
    page.window_center()
    page.window_width = 900
    page.window_height = 900

    # Add the buttons to the page
    page.add(welcome_label,google_login, username_login, register_new_account, quit_button)

ft.app(target=main)