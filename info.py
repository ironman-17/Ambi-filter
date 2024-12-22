import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '20902603'))
API_HASH = environ.get('API_HASH', '79e5caa103a9e9fb0183390b4800845d')
BOT_TOKEN = environ.get('BOT_TOKEN', "7736206406:AAEMXlEqIBi05OSEKaf6PPvyhW8XZ0-GH8U")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://envs.sh/797.jpg https://envs.sh/79o.jpg https://envs.sh/79r.jpg https://envs.sh/799.jpg https://envs.sh/79v.jpg https://envs.sh/79N.jpg https://envs.sh/79H.jpg https://envs.sh/79g.jpg https://envs.sh/79f.jpg https://envs.sh/79a.jpg https://envs.sh/79O.jpg https://envs.sh/79m.jpg https://envs.sh/79M.jpg ')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://envs.sh/79y.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://envs.sh/0RT.jpg'))
SUBSCRIPTIO = (environ.get('SUBSCRIPTION', 'https://envs.sh/0RT.jpg')).split()
CODE = (environ.get('CODE', 'https://envs.sh/0RB.jpg'))
PAYPICS = (environ.get('PAYPICS', 'https://envs.sh/0RB.jpg')).split()
REFER_PICS = (environ.get("REFER_PICS", "https://graph.org/file/1a2e64aee3d4d10edd930.jpg")).split() 

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', 'modijiurl.com')) # not support
STREAM_API = (environ.get('STREAM_API', 'cd8531f15046b37126cc9b9edb86456dde10db5a'))
STREAMHTO = (environ.get('STREAMHTO', ''))
BOT_USERNAME = environ.get("BOT_USERNAME", "Madara_Uchiha_17_bot")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6283322330').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002473385674').split()] #Channel id for auto indexing ( make sure bot is admin )
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '6283322330').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '6283322330').split()]
auth_channel = environ.get('AUTH_CHANNEL', '-1002242439175') #Channel / Group Id for force sub ( make sure bot is admin )
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', 'https://t.me/+aEZ3qtcawX44MmRl') # support group id ( make sure bot is admin )
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002416538920') # request channel id ( make sure bot is admin )
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Mastersender:17032008@cluster0.dt8i8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'AutofilterBot')



#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nYᴏᴜʀ Rᴇǫᴜᴇsᴛ Tᴏ Jᴏɪɴ {title} Is Aᴘᴘʀᴏᴠᴇᴅ.\n\‣ Pᴏᴡᴇʀᴇᴅ Bʏ @Madarauchiha1703 💖</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'Modijiurl.com')
SHORTLINK_API = environ.get('SHORTLINK_API', 'cd8531f15046b37126cc9b9edb86456dde10db5a')

#SHORTLINK_URL = ''
#SHORTLINK_API = ''

IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+onQoosyNxDkxNDVl')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/+8_DwkRbGlEE0YTll')
TUTORIAL = environ.get('TUTORIAL', '')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))
MSG_ALRT = environ.get('MSG_ALRT', '✯ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : @Madarauchiha1703')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002179136370')) #Log channel id ( make sure bot is admin )
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/+aEZ3qtcawX44MmRl') #Support group link ( make sure bot is admin )
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]
PREFIX = environ.get("PREFIX", "/")
# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "".format(FQDN) if ON_HEROKU or NO_PORT else \
    "".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'JisshuBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'Jisshu'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',True))
if HAS_SSL:
    URL = "".format(FQDN)
else:
    URL = "".format(FQDN)


# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase

# online Stream and Download support only premium user, True or Flase
JS_WEB_PREMIUM = is_enabled((environ.get('JS_WEB_PREMIUM', "True")), True)

# website themes changing (https://bootswatch.com)
JS_THEMES = "cerulean"

# add premium logs channel id
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002452837705'))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
