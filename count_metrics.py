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
    [print(f) for f in list_xml_files]

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-d', '--dts', help='directory dts')
    parse.add_argument('-g', '--gst', help='directory gst')
    args = parse.parse_args()

    parse_xml_files(args.dts)
    print(get_list_files(args.gst))

    print('End program')


