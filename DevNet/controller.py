from csv import excel
from webex_bot.models.command import Command
from task1 import get_device_info
from task2 import get_config_info
from task3 import excel_read

class Device(Command):
    def __init__(self):
        super().__init__(
            command_keyword="device",
            help_message="Get device info",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        response = get_device_info()
        response_message = "{0:23}{1:17}{2:12}{3:18}{4:12}".format("hostname","mgmt IP","serial","SW Version","Uptime")

        for device in response['response']:
            uptime = "N/A" if device['upTime'] is None else device['upTime']

            if  device['serialNumber'] is not None and "," in device['serialNumber']:
                serialPlatformList = zip(device['serialNumber'].split(","))
            else:
                serialPlatformList = [(device['serialNumber'])]
            for (serialNumber) in serialPlatformList:
                response_message += "{0:23}{1:17}{2:12}{3:18}{4:12}".format(device['hostname'],device['managementIpAddress'],serialNumber,
                            device['softwareVersion'],
                            uptime)
        return response_message

class Config(Command):
    def __init__(self):
        super().__init__(
            command_keyword="config",
            help_message="Get config info",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        response_message = get_config_info()
        return response_message

class Excel(Command):
    def __init__(self):
        super().__init__(
            command_keyword="",
            help_message="Type company name for lookup",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        result = excel_read(message)
        if result == None:
            response_message = """Sorry, there is no data about this company. Check your message for typo, or try other commands like /device and /config!"""
        else:
            response_message = f"Company: {result[0]}\nManager: {result[1]}\nEmail: {result[2]}"
        return response_message