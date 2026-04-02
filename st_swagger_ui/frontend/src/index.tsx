import {
  FrontendRenderer,
  FrontendRendererArgs,
} from "@streamlit/component-v2-lib";
import { StrictMode } from "react";
import { createRoot, Root } from "react-dom/client";
import SwaggerUI from "swagger-ui-react";
import "swagger-ui-react/swagger-ui.css";
import "./swagger-ui-overrides.css";

export type DocExpansion = "list" | "full" | "none";
export type DefaultModelRendering = "example" | "model";

export type MyComponentDataShape = {
  url?: string | null;
  spec?: object | null;
  docExpansion?: DocExpansion | null;
  tryItOutEnabled?: boolean | null;
  displayOperationId?: boolean | null;
  defaultModelRendering?: DefaultModelRendering | null;
};

const reactRoots: WeakMap<FrontendRendererArgs["parentElement"], Root> =
  new WeakMap();

const SwaggerUIComponent: FrontendRenderer<
  Record<string, never>,
  MyComponentDataShape
> = (args) => {
  const { data, parentElement } = args;

  const rootElement = parentElement.querySelector(".react-root");

  if (!rootElement) {
    throw new Error("Unexpected: React root element not found");
  }

  let reactRoot = reactRoots.get(parentElement);
  if (!reactRoot) {
    reactRoot = createRoot(rootElement);
    reactRoots.set(parentElement, reactRoot);
  }

  const url: string | undefined = data.url ?? undefined;
  const spec: object | undefined = data.spec ?? undefined;
  const docExpansion: DocExpansion | undefined = data.docExpansion ?? undefined;
  const tryItOutEnabled: boolean | undefined =
    data.tryItOutEnabled ?? undefined;
  const displayOperationId: boolean | undefined =
    data.displayOperationId ?? undefined;
  const defaultModelRendering: DefaultModelRendering | undefined =
    data.defaultModelRendering ?? undefined;

  if (url && spec) {
    throw new Error("Cannot provide both 'url' and 'spec'. Use only one.");
  }

  if (!url && !spec) {
    throw new Error("Either 'url' or 'spec' must be provided.");
  }

  if (
    docExpansion !== undefined &&
    !["list", "full", "none"].includes(docExpansion)
  ) {
    throw new Error(
      `docExpansion must be one of: "list", "full", or "none". Got: ${docExpansion}`,
    );
  }

  if (
    defaultModelRendering !== undefined &&
    !["example", "model"].includes(defaultModelRendering)
  ) {
    throw new Error(
      `defaultModelRendering must be one of: "example" or "model". Got: ${defaultModelRendering}`,
    );
  }

  reactRoot.render(
    <StrictMode>
      <SwaggerUI
        url={url}
        spec={spec}
        docExpansion={docExpansion}
        tryItOutEnabled={tryItOutEnabled}
        displayOperationId={displayOperationId}
        defaultModelRendering={defaultModelRendering}
      />
    </StrictMode>,
  );

  return () => {
    const reactRoot = reactRoots.get(parentElement);

    if (reactRoot) {
      reactRoot.unmount();
      reactRoots.delete(parentElement);
    }
  };
};

export default SwaggerUIComponent;
