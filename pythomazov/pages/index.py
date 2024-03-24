import reflex as rx
import pythomazov.utils as utils
import pythomazov.styles.styles as styles
from pythomazov.routes import Route
from pythomazov.components.navbar import navbar
from pythomazov.components.footer import footer
from pythomazov.views.header import header
from pythomazov.views.index_links import index_links
from pythomazov.views.sponsors import sponsors
from pythomazov.styles.styles import Size
from pythomazov.state.PageState import PageState


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
    on_load=[PageState.featured_links]
)
def index() -> rx.Component:
    return rx.chakra.box(
        utils.lang(),
        navbar(),
        rx.chakra.center(
            rx.chakra.vstack(
                header(Route.INDEX.value),
                index_links(PageState.featured_info),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )
