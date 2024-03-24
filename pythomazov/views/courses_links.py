import reflex as rx
import pythomazov.constants as const
from pythomazov.components.link_button import link_button
from pythomazov.components.title import title
from pythomazov.styles.styles import Size


def courses_links() -> rx.Component:
    return rx.chakra.vstack(
        title("Kara's (free) courses"),
        link_button(
            "Python: Introduction",
            "Level 1: Foundations, front-end, back-end, and testing",
            "/icons/python.svg",
            const.PYTHON_INTRODUCTION_COURSE_URL
        ),
        link_button(
            "Your IDE and you",
            "Get ready to code with PyCharm, VSCode, Spyder...",
            "/icons/branch.svg",
            const.IDE_INTRODUCTION_COURSE_URL
        ),
        link_button(
            "Git & GitHub",
            "Learn more about your two new-besties",
            "/icons/git.svg",
            const.GIT_COURSE_URL
        ),
        title("Certificated courses"),
        link_button(
            "Take this (diploma)!",
            "A curated list of online programs offering certificates",
            "/icons/certificate.svg",
            const.CERTIFICATES_URL
        ),
        width="100%",
        spacing=Size.DEFAULT.value,
    )
