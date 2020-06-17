import collisionDetector as cd
import coordsProcessor as cp
import dataExtractor as de


class Test:

    testcases = [
        [
            ('Person', 0, 0, 20, 40),
            ('forklift', 0, 0, 100, 30),
        ],

        [
            ('Person', 0, 500, 20, 40),
            ('forklift', 500, 0, 100, 30),
        ],
        [
            ('Person', 0, 100, 50, 10),
            ('forklift', 100, 0, 100, 70),
        ],
        [
            ('Person', 845.7024, 216.84294000000003, 36.14976, 72.54036),
            ('Person', 745.60416, 236.42819999999998, 32.90304, 76.69511999999999),
            ('forklift', 594.22176, 470.11697999999996, 303.50016, 232.57692),
        ],
        [
            ('Person', 365.45664, 835.60086, 115.69152, 248.63868000000002),
            ('forklift', 538.04544, 873.4041, 417.99936, 398.07396)
        ]
    ]

    def run(self):
        print("working on testcases")
        dataExtractor = de.dataExtractor(outputJsonPath='json')
        self.testcases += (dataExtractor.processImgSet())
        for testcase in self.testcases:
            print('Testcase: ', testcase)
            coordinates_processor = cp.CoordinatesProcessor(testcase)
            coordinates_processor.processBoundingBoxes()
            collision_detector = cd.CollisionDetector(
                coordinates_processor.results)

            print('result: ', collision_detector.processSamples(), end='\n \n \n')


test = Test()
test.run()
