# omegaQE

Forked from [mfrobertson/omegaQE](https://github.com/mfrobertson/omegaQE). Originally used to produce results in [arXiv:2303.13313]https://arxiv.org/abs/2303.13313 and [arXiv:2405.19998](https://arxiv.org/abs/2406.19998).

Contains general tools for analytical modelling of large-scale structure power spectra, post-Born bispectra, Fisher-forecasting, Gaussian flat sky simulations, quadratic estimator biases etc.

All code interacting with the [DEMNUnii](https://arxiv.org/abs/1505.07148) and [AGORA](https://yomori.github.io/agora/index.html) N-body simulations to produce the results in
[arXiv:2405.19998](https://arxiv.org/abs/2406.19998) can be found in `fullsky_sims`.


### Installation
Clone the repo and the submodules, then run `poetry install`. The install the submodules.

### Requirements
Most requirements are listed in `pyproject.toml`. Additional requirements are:
- [`poetry`](https://python-poetry.org/)
- [`LensIt`](https://lensit.readthedocs.io/en/latest/) for flat-sky CMB lensing reconstruction
- [`plancklens`](https://plancklens.readthedocs.io/en/latest/) for CMB iterative reconstruction bias forecasts
- [`delensalot`](https://github.com/NextGenCMB/delensalot/tree/eb_tests)
- [`lensitbiases`](https://github.com/carronj/plancklens/tree/master)

Specific version requirements:
- `python < 3.10, > 3.11`
- `numpy <= 1.22`
- `setuptools <= 64`
- [`vector = 0.8.5`](https://pypi.org/project/vector/)
