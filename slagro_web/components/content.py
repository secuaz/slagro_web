import reflex as rx


def content() -> rx.Component:
    return rx.box(
        rx.image(
            src="sl_logo.png"
        )
    )