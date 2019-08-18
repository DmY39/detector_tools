import argparse
import os
import xml.etree.cElementTree as ET


def get_list_files(path_dir):
    # get all files in path_dir
    files = os.listdir(path_dir)
    # get list of special files
    xml_files = [f for f in files if f.split('.')[-1] == 'xml']
    return xml_files


def parse_xml_files(path_dir_xml):
    list_dict = []
    # get info from every xml_files
    # list_xml_files = get_list_files(path_dir)
    # path + name_file
    # list_xml_files = [os.path.join(path_dir, f) for f in list_xml_files]

    # for xml_file in list_xml_files:
    tree = ET.parse(path_dir_xml)
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


def intersection_over_union(rect1, rect2):
    # rect1 = parse_xml_files(path_dir)[0]['rect']
    # rect2 = parse_xml_files(path_dir)[1]['rect']
    xA = max(rect1[0], rect2[0])
    yA = max(rect1[1], rect2[1])
    xB = min((rect1[0]+rect1[2]), (rect2[0]+rect2[2]))
    yB = min((rect1[1]+rect1[3]), (rect2[1]+rect2[3]))

    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    # area for every rect
    boxAArea = (rect1[2] + 1) * (rect1[3] + 1)
    boxBArea = (rect2[2] + 1) * (rect2[3] + 1)

    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou

    # if (rect1[0]+rect1[2]) < rect2[0] or (rect1[1]+rect1[3]) < rect2[1]:
    #     return 0


def comparison_dict(path_dts, path_gst):
    # we get two list with xml_files from different path
    list_xml_dts = get_list_files(path_dts)
    list_xml_gst = get_list_files(path_gst)
    # for every file in every path
    for xml_dts in list_xml_dts:
        for xml_gst in list_xml_gst:
            # we have two xml file with same name
            if xml_dts == xml_gst:
                # get two list dict from two path
                list_dict_dts = parse_xml_files(os.path.join(path_dts, xml_dts))
                list_dict_gst = parse_xml_files(os.path.join(path_gst, xml_gst))
                for i in range(len(list_dict_dts)):
                    for j in range(len(list_dict_gst)):
                        if i == j:
                            print(intersection_over_union(list_dict_dts[i]['rect'], list_dict_gst[i]['rect']))
                print('\n')


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-d', '--dts', help='directory dts')
    parse.add_argument('-g', '--gst', help='directory gst')
    args = parse.parse_args()

    # print(parse_xml_files(args.dts))
    comparison_dict(args.dts, args.gst)
    # print(intersection_over_union(parse_xml_files(args.dts)[0]['rect'], parse_xml_files(args.gst)[0]['rect']))

    print('iou = ', intersection_over_union([774, 355, 71, 25], [774, 355, 75, 30]))
    # print(intersection_over_union(parse_xml_files(args.dts)[0]['rect'], parse_xml_files(args.dts)[1]['rect']))
    print('End program')


