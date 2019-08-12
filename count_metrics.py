import argparse
import os
import xml.etree.cElementTree as ET


def get_list_files(path_dir):
    # get all files in path_dir
    files = os.listdir(path_dir)
    # get list of special files
    xml_files = [f for f in files if f.split('.')[-1] == 'xml']
    return xml_files


def parse_xml_files(path_dir):
    list_dict = []
    # get info from every xml_files
    list_xml_files = get_list_files(path_dir)
    # path + name_file
    list_xml_files = [os.path.join(path_dir, f) for f in list_xml_files]

    for xml_file in list_xml_files:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # for every tag 'object' find parameters
        for obj in root.findall('object'):
            dict = {}
            # add key label and item class
            class_object = obj.find('name').text
            dict[os.path.basename(xml_file)] = class_object

            # add key 'rect' and items
            for x_tl in obj.iter('xmin'):
                dict['rect'] = [x_tl.text]
            for y_tl in obj.iter('ymin'):
                dict['rect'].append(y_tl.text)
            for width in root.iter('width'):
                dict['rect'].append(width.text)
            for height in root.iter('height'):
                dict['rect'].append(height.text)
            # add dict in list_dict
            list_dict.append(dict)

    return list_dict


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-d', '--dts', help='directory dts')
    parse.add_argument('-g', '--gst', help='directory gst')
    args = parse.parse_args()

    print(parse_xml_files(args.dts))

    print('End program')


