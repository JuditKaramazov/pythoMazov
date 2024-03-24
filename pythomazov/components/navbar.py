import reflex as rx
import pythomazov.constants as const
from pythomazov.routes import Route
from pythomazov.styles.styles import Size
from pythomazov.styles.colors import Color


def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.link(
            rx.chakra.image(
                src="/pythoLogo.png",
                alt="PythoMazov original logo, displaying a cartoonish snake.",
                style={"width": "70px", "height": "auto"}
            ),
            href=Route.INDEX.value
        ),
       rx.spacer(),
        rx.menu.root(
            rx.menu.trigger(
                rx.chakra.image(
                    src="/icons/hamburger.png",
                    alt="Menu",
                    style={"width": "55px", "height": "55px"},
                    color=Color.PRIMARY.value,
                    cursor="pointer",
                    filter="drop-shadow(0 0 2px rgba(67, 166, 153, 0.8))",
                    padding=Size.MEDIUM.value,
                ),
            ),
            rx.menu.content(
                rx.chakra.text(
                    "--------------"
                ),
                rx.menu.separator(),
                rx.chakra.link(
                    "Home ⌂",
                    href=Route.INDEX.value,
                    style={"margin_top": "20px", "padding": "0px 0px 0px 5px"},
                    _hover={"text_decoration": "underline", "color": Color.SECONDARY.value}
                ),
                rx.menu.separator(),
                rx.chakra.link(
                    "Courses ⛁",
                    href=Route.COURSES.value,
                    style={"padding": "0px 0px 0px 5px"},
                    _hover={"text_decoration": "underline", "color": Color.SECONDARY.value}
                ),
                rx.menu.separator(),
                rx.chakra.link(
                    "Cheatsheets ☈",
                    href=Route.CHEATSHEETS.value,
                    style={"padding": "0px 0px 0px 5px"},
                    _hover={"text_decoration": "underline", "color": Color.SECONDARY.value}
                ),
                rx.menu.separator(),
                rx.chakra.link(
                    "Challenges ♜",
                    href=Route.CHALLENGES.value,
                    style={"margin_bottom": "20px", "padding": "0px 0px 0px 5px"},
                    _hover={"text_decoration": "underline", "color": Color.SECONDARY.value}
                ),
                rx.menu.separator(),
                rx.chakra.text(
                    "--------------"
                ),
                position="relative",
                height="100vh",
                width="300px",
                top="10px",
                margin_right="-15px",
                align_items="center",
                background_color=Color.CONTENT.value,
                color=Color.PRIMARY.value,
                text_align="center",
                padding=Size.BIG.value,
                transition="right 2.5s ease-in-out",
            ),
        ),
        position="sticky",
        top="0",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        opacity="0.9",
        z_index="999",
    )
