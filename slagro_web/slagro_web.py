import reflex as rx
import slagro_web.styles.styles as styles
from slagro_web.components.header import header
from slagro_web.components.navbar import navbar
from slagro_web.components.footer import footer
from slagro_web.components.content import content


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        header(),
        rx.center(
            rx.vstack(
                navbar(),
                content(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
            )
        ),
        footer(),
    )


app = rx.App(
    styles = styles.BASE_STYLES,
    title = "SL Agro | Sembrar nunca fué tan eficiente",
    description = "Cubiertas semineumáticas para cuerpos de siembra",
    imagen = "sl_logo.png"
    )
app.add_page(index)
