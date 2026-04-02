import streamlit as st
from st_swagger_ui import st_swagger_ui

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run st_swagger_ui/example.py`

# st.subheader("Component with constant args")

# # Create an instance of our component with a constant `name` arg, and
# # print its output value.
# result = st_swagger_ui("World")
# st.markdown("You've clicked %s times!" % int(result["num_clicks"]))

# st.markdown("---")
st.subheader("Component with variable args")

# Create a second instance of our component whose `name` arg will vary
# based on a text_input widget.
#
# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.
spec = {
    "openapi": "3.0.0",
    "info": {
        "title": "ESIGN",
        "description": "\u64a4\u9500\u7b7e\u7f72\u6d41\u7a0b",
        "version": "1.0.0",
    },
    "servers": [{"url": "https://podev.segway-ninebot.com:50001/RESTAdapter"}],
    "paths": {
        "/cn-ninebot/esign/sign-flow/{signFlowId}/revoke": {
            "post": {
                "tags": ["PUBLIC"],
                # "summary": "\u64a4\u9500\u7b7e\u7f72\u6d41\u7a0b",
                "description": "描述:\u64a4\u9500\u7b7e\u7f72\u6d41\u7a0b",
                "operationId": "urn:CN:Ninebot:PUBLIC:ESIGN-SI_SignFlowRevoke_Out",
                "parameters": [
                    {
                        "name": "signFlowId",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "string"},
                    },
                    {
                        "name": "esignAppId",
                        "required": False,
                        "schema": {"type": "string"},
                        "in": "header",
                    },
                    {
                        "name": "esignAppSecret",
                        "required": False,
                        "schema": {"type": "string"},
                        "in": "header",
                    },
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/Request"}
                        }
                    },
                    "required": True,
                },
                "responses": {
                    "200": {
                        "description": "Successful operation",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Response"}
                            }
                        },
                    },
                    "400": {"description": "Internal Error"},
                },
            }
        }
    },
    "components": {
        "schemas": {
            "Request": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "object",
                        "properties": {"field1": {"type": "string"}},
                    }
                },
            },
            "Response": {
                "type": "object",
                "properties": {
                    "code": {"type": "integer", "format": "int64", "example": 0},
                    "message": {"type": "string", "example": "success"},
                },
            },
        }
    },
}
result = st_swagger_ui(
    spec=spec,
    key="foo",
    doc_expansion="full",
    display_operation_id=False,
    default_model_rendering="model",
    # try_it_out_enabled=False,
)
