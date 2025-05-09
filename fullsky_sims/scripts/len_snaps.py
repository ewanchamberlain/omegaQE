from omegaqe.tools import getFileSep
from fullsky_sims.demnunii import Demnunii
import fullsky_sims
import numpy as np
import sys
import os
from pathlib import Path


if not 'PLENS' in os.environ.keys():
    os.environ['PLENS'] = '_tmp'


def _lensing_fac(lmax):
    ells = np.arange(lmax+1)[1:]
    fac = np.zeros(lmax+1)
    fac[1:] = 2 / np.sqrt(ells * (ells + 1))
    return fac


def get_glm(nthreads, snap, dm, lmax, verbose):
    lensing_fac = _lensing_fac(lmax)
    gal_kappa_map = dm.get_gal_kappa_map(snap, verbose=verbose)
    klm = dm.sht.map2alm(gal_kappa_map, lmax=lmax, nthreads=nthreads)
    return dm.sht.almxfl(klm, lensing_fac)


def get_lensed_map(dlm, unl_alm, nthreads, dm):
    return dm.sht.alm2lenmap(unl_alm, dlm, nthreads=nthreads)


def save_lens_maps(len_map, snap, dm):
    directory = Path(dm.cache_dir)/"len_snaps"
    if not os.path.isdir(directory):
        os.makedirs(directory)
    snap_num_app = "0" if len(str(snap)) == 2 else "00"
    dm.sht.write_map(str(directory / f"len_snap_{snap_num_app}{snap}.fits"), len_map)


def main(nthreads, verbose=False):
    dm = Demnunii()
    LMAX_MAP = 6000
    for snap in np.arange(63):
        
        glm_snap = get_glm(nthreads, snap, dm, LMAX_MAP, verbose)
        unl_snap = dm.get_particle_snap(snap)
        unl_alm = dm.sht.map2alm(unl_snap, lmax=LMAX_MAP, nthreads=nthreads)
        len_map = get_lensed_map(glm_snap, unl_alm, nthreads, dm)
        save_lens_maps(len_map, snap, dm)


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) not in (1, 2):
        raise ValueError(
            "Arguments should be nthreads, (optional: is_verbose)")
    nthreads = int(args[0])
    is_verbose = bool(args[1]) if len(args) == 2 else None
    if is_verbose:
        print(f"Running with {nthreads} threads.")
    main(nthreads)
