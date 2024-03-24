import reflex as rx
import pythomazov.utils as utils
import pythomazov.styles.styles as styles
from pythomazov.routes import Route
from pythomazov.components.navbar import navbar
from pythomazov.components.footer import footer
from pythomazov.views.header import header
from pythomazov.views.cheatsheets_links import cheatsheets_links
from pythomazov.styles.styles import Size

@rx.page(
    route=Route.CHEATSHEETS.value,
    title=utils.cheatsheets_title,
    description=utils.cheatsheets_description,
    image=utils.preview,
    meta=utils.cheatsheets_meta,
)
def cheatsheets() -> rx.Component:
    return rx.chakra.box(
        utils.lang(),
        navbar(),
        rx.chakra.center(
            rx.chakra.vstack(
                header(Route.CHEATSHEETS.value),
                cheatsheets_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )