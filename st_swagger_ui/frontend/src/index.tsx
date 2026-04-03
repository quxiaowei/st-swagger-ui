import {
  FrontendRenderer,
  FrontendRendererArgs,
} from "@streamlit/component-v2-lib";
import { StrictMode } from "react";
import { createRoot, Root } from "react-dom/client";
import SwaggerUI from "swagger-ui-react";
import "swagger-ui-react/swagger-ui.css";

export type DocExpansion = "list" | "full" | "none";
export type DefaultModelRendering = "example" | "model";
export type Width = number | "stretch" | null;

export type MyComponentDataShape = {
  url?: string | null;
  spec?: object | null;
  docExpansion?: DocExpansion;
  tryItOutEnabled?: boolean;
  displayOperationId?: boolean;
  defaultModelRendering?: DefaultModelRendering;
  width?: Width | null;
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
  const docExpansion: DocExpansion = data.docExpansion ?? "list";
  const tryItOutEnabled: boolean = data.tryItOutEnabled ?? false;
  const displayOperationId: boolean = data.displayOperationId ?? false;
  const defaultModelRendering: DefaultModelRendering =
    data.defaultModelRendering ?? "example";
  const width: Width = data.width ?? "stretch";

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

  const containerStyle: React.CSSProperties = {
    width: "100%",
    maxWidth: width === "stretch" ? "100%" : (width ?? undefined),
    margin: width !== "stretch" && width !== null ? "0 auto" : undefined,
  };

  reactRoot.render(
    <StrictMode>
      <div className="st-swagger-ui-container" style={containerStyle}>
        <SwaggerUI
          url={url}
          spec={spec}
          docExpansion={docExpansion}
          tryItOutEnabled={tryItOutEnabled}
          displayOperationId={displayOperationId}
          defaultModelRendering={defaultModelRendering}
        />
      </div>
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
