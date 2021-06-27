"""Constants for frigate."""
# Base component constants
NAME = "Frigate"
DOMAIN = "frigate"

# Icons
ICON_CAR = "mdi:shield-car"
ICON_CAT = "mdi:cat"
ICON_DOG = "mdi:dog-side"
ICON_FILM_MULTIPLE = "mdi:filmstrip-box-multiple"
ICON_IMAGE_MULTIPLE = "mdi:image-multiple"
ICON_MOTION_SENSOR = "hass:motion-sensor"
ICON_OTHER = "mdi:shield-alert"
ICON_PERSON = "mdi:shield-account"
ICON_SPEEDOMETER = "mdi:speedometer"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
CAMERA = "camera"
PLATFORMS = [SENSOR, CAMERA, SWITCH, BINARY_SENSOR]

# Unit of measurement
FPS = "fps"
MS = "ms"

# Attributes
ATTR_CLIENT = "client"
ATTR_CONFIG = "config"
ATTR_COORDINATOR = "coordinator"
ATTR_MQTT = "mqtt"
ATTR_CLIENT_ID = "client_id"

# Configuration and options
CONF_RTMP_URL_TEMPLATE = "rtmp_url_template"
CONF_NOTIFICATION_PROXY_ENABLE = "notification_proxy_enable"

# Defaults
DEFAULT_NAME = DOMAIN
DEFAULT_HOST = "http://ccab4aaf-frigate:5000"


STARTUP_MESSAGE = """
-------------------------------------------------------------------
{title}
Integration Version: {integration_version}
This is a custom integration!
If you have any issues with this you need to open an issue here:
https://github.com/blakeblackshear/frigate-hass-integration/issues
-------------------------------------------------------------------
"""

# States
STATE_DETECTED = "active"
STATE_IDLE = "idle"
