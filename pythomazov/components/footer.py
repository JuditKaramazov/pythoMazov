import reflex as rx
import datetime
import pythomazov.constants as const
from pythomazov.styles.styles import Size
from pythomazov.styles.colors import Color, TextColor
from pythomazov.components.ant_components import back_top


def footer() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.image(
            src="/pythoFooter.png",
            height="auto",
            width="7em",
            margin_top="20px",
            alt="pythoMazov's secondary logo, with a command snake."
        ),
        rx.chakra.link(
            rx.chakra.box(
                f"© 1994-{datetime.date.today().year} ",
                rx.chakra.span("{ judit lázaro moyano }", color=Color.PRIMARY.value),
                padding_top=Size.DEFAULT.value
            ),
            href=const.KARAMAZFOLIO_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.chakra.link(
            rx.chakra.hstack(
                rx.chakra.image(
                    src="/icons/github-alt.svg",
                    height=Size.VERY_BIG.value,
                    width="45px",
                    margin_top="20px",
                ),
            ),
            href=const.REPO_URL,
            is_external=True
        ),
        back_top(
            right="45px",
            bottom="45px",
        ),
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.ZERO.value,
        color=TextColor.FOOTER.value
    )
