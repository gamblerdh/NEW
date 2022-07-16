from webex_bot.webex_bot import WebexBot
from controller import Device, Excel, Config
#from webex_bot.commands.echo import EchoCommand

webex_token = "MWIzMTNlZmEtZTcyNC00YTVhLTg3MzEtNzg0Y2E3YzkwZDI1NTRlZWE0MWItYjg1_P0A1_8985b8cd-1e49-46dd-a72f-38e504085125"

bot = WebexBot(webex_token)
bot.add_command(Device())
bot.add_command(Excel())
bot.add_command(Config())

bot.run()