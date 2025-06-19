# Proxy Spider & Tester

A high-performance Python tool for automatically discovering, collecting, and validating HTTP/HTTPS proxies from multiple online sources.

## 🚀 Features

- **Multi-Source Collection**: Harvests proxies from 50+ public proxy lists
- **High-Speed Testing**: Concurrent testing with up to 500 workers
- **Real-Time Progress**: Visual progress bar with ETA and performance metrics
- **Multiple Protocols**: Supports HTTP, HTTPS, SOCKS4, and SOCKS5 proxies
- **Smart Deduplication**: Automatically removes duplicate proxies
- **Comprehensive Reporting**: Detailed statistics and success rates
- **Export Functionality**: Saves working proxies to file

## 📋 Requirements

- Python 3.6+
- Required packages:
  ```
  requests
  ```

## 🛠️ Installation

1. Clone or download the repository
2. Install dependencies:
   ```bash
   pip install requests
   ```

## 🚀 Usage

### Basic Usage
```bash
python proxy_spider_tester.py
```

The script will:
1. Fetch proxies from all configured sources
2. Test each proxy for connectivity
3. Display real-time progress and results
4. Save working proxies to `working_proxies.txt`

### Sample Output
```
Fetching proxies from online sources...
Found 2,847 proxies in 12.3s. Starting tests...
Testing 2,847 proxies with 500 workers...
Progress: [████████████████████████████████████████..........] 80.0% | 2,278/2,847 tested | 156 working | 185.2 tests/sec | ETA: 3s
✓ WORKING: 192.168.1.100:8080
✓ WORKING: 203.142.71.52:3128

=== TESTING COMPLETE ===
Total time: 28.7s (fetch: 12.3s, test: 16.4s)
Total tested: 2,847
Working proxies: 156
Success rate: 5.5%
Average test rate: 173.5 tests/second
Saved working proxies to working_proxies.txt
```

## 📊 Performance

- **Speed**: Tests 100-300 proxies per second
- **Efficiency**: Typically finds 5-15% working proxies
- **Scalability**: Handles thousands of proxies simultaneously
- **Resource Usage**: Optimized for minimal memory footprint

## 🔧 Configuration

### Adjusting Thread Count
Modify the `max_workers` parameter in the `main()` function:
```python
max_workers = min(500, len(proxies))  # Adjust 500 to your preference
```

### Changing Test URL
Modify the test URL in the `test_proxy()` function:
```python
def test_proxy(proxy, test_url='http://httpbin.org/ip', timeout=5):
```

### Adding More Sources
Add new proxy sources to the `PROXY_SOURCES` list:
```python
PROXY_SOURCES = [
    'https://your-proxy-source.com/list.txt',
    # ... existing sources
]
```

## 📁 Output Files

- **`working_proxies.txt`**: Contains all validated working proxies (IP:PORT format)

## 🎯 Use Cases

- **Web Scraping**: Building proxy pools for IP rotation
- **Privacy Testing**: Finding anonymous proxies
- **Load Testing**: Distributing requests across multiple IPs
- **Geo-location Testing**: Accessing region-restricted content
- **Security Research**: Analyzing proxy networks

## ⚠️ Important Notes

- **Legal Usage**: Only use proxies for legitimate purposes
- **Rate Limiting**: Some sources may implement rate limiting
- **Proxy Reliability**: Public proxies can be unreliable and short-lived
- **Security**: Never use untrusted proxies for sensitive data

## 🔒 Ethical Considerations

This tool is designed for:
- ✅ Educational purposes
- ✅ Security research
- ✅ Performance testing
- ✅ Development and debugging

**Not intended for:**
- ❌ Malicious activities
- ❌ Bypassing security measures
- ❌ Unauthorized access
- ❌ Illegal activities

## 🐛 Troubleshooting

### Common Issues

1. **No proxies found**
   - Check internet connection
   - Some sources may be temporarily unavailable
   - Firewall may be blocking requests

2. **Low success rate**
   - Public proxies are often unreliable
   - Try running at different times
   - Some proxies may have geographic restrictions

3. **Slow performance**
   - Reduce `max_workers` value
   - Check your internet connection speed
   - Some proxy sources may be slow to respond

### Error Messages

- `Error fetching from [URL]`: Source is unavailable or blocked
- `Connection timeout`: Proxy is not responding
- `Proxy error`: Proxy rejected the connection

## 📈 Statistics

The script provides comprehensive statistics including:
- Total proxies discovered
- Number of working proxies
- Success rate percentage
- Average testing speed
- Time breakdown (fetch vs test)

## 🤝 Contributing

Feel free to contribute by:
- Adding new proxy sources
- Improving error handling
- Optimizing performance
- Adding new features

## 📄 License

This project is for educational and research purposes. Use responsibly and in accordance with applicable laws and terms of service.

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section
2. Verify your Python and dependency versions
3. Test with a smaller number of workers first

---

**Disclaimer**: This tool is provided as-is for educational purposes. Users are responsible for ensuring their usage complies with applicable laws and terms of service.
