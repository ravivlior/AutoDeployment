import shutil
import xml.etree.ElementTree
import os

## delete file
# if os.path.exists('/home/ravivl/PycharmProjects/db/2/file.xml'):
#   os.remove('/home/ravivl/PycharmProjects/db/2/file.xml')
# else:
#   print("The file does not exist")

## copy files
# src = "/home/ravivl/PycharmProjects/db/1/data.txt"
# dst = "/home/ravivl/PycharmProjects/db/2"
# shutil.copy2(src,dst)

## delete folder
# shutil.rmtree('/home/ravivl/PycharmProjects/db/2/DataFolder')

## create folder
# os.mkdir ('/home/ravivl/PycharmProjects/db/2/dataFolder1')

## copy folder
# src = "/home/ravivl/PycharmProjects/db/1/dataFolder"
# dst = "/home/ravivl/PycharmProjects/db/2/DataFolder"
# shutil.copytree(src,dst)

## update XML element text
# xmlFile = xml.etree.ElementTree.parse('/home/ravivl/PycharmProjects/db/1/file.xml')
# xmlFile.find('.//item[2]/price').text = '111'

## update XML element attribute
# xmlFile = xml.etree.ElementTree.parse('/home/ravivl/PycharmProjects/db/1/file.xml')
# sh = xmlFile.find('.//item')
# sh.set('orderid', '101010')

## add Element to XML
# xmlFile = xml.etree.ElementTree.parse('/home/ravivl/PycharmProjects/db/1/file.xml')
# new_tag = xml.etree.ElementTree.SubElement(xmlFile.find('.//item[2]'), 'newElement')
# new_tag.text = 'body text'
# new_tag.attrib['x'] = '1' # must be str; cannot be an int
# new_tag.attrib['y'] = 'abc'

## Write back to file
# xmlFile.write('/home/ravivl/PycharmProjects/db/2/file.xml')

# run CLI commands
os.system ('ifconfig')