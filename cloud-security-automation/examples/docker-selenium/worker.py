"""Smoke check against a local synthetic page; one isolated result per worker."""
import json, os, socket, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    started=time.monotonic()
    options=webdriver.ChromeOptions()
    options.binary_location='/usr/bin/chromium'
    options.add_argument('--headless=new')
    options.add_argument('--disable-dev-shm-usage')
    # Container-only Chromium execution; run this image against the bundled fixture only.
    options.add_argument('--no-sandbox')
    result={'worker':socket.gethostname(),'fixture':'synthetic-local-page','status':'failed'}
    try:
        with webdriver.Chrome(service=Service('/usr/bin/chromedriver'),options=options) as driver:
            driver.set_page_load_timeout(20)
            driver.get('http://demo-site:8000/')
            field=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.ID,'reference')))
            field.send_keys('DEMO-001')
            driver.find_element(By.ID,'lookup').click()
            WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.ID,'result'),'DEMO-001 | ready'))
            result['status']='passed'
    except Exception as exc:
        result['error_type']=type(exc).__name__
    result['elapsed_seconds']=round(time.monotonic()-started,3)
    print(json.dumps(result),flush=True)
    return 0 if result['status']=='passed' else 1
if __name__=='__main__': raise SystemExit(main())
