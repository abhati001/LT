import xml.etree.ElementTree as ET
tree = ET.parse('param.xml')


for elem in tree.iter():
    if(elem.text!=None):
       print(elem.tag, '\t', '\t', ':', '\t', elem.text)


# Here we have to write code to put parsing data above into file
# with enhancing and matching
# the column as per sheet. Pending..............
    
       
