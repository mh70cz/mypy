"""  xxx """
from lxml import etree
import xmlformatter

os_type = "Win" # Win | Linux


f_name_in = "TradeRegisterListRequest_orig.xsd"
f_name_out = "TradeRegisterListRequest.xsd"

def main():
    tree = etree.parse(f_name_in)
    root = tree.getroot()
    namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema',}
    annotations = root.findall(".//xs:annotation", namespaces)
    xml_lang = '{http://www.w3.org/XML/1998/namespace}lang'

    for annotation in annotations:
        documentations = annotation.findall("./xs:documentation", namespaces)
        for documentation in documentations:
            att = documentation.attrib
            if att.get(xml_lang, None) == "cs":
                # print(documentation.text)
                pass
            elif att.get(xml_lang, None) == "en":
                #print(documentation.text)
                pass
            elif att.get(xml_lang, None) is None:
                txt = documentation.text
                comment = etree.Comment(txt)
                annotation.insert(0, comment)
                documentation.getparent().remove(documentation)
                # print("delelted: " + str(txt))


    #tree.write(open('output.xml', 'wb'))
    tree.write(open(f_name_out, 'wb'), encoding='utf-8', xml_declaration=True, pretty_print=True)

def add_nl():
    """ přidej odřádkování za '-->'  """
    if os_type == "Linux":
        with open('output.xml') as f:
            read_data = f.read()

        write_data = read_data.replace("--><", "-->\r<")

        with open("output_ref.xml", "w") as wf:
            wf.write(write_data)
    elif os_type == "Win":
        with open(f_name_out, encoding="utf-8") as f:
            read_data = f.read()

        write_data = read_data.replace("--><", "-->\r<")

        with open(f_name_out, "w", encoding="utf-8") as wf:
            wf.write(write_data)


def reformat():
    """ formatuj xml """
    formatter = xmlformatter.Formatter(indent="2", indent_char=" ")
    formatter.format_file(f_name_out)

main()
add_nl()
reformat()
