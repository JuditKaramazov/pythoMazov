import reflex as rx

# Common
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='en'")

preview = "https://raw.githubusercontent.com/JuditKaramazov/InsightsFromJuniorToFutureSeniors/main/images/pythoLogo.png"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@V_Karamazov"}
]

# Index
index_title = "pythoMazov | Let's shake some snakes together!"
index_description = "Judit Lázaro here! Software developer, Spanish Philologist, and Digital Animal of this beautiful realm."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# Courses
courses_title = "pythoMazov | Free learning resources"
courses_description = "Here you'll access some (hopefully useful) courses related to the Digital Realm: let's start with Python!"

courses_meta = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description},
]
courses_meta.extend(_meta)

# Cheatsheets
cheatsheets_title = "pythoMazov | Homemade Cheatsheets"
cheatsheets_description = "You don't need to know everything, but it's essential to know where to find the right information - and what for!"

cheatsheets_meta = [
    {"name": "og:title", "content": cheatsheets_title},
    {"name": "og:description", "content": cheatsheets_description},
]
cheatsheets_meta.extend(_meta)

# Challenges
challenges_title = "pythoMazov | Test yourself!"
challenges_description = "Are you ready to test your skills? It seems it's time for you to go through some katas, games, and projects, then!"

challenges_meta = [
    {"name": "og:title", "content": challenges_title},
    {"name": "og:description", "content": challenges_description},
]
challenges_meta.extend(_meta)
