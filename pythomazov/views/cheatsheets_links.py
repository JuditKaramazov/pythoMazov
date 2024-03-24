import reflex as rx
import pythomazov.constants as const
from pythomazov.components.link_button import link_button
from pythomazov.components.title import title
from pythomazov.styles.styles import Size


def cheatsheets_links() -> rx.Component:
    return rx.chakra.vstack(
        title("Cheatsheets made with ♥"),
        link_button(
            "Python",
            "Quick and accessible paper-snakesss live here!",
            "/icons/python.svg",
            const.PYTHON_CHEATSHEETS_URL
        ),
        link_button(
            "Git",
            "Commands, best practices, and advanced usage.",
            "/icons/git.svg",
            const.GIT_CHEATSHEETS_URL
        ),
        width="100%",
        spacing=Size.DEFAULT.value,
    )