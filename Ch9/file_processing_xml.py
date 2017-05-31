'''
xml格式為以下方式
<?xml version="1.0"?>
<root>
  <tag1 attr1=a1...>
    <tag2>82</tag2>
    <tag3>87</tag3>
    ....
  </tag1>
...
</root> 

'''

import xml.etree.ElementTree as ET #簡稱模組名稱為ET

def main():
    tree = ET.ElementTree(file = 'student.xml')
    print(type(tree))

    root = tree.getroot()   #取得該xml格式的root節點
    print(type(root))
    print(root.tag,root.attrib) #由於該節點沒有attrib，故會印空值{}出來
    print()

    for child in root:      #取得root底下的子節點 (student)的值
        print(child.tag,child.attrib)

    print(root[0][1].text)  
    #root[0]是將索引移到root底下第一個child，然後再移動到child中第2個child。再透過.text取得tag裡面的內容

if __name__ == '__main__':
    main()