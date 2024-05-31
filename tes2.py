import requests
import os

def scrape_proxy(url, token=None):
    try:
        headers = {}
        if token:
            headers['Authorization'] = f'token {token}'
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch proxies from {url}. Status code: {response.status_code}")
        proxies = response.text.strip().split('\n')
        return proxies
    except Exception as e:
        print(f"Error saat melakukan scraping {url}: {str(e)}")
        return []

def scrape_proxies(urls, token=None):
    all_proxies = []
    for url in urls:
        proxies = scrape_proxy(url, token=token)
        all_proxies.extend(proxies)
    return all_proxies

def check_proxy_file_exists():
    return os.path.exists('proxy.txt')

def scrape_and_save_proxies():
    try:
        # Ambil daftar URL proxy web dari URL yang disediakan
        token = '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'  # Ganti dengan token GitHub Anda
        headers = {'Authorization': f'token {token}'}
        response = requests.get('https://raw.githubusercontent.com/VampXDH/Coba1/main/Tes.txt', headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch proxy URLs. Status code: {response.status_code}")
        web_list = response.text.strip().split('\n')

        # Lakukan scraping proxy dari URL proxy web
        proxies = scrape_proxies(web_list, token=token)

        # Periksa apakah proxy.txt ada, jika ya, hapus
        if check_proxy_file_exists():
            os.remove('proxy.txt')
            print('proxy.txt yang ada dihapus')

        # Tulis proxy ke proxy.txt
        with open('proxy.txt', 'w') as f:
            # Hapus 'http://', 'socks5://', dan 'socks4://' dari setiap proxy
            cleaned_proxies = [proxy.replace('http://', '').replace('socks5://', '').replace('socks4://', '').replace('|http', '') for proxy in proxies]
            f.write('\n'.join(cleaned_proxies))
        print('Proxy disimpan di proxy.txt')
    except Exception as e:
        print('Error saat melakukan scraping dan menyimpan proxy:', str(e))

# Menjalankan fungsi scrape_and_save_proxies sekali saja
scrape_and_save_proxies()
