"""Test script to verify all final default values."""

import streamlit as st
from st_swagger_ui import st_swagger_ui

st.title("Final Default Values Test")

st.header("Test 1: All defaults")
st.write("""
**All parameters at default values:**
- doc_expansion='list' (default)
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
**Explicitly set all defaults:**
- doc_expansion='list'
- try_it_out_enabled=False
- display_operation_id=False
- default_model_rendering='example'
""")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    doc_expansion="list",
    try_it_out_enabled=False,
    display_operation_id=False,
    default_model_rendering="example",
    key="test2"
)

st.header("Test 3: All expanded/visible")
st.write("""
**Show everything:**
- doc_expansion='full'
- try_it_out_enabled=True
- display_operation_id=True
- default_model_rendering='model'
""")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    doc_expansion="full",
    try_it_out_enabled=True,
    display_operation_id=True,
    default_model_rendering="model",
    key="test3"
)

st.header("Test 4: All collapsed/hidden")
st.write("""
**Hide everything:**
- doc_expansion='none'
- try_it_out_enabled=False
- display_operation_id=False
- default_model_rendering='example'
""")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    doc_expansion="none",
    try_it_out_enabled=False,
    display_operation_id=False,
    default_model_rendering="example",
    key="test4"
)
