import os
import tomllib
from pathlib import Path
from fullsky_sims.demnunii import Demnunii
from fullsky_sims.agora import Agora


def wrapper_class(nbody, nthreads):
    if nbody.lower() == "demnunii":
        return Demnunii(nthreads)
    if nbody.lower() == "agora":
        return Agora(nthreads)
    raise ValueError(f"Nbody sim {nbody} not recognised.")


ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
HOME_DIR = Path(os.path.expanduser("~"))
RESOURCE_DIR = ROOT_DIR / "resources"

with open(RESOURCE_DIR / "config.toml", "rb") as f:
    config = tomllib.load(f)

DEMNUNII_DIR = Path(os.path.expanduser(config["Paths"]["demnunii_dir"]))
CACHE_DIR = Path(os.path.expanduser(config["Paths"]["cache_dir"]))