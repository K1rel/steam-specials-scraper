from time import sleep
from playwright.sync_api import sync_playwright 


def extract_html(URL):

    with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(URL)

            page.wait_for_load_state("load")
            
            last_position = 0
            reached_end = False

            while not reached_end:
            
                page.evaluate("window.scrollBy(0, 800)")
                sleep(2) 

            
                current_position = page.evaluate("() => window.scrollY")
                page_height = page.evaluate("() => document.body.scrollHeight")

                
                if current_position + page.viewport_size['height'] >= page_height:
                    reached_end = True  
                
            
                if current_position == last_position:
                    reached_end = True  
                last_position = current_position
            html = page.inner_html("body")
            browser.close() 
            return html
                   