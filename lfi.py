import random, time, argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

class colors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

def entryy():
    print("LFI-FINDER --- by github.com/capture0x")

def check_lfi_vulnerability(url):
    print(colors.CBLUE +"Trying payloads list, please wait...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    count = 0
    vulnerable_urls = []
    with open("lfi.txt", "r", encoding="UTF-8") as file:
        payloads = file.readlines()
        try:
            while count < len(payloads):
                target_url = url + payloads[count]
                browser.get(target_url)
                print(colors.CGREEN +"Testing: "+ payloads[count])
                count += 1
                if "root:x:0:0:root" in browser.page_source:
                    vulnerable_urls.append(target_url)
                    print(colors.CRED +"Vuln Url: " +target_url)
                if count == len(payloads):
                    browser.close()
        except NoSuchElementException:
            pass 

    browser.quit()
    return vulnerable_urls

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", "-t", help="Target url")
    args = parser.parse_args()


    entryy()
    target_url = args.target
    vulnerable_urls = check_lfi_vulnerability(target_url)
    
    if vulnerable_urls:
        print("LFI Vulnerability Found!")
        print("Vulnerable URLs:")
        for url in vulnerable_urls:
            print(url)
    else:
        print("No LFI Vulnerability Found.")