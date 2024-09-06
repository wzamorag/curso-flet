import flet as ft
# from flet import IconButton, Page, Row, TextField, icons

def main(page:ft.Page):
    page.title="Contador "
    page.vertical_alignment="center"
    txt_number=ft.TextField(value="0",text_align="right",width=100)

    def minus_click(e):
        txt_number.value=int(txt_number.value)-1
        page.update()

    def plus_click(e):
        txt_number.value=int(txt_number.value)+1
        page.update()


    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )

    page.add(
        ft.Row([
            ft.IconButton(ft.icons.REMOVE,on_click=minus_click),
            txt_number,
            ft.IconButton(ft.icons.ADD,on_click=plus_click),
        ],
        alignment="center",
        ),
        ft.Row([
            color_dropdown
        ],
        alignment="center",
        )
    )


ft.app(main)

