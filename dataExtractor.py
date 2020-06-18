import os
import json
from PIL import Image


class dataExtractor:

    def __init__(self, outputJsonPath=None, inputPath=None):
        self.outputJsonPath = outputJsonPath
        self.inputPath = inputPath

    def __str__(self):
        return self.outputJsonPath

    def convert(self, size, box, name):
        return (name, box[1] - box[0], box[3] - box[2])

    def processImgSet(self):
        '''
        Checks an img bounding boxes' coordinates and x,y location and returns it.
        '''
        processed_data = []
        with open(f'{self.outputJsonPath}/result_8.json') as jsonFile:
            jsonOutput = json.load(jsonFile)
            for jsonObj in jsonOutput:
                processed_img = []
                for class_tag in jsonObj['objects']:
                    x_min = (class_tag['relative_coordinates']['center_x'] * 1920) - \
                        ((class_tag['relative_coordinates']
                          ['width'] * 1920) / 2)

                    y_max = (class_tag['relative_coordinates']['center_y'] * 1080) + \
                        ((class_tag['relative_coordinates']
                          ['height'] * 1080) / 2)

                    w = ((class_tag['relative_coordinates']['width'] * 1920))
                    h = ((class_tag['relative_coordinates']['height'] * 1080))
                    processed_img.append(
                        (str(class_tag['name']), x_min, y_max, w, h))
                print(processed_img)
                processed_data.append(processed_img)
        return processed_data

    def processRawData(self, data_list=None):
        processed_data = []
        for tag in data_list:
            tag_info = list(tag)
            w = (tag_info[2][2] * 1920)
            h = (tag_info[2][3] * 1080)
            x_min = (tag_info[2][0] * 1920) - (w / 2)
            y_max = (tag_info[2][1] * 1080) - (h / 2)
            processed_data.append([str(tag_info[0]), x_min, y_max, w, h])
        return processed_data


de = dataExtractor(outputJsonPath='json')
de.processImgSet()
