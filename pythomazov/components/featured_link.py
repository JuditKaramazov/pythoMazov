import reflex as rx
import pythomazov.styles.styles as styles
from pythomazov.styles.colors import Color, TextColor
from pythomazov.styles.styles import Size
from pythomazov.model.Featured import Featured


def featured_link(featured: Featured) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.vstack(
            rx.chakra.image(
                src=featured.image,
                height="8em",
            ),
            rx.chakra.text(
                featured.title,
            ),
            color=TextColor.HEADER.value,
            spacing=Size.BIG.value,
        ),
        href=featured.url,
        is_external=True
    )
