"""Test script to verify default values for try_it_out_enabled and display_operation_id."""

import streamlit as st
from st_swagger_ui import st_swagger_ui

st.title("Default Values Test")

st.header("Test 1: Default values (both should be False)")
st.write("try_it_out_enabled=False (default), display_operation_id=False (default)")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    key="test1"
)

st.header("Test 2: Explicit False values")
st.write("try_it_out_enabled=False, display_operation_id=False")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    try_it_out_enabled=False,
    display_operation_id=False,
    key="test2"
)

st.header("Test 3: Enable Try It Out")
st.write("try_it_out_enabled=True, display_operation_id=False")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    try_it_out_enabled=True,
    display_operation_id=False,
    key="test3"
)

st.header("Test 4: Display Operation IDs")
st.write("try_it_out_enabled=False, display_operation_id=True")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    try_it_out_enabled=False,
    display_operation_id=True,
    key="test4"
)

st.header("Test 5: Both enabled")
st.write("try_it_out_enabled=True, display_operation_id=True")
st_swagger_ui(
    url="https://petstore.swagger.io/v2/swagger.json",
    try_it_out_enabled=True,
    display_operation_id=True,
    key="test5"
)
