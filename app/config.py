import os
import yaml
from pathlib import Path

from betterconf import Config, field
from betterconf.config import AbstractProvider

BASE_DIR = Path(__file__).resolve().parent


class YMLProvider(AbstractProvider):
    def __init__(self):
        env = os.environ.get("ENVIRON", "local").lower()
        path_to_yml = str(BASE_DIR) + f"\\etc\\{env}\\config.yml"

        with open(path_to_yml, "r") as f:
            self._settings = yaml.safe_load(f)

    def get(self, name):
        return self._settings.get(name)


provider = YMLProvider()


class AppConfig(Config):
    APP_PORT = field("app_port", provider=provider, default=8855)
    ADMIN_API_SECRET = field("admin_api_secret", provider=provider, default="")


app_config = AppConfig()
