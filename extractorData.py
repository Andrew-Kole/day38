import requests
import selectorlib as sl

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url=URL, headers=HEADERS):
    response = requests.get(url,headers)
    content = response.text
    return content


def extract_temperature(source):
    extractor = sl.Extractor.from_yaml_file("files/extract.yaml")
    temperature = extractor.extract(source)["temperature"]
    return temperature


def extract_label(source):
    extractor = sl.Extractor.from_yaml_file("files/extract.yaml")
    label = extractor.extract(source)["label"]
    return label


if __name__ == "__main__":
    source = scrape()
    print(source)
    temperature = extract_temperature(source)
    print(temperature)
    print(extract_label(source))