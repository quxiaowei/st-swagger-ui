# Build Summary - st_swagger_ui v0.1.1

## Build Information

- **Build Tool**: Hatchling
- **Build Date**: 2024-04-03
- **Version**: 0.1.1
- **Python Version**: >=3.10

## Build Artifacts

### Wheel Distribution
- **File**: `dist/st_swagger_ui-0.1.1-py3-none-any.whl`
- **Size**: 508K
- **Format**: Universal wheel (py3)
- **Contents**: 13 files, 2.2MB total

### Source Distribution
- **File**: `dist/st_swagger_ui-0.1.1.tar.gz`
- **Size**: 10K
- **Format**: Source tarball

## New Features in v0.1.1

### Width Parameter

Added `width` parameter to control component width:

```python
# Full width (default)
st_swagger_ui(url="...")  # width="stretch"

# Fixed max-width (centered)
st_swagger_ui(url="...", width=800)

# No constraint
st_swagger_ui(url="...", width=None)
```

**Implementation Details:**
- CSS: `width: 100%`, `max-width: {value}`, `margin: 0 auto`
- Class: `.st-swagger-ui-container` for custom styling
- Type: `Union[int, Literal["stretch"], None]`
- Default: `"stretch"`

## Package Contents

```
st_swagger_ui/
├── __init__.py (5.9K) - Main Python package
├── pyproject.toml (222B) - Streamlit component metadata
├── frontend/
│   ├── package.json (1.1K)
│   ├── tsconfig.json (536B)
│   ├── vite.config.ts (1.2K)
│   ├── src/
│   │   ├── index.tsx (3.2K) - React component
│   │   └── vite-env.d.ts (38B)
│   └── build/
│       ├── index-Dbq-092K.js (2.0MB) - Bundled JS
│       └── index-_hash_.css (177KB) - Styles
```

## Metadata

- **Name**: st_swagger_ui
- **Summary**: Swagger UI for Streamlit
- **License**: MIT
- **Author**: qu xiaowei <quxw.work@gmail.com>
- **Homepage**: https://github.com/quxiaowei/st-swagger-ui
- **Repository**: https://github.com/quxiaowei/st-swagger-ui.git
- **Issues**: https://github.com/quxiaowei/st-swagger-ui/issues

## Dependencies

### Runtime
- streamlit >= 1.51

### Development
- pytest == 7.4.0
- playwright == 1.48.0
- requests == 2.31.0
- pytest-playwright-snapshot == 1.0
- pytest-rerunfailures == 12.0
- wheel

## Classifiers

- Development Status :: 4 - Beta
- Intended Audience :: Developers
- License :: OSI Approved :: MIT License
- Operating System :: OS Independent
- Programming Language :: Python :: 3
- Programming Language :: Python :: 3.10
- Programming Language :: Python :: 3.11
- Programming Language :: Python :: 3.12
- Topic :: Software Development :: Libraries :: Python Modules

## Build Commands

```bash
# Clean build
hatch build --clean

# Build wheel only
hatch build --target wheel

# Build sdist only
hatch build --target sdist

# Publish to PyPI
hatch publish

# Publish to TestPyPI
hatch publish -r test
```

## Installation

```bash
# From wheel
pip install dist/st_swagger_ui-0.1.1-py3-none-any.whl

# From PyPI (after publish)
pip install st-swagger-ui

# From TestPyPI
pip install --index-url https://test.pypi.org/simple/ st-swagger-ui
```

## Testing

```bash
# Test width parameter
streamlit run test_width.py

# Test all defaults
streamlit run test_final_defaults.py

# Test try_it_out_enabled
streamlit run test_try_it_out.py
```

## Verification Checklist

- [x] Wheel builds successfully
- [x] Sdist builds successfully
- [x] All files included
- [x] Frontend build included
- [x] LICENSE included
- [x] Metadata correct
- [x] Width parameter works
- [x] CSS class added
- [x] Validation works
- [x] Type hints correct

## Next Steps

1. ✅ Build completed successfully
2. ⏳ Test installation from wheel
3. ⏳ Upload to TestPyPI
4. ⏳ Test from TestPyPI
5. ⏳ Upload to PyPI
6. ⏳ Verify on PyPI

## Notes

- Version bumped from 0.1.0 to 0.1.1 (minor feature release)
- All previous features retained
- Width parameter is backward compatible (has default value)
- No breaking changes in this version
