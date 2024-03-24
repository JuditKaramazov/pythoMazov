import reflex as rx
from pythomazov.styles.styles import Size


def link_sponsor(image: str, alt: str) -> rx.Component:
    return rx.chakra.image(
        src=image,
        height="10em",
        alt=alt
    )
