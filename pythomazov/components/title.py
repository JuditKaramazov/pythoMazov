import reflex as rx
import pythomazov.styles.styles as styles


def title(text: str) -> rx.Component:
    return rx.chakra.heading(
        text,
        style=styles.title_style
    )
