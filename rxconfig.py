import reflex as rx

config = rx.Config(
    app_name="pythomazov",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://pythomazov.reflex.run",
        "https://pythomazov.tech"
    ]
)
