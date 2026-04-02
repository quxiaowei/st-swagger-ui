from typing import Literal, Optional

import streamlit as st

DocExpansion = Literal["list", "full", "none"]
DefaultModelRendering = Literal["example", "model"]

out = st.components.v2.component(
    "st_swagger_ui.st_swagger_ui",
    js="index-*.js",
    css="index-*.css",
    html='<div class="react-root"></div>',
)

_VALID_DOC_EXPANSIONS = {"list", "full", "none"}
_VALID_DEFAULT_MODEL_RENDERINGS = {"example", "model"}


def st_swagger_ui(
    url: Optional[str] = None,
    spec: Optional[dict] = None,
    doc_expansion: Optional[DocExpansion] = None,
    try_it_out_enabled: Optional[bool] = None,
    display_operation_id: Optional[bool] = None,
    default_model_rendering: Optional[DefaultModelRendering] = None,
    key: Optional[str] = None,
) -> None:
    """Create a new instance of "st_swagger_ui".

    Parameters
    ----------
    url: str or None
        URL to fetch the OpenAPI/Swagger specification from.
        Example: "https://petstore.swagger.io/v2/swagger.json"
    spec: dict or None
        OpenAPI/Swagger specification as a Python dict.
        Use this when you have the spec already loaded in memory.
    doc_expansion: str or None
        Controls the default expansion setting for operations.
        Must be one of: "list", "full", or "none".
        - "list": Show only the operation names (default)
        - "full": Show operations and their details expanded
        - "none": Show operations collapsed
    try_it_out_enabled: bool or None
        Controls whether the "Try it out" section is enabled.
        - True: Enable the "Try it out" functionality
        - False: Disable the "Try it out" functionality
        - None: Use SwaggerUI default (enabled)
    display_operation_id: bool or None
        Controls whether to display the operationId for each operation.
        - True: Show the operationId next to the operation name
        - False: Hide the operationId
        - None: Use SwaggerUI default (hidden)
    default_model_rendering: str or None
        Controls how to render the model section.
        Must be one of: "example" or "model".
        - "example": Show example values (default)
        - "model": Show the model structure
    key: str or None
        An optional key that uniquely identifies this component.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If both 'url' and 'spec' are provided, or neither is provided.
        If 'doc_expansion' is not one of the valid values.
        If 'default_model_rendering' is not one of the valid values.

    Examples
    --------
    >>> # Load from URL
    >>> st_swagger_ui(url="https://petstore.swagger.io/v2/swagger.json")
    
    >>> # Load from local file with full expansion
    >>> import json
    >>> with open("openapi.json") as f:
    ...     spec = json.load(f)
    >>> st_swagger_ui(spec=spec, doc_expansion="full")
    
    >>> # Disable "Try it out" feature
    >>> st_swagger_ui(url="https://petstore.swagger.io/v2/swagger.json", try_it_out_enabled=False)
    
    >>> # Display operation IDs
    >>> st_swagger_ui(
    ...     url="https://petstore.swagger.io/v2/swagger.json",
    ...     display_operation_id=True
    ... )
    
    >>> # Show model structure instead of example values
    >>> st_swagger_ui(
    ...     url="https://petstore.swagger.io/v2/swagger.json",
    ...     default_model_rendering="model"
    ... )
    """
    if url and spec:
        raise ValueError("Cannot provide both 'url' and 'spec'. Use only one.")
    
    if not url and not spec:
        raise ValueError("Either 'url' or 'spec' must be provided.")
    
    if doc_expansion is not None and doc_expansion not in _VALID_DOC_EXPANSIONS:
        raise ValueError(
            f"doc_expansion must be one of: {', '.join(repr(x) for x in _VALID_DOC_EXPANSIONS)}. "
            f"Got: {doc_expansion!r}"
        )
    
    if (
        default_model_rendering is not None
        and default_model_rendering not in _VALID_DEFAULT_MODEL_RENDERINGS
    ):
        raise ValueError(
            f"default_model_rendering must be one of: {', '.join(repr(x) for x in _VALID_DEFAULT_MODEL_RENDERINGS)}. "
            f"Got: {default_model_rendering!r}"
        )
    
    out(
        key=key,
        default=None,
        data={
            "url": url,
            "spec": spec,
            "docExpansion": doc_expansion,
            "tryItOutEnabled": try_it_out_enabled,
            "displayOperationId": display_operation_id,
            "defaultModelRendering": default_model_rendering,
        },
    )
