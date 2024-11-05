
SELECTORS = {
    "title": {
        "selector": "div[class*='StoreSaleWidgetTitle']",
        "method": "css_first",
        "type": "text"
    },
    "img_url": {
        "selector": "div[class*='CapsuleImageCtn'] img",
        "method": "css_first",
        "type": "attribute",
        "attribute_name": "src"
    },
    "tags": {
        "selector": "a[class*='WidgetTag']",
        "method": "css",
        "type": "text",
        "limit": 5
    },
    "release_date": {
        "selector": "div + div > div + div > div",
        "method": "css_first",
        "type": "text",
        "parent_selector": "div.StoreSaleWidgetTitle",
        "parent_hops": 2
    },
    "review_score": {
        "selector": "a[class*='ReviewScore'] > div > div",
        "method": "css",
        "type": "text",
        "index": 0
    },
    "reviews_count": {
        "selector": "a[class*='ReviewScore'] > div > div",
        "method": "css",
        "type": "text",
        "index": 2
    },
    "original_price": {
        "selector": "div[class*=StoreSalePriceWidgetContainer] > div + div > div",
        "method": "css",
        "type": "text",
        "index": 0
    },
    "discount_price": {
        "selector": "div[class*=StoreSalePriceWidgetContainer] > div + div > div",
        "method": "css",
        "type": "text",
        "index": 1
    }
}
