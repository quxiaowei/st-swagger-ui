"""Test script to verify all default values."""

import streamlit as st
from st_swagger_ui import st_swagger_ui

st.title("All Default Values Test")

st.header("Test 1: All defaults")
st.write("""
- try_it_out_enabled=False (default)
- display_operation_id=False (default)
- default_model_rendering='example' (default)
""")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    key="test1"
)

st.header("Test 2: Explicit defaults")
st.write("""
- try_it_out_enabled=False
- display_operation_id=False
- default_model_rendering='example'
""")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    try_it_out_enabled=False,
    display_operation_id=False,
    default_model_rendering="example",
    key="test2"
)

st.header("Test 3: Model rendering = 'model'")
st.write("""
- try_it_out_enabled=False
- display_operation_id=False
- default_model_rendering='model'
""")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    try_it_out_enabled=False,
    display_operation_id=False,
    default_model_rendering="model",
    key="test3"
)

st.header("Test 4: All enabled/custom")
st.write("""
- try_it_out_enabled=True
- display_operation_id=True
- default_model_rendering='model'
""")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    try_it_out_enabled=True,
    display_operation_id=True,
    default_model_rendering="model",
    key="test4"
)
