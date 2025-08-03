from omegaconf import OmegaConf


def save_config(config, path: str):
    """
    Save an OmegaConf config back to a YAML file.

    Args:
        config (OmegaConf.DictConfig): Config object.
        path (str): Output file path.
    """
    with open(path, "w") as f:
        OmegaConf.save(config=config, f=f)
