import reflex as rx
import pythomazov.constants as const
from pythomazov.styles.styles import Size
from pythomazov.components.title import title
from pythomazov.components.link_sponsor import link_sponsor


def sponsors() -> rx.Component:
    return rx.chakra.vstack(
        title("Sponsored by"),
        rx.chakra.responsive_grid(
            link_sponsor(
                "/lemrhali-entreprises.png",
                "Entreprises Lemrhali original logo."
            ),
            spacing=Size.BIG.value,
            columns=[1]
        ),
        width="100%",
        align_items="center",
        spacing=Size.MEDIUM.value
    )
