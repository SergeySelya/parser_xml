import xml.etree.ElementTree as ET
import xml.dom.minidom

n = []
p = []
a = []

doc = xml.dom.minidom.parse('Hotels.xml')
hotels = doc.getElementsByTagName("Hotel")
root = ET.parse('Hotels.xml')

# selection by condition
for hotel in root.findall('Hotel'):
    name = hotel.find('Name').text
    if 'Hilton' in name and hotel[1][1].text == 'New York':
        n.append(name)  # Name
        p.append(hotel.attrib['Price'])  # Price
        a.append(hotel[1][0].text)  # Address

print(n, '\n', p, '\n', a, '\n')  # list of name,price,address

# create XML format
root = ET.Element('Lists')

names = ET.Element('Names')
for el1 in n:
    name = ET.Element('Name')
    name.text = el1
    names.append(name)
root.append(names)

prices = ET.Element('Prices')
for el2 in p:
    price = ET.Element('Price')
    price.text = el2
    prices.append(price)
root.append(prices)

addresses = ET.Element('Addresses')
for el3 in a:
    address = ET.Element('Address')
    address.text = el3
    addresses.append(address)
root.append(addresses)

# write output in file "parser.xml"
xml_str = ET.tostring(root, encoding="utf-8", method="xml")
output = open('parser.xml', 'wb')
output.write(xml_str)
print(xml_str.decode(encoding="utf-8"))  # output in console
