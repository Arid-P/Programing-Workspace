import flet as ft


def main(page: ft.Page):
    page.title = "Calculator"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window_width = 360
    page.window_height = 640

    expression = ft.Text(
        value="0",
        size=32,
        text_align=ft.TextAlign.RIGHT,
        weight=ft.FontWeight.BOLD,
    )

    def update_display(value):
        expression.value = value
        page.update()

    def on_button_click(e):
        current = expression.value
        text = e.control.text

        if text == "C":
            update_display("0")

        elif text == "⌫":
            update_display(current[:-1] if len(current) > 1 else "0")

        elif text == "=":
            try:
                # restricted eval
                result = eval(current, {"__builtins__": None}, {})
                update_display(str(result))
            except Exception as e:
                update_display("Error", e)

        else:
            if current == "0":
                update_display(text)
            else:
                update_display(current + text)

    def btn(text, expand=1):
        return ft.ElevatedButton(
            text=text,
            expand=expand,
            height=60,
            on_click=on_button_click,
        )

    page.add(
        ft.Column(
            expand=True,
            controls=[
                ft.Container(
                    content=expression,
                    padding=20,
                    alignment=ft.alignment.center_right,
                ),
                ft.Column(
                    expand=True,
                    controls=[
                        ft.Row([btn("C"), btn("⌫"), btn("/"), btn("*")]),
                        ft.Row([btn("7"), btn("8"), btn("9"), btn("-")]),
                        ft.Row([btn("4"), btn("5"), btn("6"), btn("+")]),
                        ft.Row([btn("1"), btn("2"), btn("3"), btn("=")]),
                        ft.Row([btn("0", expand=2), btn(".")]),
                    ],
                ),
            ],
        )
    )


ft.app(target=main)