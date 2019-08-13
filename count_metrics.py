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
            dict['label'] = class_object

            # find rect for every object
            for rect in obj.findall('bndbox'):
                x_tl = int(rect.find('xmin').text)
                y_tl = int(rect.find('ymin').text)
                width = int(rect.find('xmax').text) - int(rect.find('xmin').text)
                height = int(rect.find('ymax').text) - int(rect.find('ymin').text)
                dict['rect'] = [x_tl, y_tl, width, height]

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


