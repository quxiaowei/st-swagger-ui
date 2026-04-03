import json

import streamlit as st
from st_swagger_ui import st_swagger_ui

result = st.radio("Input type", ("URL", "Raw spec"), index=0, key="input_type")
st.markdown(
    "Enter an OpenAPI spec URL or paste the spec directly into the text area below."
)
url = st.text_input(
    "OpenAPI spec URL", "https://petstore3.swagger.io/api/v3/openapi.json"
)
spec_content = st.text_area("OpenAPI spec (JSON or YAML)", height=300)
spec_json = json.loads(spec_content) if spec_content else None
st.set_page_config(page_title="st_swagger_ui Example", layout="wide")
with st.container():
    if result == "URL":
        st_swagger_ui(
            url=url,
            key="bar",
        )
    else:
        st_swagger_ui(
            spec=spec_json,
            key="foo",
            doc_expansion="full",
            display_operation_id=False,
            default_model_rendering="model",
            try_it_out_enabled=False,
        )
