# Time Calculator

> A tool for calculating relative solar time offsets using <JSON/YAML/TOML/> files.



## Quick Start

#### v1

runs using coded path, requires edit if you use something else instead of JSON.
```bash
python main.py
```

### v2

Supports custom file paths and input if missing.

```bash
python main.py
```

If no file path is set in the code, the script will prompt you to enter one at runtime. )

---

## Configuration

Place your configuration file in your project directory using one of the supported formats:

### JSON (`usage/settings.json`)

```json
{
  "sunrise": 6.0,
  "sunset": 20.0,
  "degree": 50.0
}
```

### TOML (`usage/settings.toml`)

```toml
sunrise = 6.0
sunset = 20.0
degree = 50.0
```

### YAML (`usage/settings.yaml`)

```yaml
sunrise: 6.0
sunset: 20.0
degree: 50.0
```

---

## Key Differences

* **v1:** Basic calculation using a hardcoded JSON path with support for YAML/TOML.
* **(v2):** Added interactive path entry, and stricter input validation.

---

For version details and release notes, see [CHANGELOG.md](CHANGELOG.md).