"""Config values for archivebot."""
import os
import sys
import toml

default_config = {
    "telegram": {
        "userbot": True,
        "api_key": "1425278481:AAHTCRS9agrLu4-TX5w-ax_IZ7NTkFz7L7s",
        "phone_number": "",
        "app_api_id": 1555704,
        "app_api_hash": "f08030f122370b15dbeaefb39cb0f693",
    },
    "database": {"sql_uri": "sqlite:///archivebot.db",},
    "logging": {"sentry_enabled": False, "sentry_token": "",},
    "download": {
        "allowed_types": ["document", "photo"],
        "target_dir": "/home/user/archivebot/",
    },
    "zip": {"volume_size": "1400m",},
}
