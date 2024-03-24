from enum import Flag
import reflex as rx
from pythomazov.api.api import featured
from pythomazov.model.Featured import Featured

USER = "JuditKaramazov"


class PageState(rx.State):

    featured_info: list[Featured]

    async def featured_links(self):
        self.featured_info = await featured()
