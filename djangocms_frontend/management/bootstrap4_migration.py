from djangocms_bootstrap4.constants import DEVICE_SIZES

from djangocms_frontend import settings


def breakpoints(props):
    lst = []
    for size in DEVICE_SIZES:
        for prop in props:
            if prop == "ml":
                lst.append(f"{size}_ml -> {size}_ms")
            elif prop == "mr":
                lst.append(f"{size}_mr -> {size}_me")
            else:
                lst.append(f"{size}_{prop}")
    return lst


plugin_migrations = {
    "bootstrap4_alerts.Bootstrap4Alerts -> alert.Alert": [
        "alert_context",
        "alert_dismissable -> alert_dismissible",
        "tag_type",
        "attributes",
        "P001",  # additional data migration, see below
        "M001",  # SpacingMixin
        "M002",  # ResponsiveMixin
    ],
    "bootstrap4_badge.Bootstrap4Badge -> badge.Badge": [
        "badge_text",
        "badge_context",
        "badge_pills",
        "attributes",
        "P001",  # additional data migration, see below
    ],
    "bootstrap4_card.Bootstrap4Card -> card.Card": [
        "card_type",
        "card_context -> background_context",
        "card_alignment",
        "card_outline",
        "card_text_color",
        "tag_type",
        "attributes",
        "P001",
        "X002",  # Replace v4 card deck
        "X003",  # Align card_outline and background_context
        "A001_card",  # fix alignment
        "M001",  # SpacingMixin
        "M002",  # ResponsiveMixin
        "M003",  # BackgroundMixin
    ],
    "bootstrap4_card.Bootstrap4CardInner -> card.CardInner": [
        "inner_type",
        "tag_type",
        "attributes",
        "M001",  # SpacingMixin
        "M002",  # ResponsiveMixin
        "M003",  # BackgroundMixin
    ],
    # carousel
    "bootstrap4_collapse.Bootstrap4Collapse -> collapse.Collapse": [
        "siblings",
        "tag_type",
        "attributes",
        "P001",
    ],
    "bootstrap4_collapse.Bootstrap4CollapseContainer -> collapse.CollapseContainer": [
        "identifier -> container_identifier",
        "tag_type",
        "attributes",
    ],
    "bootstrap4_collapse.Bootstrap4CollapseTrigger -> collapse.CollapseTrigger": [
        "identifier -> trigger_identifier",
        "tag_type",
        "attributes",
        "P001",
    ],
    "bootstrap4_content.Bootstrap4Blockquote -> content.Blockquote": [
        "quote_content",
        "quote_origin",
        "quote_alignment",
        "attributes",
        "P001",
        "A001_quote",  # fix alignment
        "M001",  # SpacingMixin
        "M002",  # ResponsiveMixin
        "M003",  # BackgroundMixin
    ],
    "bootstrap4_content.Bootstrap4Code -> content.CodeBlock": [
        "code_content",
        "attributes",
        "P001",
        "M001",  # SpacingMixin
        "M002",  # ResponsiveMixin
        "M003",  # BackgroundMixin
    ],
    "bootstrap4_content.Bootstrap4Figure -> content.Figure": [
        "figure_caption",
        "figure_alignment",
        "attributes",
        "M001",  # SpacingMixin
        "M002",  # ResponsiveMixin
        "M003",  # BackgroundMixin
    ],
    "bootstrap4_grid.Bootstrap4GridContainer -> grid.GridContainer": [
        "container_type",
        "attributes",
        "P001",
        "tag_type",
        "M001",  # SpacingMixin
        "M002",  # ResponsiveMixin
        "M003",  # BackgroundMixin
    ],
    "bootstrap4_grid.Bootstrap4GridRow -> grid.GridRow": [
        "horizontal_alignment",
        "vertical_alignment",
        "gutters",
        "attributes",
        "P001",
        "tag_type",
        "M001",  # SpacingMixin
        "M002",  # ResponsiveMixin
        "M003",  # BackgroundMixin
    ],
    "bootstrap4_grid.Bootstrap4GridColumn -> grid.GridColumn": [
        "column_alignment",
        "() -> text_alignment",
        "attributes",
        "P001",
        "G001",  # fill text_alignment from attributes if possible
        "tag_type",
        "M001",  # SpacingMixin
        "M002",  # ResponsiveMixin
        "M003",  # BackgroundMixin
    ]
    + breakpoints(("col", "order", "ml", "mr", "offset")),
    "bootstrap4_jumbotron.Bootstrap4Jumbotron -> jumbotron.Jumbotron": [
        "fluid -> jumbotron_fluid",
        "(default) -> template",
        "() -> jumbotron_context",
        "() -> jumbotron_opacity",
        "tag_type",
        "attributes",
        "P001",
        "M001",  # SpacingMixin
        "M002",  # ResponsiveMixin
        "M003",  # BackgroundMixin
    ],
    "bootstrap4_link.Bootstrap4Link -> link.Link": [
        "template",
        "name",
        "external_link",
        "anchor",
        "mailto",
        "phone",
        "link_type",
        "target -> link_target",
        "link_context",
        "link_size",
        "link_outline",
        "link_block",
        "internal_link",
        "icon_left",
        "icon_right",
        "file_link",
        "attributes",
        "P001",
        "M001",  # SpacingMixin
    ],
    "bootstrap4_listgroup.Bootstrap4ListGroup -> listgroup.ListGroup": [
        "list_group_flush",
        "tag_type",
        "attributes",
        "P001",
        "M001",  # SpacingMixin
        "M002",  # ResponsiveMixin
    ],
    "bootstrap4_listgroup.Bootstrap4ListGroupItem -> listgroup.ListGroupItem": [
        "list_context",
        "list_state",
        "tag_type",
        "attributes",
        "P001",
    ],
    "bootstrap4_media.Bootstrap4Media -> media.Media": [
        "tag_type",
        "attributes",
        "M002",  # ResponsiveMixin
    ],
    "bootstrap4_media.Bootstrap4MediaBody -> media.MediaBody": [
        "tag_type",
        "attributes",
    ],
    "bootstrap4_picture.Bootstrap4Picture -> image.Image": [
        "template",
        "external_picture",
        "width",
        "height",
        "alignment",
        "caption_text",
        "link_url -> external_link",
        "link_target",
        "link_attributes",
        "use_automatic_scaling",
        "use_no_cropping",
        "use_crop",
        "use_upscale",
        "picture_fluid",
        "picture_rounded",
        "picture_thumbnail",
        "link_page -> internal_link",
        "picture",
        "thumbnail_options",
        "use_responsive_image",
        "attributes",
        "P001",
        "A001_picture",  # fix alignment
        "M002",  # ResponsiveMixin
    ],
    "bootstrap4_tabs.Bootstrap4Tab -> tabs.Tab": [
        "template",
        "tab_type",
        "tab_alignment",
        "tab_index",
        "tab_effect",
        "tag_type",
        "attributes",
        "P001",
        "M001",  # SpacingMixin
    ],
    "bootstrap4_tabs.Bootstrap4TabItem -> tabs.TabItem": [
        "tab_title",
        "tag_type",
        "attributes",
        "M001",  # SpacingMixin
        "P001",
    ],
    "bootstrap4_utilities.Bootstrap4Spacing -> utilities.Spacing": [
        "space_property",
        "space_sides",
        "space_device",
        "space_size",
        "tag_type",
        "attributes",
        "P001",
    ],
}


