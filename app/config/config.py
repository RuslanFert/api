
import yaml
from pathlib import Path

from betterconf import Config, field
from betterconf.config import AbstractProvider

#TODO: в этом месте избавиться от хадкода
BASE_DIR = Path("etc/local/config.yml").resolve()


class YMLProvider(AbstractProvider):
    def __init__(self):
        path_to_yml = BASE_DIR

        with open(path_to_yml, "r") as f:
            self._settings = yaml.safe_load(f)

    def get(self, name):
        return self._settings.get(name)


provider = YMLProvider()


class AppConfig(Config):
    APP_PORT = field("app_port", provider=provider, default=8855)
    ADMIN_API_SECRET = field("admin_api_secret", provider=provider, default="")


app_config = AppConfig()
