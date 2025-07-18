# Educational Document Scraper

A Python tool for converting dynamically loaded web documents into clean, readable PDFs. Built to handle JavaScript-rendered content and provide clean output for studying.

## What We Built

- 🔄 **Dynamic Content Loading** - Scrolls through pages to trigger lazy loading
- 📄 **Clean PDF Output** - Removes watermarks and background images
- 🎯 **Complete Page Extraction** - Captures all pages from preview mode
- 🧹 **Content Cleaning** - Generates clean white background PDFs
- 📱 **Browser Automation** - Uses Selenium WebDriver for content capture

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

## How It Works

1. **Page Loading**: Uses Selenium WebDriver to load the document
2. **Dynamic Content**: Scrolls through pages to trigger lazy loading
3. **Content Extraction**: Captures all visible content including text and images
4. **Styling Options**: Applies clean white background or preserves original
5. **PDF Generation**: Uses Chrome's print-to-PDF for high-quality output

## Technical Details

- **Browser Automation**: Selenium WebDriver with Chrome
- **Content Detection**: CSS selectors and JavaScript execution
- **PDF Generation**: Chrome DevTools Protocol print-to-PDF
- **Image Processing**: PIL for image manipulation
- **Layout Preservation**: Maintains original document structure

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

## Legal Note

This tool is for educational and personal use only. Ensure you comply with website terms of service and copyright laws.

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

This tool is provided for educational purposes only. Always respect website terms of service and copyright laws.