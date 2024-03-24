import reflex as rx
import pythomazov.constants as const
from pythomazov.components.featured_link import featured_link
from pythomazov.model.Featured import Featured
from pythomazov.routes import Route
from pythomazov.components.link_button import link_button
from pythomazov.components.title import title
from pythomazov.styles.styles import Size, Color


def index_links(featured: list[Featured]) -> rx.Component:
    return rx.chakra.vstack(
        title("Starter Kit"),
        link_button(
            "Digital animal: courses",
            "Get started with some coding essentials",
            "/icons/code.svg",
            Route.COURSES.value,
            False,
            Color.SECONDARY.value
        ),
        link_button(
            "Cheatsheets",
            "Keep info simple & always at reach",
            "/icons/file.svg",
            Route.CHEATSHEETS.value
        ),
        link_button(
            "Gaming DevDiary",
            "Personal list of engines, art, audio, and more",
            "/icons/gamepad.svg",
            const.GAME_DEVELOPMENT_URL
        ),
        link_button(
            "Learn by coding",
            "Ready to test yourself? Give these challenges a try!",
            "/icons/keyboard.svg",
            Route.CHALLENGES.value
        ),

        title("Useful resources"),
        link_button(
            "Books",
            "Useful books about technology, computing arts, and design",
            "/icons/book.svg",
            const.BOOKS_URL
        ),
        link_button(
            "Sites",
            "Explore new perspectives, articles, and tools",
            "/icons/sites.svg",
            const.SITES_URL
        ),
        link_button(
            "Setup time",
            "Sexy setup of the programmer",
            "/icons/setup.svg",
            const.SETUP_URL
        ),

        title("Stay tuned"),
        link_button(
            "KaramaBlog - go Astro!",
            "Chunks of development, game design, goodies, and analysis",
            "/icons/astronaut.svg",
            const.KARAMABLOG_URL
        ),
        
        title("Contact & Support"),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        link_button(
            "Linktree",
            "The rest of cakes are a lie",
            "/icons/tree.svg",
            const.LINKTREE_URL
        ),
         link_button(
            "Buy me a cafelito",
            "Every coffee is deeply appreciated!",
            "/icons/coffee.svg",
            const.COFFEE_URL
        ),

        rx.cond(
            featured,
            rx.chakra.vstack(
                title("Based on"),
                rx.chakra.responsive_grid(
                    rx.foreach(
                        featured,
                        featured_link
                    ),
                    columns=[1],
                    spacing=Size.DEFAULT.value,
                ),
                width="100%",
                align_items="center",
                spacing=Size.MEDIUM.value
            )
        ),
        width="100%",
        spacing=Size.DEFAULT.value,
    )
