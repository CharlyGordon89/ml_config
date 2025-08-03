from pydantic import BaseModel, ValidationError
from omegaconf import OmegaConf


def validate_config(config, schema_cls: type[BaseModel]):
    """
    Validates a config against a Pydantic schema.

    Args:
        config (OmegaConf.DictConfig): The config to validate.
        schema_cls (Type[BaseModel]): The Pydantic schema class.

    Returns:
        schema_cls: Parsed and validated config.

    Raises:
        ValidationError: If validation fails.
    """
    config_dict = OmegaConf.to_container(config, resolve=True)
    try:
        return schema_cls(**config_dict)
    except ValidationError as e:
        raise e
