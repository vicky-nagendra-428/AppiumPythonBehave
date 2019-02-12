from commonFunctions.config import ConfigSetup as Config
from commonFunctions.util import Utils
from commonFunctions.session_handler import Session


def before_feature(context, feature):
    print("==============================> In before feature")
    Config.start_appium_server()


def after_feature():
    print("==============================> In after feature")


def before_scenario(context, scenario):
    print("==============================> In before scenario")
    device_name = None

    '''from tags get the tag name which contains device name'''
    for eachTag in scenario.tags:
        if eachTag.startswith('device'):
            device_name = eachTag.split("-")[1]
            break

    '''Here desired capabilities are set into current_config of ConfigSetup class'''
    Config.current_config = Utils.read_yaml_get_data_for(r'./externalResources/deviceinfo.yaml', device_name)
    Config.current_config['scenario_name'] = scenario.name
    Session.session_name_config[scenario.name] = Config.current_config


def after_scenario(context, scenario):
    print("==============================> In after scenario")
    Session.kill_current_session(scenario.name)
    pass


