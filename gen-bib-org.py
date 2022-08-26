import argparse
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter

def generate(bibstring: str) -> str:
    """
    Generates the required org string
    """
    db = bibtexparser.loads(bibstring)

    orgstring = ""
    for entry in db.entries:
        dummy = BibDatabase()
        dummy.entries = [entry]
        orgstring += "* " + entry["title"].replace("{", "").replace("}", "") + "\n\n#+BEGIN_SRC bibtex\n" + bibtexparser.dumps(dummy) + "#+END_SRC\n"

    return orgstring

def append_entries(bibstring: str):
    """
    Appends the entries into the annotated bibliography
    """
    orgstring = generate(bibstring)
    updates = bibtexparser.loads(bibstring)

    writer = BibTexWriter()
    with open("/home/anirudh/org/papers.bib", "a") as bibfile:
        bibfile.write(writer.write(updates))

    with open("/home/anirudh/org/papers.org", "a") as orgfile:
        orgfile.write(orgstring)

    print("Updated {:d} entries!".format(len(updates.entries)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and write org-mode entry from bibtex")
    parser.add_argument("bibstring", type=str, help="Bibtex string input")
    args = parser.parse_args()

    append_entries(args.bibstring)
