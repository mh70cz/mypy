"""
Bite 164. CLI tool: HTML link converter (stdin to stdout)

!cat tst.txt|python bite_164.py

tst.txt:
    
https://www.python.org, Python Homepage
bad data,blabla,123
https://pybit.es/generators.html , Generators are Awesome
more bad data

bogus data, again
https://codechalleng.es/bites/ , Bites of Py
https://stackoverflow.com/a/12927564,How to capture subprocess.call stdout
https://pybit.es/,Our labor of love
https://pybit.es/pages/about.html, About Us
https://nu.nl, Dutch news site

"""

import sys

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


def make_html_links():

    for line in sys.stdin:
        chunks = line.split(",")
        if len(chunks) != 2:
            continue
        
        href = chunks[0].strip()
        name = chunks[1].strip()
        
        if not href.startswith(("http://", "https://")):
            continue

        domain_start = href.index("//") + 2
        domain = href[domain_start:].split("/")[0]
        if domain.endswith((INTERNAL_LINKS)):
            target = ""
        else:
            target = " target=\"_blank\""
                 
            
        print (f"<a href=\"{href}\"{target}>{name}</a>")

if __name__ == '__main__':
    make_html_links()