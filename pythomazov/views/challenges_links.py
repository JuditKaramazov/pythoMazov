import reflex as rx
import pythomazov.constants as const
from pythomazov.components.link_button import link_button
from pythomazov.components.title import title
from pythomazov.styles.styles import Size


def challenges_links() -> rx.Component:
    return rx.chakra.vstack(
        title("Was it a challenge? ♥"),
        link_button(
            "Codewars",
            "Where developers achieve code mastery through challenge",
            "/icons/codewars.svg",
            const.CODEWARS_URL
        ),
        link_button(
            "Exercism",
            "Increase your coding craftsmanship by solving problems",
            "/icons/exercism.svg",
            const.EXERCISM_URL
        ),

        title("Gamify your skills"),
        link_button(
            "Codédex",
            "Python, HTML/CSS, JS? Start your coding adventure!",
            "/icons/retro-computer.svg",
            const.CODEDEX_URL
        ),
        link_button(
            "OhMyGit",
            "It's here, guys: An interactive Git learning game!",
            "/icons/git.svg",
            const.OHMYGIT_URL
        ),
        link_button(
            "WarriorJS",
            "Climb the tower and reach The JavaScript Sword!",
            "/icons/sword.svg",
            const.WARRIORJS_URL
        ),
        width="100%",
        spacing=Size.DEFAULT.value,
    )
