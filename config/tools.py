from utils.process import apply_transformation

def extract_attribute(div, config):
   
    if config["method"] == "css":
        elements = div.css(config["selector"])
        element = elements[config.get("index", 0)] if elements else None
    elif config["method"] == "css_first":
        element = div.css_first(config["selector"])
    
    if not element:
        return None

    transformation_args = []
    if "attribute_name" in config:  
        transformation_args.append(config["attribute_name"])

    if "transformation" in config:
        return apply_transformation(element, config["transformation"], *transformation_args)
    
   
    return element.text() if element else None

def extract_tags(div, config):
   
    elements = div.css(config["selector"])
    tags = [element for element in elements[:config["limit"]]]
    
   
    if "transformation" in config:
        return [apply_transformation(tag, config["transformation"]) for tag in tags]
    
    return tags

def extract_release_date(div, config):
   
    parent_element = div.css_first(config["parent_selector"])
    for _ in range(config["parent_hops"]):
        if parent_element:
            parent_element = parent_element.parent

    
    if parent_element:
        raw_date = parent_element.css_first(config["selector"]).text() if parent_element.css_first(config["selector"]) else None
        if raw_date and "transformation" in config:
            return apply_transformation(raw_date, config["transformation"])
        return raw_date
    
    return None

