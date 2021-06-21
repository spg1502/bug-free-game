import pyglet


# TODO: figure out how to pass x,y coordinates based on scaling window, or decide to lock window resolution
def create_h1_label(text, x_start=0, y_start=0, batch=None):
    return pyglet.text.Label(
        text=text,
        x=x_start,
        y=y_start,
        anchor_x="center",
        anchor_y="center",
        # define font_name here
        font_size=62,
        color=(255, 255, 255, 255),
        batch=batch,
    )


def create_h2_label(text, x_start=0, y_start=0, selected=False, batch=None):
    return pyglet.text.Label(
        text=text,
        x=x_start,
        y=y_start,
        anchor_x="center",
        anchor_y="center",
        # define font_name here
        font_size=42,
        color=(255, 255, 255, 255 if selected else 76),
        batch=batch,
    )


def create_menu_labels(texts, x_start=0, y_start=0, batch=None, y_step=80):
    menu = []
    y = y_start
    for i in range(len(texts)):
        is_selected = i == 0
        menu_item = create_h2_label(texts[i], x_start, y, is_selected, batch)
        menu.append(menu_item)
        y -= y_step

    return menu


def create_debug_label(text, x_start=0, y_start=0, batch=None):
    return pyglet.text.Label(
        text=text,
        x=x_start,
        y=y_start,
        anchor_x="left",
        anchor_y="top",
        # define font_name here
        font_size=9,
        color=(204, 0, 0, 255),
        batch=batch,
    )
