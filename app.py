import os
from embedchain import App

bistec_bot = App()

bistec_bot.add("https://bistecglobal.com/")
bistec_bot.add("https://bistecglobal.com/life/")
bistec_bot.add("https://bistecglobal.com/case-studies/")

response = bistec_bot.query("What is hearts academy ?")
print(response)
