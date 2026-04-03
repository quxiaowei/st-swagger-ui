"""Test script to verify try_it_out_enabled parameter."""

import streamlit as st
from st_swagger_ui import st_swagger_ui

st.title("Try It Out Enabled Test")

st.header("Test 1: try_it_out_enabled=False (should be disabled)")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    try_it_out_enabled=False,
    key="test1"
)

st.header("Test 2: try_it_out_enabled=True (should be enabled)")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    try_it_out_enabled=True,
    key="test2"
)

st.header("Test 3: Default behavior (try_it_out_enabled=None)")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    key="test3"
)

st.header("Test 4: Combined with other parameters")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    try_it_out_enabled=False,
    doc_expansion="full",
    display_operation_id=True,
    default_model_rendering="model",
    key="test4"
)
