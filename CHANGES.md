# Changelog

## [0.1.0] - 2024-04-03

### New Features

#### Width Parameter Support

Added `width` parameter to control the maximum width of the Swagger UI component.

**Parameters:**

- **Type**: `Union[int, Literal["stretch"], None]`
- **Default**: `"stretch"` (full width of parent container)
- **CSS Implementation**: Uses `max-width` with centered layout

**Options:**

| Value                 | CSS `max-width` | CSS `margin` | Effect                            |
| --------------------- | --------------- | ------------ | --------------------------------- |
| `"stretch"` (default) | `100%`          | `0`          | Fills parent container            |
| `int` (e.g., `800`)   | `{value}px`     | `0 auto`     | Centered with max width           |
| `None`                | `undefined`     | `0`          | No constraint (SwaggerUI default) |

**Examples:**

```python
from st_swagger_ui import st_swagger_ui

# Default: Full width (stretch)
st_swagger_ui(url="...")

# Fixed max-width (centered)
st_swagger_ui(url="...", width=800)

# Large max-width (centered)
st_swagger_ui(url="...", width=1600)

# No constraint
st_swagger_ui(url="...", width=None)

# In columns (responsive)
col1, col2 = st.columns(2)
with col1:
    st_swagger_ui(url="...", width="stretch")  # Fills column
with col2:
    st_swagger_ui(url="...", width=600)  # Max 600px in column
```

**CSS Implementation:**

```css
.st-swagger-ui-container {
  width: 100%;
  max-width: 100%; /* or 800px, or undefined */
  margin: 0 auto; /* when max-width is set */
}
```

**Validation:**

- `int` must be positive (> 0)
- `str` must be exactly `"stretch"`
- Other types raise `ValueError`

```python
# Valid
st_swagger_ui(url="...", width=800)
st_swagger_ui(url="...", width="stretch")
st_swagger_ui(url="...", width=None)

# Invalid - raises ValueError
st_swagger_ui(url="...", width=0)       # Zero
st_swagger_ui(url="...", width=-100)    # Negative
st_swagger_ui(url="...", width="50%")   # Invalid string
st_swagger_ui(url="...", width=800.5)   # Float not supported
```

**Technical Details:**

- **Python Type**: `Width = Union[int, Literal["stretch"], None]`
- **TypeScript Type**: `type Width = number | "stretch" | null`
- **CSS Class**: `.st-swagger-ui-container` (for custom styling)
- **Default**: Changed from no parameter to `"stretch"` for better UX

**Benefits:**

1. **Responsive Layout**: Works seamlessly with Streamlit's column system
2. **Centered Content**: Fixed max-width looks better on large screens
3. **Flexible**: Supports multiple layout preferences
4. **Customizable**: CSS class allows override styles

### Summary of All Parameters

| Parameter                 | Type                    | Default         | Description                                       |
| ------------------------- | ----------------------- | --------------- | ------------------------------------------------- |
| `url`                     | `Optional[str]`         | `None`          | OpenAPI spec URL (mutually exclusive with `spec`) |
| `spec`                    | `Optional[dict]`        | `None`          | OpenAPI spec dict (mutually exclusive with `url`) |
| `doc_expansion`           | `DocExpansion`          | `"list"`        | Operation expansion mode                          |
| `try_it_out_enabled`      | `bool`                  | `False`         | Enable "Try it out" functionality                 |
| `display_operation_id`    | `bool`                  | `False`         | Show operation IDs                                |
| `default_model_rendering` | `DefaultModelRendering` | `"example"`     | Model display mode                                |
| **`width`**               | **`Width`**             | **`"stretch"`** | **Max width control (NEW)**                       |
| `key`                     | `Optional[str]`         | `None`          | Streamlit component key                           |

### Breaking Changes

**Default Behavior Change:**

The component now defaults to `width="stretch"` instead of no width constraint.

**Before (implicit):**

```python
st_swagger_ui(url="...")
# No max-width, SwaggerUI default behavior
```

**After (explicit):**

```python
st_swagger_ui(url="...")
# max-width: 100%, fills parent container
```

**Migration:**

If you relied on the old SwaggerUI default behavior (no max-width), explicitly set `width=None`:

```python
# Old behavior (no max-width constraint)
st_swagger_ui(url="...", width=None)

# New default (full width)
st_swagger_ui(url="...")
```

### Technical Changes

#### Python (`__init__.py`)

```python
# Added type
Width = Union[int, Literal["stretch"], None]

# Added parameter with default
def st_swagger_ui(
    ...
    width: Width = "stretch",
    ...
)

# Added validation
if width is not None:
    if isinstance(width, str):
        if width != "stretch":
            raise ValueError(f"width must be an int or 'stretch'. Got: {width!r}")
    elif isinstance(width, int):
        if width <= 0:
            raise ValueError(f"width must be a positive integer. Got: {width}")
    else:
        raise ValueError(f"width must be an int or 'stretch', not {type(width).__name__}")
```

#### TypeScript (`index.tsx`)

```typescript
// Added type
export type Width = number | "stretch" | null;

// Added to shape
export type MyComponentDataShape = {
  ...
  width?: Width | null;
};

// Added CSS logic
const width: Width = data.width ?? "stretch";

const containerStyle: React.CSSProperties = {
  width: "100%",
  maxWidth: width === "stretch" ? "100%" : width ?? undefined,
  margin: width !== "stretch" && width !== null ? "0 auto" : undefined,
};

// Wrapped with styled container
<div className="st-swagger-ui-container" style={containerStyle}>
  <SwaggerUI ... />
</div>
```

### Files Modified

- `st_swagger_ui/__init__.py`: Added `width` parameter and validation
- `st_swagger_ui/frontend/src/index.tsx`: Added width handling and CSS styling
- `test_width.py`: Added comprehensive test script

### Build Artifacts

- **Frontend**: `index-Dbq-092K.js` (2.02 MB)
- **Wheel**: `dist/st_swagger_ui-0.1.0-py3-none-any.whl` (508K)
- **Sdist**: `dist/st_swagger_ui-0.1.0.tar.gz` (9.4K)

### Testing

Run the test script to verify all width options:

```bash
streamlit run test_width.py
```

**Test Coverage:**

- ✅ Default behavior (`width="stretch"`)
- ✅ Fixed pixel widths (`width=800`, `width=1600`, `width=400`)
- ✅ Column layout integration
- ✅ No constraint mode (`width=None`)
- ✅ Validation errors (invalid string, zero, negative)
