import reflex as rx
import pythomazov.utils as utils
import pythomazov.styles.styles as styles
from pythomazov.routes import Route
from pythomazov.components.navbar import navbar
from pythomazov.components.footer import footer
from pythomazov.views.header import header
from pythomazov.views.challenges_links import challenges_links
from pythomazov.styles.styles import Size

@rx.page(
    route=Route.CHALLENGES.value,
    title=utils.challenges_title,
    description=utils.challenges_description,
    image=utils.preview,
    meta=utils.challenges_meta,
)
def challenges() -> rx.Component:
    return rx.chakra.box(
        utils.lang(),
        navbar(),
        rx.chakra.center(
            rx.chakra.vstack(
                header(Route.CHALLENGES.value),
                challenges_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )