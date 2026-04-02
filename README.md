# st_swagger_ui

Streamlit component for embedding Swagger UI to display OpenAPI/Swagger specifications.

## Features

- Display OpenAPI/Swagger specifications from URL or local file
- Configurable operation expansion (`doc_expansion`)
- Enable/disable "Try it out" functionality (`try_it_out_enabled`)
- Show/hide operation IDs (`display_operation_id`)
- Control model rendering (`default_model_rendering`)
- Custom CSS overrides for reduced indentation

## Installation

```sh
uv pip install st_swagger_ui
```

### Development install (editable)

When developing this component locally, install it in editable mode:

```sh
uv pip install -e . --force-reinstall
```

## Usage

### Basic Usage

```python
import streamlit as st
from st_swagger_ui import st_swagger_ui

# Load from URL
st_swagger_ui(url="https://petstore.swagger.io/v2/swagger.json")
```

### Load from Local File

```python
import json

with open("openapi.json") as f:
    spec = json.load(f)

st_swagger_ui(spec=spec)
```

### Configuration Options

```python
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    doc_expansion="list",           # "list" | "full" | "none"
    try_it_out_enabled=True,        # True | False | None
    display_operation_id=False,     # True | False | None
    default_model_rendering="example",  # "example" | "model" | None
)
```

### Parameters

| Parameter                 | Type   | Default | Description                                        |
| ------------------------- | ------ | ------- | -------------------------------------------------- |
| `url`                     | `str`  | `None`  | URL to fetch OpenAPI specification from            |
| `spec`                    | `dict` | `None`  | OpenAPI specification as a Python dict             |
| `doc_expansion`           | `str`  | `None`  | Default expansion: `"list"`, `"full"`, or `"none"` |
| `try_it_out_enabled`      | `bool` | `None`  | Enable "Try it out" functionality                  |
| `display_operation_id`    | `bool` | `None`  | Show operation IDs next to operation names         |
| `default_model_rendering` | `str`  | `None`  | Model display: `"example"` or `"model"`            |

**Note:** Either `url` or `spec` must be provided (mutually exclusive).

### Examples

#### Full Expansion with Model View

```python
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    doc_expansion="full",
    default_model_rendering="model"
)
```

#### Read-Only Mode (No "Try it out")

```python
st_swagger_ui(
    url="https://api.example.com/openapi.json",
    try_it_out_enabled=False,
    display_operation_id=True
)
```

#### Load from FastAPI App

```python
from fastapi import FastAPI
import fastapi.openapi.utils

app = FastAPI()

spec = fastapi.openapi.utils.get_openapi(
    title="My API",
    version="1.0.0",
    openapi_version="3.0.0",
    routes=app.routes,
)

st_swagger_ui(spec=spec, doc_expansion="list")
```

## Build Instructions

To package this component for distribution:

### 1. Build Frontend Assets

```sh
cd st_swagger_ui/frontend
npm install
npm run build
```

### 2. Build Python Wheel

From the project root:

```sh
uv build
```

This creates a `dist/` directory containing:

- `dist/st_swagger_ui-<version>-py3-none-any.whl`
- `dist/st_swagger_ui-<version>.tar.gz` (sdist)

### Requirements

- **Python**: >= 3.10
- **Node.js**: >= 24 (LTS)
- **npm**: Latest version (bundled with Node.js)

## Development

### Frontend Development

The frontend is built with:

- React 18
- TypeScript
- Vite
- swagger-ui-react

To run in development mode:

```sh
cd st_swagger_ui/frontend
npm run dev
```

### Project Structure

```
st_swagger_ui/
├── st_swagger_ui/
│   ├── __init__.py          # Python component
│   └── frontend/
│       ├── src/
│       │   ├── index.tsx    # React entry point
│       │   └── swagger-ui-overrides.css  # Custom CSS
│       ├── package.json
│       ├── vite.config.ts
│       └── build/           # Generated build output
├── pyproject.toml
├── README.md
└── example.py
```

## License

MIT
