
import datetime
import re

SELECTORS = {
    "title": {
        "selector": "div[class*='StoreSaleWidgetTitle']",
        "method": "css_first",
        "transformation": "text"
    },
    "img_url": {
        "selector": "div[class*='CapsuleImageCtn'] img",
        "method": "css_first",
        "attribute_name": "src",
        "transformation": "attr"  
    },
    "tags": {
        "selector": "a[class*='WidgetTag']",
        "method": "css",
        "transformation": "text",
        "limit": 5
    },
    "release_date": {
        "selector": "div + div > div + div > div",
        "method": "css_first",
        "transformation": "date_format",
        "parent_selector": "div.StoreSaleWidgetTitle",
        "parent_hops": 2
    },
    "review_score": {
        "selector": "a[class*='ReviewScore'] > div > div",
        "method": "css",
        "transformation": "text",
        "index": 0
    },
    "reviews_count": {
        "selector": "a[class*='ReviewScore'] > div > div",
        "method": "css",
        "transformation": "digit_only",
        "index": 2
    },
    "original_price": {
        "selector": "div[class*=StoreSalePriceWidgetContainer] > div + div > div",
        "method": "css",
        "transformation": "split_price",
        "index": 0
    },
    "discount_price": {
        "selector": "div[class*=StoreSalePriceWidgetContainer] > div + div > div",
        "method": "css",
        "transformation": "split_price",
        "index": 1
    }
}