def p001_left_right_migration(obj, new_obj):
    if "class" in new_obj.attributes:

        def replace(item, old, new):
            if item == old:
                return new
            return item

        def replace_left(item, old, new):
            if item[: len(old)] == old:
                return new + item[len(old) :]
            return item

        classes = new_obj.attributes["class"].split()
        classes = map(lambda x: replace(x, "text-left", "text-start"), classes)
        classes = map(lambda x: replace(x, "text-right", "text-end"), classes)
        classes = map(lambda x: replace(x, "float-left", "float-start"), classes)
        classes = map(lambda x: replace(x, "float-right", "float-end"), classes)
        classes = map(lambda x: replace(x, "border-left", "border-start"), classes)
        classes = map(lambda x: replace(x, "border-right", "border-end"), classes)
        classes = map(lambda x: replace(x, "no-gutter", "g-0"), classes)
        classes = map(lambda x: replace(x, "text-monospace", "font-monospace"), classes)
        classes = map(lambda x: replace(x, "sr-only", "visually-hidden"), classes)
        classes = map(lambda x: replace_left(x, "left-", "start-"), classes)
        classes = map(lambda x: replace_left(x, "right-", "end-"), classes)
        classes = map(lambda x: replace_left(x, "ml-", "ms-"), classes)
        classes = map(lambda x: replace_left(x, "mr-", "me-"), classes)
        classes = map(lambda x: replace_left(x, "pl-", "ps-"), classes)
        classes = map(lambda x: replace_left(x, "pr-", "pe-"), classes)
        new_obj.config["attributes"]["class"] = " ".join(classes)


