import requests
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

PROXY_SOURCES = [
    'https://www.proxy-list.download/api/v1/get?type=http',
    'https://www.proxyscan.io/download?type=http',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
    'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all',
    'https://api.openproxylist.xyz/http.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
    'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt',
    'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/UserR3X/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
    # Additional sources
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTP_RAW.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/all.txt',
    'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/https.txt',
    'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt',
    'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt',
    'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/https.txt',
    'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt',
    'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/https.txt',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
    'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt',
    'https://raw.githubusercontent.com/mertguvencli/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/mertguvencli/proxy-list/main/https.txt',
    'https://raw.githubusercontent.com/mertguvencli/proxy-list/main/socks4.txt',
    'https://raw.githubusercontent.com/mertguvencli/proxy-list/main/socks5.txt',
    'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/https.txt',
    'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt',
    'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies_anonymous.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies_http.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies_https.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies_socks4.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies_socks5.txt',
]

PROXY_REGEX = re.compile(r'(\d+\.\d+\.\d+\.\d+):(\d+)')


def fetch_proxies_from_url(url):
    try:
        resp = requests.get(url, timeout=10)
        proxies = PROXY_REGEX.findall(resp.text)
        return [f"{ip}:{port}" for ip, port in proxies]
    except Exception as e:
        print(f"Error fetching from {url}: {e}")
        return []

def get_all_proxies():
    all_proxies = set()
    for url in PROXY_SOURCES:
        proxies = fetch_proxies_from_url(url)
        all_proxies.update(proxies)
    return list(all_proxies)

def test_proxy(proxy, test_url='http://httpbin.org/ip', timeout=5):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    try:
        resp = requests.get(test_url, proxies=proxies, timeout=timeout)
        if resp.status_code == 200:
            return proxy, True
    except Exception:
        pass
    return proxy, False

def main():
    print('Fetching proxies from online sources...')
    start_time = time.time()
    proxies = get_all_proxies()
    fetch_time = time.time() - start_time
    print(f'Found {len(proxies)} proxies in {fetch_time:.1f}s. Starting tests...')
    
    if not proxies:
        print("No proxies found. Exiting.")
        return
    
    good_proxies = []
    tested_count = 0
    max_workers = min(500, len(proxies)) if len(proxies) > 0 else 100
    
    print(f'Testing {len(proxies)} proxies with {max_workers} workers...')
    print('Progress: [' + '.' * 50 + '] 0%')
    
    test_start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(test_proxy, proxy) for proxy in proxies]
        for future in as_completed(futures):
            proxy, is_good = future.result()
            tested_count += 1
            
            if is_good:
                print(f'✓ WORKING: {proxy}')
                good_proxies.append(proxy)
            
            # Show progress every 25 tests or at certain percentages
            if tested_count % 25 == 0 or tested_count == len(proxies):
                percentage = (tested_count / len(proxies)) * 100
                elapsed = time.time() - test_start_time
                rate = tested_count / elapsed if elapsed > 0 else 0
                remaining = (len(proxies) - tested_count) / rate if rate > 0 else 0
                
                # Create progress bar
                progress_filled = int(percentage / 2)  # 50 chars for 100%
                progress_bar = '█' * progress_filled + '.' * (50 - progress_filled)
                
                print(f'\rProgress: [{progress_bar}] {percentage:.1f}% | '
                      f'{tested_count}/{len(proxies)} tested | '
                      f'{len(good_proxies)} working | '
                      f'{rate:.1f} tests/sec | '
                      f'ETA: {remaining:.0f}s', end='')
                
                if tested_count == len(proxies):
                    print()  # New line at completion
    
    # Final results
    total_time = time.time() - start_time
    test_time = time.time() - test_start_time
    success_rate = (len(good_proxies) / len(proxies)) * 100 if len(proxies) > 0 else 0
    
    print(f'\n=== TESTING COMPLETE ===')
    print(f'Total time: {total_time:.1f}s (fetch: {fetch_time:.1f}s, test: {test_time:.1f}s)')
    print(f'Total tested: {tested_count}')
    print(f'Working proxies: {len(good_proxies)}')
    print(f'Success rate: {success_rate:.1f}%')
    print(f'Average test rate: {tested_count/test_time:.1f} tests/second')
    
    if good_proxies:
        with open('working_proxies.txt', 'w') as f:
            for proxy in good_proxies:
                f.write(proxy + '\n')
        print('Saved working proxies to working_proxies.txt')
    else:
        print('No working proxies found.')

if __name__ == '__main__':
    main()
