import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))
settings = Dynaconf(
    envvar_prefix="app",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".env"],
    environments=["development", "production", "testing"],
    env_switcher="APP_ENV",
)