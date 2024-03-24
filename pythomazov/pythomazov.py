import reflex as rx
import pythomazov.constants as const
import pythomazov.styles.styles as styles
from pythomazov.pages.index import index
from pythomazov.pages.courses import courses
from pythomazov.pages.cheatsheets import cheatsheets
from pythomazov.pages.challenges import challenges
from pythomazov.api.api import repo

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={const.GOOGLE_TAG}"),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{const.GOOGLE_TAG}');
"""
        ),
    ],
)

app.api.add_api_route("/repo", repo)
