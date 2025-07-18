# Scraping Dynamic Loaded Data

I needed to scrape a website where the data was dynamically loaded in a PDF with watermarked pages. The content wasn't available in static HTML - it only loaded as you scrolled through the document. Here's how I solved it.

## The Problem

- Website had 25 pages but only showed 3 in static HTML
- Content loaded dynamically as you scrolled down
- Pages had watermarks and background images that made text hard to read
- Needed to capture all the content in a clean, readable format

## Requirements

- Python 3.7+
- Chrome/Chromium browser
- ChromeDriver (automatically managed by Selenium)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/educational-document-scraper.git
cd educational-document-scraper
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```bash
python clean_white_bg_capture.py output_document.pdf
```

## File Structure

```
educational-document-scraper/
├── clean_white_bg_capture.py    # Main script
├── requirements.txt             # Python dependencies
├── README.md                   # This file
├── LICENSE                     # MIT License
└── .gitignore                  # Git ignore file
```

## My Solution

1. **Browser Automation**: Used Selenium WebDriver to load the page
2. **Progressive Scrolling**: Scrolled through the document to trigger lazy loading of all 25 pages
3. **Content Capture**: Captured all visible content including text overlays
4. **Clean Output**: Removed watermarks and background images with CSS manipulation
5. **PDF Generation**: Used Chrome's print-to-PDF for high-quality output

## What I Learned

- **Dynamic Content**: Many websites load content progressively to improve performance
- **Browser Automation**: Selenium can handle JavaScript-heavy sites that traditional scrapers can't
- **CSS Manipulation**: You can modify page styling in real-time to clean up content
- **PDF Generation**: Chrome's print-to-PDF captures both HTML elements and their visual styling
- **Scroll Timing**: Need to balance speed vs. ensuring all content loads properly

## Configuration

### Chrome Options
The tool uses optimized Chrome options for document capture:
- Headless mode for server deployment
- Disabled security features for content access
- Optimized window sizing for document capture

### PDF Settings
- Paper size: Letter (8.5" x 11")
- Margins: Minimal for maximum content
- Scale: Optimized for readability
- Background: Optional (clean vs. original)

## Troubleshooting

### Common Issues

**Chrome driver not found**:
```bash
# Install ChromeDriver manually or use:
pip install webdriver-manager
```

**Content not loading**:
- Increase scroll delays in the script
- Check internet connection
- Verify the document URL is accessible

**PDF quality issues**:
- Adjust the scale parameter in print options
- Modify window size settings
- Use clean white background mode

### Performance Tips

- Use clean white background for faster processing
- Reduce scroll delays for faster execution
- Set appropriate timeouts for your internet speed

## Note

This was built for personal use to access content I had legitimate access to. Always respect website terms of service and copyright laws.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Selenium WebDriver for browser automation
- Chrome DevTools Protocol for PDF generation
- PIL for image processing
- ReportLab for PDF manipulation

## Disclaimer

This was a personal project to solve a specific scraping challenge. Use responsibly and respect website terms of service.