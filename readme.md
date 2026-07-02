<center> Time Calculator </center>

> A CLI tool for calculating time from sunset, solar noon, or degrees.

## Features

- Calculate times from **sunset**, **solar noon**, and **degrees**
- Support for **YAML**, **TOML**, **JSON** config formats
- Cross-platform (Windows/Linux/macOS)
- Multiple output formats (table, JSON, CSV)

## Installation

```bash
# From source
git clone https://github.com/thenbue/time-calculator
cd time-calculator
py main.py

# Or download binary from Releases
```

## Configuration

| Format | File          |
| ------ | ------------- |
| YAML   | `config.yaml` |
| TOML   | `config.toml` |
| JSON   | `config.json` |

<details>

<summary>Sample TOML config</summary>

```toml
sunrise = 6.0
sunset = 20.0
degree = 50


```

</details>

<details>
<summary>Sample YAML config</summary>

```yaml
sunrise: 6.0
sunset: 20.0
degree: 50
```

</details>
<details>
<summary>Sample JSON config</summary>

```json
{
  "sunrise": 6.0,
  "sunset": 20.0,
  "degree": 50
}
```

</details>

## Usage

```powershell
py main.py
```

</details>

## Building from Source

```bash
# via gh
gh repo clone thenbue/time-calculator
# via git
git clone https://github.com/thenbue/time-calculator
```

## Contributing

1. Fork the repo
2. Create feature branch (`git checkout -b feature/xyz`)
3. Commit changes (`git commit -m 'Add xyz'`)
4. Push and open PR

## Notice

Not to the minute accurate

## License

MIT © [thenbue](https://github.com/thenbue)

---

**See also:** [Changelog](CHANGELOG.md) • [Issues](https://github.com/thenbue/time-calculator/issues)
