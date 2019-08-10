import argparse
import os
import xml.dom.minidom


def get_list_files(path_dir):
    # get all files in path_dir
    files = os.listdir(path_dir)
    # get list of special files
    xml_files = [f for f in files if f.split('.')[-1] == 'xml']
    return xml_files


def parse_xml_files(path_dir):
    # get info from every xml_files
    list_xml_files = get_list_files(path_dir)
    list_xml_files = [os.path.join(path_dir, f) for f in list_xml_files]
    for f in list_xml_files:
        print(f)
        dom = xml.dom.minidom.parse(f).normalize()
        width = dom.getElementsByTagName("width")[0]
        print("name=" + width.nodeName)
        print("attr=" + width.getAttribute("width"))
        print("attr=" + width.attributes.item(0).value)
        print(width)


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-d', '--dts', help='directory dts')
    parse.add_argument('-g', '--gst', help='directory gst')
    args = parse.parse_args()

    parse_xml_files(args.dts)

    print('End program')


