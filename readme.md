# Time Calculator

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

## Quick Start

<details>
<summary>Change config.json via PowerShell</summary>

```powershell
@'
{
    "world": {
        "sunrise": 6.0,
        "sunset": 20.0,
        "degree": 50
    }
}
'@ | Out-File -Encoding utf8 "./settings/settings.json"
```

</details>

<details>
<summary>Change .toml via PowerShell</summary>

```powershell
@'
[world]
sunrise = 6.0
sunset = 20.0
degree = 50
'@ | Out-File -Encoding utf8 "./settings/settings.json"
```

</details>

<details>
<summary>Change .yaml via PowerShell</summary>

```powershell
@'
world:
  sunrise: 6.0
  sunset: 20.0
  degree: 50
'@ | Out-File -Encoding utf8 "./settings/settings.json"
```

</details>

```bash
time-calculator calc --config config.yaml
```

## Configuration

| Format | Example File  |
| ------ | ------------- |
| YAML   | `config.yaml` |
| TOML   | `config.toml` |
| JSON   | `config.json` |

**Key settings:**

```yaml
location:
  latitude: 40.7128
  longitude: -74.0060
  timezone: "America/New_York"
calculation:
  method: "degrees" # sunset | sunnoon | degrees
  angle: 18.0 # degrees below horizon
output:
  format: "table" # table | json | csv
  timezone: "local" # local | utc
```

## Usage

```bash
# Calculate from sunset
time-calculator calc --method sunset --angle 18

# Calculate from solar noon
time-calculator calc --method sunnoon --angle 90

# From config file
time-calculator calc -c config.yaml

# Output formats
time-calculator calc --format json
time-calculator calc --format table
time-calculator calc --format csv
```

## Examples

<details>
<summary>Sample YAML config</summary>

```yaml
location:
  latitude: 51.5074
  longitude: -0.1278
  timezone: "Europe/London"
calculation:
  method: "degrees"
  angle: 15.0
output:
  format: "table"
  timezone: "local"
```

</details>

## Building from Source

```bash
go mod tidy
go build -ldflags="-s -w" -o time-calculator
```

## Contributing

1. Fork the repo
2. Create feature branch (`git checkout -b feature/xyz`)
3. Commit changes (`git commit -m 'Add xyz'`)
4. Push and open PR

## License

MIT © [thenbue](https://github.com/thenbue)

---

**See also:** [Changelog](CHANGELOG.md) • [Issues](https://github.com/thenbue/time-calculator/issues)
