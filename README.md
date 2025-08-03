# ml_config

**Reusable, scalable, and production-grade configuration management for ML pipelines.**  
Built on top of `OmegaConf` and `Pydantic`, `ml_config` simplifies configuration loading, validation, overriding, and serialization.

---

## ✅ Features

- 📁 Load YAML-based configuration files
- 🔁 Override with Python dicts or environment variables
- 🌿 Access configs with dot notation (`config.training.lr`)
- 🔒 Validate configs using `pydantic` schemas
- 💾 Save configs back to YAML (for checkpoints or audit)
- 🧪 Fully tested, modular, and CI/CD-ready

---

## 🛠️ Installation

```bash
pip install -e .
```

> Requires Python 3.8+, `omegaconf`, `pydantic`, `pyyaml`

---

## 🚀 Usage

### 1. Load from YAML

```python
from ml_config import load_base_config

config = load_base_config("config.yaml")
print(config.model.name)
```

### 2. With overrides

```python
config = load_base_config("config.yaml", overrides={"model": {"name": "xgboost"}})
```

### 3. Load using an environment variable

```bash
export CONFIG_PATH="config.yaml"
```

```python
from ml_config import load_from_env

config = load_from_env()
```

### 4. Validate with `pydantic`

```python
from pydantic import BaseModel
from ml_config import validate_config

class MySchema(BaseModel):
    model: dict
    training: dict

validated = validate_config(config, MySchema)
```

### 5. Save config back to YAML

```python
from ml_config import save_config

save_config(config, "final_config.yaml")
```

---

## 📁 Folder Structure

```
ml_config/
├── loaders/            # base and env loaders
├── utils/              # validation logic
├── saver.py            # save config to YAML
├── config_loader.py    # legacy flat loader
├── tests/              # pytest-based tests
├── __init__.py         # unified import interface
```

---

## 🧪 Running Tests

```bash
pytest -v ml_config/tests
```

