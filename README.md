# Mordoku

A Python project starter template.

## Quick Start

```bash
# Clone the repository
git clone https://github.com/ra-spec/Mordoku.git
cd Mordoku

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest
```

## Project Structure

```
Mordoku/
├── src/
│   └── mordoku/           # Main package
│       ├── __init__.py
│       └── main.py
├── tests/                 # Test suite
│   ├── __init__.py
│   └── test_main.py
├── docs/                  # Documentation
├── .gitignore
├── .github/
│   └── workflows/         # CI/CD workflows
├── pyproject.toml         # Project metadata
├── requirements.txt       # Dependencies
├── requirements-dev.txt   # Development dependencies
├── pytest.ini
└── README.md
```

## Development

### Install development dependencies
```bash
pip install -r requirements-dev.txt
```

### Run tests
```bash
pytest
```

### Format code
```bash
black src/ tests/
isort src/ tests/
```

### Lint
```bash
flake8 src/ tests/
pylint src/
```

## Contributing

1. Create a feature branch from `develop`
2. Make your changes
3. Write or update tests
4. Ensure all tests pass
5. Submit a pull request

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for more details.

## License

MIT
