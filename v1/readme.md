# Time Calculator (v1)

> A lightweight CLI tool to calculate time offsets based on solar angles and key solar events.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

### Quick Start

```bash
# Clone the repository
git clone https://github.com/thenbue/time-calculator.git
cd time-calculator

# Run the program
python main.py
```

Runs using the default configuration file at `./settings/settings.json`.

---

### Configuration

Place a `settings.json` file in the `./settings/` folder:

```json
{
  "sunrise": 6.0,
  "sunset": 20.0,
  "degree": 50.0
}
```

`degree` is the solar angle. The computed time is `sunrise + degree / 180 * (sunset - sunrise)`.

### Supported Formats

`.json`, `.toml`, `.yaml` — the extension of the file in `./settings/` determines the format.

---

### Known Issues

- Failed file loads (e.g. missing file or bad JSON) are silently swallowed and the script
  computes a result using default values instead of reporting the error.
- Output time is not zero-padded (`6:5` instead of `06:05`) and minutes are not rounded.
- Error handling relies on a fragile string flag (`x.dec`) instead of proper error states.

**These bugs will be fixed in the next patches.**

---

### Roadmap

- Fix silent load failures and surface clear errors.
- Proper `HH:MM` output formatting.
- Replace string-based error handling with explicit error states.

---

[Report Issue](https://github.com/thenbue/time-calculator/issues) • MIT © [thenbue](https://github.com/thenbue)
