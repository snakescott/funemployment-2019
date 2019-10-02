from bs4 import BeautifulSoup
from os.path import join
from itertools import chain
from csv import DictWriter

def dump_links(links, f):
    fieldnames = ["text", "href", "issue"]
    w = DictWriter(f, fieldnames)
    w.writeheader()
    w.writerows(links)

def all_links():
    return list(chain.from_iterable(yield_links("/Users/jhscott/src/sre_weekly", 1, 188)))


def yield_links(root_dir, low, high):
    for issue in range(low, high):
        with open(join(root_dir, "{issue}.html".format(issue=issue)), "r") as f:
            text = f.read()
        yield links_for_issue(issue, text)


def links_for_issue(issue_num, text):
    for link in extract_outage_links(text):
        d = anchor_to_dict(link)
        d["issue"] = issue_num
        yield d


def anchor_to_dict(anchor):
    return {
        "text": anchor.text,
        "href": anchor.attrs["href"]
    }

def extract_outage_links(text):
    soup = BeautifulSoup(text, 'html.parser')

    outage_ul = soup.find(attrs={'class': 'sreweekly-outages'})
    if not outage_ul:
        return []
    outage_li = outage_ul.find_all("li")
    outage_links = [li.find("a") for li in outage_li]
    return filter(None, outage_links)




