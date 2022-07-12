import requests
import xml.etree.ElementTree as ET
import os

def download_file(input, output):
    #xmlresp = requests.get(snakemake.input[0])

    #root = ET.fromstring(xmlresp.content)
    root = ET.parse(input)

    urls = root.findall("./dataset/dataTable/physical/distribution/online/url")
    filenames = root.findall("./dataset/dataTable/entityName")

    file_pairs = {filenames[i].text[:4]: urls[i].text for i in range(len(urls))}

    #for yr in list(file_pairs.keys()):
    #    resp = requests.get(file_pairs[yr])
    #    #out = "data/" + yr + ".csv"
    #    open(out, "wb").write(resp.content)

    yr = output[5:9]

    resp = requests.get(file_pairs[yr])
    open(output, "wb").write(resp.content)