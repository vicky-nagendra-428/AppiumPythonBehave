

class Session:

    session_name_config = {}
    session_config_instance = {}

    @staticmethod
    def kill_current_session(scenario_name):
        session_config = Session.session_name_config[scenario_name]

        for instance, config in Session.session_config_instance.items():
            if config == session_config:
                print("Trying to close the Session")
                instance.quit()
                print("Closed the instance : {}".format(config))
                break



