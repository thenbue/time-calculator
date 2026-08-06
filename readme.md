# Time Calculator

> A PY-CLI tool for calculating relative solar time offsets using configuration files.

---

## Quick Start

### Version 1

Runs using the default configuration file at `./settings/settings.json`.

```bash
python main.py
```

### Version 2

Supports custom file paths and multiple configuration formats (`.json`, `.yaml`, `.toml`).

```bash
python main.py
```

If no file path is set in the code, the script will prompt you to enter one at runtime.

---

## Configuration

Place your configuration file in your project directory using one of the supported formats:

### JSON (`settings.json`)

```json
{
  "sunrise": 6.0,
  "sunset": 20.0,
  "degree": 50.0
}

```

### TOML (`settings.toml`)

```toml
sunrise = 6.0
sunset = 20.0
degree = 50.0
```

### YAML (`settings.yaml`)

```yaml
sunrise: 6.0
sunset: 20.0
degree: 50.0

```

---

## Key Differences

* **v1:** Basic linear calculation using a hardcoded JSON path.
* **v2:** Added support for YAML/TOML, interactive path entry, and stricter input validation.

---

For version details and release notes, see [CHANGELOG.md](CHANGELOG.md).