# Time Calculator

> A tool for calculating relative solar time offsets using <JSON/YAML/TOML/> files.



## Quick Start

#### v1
> enter path at runtime or in the first few lines
```bash
python main.py
```

### v2
> enter path at runtime or in the first few lines

```bash
python main.py
```
---

## Configuration

Place your configuration file in your project directory using one of the supported formats:

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


### JSON (`usage/settings.json`)

```json
{
  "sunrise": 6.0,
  "sunset": 20.0,
  "degree": 50.0
}
```
## Key Differences

* **v1:** Basic calculation using a hardcoded JSON path with support for YAML/TOML.
* **(v2):** Added interactive path entry, and stricter input validation.

---

For version details and release notes, see [CHANGELOG.md](CHANGELOG.md).