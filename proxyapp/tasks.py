from celery import shared_task
from .models import Proxy
import requests
from bs4 import BeautifulSoup

@shared_task(bind=True)
def scrape_proxy_list(self):
    url = 'https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc'
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')[1:]  
        proxies = []
        for row in rows:
            cols = row.find_all('td')
            proxies.append({
                'ip': cols[0].text.strip(),
                'port': cols[1].text.strip(),
                'protocol': cols[4].text.strip(),
                'country': cols[3].text.strip(),
                'uptime': cols[6].text.strip()
            })

        for proxy in proxies:
            Proxy.objects.create(**proxy)
    except Exception as e:
        print(f"An error occurred: {e}")
