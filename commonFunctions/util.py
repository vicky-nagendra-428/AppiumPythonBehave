import socket
import errno
import yaml


class Utils:

    @staticmethod
    def check_appium_is_already_running():

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind(('127.0.0.1', 4723))

        except socket.error as e:
            if e.errno == errno.EADDRINUSE:
                return True
            else:
                return False
        finally:
            s.close()

    @staticmethod
    def read_yaml_get_data_for(file_name, segment):
        try:
            with open(file_name, 'r') as file:
                yaml_doc = yaml.safe_load(file)
                return yaml_doc.get(segment)
        except FileNotFoundError:
            return {}
