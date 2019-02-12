import appscript
from commonFunctions.util import Utils
from appium import webdriver
import time
from commonFunctions.session_handler import Session


class ConfigSetup:

    current_config = {}

    @staticmethod
    def start_appium_server():
        if not Utils.check_appium_is_already_running():
            appscript.app('terminal').do_script('appium --address 127.0.0.1 --port 4723')
            time.sleep(4)
            print("Appium is started")
        else:
            print("Appium is already running")

    def __init__(self):
        self.driver = None

    def launch_app(self):

        app_name = ConfigSetup.current_config['appName']
        platform_name = ConfigSetup.current_config['platformName']
        platform_version = ConfigSetup.current_config['platformVersion']
        device_name = ConfigSetup.current_config['deviceName']
        udid = ConfigSetup.current_config['udid']

        print("Launching app with below config, for scenario : {}".format(ConfigSetup.current_config['scenario_name']))
        print("app {0} platformName {1} platformVersion {2} deviceName {3} udid {4}".format(app_name, platform_name,
                                                                                            platform_version, device_name,
                                                                                            udid))
        dc = {
            "app": "/Users/nagendraa/Nagendra/preparationDocs/apps/{}".format(app_name),
            "platformName": "{}".format(platform_name),
            "platformVersion": "{}".format(platform_version),
            "deviceName": "{}".format(device_name),
            "automationName": "appium",
            "udid": "{}".format(udid),
            # "noReset": True,
            "newCommandTimeout": 60
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dc)
        Session.session_config_instance[self.driver] = ConfigSetup.current_config

    def get_driver(self):
        return self.driver



