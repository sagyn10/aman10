import flet as ft



def main(page:ft.Page):
    greeting_text = ft.Text("Привет мир")


    page.add(greeting_text)

ft.app(target=main, view=ft.WEB_BROWSER)