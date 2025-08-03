"""
Reusable config loader using OmegaConf.
Supports YAML files, CLI overrides, and environment variables.
"""

import os
from omegaconf import OmegaConf


def load_config(config_path: str = "config/config.yaml",
                overrides: dict = None):
    """
    Load configuration from a YAML file with optional overrides.

    Args:
        config_path (str): Path to the YAML config file.
        overrides (dict): Dictionary of values to override in the config.

    Returns:
        OmegaConf.DictConfig: Final merged config object.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    base_cfg = OmegaConf.load(config_path)

    if overrides:
        overrides_cfg = OmegaConf.create(overrides)
        config = OmegaConf.merge(base_cfg, overrides_cfg)
    else:
        config = base_cfg

    return config
