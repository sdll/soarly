import json
import os


class Configuration:
    def __init__(self, constantsPath="constants.json"):
        self.constants = self.__init_constants__(constantsPath)
        self.customHierarchyBlueprint = self.__init_custom_hierarchy_blueprint__()
        self.trajectoryBlueprint = self.__init_trajectory_blueprint__()

    def __init_constants__(self, constantsPath="constants.json"):
        settingsDir = os.path.dirname(__file__)
        constantsPath = os.path.join(settingsDir, constantsPath)
        with open(constantsPath) as data:
            try:
                constants = json.load(data)
                return constants
            except ValueError:
                raise ValueError("Could not read constants, aborting")

    def __init_custom_hierarchy_blueprint__(self):
        goto = self.constants["primitives"]["navigation"]
        pickup = self.constants["primitives"]["service"]["PICKUP"]
        dropoff = self.constants["primitives"]["service"]["DROPOFF"]

        blueprint = {
            "ROOT": {
                "GET": {
                    "PICKUP": pickup,
                    "GO_TO_PASSENGER_AT_R": goto,
                    "GO_TO_PASSENGER_AT_G": goto,
                    "GO_TO_PASSENGER_AT_B": goto,
                    "GO_TO_PASSENGER_AT_Y": goto,
                },
                "PUT": {
                    "DROPOFF": dropoff,
                    "GO_TO_PASSENGER_AT_R": goto,
                    "GO_TO_PASSENGER_AT_G": goto,
                    "GO_TO_PASSENGER_AT_B": goto,
                    "GO_TO_PASSENGER_AT_Y": goto,
                },
            }
        }
        return blueprint

    def __init_trajectory_blueprint__(self):
        blueprint = self.constants["trajectory"]
        return blueprint
