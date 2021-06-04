import configparser as config
import pathlib
from typing import Dict

PATHS: Dict[str, pathlib.Path] = {
    "project": pathlib.Path("./config.ini"),
    "home": pathlib.Path.home().joinpath(pathlib.Path(".AzuryModerator.ini")),
    "config": pathlib.Path.home().joinpath(pathlib.Path(".config/AzuryModerator/config.ini")),
}


def _get_config() -> str:
    return str([PATHS[path] for path in PATHS if PATHS[path].exists()][0].absolute())


CONFIG: config.ConfigParser = config.ConfigParser()
CONFIG.read(_get_config())

DATABASE: config.SectionProxy = CONFIG["DATABASE"]
COMMANDS: Dict[str, config.SectionProxy] = {
    "BAN": CONFIG["BAN"],
    "KICK": CONFIG["KICK"],
    "MUTE": CONFIG["MUTE"],
    "WARN": CONFIG["WARN"],
    "USER": CONFIG["USER"],
}
ERRORS: Dict[str, config.SectionProxy] = {
    "CNF": CONFIG["CommandNotFound"],
    "MRA": CONFIG["MissingRequiredArgument"],
    "RNF": CONFIG["RoleNotFound"],
    "MNF": CONFIG["MemberNotFound"],
}
