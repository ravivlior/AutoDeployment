import shutil
import xml.etree.ElementTree
import os

## copy files
# src = "/home/ravivl/PycharmProjects/db/1/data.txt"
# dst = "/home/ravivl/PycharmProjects/db/2"
# shutil.copy2(src,dst)

## copy folder
# src = "/home/ravivl/PycharmProjects/db/1/dataFolder"
# dst = "/home/ravivl/PycharmProjects/db/2/newDataFolder"
# shutil.copytree(src,dst)

## update XML element text
# xmlFile = xml.etree.ElementTree.parse('/home/ravivl/PycharmProjects/db/1/file.xml')
# xmlFile.find('.//item[2]/price').text = '111'

## update XML element attribute
# xmlFile = xml.etree.ElementTree.parse('/home/ravivl/PycharmProjects/db/1/file.xml')
# sh = xmlFile.find('.//item[2]/price')
# sh.set('attributeName', 'value')

## add Element to XML
# xmlFile = xml.etree.ElementTree.parse('/home/ravivl/PycharmProjects/db/1/file.xml')
# new_tag = xml.etree.ElementTree.SubElement(xmlFile.find('.//item[2]'), 'newElement')
# new_tag.text = 'body text'
# new_tag.attrib['x'] = '1' # must be str; cannot be an int
# new_tag.attrib['y'] = 'abc'

## Write back to file
# xmlFile.write('/home/ravivl/PycharmProjects/db/1/file_new.xml')

# run CLI commands
os.system ('ls')