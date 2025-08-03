import os
from omegaconf import OmegaConf


def load_base_config(path: str, overrides: dict = None):
    """
    Load configuration from a YAML file and apply overrides.

    Args:
        path (str): Path to the YAML config file.
        overrides (dict): Optional dictionary of overrides.

    Returns:
        OmegaConf.DictConfig: Loaded and merged config object.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")

    base = OmegaConf.load(path)
    if overrides:
        overrides_conf = OmegaConf.create(overrides)
        return OmegaConf.merge(base, overrides_conf)
    return base
