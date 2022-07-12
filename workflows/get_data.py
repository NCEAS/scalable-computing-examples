import requests
import xml.etree.ElementTree as ET
import os


def download_csvs():

    if not os.path.exists("data"):
        os.makedirs("data")

    xmlresp = requests.get("https://arcticdata.io/metacat/d1/mn/v2/object/urn%3Auuid%3A0b0a5a34-a950-4685-a6d1-76714116ac82")

    root = ET.fromstring(xmlresp.content)

    urls = root.findall("./dataset/dataTable/physical/distribution/online/url")
    filenames = root.findall("./dataset/dataTable/entityName")

    file_pairs = {filenames[i].text[:4]: urls[i].text for i in range(len(urls))}

    for yr in list(file_pairs.keys()):
        resp = requests.get(file_pairs[yr])
        out = "data/" + yr + ".csv"
        open(out, "wb").write(resp.content)


download_csvs()