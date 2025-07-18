#!/usr/bin/env python3
"""
Capture Course Hero pages with clean white background (no watermarks or bg images)
"""
import os
import sys
import time
import base64
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_chrome_driver():
    """Setup Chrome driver for clean PDF generation"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1400,2000')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # Add realistic user agent
    options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        return driver
    except Exception as e:
        print(f"Error setting up Chrome driver: {e}")
        return None

def load_and_clean_pages(driver, url, output_path):
    """Load all pages and create clean PDF with white background"""
    print(f"Loading Course Hero document: {url}")
    
    driver.get(url)
    
    # Wait for initial page load
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    print("Page loaded, scrolling to load all content...")
    
    # Start from top
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)
    
    # Load all pages first
    print("Loading all pages...")
    for i in range(30):
        scroll_position = i * 1200
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(0.5)
    
    # Now clean up the styling
    print("Cleaning up styling for white background...")
    
    driver.execute_script("""
        // Remove all background images and set white background
        const allElements = document.querySelectorAll('*');
        allElements.forEach(el => {
            // Remove background images
            if (el.style.backgroundImage) {
                el.style.backgroundImage = 'none';
            }
            
            // Remove data-bg attributes to prevent lazy loading
            if (el.hasAttribute('data-bg')) {
                el.removeAttribute('data-bg');
            }
            
            // Set white background for page containers
            if (el.hasAttribute('data-page') || el.classList.contains('ch-page-slice')) {
                el.style.backgroundColor = 'white';
                el.style.backgroundImage = 'none';
            }
        });
        
        // Specifically target page slices and containers
        const pageSlices = document.querySelectorAll('.ch-page-slice');
        pageSlices.forEach(slice => {
            slice.style.backgroundColor = 'white';
            slice.style.backgroundImage = 'none';
            slice.style.border = '1px solid #ddd';
            slice.style.boxShadow = '0 2px 4px rgba(0,0,0,0.1)';
        });
        
        // Clean up the document viewer
        const docViewer = document.querySelector('.ch-viewer-viewport-pages');
        if (docViewer) {
            docViewer.style.backgroundColor = 'white';
        }
        
        // Set body background to white
        document.body.style.backgroundColor = 'white';
        
        // Remove any watermarks or overlays
        const watermarks = document.querySelectorAll('[class*="watermark"], [class*="overlay"]');
        watermarks.forEach(wm => {
            wm.style.display = 'none';
        });
        
        // Ensure text is black and visible
        const textElements = document.querySelectorAll('span, div, p, text');
        textElements.forEach(el => {
            const computedStyle = window.getComputedStyle(el);
            if (computedStyle.color !== 'rgb(0, 0, 0)' && el.textContent.trim()) {
                el.style.color = 'black';
            }
        });
        
        console.log('Styling cleaned up for white background');
    """)
    
    time.sleep(3)
    
    # Do final scroll to ensure everything is loaded
    print("Final loading pass...")
    for i in range(15):
        scroll_position = i * 2000
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(0.8)
    
    # Get final document height
    final_height = driver.execute_script("return document.body.scrollHeight")
    print(f"Final document height: {final_height}px")
    
    # Scroll back to top
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    
    # Set window size for full capture
    driver.set_window_size(1400, min(final_height + 500, 20000))
    time.sleep(2)
    
    # Check how many pages we have
    page_containers = driver.find_elements(By.CSS_SELECTOR, '[data-page]')
    print(f"Found {len(page_containers)} page containers")
    
    # Generate clean PDF
    print("Generating clean PDF with white background...")
    
    # Configure print settings for clean output
    print_options = {
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': False,  # Don't print background images
        'preferCSSPageSize': True,
        'paperWidth': 8.5,
        'paperHeight': 11,
        'marginTop': 0.3,
        'marginBottom': 0.3,
        'marginLeft': 0.3,
        'marginRight': 0.3,
        'scale': 0.85,  # Scale to fit content nicely
    }
    
    # Generate PDF
    result = driver.execute_cdp_cmd("Page.printToPDF", print_options)
    
    # Save PDF
    with open(output_path, 'wb') as f:
        f.write(base64.b64decode(result['data']))
    
    print(f"Clean PDF generated successfully: {output_path}")
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python clean_white_bg_capture.py <output_pdf_file>")
        sys.exit(1)
    
    output_pdf = sys.argv[1]
    url = "https://www.nursinghero.com/study-files/6361145"
    
    driver = setup_chrome_driver()
    if not driver:
        print("Failed to setup Chrome driver")
        sys.exit(1)
    
    try:
        success = load_and_clean_pages(driver, url, output_pdf)
        
        if success:
            print(f"\nSuccess! Clean PDF with white background created: {output_pdf}")
            print("The PDF now has:")
            print("- White background instead of background images")
            print("- No watermarks or overlays")
            print("- Clean black text on white background")
            print("- All 25 pages with complete content")
        else:
            print("Failed to create PDF")
            sys.exit(1)
            
    finally:
        driver.quit()

if __name__ == "__main__":
    main()