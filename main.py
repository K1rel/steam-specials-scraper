from config.config import SELECTORS
from config.tools import extract_attribute, extract_release_date, extract_tags
from utils.process import save_to_file
from utils.extract import extract_html
from selectolax.parser import HTMLParser

URL = "https://store.steampowered.com/specials"

if __name__ == "__main__":
   
    tree = HTMLParser(extract_html(URL))

    divs = tree.css('div[class*="gASJ2lL_xmVNuZkWGvrWg"]')

    data = []
    for div in divs:
        attrs = {
            "title": extract_attribute(div, SELECTORS["title"]),
            "img_url": extract_attribute(div, SELECTORS["img_url"]),
            "tags": extract_tags(div, SELECTORS["tags"]),
            "release_date": extract_release_date(div, SELECTORS["release_date"]),
            "review_score": extract_attribute(div, SELECTORS["review_score"]),
            "reviews_count": extract_attribute(div, SELECTORS["reviews_count"]),
            "original_price": extract_attribute(div, SELECTORS["original_price"]).get("amount"),
            "discount_price": extract_attribute(div, SELECTORS["discount_price"]).get("amount"),
            "currency": extract_attribute(div, SELECTORS["original_price"]).get("currency") 
        }
        attrs["discount_perc"] = ((attrs["original_price"] - attrs["discount_price"]) / attrs["original_price"] * 100)
        data.append(attrs)
    save_to_file("extract", data)    

    
      




