from utils.extract import extract_html
from selectolax.parser import HTMLParser


URL = "https://store.steampowered.com/specials"

if __name__ == "__main__":
   
    tree = HTMLParser(extract_html(URL))

    divs = tree.css('div[class*="gASJ2lL_xmVNuZkWGvrWg"]')

    for div in divs:
        parent_for_date = div.css_first("div.StoreSaleWidgetTitle").parent.parent
        attrs = {
            "title" : div.css_first("div[class*='StoreSaleWidgetTitle']").text(),
            "img_url": div.css_first("div[class*=CapsuleImageCtn] img").attributes.get("src"),
            "tags" : [i.text() for i in div.css("a[class*='WidgetTag']")[:5]],
            "release_date": parent_for_date.css_first("div + div > div + div > div").text(),
            "review_score": div.css("a[class*='ReviewScore'] > div  > div")[0].text(),
            "reviews_count": div.css("a[class*='ReviewScore'] > div  > div")[2].text(),
            "original_price": div.css("div[class*=StoreSalePriceWidgetContainer] > div + div > div")[0].text(),
            "discount_price": div.css("div[class*=StoreSalePriceWidgetContainer] > div + div > div")[1].text()

        }

        
        print(attrs)


