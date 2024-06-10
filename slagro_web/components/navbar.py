import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        navbar_dropdown(),
    )


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def navbar_dropdown() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/sl_logo.png",
                        width="15.25em",
                        height="auto",
                        # border_radius="25%",
                    ),
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.text(
                                    "Productos",
                                    size="4",
                                    weight="medium",
                                ),
                                rx.icon("chevron-down"),
                                weight="medium",
                                variant="ghost",
                                size="3",
                            ),
                        ),
                        rx.menu.content(
                            rx.menu.item("Niveladoras"),
                            rx.menu.item("Compactadoras"),
                            rx.menu.item("Tapadoras"),
                        ),
                    ),
                    navbar_link("Fabricación Blow Molding", "/#"),
                    navbar_link("Contacto", "/#"),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/sl_logo_cuadrado.png",
                        width="2em",
                        height="auto",
                        # border_radius="25%",
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.sub(
                            rx.menu.sub_trigger("Productos"),
                            rx.menu.sub_content(
                                rx.menu.item("Niveladoras"),
                                rx.menu.item("Compactadoras"),
                                rx.menu.item("Tapadoras"),
                            ),
                        ),
                        rx.menu.item("About"),
                        rx.menu.item("Fabricación Blow Molding"),
                        rx.menu.item("Contacto"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )
