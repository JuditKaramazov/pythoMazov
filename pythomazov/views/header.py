import reflex as rx
import datetime
import pythomazov.constants as const
from pythomazov.routes import Route
from pythomazov.styles.styles import Size
from pythomazov.styles.colors import Color, TextColor
from pythomazov.components.link_icon import link_icon
from pythomazov.components.info_text import info_text

def header(route, details=True) -> rx.Component:
    if route == Route.INDEX.value:
        title = "Judit Lázaro goes hiss"
        description = """
            A Software Developer, Tightrope Walker & Spanish Philologist
            from the interwebz welcomes you. What do you do? Since this
            is not an adventure game, grab some snacks, gather your courage, 
            and feel free to access all the content I can provide you with! ⚔️
        """
    elif route == Route.CHALLENGES.value:
        title = "Judit goes challenging!"
        description = """
            "You are challenged by Pokémon Trainer Karamazov!" Although that 
            wouldn't be much of a challenge, here you'll find a collection of 
            sites to put what you're learning to the test. 3, 2, 1...
        """
    elif route == Route.CHEATSHEETS.value:
        title = "Judit is a court clerk"
        description = """
            "Nobody said it was easy" - yet Coldplay wasn't that right in the 
            end! Here, you will find some of the interwebz's "greatest hits", 
            giving you easy access to shortcuts and quick references! 
        """
    elif route == Route.COURSES.value:
        title = "Judit, so disCOURSEsive"
        description = """
            "The secret of getting ahead is getting started". Let's dive into the 
            programming world thanks to some accessible courses, ranging from basic 
            to advanced levels: understanding what's an IDE, Python, Git...
        """
    else:
        title = "Judit Lázaro goes hiss"
        description = """
            A Software Developer, Tightrope Walker & Spanish Philologist
            from the interwebz welcomes you. What do you do? Since this
            is not an adventure game, grab some snacks, gather your courage, 
            and feel free to access all the content I can provide you with! ⚔️
        """

    return rx.chakra.vstack(
        rx.chakra.hstack(
            rx.chakra.avatar(
                name="Judit Karamazov",
                size="xl",
                src="/avatar.png",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.chakra.vstack(
                rx.chakra.heading(
                    title,
                    align_items="end",
                    size="lg"
                ),
                rx.chakra.text(
                    "@JuditKaramazov",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.chakra.hstack(
                    link_icon(
                        "/icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "/icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    spacing=Size.LARGE.value
                ),
                align_items="end",
            ),
            spacing=Size.DEFAULT.value
            ),
            rx.cond(
                details,
                rx.chakra.vstack(
                    rx.chakra.flex(
                        info_text(
                            "(Cool apps", "around)"
                        ),
                        rx.chakra.spacer(),
                        info_text(
                            f"↓ {experience()}",
                            "max... ↓"
                        ),
                        rx.chakra.spacer(),
                        info_text(
                            "(Articles", "& more)"
                        ),
                        width="100%"
                    ),
                    rx.chakra.image(
                        src="/hp.gif",
                        height="30px",
                        width="70px",
                    ),
                    rx.chakra.text(
                        description,
                        font_size=Size.DEFAULT.value,
                        color=TextColor.FOOTER.value,
                        padding="20px",
                        background=Color.BACKGROUND.value,
                        border_radius="12px",
                        box_shadow=(
                            "inset 0 0 2px 1px hsla(0, 0%, 100%, 0.1), "
                            "2px 2px 5px hsla(230, 13%, 9%, 0.3), "
                            "-2px -2px 5px hsla(230, 13%, 9%, 0.3)"
                            ),
                        border="1px solid hsla(230, 13%, 9%, 0.2)",
                    ),
                    width="100%",
                    spacing=Size.BIG.value
                )
            ),
            width="100%",
            spacing=Size.BIG.value,
            align_items="flex-end",
            justify_content="end"
        )


def experience() -> int:
    return datetime.date.today().year - 1994
