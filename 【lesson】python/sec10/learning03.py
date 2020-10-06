# import xml.etree.ElementTree as ET
# import xml.dom.minidom as minidom

# data_list = [
#     {
#         "id":"0001",
#         "name":"TaroYamada",
#         "type":"regularEmployee"
#     },
#     {
#         "id":"0002",
#         "name":"HanakoIto",
#         "type":"partTime"

#     }
# ]

# root = ET.Element("employee")
# for data in data_list:
#     user_elm = ET.SubElement(root, "user")
#     user_elm.attrib = {"type": data["type"]}

#     id_elm = ET.SubElement(user_elm, "id")
#     id_elm.text = data["id"]

#     name_elm = ET.SubElement(user_elm, "name")
#     name_elm.text = data["name"]


# filename = r"C:\Users\r_sas\Desktop\hello_sublime\sec10\xml_sample.xml"
# doc = minidom.parseString(ET.tostring(root, "utf-8"))
# with open(filename, "w", encoding= "utf-8") as f:
#     doc.writexml(f, addindent="     ", newl="\n", encoding="utf-8")



import pprint
import xml.etree.ElementTree as ET
    
data_list = []

filename = r"C:\Users\r_sas\Desktop\hello_sublime\sec10\xml_sample.xml"
root = ET.ElementTree(file=filename).getroot()

for user in root:
    user_info = {}
    user_info["type"] = user.attrib["type"]

    for data in user:
        user_info[data.tag] = data.text

    data_list.append(user_info)

pprint.pprint(data_list)