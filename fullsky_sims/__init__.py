import os
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
IS_ARTEMIS = os.path.exists("/its")
DEMNUNII_DIR = (
    Path("/research/astro/cmb/DEMNUnii")
    if IS_ARTEMIS
    else HOME_DIR / "mnt" / "artemis" / "lustre" / "DEMNUnii"
)
