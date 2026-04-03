"""Test script for width parameter."""

import streamlit as st
from st_swagger_ui import st_swagger_ui

st.title("Width Parameter Test")

st.markdown("""
## Test Cases

1. **Default (width="stretch")**: Should fill parent container
2. **Fixed width (width=800)**: Should be max 800px, centered
3. **Large width (width=1600)**: Should be max 1600px, centered
4. **Small width (width=400)**: Should be max 400px, centered
5. **In columns**: Should respect column width
6. **No constraint (width=None)**: Should use SwaggerUI default
""")

st.header("Test 1: Default (width='stretch')")
st.write("Expected: Full width of parent container")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    key="test1"
)

st.header("Test 2: Fixed width (width=800)")
st.write("Expected: Max 800px, centered")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    width=800,
    key="test2"
)

st.header("Test 3: Large width (width=1600)")
st.write("Expected: Max 1600px, centered")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    width=1600,
    key="test3"
)

st.header("Test 4: Small width (width=400)")
st.write("Expected: Max 400px, centered")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    width=400,
    key="test4"
)

st.header("Test 5: In columns")
st.write("Expected: Each should fill its column (50% width)")
col1, col2 = st.columns(2)
with col1:
    st_swagger_ui(
        url="https://petstore.swagger.io/v2/swagger.json",
        width="stretch",
        key="test5a"
    )
with col2:
    st_swagger_ui(
        url="https://petstore.swagger.io/v2/swagger.json",
        width=600,
        key="test5b"
    )

st.header("Test 6: No constraint (width=None)")
st.write("Expected: SwaggerUI default behavior (no max-width)")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    width=None,
    key="test6"
)

st.header("Test 7: Validation errors")
st.write("These should raise ValueError:")

try:
    st_swagger_ui(
        url="https://petstore.swagger.io/v2/swagger.json",
        width="invalid",  # type: ignore
        key="test7a"
    )
    st.error("Test 7a failed: Should have raised ValueError for invalid string")
except ValueError as e:
    st.success(f"Test 7a passed: {e}")

try:
    st_swagger_ui(
        url="https://petstore.swagger.io/v2/swagger.json",
        width=0,
        key="test7b"
    )
    st.error("Test 7b failed: Should have raised ValueError for zero")
except ValueError as e:
    st.success(f"Test 7b passed: {e}")

try:
    st_swagger_ui(
        url="https://petstore.swagger.io/v2/swagger.json",
        width=-100,
        key="test7c"
    )
    st.error("Test 7c failed: Should have raised ValueError for negative")
except ValueError as e:
    st.success(f"Test 7c passed: {e}")
