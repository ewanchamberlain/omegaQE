#!/bin/bash
source ~/Post-Born/.venv/bin/activate
TYP="k"
EXP="SO"
FIELDS="TEB"
GMV="True"
Lmax=5000
Lcutmin=30
Lcutmax=3000
dL2=1000
Ntheta=1000
NLS=500
OUTDIR="$HOME/Post-Born/data/bias/results/$EXP"
ID="TEST"
mpirun -n 1 python ~/Post-Born/omegaQE/omegaqe/scripts/F_L_mpi.py "$TYP" "$EXP" "$FIELDS" "$GMV" "$Lmax" "$Lcutmin" "$Lcutmax" "$dL2" "$Ntheta" "$NLS" "False" "0" "False" "False" "$OUTDIR" "$ID"
