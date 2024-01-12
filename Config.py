import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "22633356"))
    API_HASH = os.environ.get("API_HASH", "3722a88cc92683bfc3590b42f28bec28")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6300181035:AAF0sXrLqcjVLGu-VR6iVxfRA8DzZkbgrR0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHYBu0RrvL6V1-W34LUnVuylTQ6fYRIRzGOa02kf7avwZVPS_e3GJsEOEVOzSxRwxJUypA7EJlS0reWRmEXsKjxYsPSYuMXWJj1ysfGL6qPI-oX23Ey3YjTg3UUenVndzr-ciEuxJKbV6BfjLJdffpLJ2jbkfAb3iEr2_5xzxWPqL7Nkdb6Glwrvt9kRuGFvzeBNEpz7HVPS3i2f8f6FjtbLofC-GM1DPTFs6hoLAxHmMRcgS4xsynrysDNRU-3QxQeq9BnFPCaVK39_c8DIeM05XyEWl0T2QTy94kyYem-0AaKY7YgkoS1LUpF_hkb37HSWnORZVA8w0lBtS4VaD5IOn7w=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5523669758")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
