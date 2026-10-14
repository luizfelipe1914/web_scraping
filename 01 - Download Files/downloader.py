import requests
from tqdm import tqdm
import argparse
from bs4 import BeautifulSoup



#Retrieves a main URL from the CLI. This URL is from an HTML page containing file URLs.
def get_opts():
    parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
    parser.add_argument("-U", "--url", nargs="?", help="URL")
    parser.add_argument("-F", "--file_type", nargs="?", help="File extension")
    return parser.parse_args()


# Extract file URLs
def get_files_urls(url: str, file_type: str) -> list[str]:
    urls = []
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all("a")
        for link in links:
            file_url = link.get('href')
            if file_url:
                if file_url.endswith(f".{file_type}") and file_url not in urls:
                    urls.append(file_url)
    except Exception as err:
        print(err)
    return urls
    


# Download file

def download_file(url: str):
    filepath = url.split("/")[-1]
    response = requests.get(url=url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers["content-length"])
        block_size = 1024
        with tqdm(total=total_size, unit="B", unit_scale=True, desc=filepath) as progress_bar:
            with open(filepath, "wb") as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)



def main():
    opts = get_opts()
    for file in get_files_urls(url=opts.url, file_type=opts.file_type):
        download_file(url=file)

if __name__ == "__main__":
    main()