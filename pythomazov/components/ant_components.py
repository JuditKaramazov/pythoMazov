import reflex as rx
import pythomazov.styles.styles as styles
from pythomazov.styles.colors import Color


class BackTop(rx.Component):
    library = "antd"
    tag = "FloatButton.BackTop"
    visibility_height = 400
    style: dict = styles.back_top_style


back_top = BackTop.create
