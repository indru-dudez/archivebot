"""Config values for archivebot."""
import os
import sys
import toml

default_config = {
    "telegram": {
        "userbot": false,
        "api_key": "1484527342:AAEktw6k1lB4yyMpzuXAxtGRIiPrvhXBUGk",
        "phone_number": "your_phone_number (empty if not in userbot mode)",
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

config_path = os.path.expanduser("~/.config/archivebot.toml")

if not os.path.exists(config_path):
    with open(config_path, "w") as file_descriptor:
        toml.dump(default_config, file_descriptor)
    print("Please adjust the configuration file at '~/.config/archivebot.toml'")
    sys.exit(1)
else:
    config = toml.load(config_path)

    # Set default values for any missing keys in the loaded config
    for key, category in default_config.items():
        if key not in config:
            config[key] = category
            continue

        for option, value in category.items():
            if option not in config[key]:
                config[key][option] = value
