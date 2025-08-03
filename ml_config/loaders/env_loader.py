import os
from .base_loader import load_base_config


def load_from_env(env_var: str = "CONFIG_PATH", overrides: dict = None):
    """
    Load configuration using a path from an environment variable.

    Args:
        env_var (str): Name of the environment variable containing the path.
        overrides (dict): Optional dictionary of overrides.

    Returns:
        OmegaConf.DictConfig: Loaded config.
    """
    path = os.getenv(env_var)
    if not path:
        raise EnvironmentError(f"Environment variable '{env_var}' is not set.")
    return load_base_config(path, overrides)