def x002_replace_card_deck(obj, new_obj):
    if obj.card_type == "card-deck":
        print("* Detected bootstrap v4 card-deck which is not part of bootstrap5")
        print("  Replaced it with Card Layout, grid cards")
        new_obj.config["card_type"] = "row"
    if obj.card_type == "card-deck" or obj.card_type == "card-group":
        new_obj.plugin_type = "CardLayoutPlugin"
        new_obj.ui_item = "CardLayout"
    classes = obj.attributes.get("class", "").split()
    if "h-100" in classes:
        classes.remove("h-100")
        new_obj.config["card_full_height"] = True
        new_obj.config["attributes"]["class"] = " ".join(classes)
    if new_obj.config["card_alignment"] == "text-left":
        new_obj.config["card_alignment"] = "text-start"
    elif new_obj.config["card_alignment"] == "text-right":
        new_obj.config["card_alignment"] = "text-end"


def x003_card_context(obj, new_obj):
    if obj.card_outline:
        new_obj.config["card_outline"] = new_obj.config["background_context"]
        new_obj.config["background_context"] = ""
    else:
        new_obj.config["card_outline"] = ""


def a001_alignment(obj, new_obj, field):
    if field in new_obj.config and new_obj.config[field]:
        new_obj.config[field].replace("text-left", "start")
        new_obj.config[field].replace("text-center", "center")
        new_obj.config[field].replace("text-right", "end")


def m001_spacing_mixin(obj, new_obj):
    classes = new_obj.config["attributes"].get("class", "").split()
    if classes:
        for size, _ in list(settings.SPACER_SIZE_CHOICES) + [("auto", "auto")]:
            if f"m-{size}" in classes:
                classes.remove(f"m-{size}")
                classes.append(f"mx-{size}")
                classes.append(f"my-{size}")
            if f"p-{size}" in classes:
                classes.remove(f"p-{size}")
                classes.append(f"px-{size}")
                classes.append(f"py-{size}")
            for side, _ in settings.SPACER_X_SIDES_CHOICES:
                if f"m{side}-{size}" in classes and not new_obj.config.get(
                    "margin_x", None
                ):
                    new_obj.config["margin_x"] = f"m{side}-{size}"
                    new_obj.config["margin_devices"] = None
                    classes.remove(f"m{side}-{size}")
            for side, _ in settings.SPACER_Y_SIDES_CHOICES:
                if f"m{side}-{size}" in classes and not new_obj.config.get(
                    "margin_y", None
                ):
                    new_obj.config["margin_y"] = f"m{side}-{size}"
                    new_obj.config["margin_devices"] = None
                    classes.remove(f"m{side}-{size}")
            for side, _ in settings.SPACER_X_SIDES_CHOICES:
                if f"p{side}-{size}" in classes and not new_obj.config.get(
                    "padding_x", None
                ):
                    new_obj.config["padding_x"] = f"p{side}-{size}"
                    new_obj.config["padding_devices"] = None
                    classes.remove(f"p{side}-{size}")
            for side, _ in settings.SPACER_Y_SIDES_CHOICES:
                if f"p{side}-{size}" in classes and not new_obj.config.get(
                    "padding_y", None
                ):
                    new_obj.config["padding_y"] = f"p{side}-{size}"
                    new_obj.config["padding_devices"] = None
                    classes.remove(f"p{side}-{size}")
        if classes:
            new_obj.config["attributes"]["class"] = " ".join(classes)
        else:
            new_obj.config["attributes"].pop("class")


