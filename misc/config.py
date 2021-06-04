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


@dataclass
class ErrorEntry:
    log: str
    embed: str


ERRORS: Dict[str, ErrorEntry] = {
    "CNF": ErrorEntry(CONFIG["CommandNotFound"]["log"], CONFIG["CommandNotFound"]["embed"]),
    "MRA": ErrorEntry(CONFIG["MissingRequiredArgument"]["log"], CONFIG["MissingRequiredArgument"]["embed"]),
    "RNF": ErrorEntry(CONFIG["RoleNotFound"]["log"], CONFIG["RoleNotFound"]["embed"]),
    "MNF": ErrorEntry(CONFIG["MemberNotFound"]["log"], CONFIG["MemberNotFound"]["embed"]),
}
