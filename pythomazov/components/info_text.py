import reflex as rx
from pythomazov.styles.styles import Size
from pythomazov.styles.colors import Color, TextColor


def info_text(title: str, body: str) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.span(
            title,
            font_weight="bold",
            color=Color.PRIMARY.value
        ),
        f" {body}",
        font_size=Size.MEDIUM.value,
        color=TextColor.FOOTER.value
    )
