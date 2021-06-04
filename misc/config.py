import configparser as config
import pathlib
from dataclasses import dataclass
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


@dataclass
class CommandEntry:
    collection: str = None
    message: str = None


COMMANDS: Dict[str, CommandEntry] = {
    "BAN": CommandEntry(CONFIG["BAN"]["collection"], CONFIG["BAN"]["message"]),
    "KICK": CommandEntry(CONFIG["KICK"]["collection"], CONFIG["KICK"]["message"]),
    "MUTE": CommandEntry(CONFIG["MUTE"]["collection"], CONFIG["MUTE"]["message"]),
    "WARN": CommandEntry(CONFIG["WARN"]["collection"], CONFIG["WARN"]["message"]),
    "USER": CommandEntry(CONFIG["USER"]["collection"]),
}
ERRORS: Dict[str, config.SectionProxy] = {
    "CNF": CONFIG["CommandNotFound"],
    "MRA": CONFIG["MissingRequiredArgument"],
    "RNF": CONFIG["RoleNotFound"],
    "MNF": CONFIG["MemberNotFound"],
}
