import os
import tempfile
import pytest
from omegaconf import DictConfig
from pydantic import BaseModel, ValidationError

from ml_config import (
    load_base_config,
    load_from_env,
    save_config,
    validate_config
)

# Sample YAML config as string
SAMPLE_YAML = """
parameters:
  seed: 42
  lr: 0.01
"""

# --- Fixtures ---

@pytest.fixture
def temp_yaml_file():
    with tempfile.NamedTemporaryFile("w+", suffix=".yaml", delete=False) as f:
        f.write(SAMPLE_YAML)
        f.flush()
        yield f.name
    os.remove(f.name)

# --- Tests: Base Loader ---

def test_load_base_config(temp_yaml_file):
    config = load_base_config(temp_yaml_file)
    assert isinstance(config, DictConfig)
    assert config.parameters.seed == 42

def test_base_loader_with_override(temp_yaml_file):
    config = load_base_config(temp_yaml_file, overrides={"parameters": {"seed": 123}})
    assert config.parameters.seed == 123
    assert config.parameters.lr == 0.01

# --- Tests: Env Loader ---

def test_env_loader(monkeypatch, temp_yaml_file):
    monkeypatch.setenv("CONFIG_PATH", temp_yaml_file)
    config = load_from_env()
    assert config.parameters.seed == 42

def test_env_loader_missing(monkeypatch):
    monkeypatch.delenv("CONFIG_PATH", raising=False)
    with pytest.raises(EnvironmentError):
        load_from_env()

# --- Tests: Saver ---

def test_save_and_reload_config(temp_yaml_file):
    config = load_base_config(temp_yaml_file)
    with tempfile.NamedTemporaryFile("r+", suffix=".yaml", delete=False) as out:
        save_config(config, out.name)
        out.seek(0)
        loaded = load_base_config(out.name)
        assert loaded.parameters.lr == 0.01
    os.remove(out.name)

# --- Tests: Validation ---

class ConfigSchema(BaseModel):
    parameters: dict

def test_valid_schema(temp_yaml_file):
    config = load_base_config(temp_yaml_file)
    validated = validate_config(config, ConfigSchema)
    assert validated.parameters["seed"] == 42

def test_invalid_schema():
    config = DictConfig({})
    with pytest.raises(ValidationError):
        validate_config(config, ConfigSchema)
