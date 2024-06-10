import reflex as rx
from slagro_web.styles.fonts import Fonts as font


def header() -> rx.Component:
    return rx.vstack(
        rx.text(
            "SLAGRO_WEB",
            height="40",
            position="sticky",
            bg="blue",
            padding_x="16px",
            padding_y="16px",
            width="100%",
            z_index="999",
            font_family=font.PRIMARY.value
        ),
        width="100%",
    )