def m002_responsive_mixin(obj, new_obj):
    classes = new_obj.config["attributes"].get("class", "").split()
    if classes:
        display = (
            "block",
            "flex",
        )
        hidden = "none"

        visible = True
        hit = False
        responsive = []

        for device, _ in settings.DEVICE_CHOICES:
            stump = f"d-{device}-" if device != "xs" else "d-"
            if f"{stump}{hidden}" in classes and visible:
                visible = False
                hit = True
                classes.remove(f"{stump}{hidden}")
            for type in display:
                if f"{stump}{type}" in classes and not visible:
                    visible = True
                    hit = True
                    classes.remove(f"{stump}{type}")
            if visible:
                responsive.append(device)
        if hit:
            new_obj.config["responsive_visibility"] = responsive
            if classes:
                new_obj.config["attributes"]["class"] = " ".join(classes)
            else:
                new_obj.config["attributes"].pop("class")
        else:
            new_obj.config["responsive_visibility"] = None


def m003_background_mixin(obj, new_obj):
    classes = new_obj.config["attributes"].get("class", "").split()
    if classes:
        for context, _ in settings.COLOR_STYLE_CHOICES:
            if f"bg-{context}" in classes:
                new_obj.config["background_context"] = context
                classes.remove(f"bg-{context}")
        for cls, key in {
            "shadow-none": "none",
            "shadow-sm": "sm",
            "shadow": "reg",
            "shadow-lg": "lg",
        }.items():
            if cls in classes:
                new_obj.config["background_shadow"] = key
                classes.remove(cls)
        if classes:
            new_obj.config["attributes"]["class"] = " ".join(classes)
        else:
            new_obj.config["attributes"].pop("class")


def g001_col_text_alignment(obj, new_obj):
    if obj.column_type != "col":
        print(f"Warning: Break column detected - not supported (id={obj.id})")
    classes = new_obj.config["attributes"].get("class", "").split()
    if "text-left" in classes or "text-start" in classes:
        classes.remove("text-left")
        classes.remove("text-start")
        new_obj.config["text_alignment"] = "start"
    if "text-center" in classes:
        classes.remove("text-center")
        new_obj.config["text_alignment"] = "center"
    if "text-right" in classes or "text-end" in classes:
        classes.remove("text-right")
        classes.remove("text-end")
        new_obj.config["text_alignment"] = "end"
    if classes:
        new_obj.config["attributes"]["class"] = " ".join(classes)
    elif "class" in new_obj.config["attributes"]:
        new_obj.config["attributes"].pop("class")


data_migration = {
    "P001": p001_left_right_migration,
    "X002": x002_replace_card_deck,
    "X003": x003_card_context,
    "A001_quote": lambda x, y: a001_alignment(x, y, "quote_alignment"),
    "A001_figure": lambda x, y: a001_alignment(x, y, "figure_alignment"),
    "A001_picture": lambda x, y: a001_alignment(x, y, "alignment"),
    "A001_card": lambda x, y: a001_alignment(x, y, "card_alignment"),
    "G001": g001_col_text_alignment,
    "M001": m001_spacing_mixin,
    "M002": m002_responsive_mixin,
    "M003": m003_background_mixin,
}
