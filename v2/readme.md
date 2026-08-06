# Time Calculator (v2)

> A lightweight CLI tool to calculate time offsets based on solar angles and key solar events.

---

### Quick Start

```bash
git clone https://github.com/thenbue/time-calculator.git
cd time-calculator
python main.py
```

Supports custom file paths and multiple configuration formats (`.json`, `.yaml`, `.toml`).
If no file path is set in the code, the script prompts you to enter one at runtime.

---

### Configuration

Create a file in the `./prefrences/` folder:

```json
{
  "sunrise": 6.0,
  "sunset": 20.0,
  "degree": 50.0
}
```

`degree` is the solar angle. The computed time is `sunrise + degree / 180 * (sunset - sunrise)`.

### Supported Formats

`.json`, `.toml`, `.yaml` — the extension of the file determines the format.

---

### Known Issues

- The extension check misses the dot (`path.endswith("json")`), so invalid paths like
  `notjson` are treated as JSON.
- `yaml.load()` is used without a safe loader.
- Both the missing `sunrise` and `sunset` warnings print `"sunrise not given"`, and the
  `{}` placeholder is never filled in.
- If `sunrise`/`sunset` are missing, the calculation still runs and crashes.
- Output is a raw float; the README previously claimed formatted `HH:MM` output.

**These bugs will be fixed in the next patches.**

---

### Roadmap

- Fix the extension check and use `yaml.safe_load()`.
- Correct the warning messages and validate all required values before calculating.
- Add proper `HH:MM` output formatting.

---

[Report Issue](https://github.com/thenbue/time-calculator/issues) • MIT © [thenbue](https://github.com/thenbue)
