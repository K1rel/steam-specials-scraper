

def extract_attribute(div, config):
    if config["method"] == "css":
        elements = div.css(config["selector"])
        element = elements[config.get("index", 0)] if elements else None
    elif config["method"] == "css_first":
        element = div.css_first(config["selector"])
    
    if not element:
        return None

    if config["type"] == "text":
        return element.text()
    elif config["type"] == "attribute":
        return element.attributes.get(config["attribute_name"])

    return None


def extract_tags(div, config):
    elements = div.css(config["selector"])
    return [element.text() for element in elements[:config["limit"]]]


def extract_release_date(div, config):
    parent_element = div.css_first(config["parent_selector"])
    for _ in range(config["parent_hops"]):
        if parent_element:
            parent_element = parent_element.parent
    return parent_element.css_first(config["selector"]).text() if parent_element else None
