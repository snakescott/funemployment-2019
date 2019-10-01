import requests
from bs4 import BeautifulSoup
from itertools import chain

ROOT = "https://status.cloud.google.com"
SUMMARY = "/summary"
COMPONENTS = ['appengine',
 'compute',
 'storage',
 'bigquery',
 'cloud-dataproc',
 'asset-inventory',
 'cloud-datastore',
 'cloud-dev-tools',
 'cloud-dns',
 'cloud-filestore',
 'cloud-firestore',
 'cloud-functions',
 'cloud-iam',
 'cloud-iot',
 'cloud-kms',
 'cloud-memorystore',
 'cloud-ml',
 'cloud-networking',
 'cloud-pubsub',
 'cloud-scheduler',
 'cloud-security-command-center',
 'cloud-spanner',
 'cloud-sql',
 'cloud-tasks',
 'cloudendpoints',
 'composer',
 'cloud-dataflow',
 'container-engine',
 'developers-console',
 'google-stackdriver',
 'cloud-bigtable',
 'support']

def _get(fragment):
    return requests.get(ROOT + fragment).text


def get_all_incident_sources():
    summary_html = _get("/summary")
    soup = BeautifulSoup(summary_html, 'html.parser')
    links = soup.find_all("a")
    links = [link.attrs["href"] for link in links if link.text == "Historic"]
    return links

def incident_uris_for_source(source):
    incidents_html = _get(source)
    soup = BeautifulSoup(incidents_html, 'html.parser')
    links = soup.find_all("a")
    links = [link.attrs["href"] for link in links if link.attrs["href"].startswith(source + "/")]
    return links

def get_all_incidents():
    sources = get_all_incident_sources()
    return list(chain.from_iterable(incident_uris_for_source(source) for source in sources)) 