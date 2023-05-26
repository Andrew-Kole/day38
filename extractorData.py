import requests
import selectorlib as sl

URL = "http://programmer100.pythonanywhere.com/"


def scrape(url=URL):
    response = requests.get(url)
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