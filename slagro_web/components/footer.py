import reflex as rx


def footer() -> rx.Component:
    return rx.hstack(
        rx.text(
            "FOOTER SLAGRO_WEB",
            height="40",
            position="sticky",
            bg="blue",
            padding_x="16px",
            padding_y="16px",
            width="100%",
            z_index="999",
        ),
        width="100%",
    )
