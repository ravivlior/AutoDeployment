import shutil
import xml.etree.ElementTree

# copy files
# src = "/home/ravivl/PycharmProjects/db/1/data.txt"
# dst = "/home/ravivl/PycharmProjects/db/2"
# shutil.copy2(src,dst)
#
# copy folder
# src = "/home/ravivl/PycharmProjects/db/1/dataFolder"
# dst = "/home/ravivl/PycharmProjects/db/2/newDataFolder"
# shutil.copytree(src,dst)

# update XML file
xmlFile = xml.etree.ElementTree.parse('/home/ravivl/PycharmProjects/db/1/file.xml')
new_tag = xml.etree.ElementTree.SubElement(xmlFile.getroot(), 'itemXXX')
new_tag.text = 'body text'
new_tag.attrib['x'] = '1' # must be str; cannot be an int
new_tag.attrib['y'] = 'abc'

# Write back to file
#et.write('file.xml')
xmlFile.write('/home/ravivl/PycharmProjects/db/1/file_new.xml')