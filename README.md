# FXMacroData for RAGFlow

Use your FXMacroData subscription to bring cross-currency indicators, full available histories and release calendars into RAGFlow workflows and Agent research. Source-linked reference chunks let generated answers cite the economic data used by each workflow.

**[Subscribe to FXMacroData](https://fxmacrodata.com/subscribe?utm_source=github&utm_medium=referral&utm_campaign=ragflow-fxmacrodata&utm_content=subscribe)** for access to covered non-USD datasets and full available history.

Evaluate the integration before subscribing with public USD catalogue, recent indicator history (currently a rolling 90-day window) and calendars, which require no FXMacroData key or account.

Select from 23 REST operations and 49 hosted MCP tools, configure typed inputs, and use source-linked reference chunks, record tables and complete API responses in subsequent workflow steps.

[FXMacroData](https://fxmacrodata.com/?utm_source=github&utm_medium=referral&utm_campaign=ragflow-fxmacrodata&utm_content=readme) · [API reference](https://fxmacrodata.com/documentation/reference?utm_source=github&utm_medium=referral&utm_campaign=ragflow-fxmacrodata&utm_content=docs)

## Install

This source integration targets RAGFlow's Python workflow engine at commit `5bd80b3455b6670cd07e0cd09c8a08a5ada6bee7` (0.27.2). Use a source installation with its documented Python and frontend build prerequisites. The installer adds the Python tool, its React forms and the workflow/Agent menu registrations.

```sh
python install.py /path/to/ragflow
python install.py /path/to/ragflow --apply
python -m pip install -r requirements.txt
```

The first command checks every changed upstream file without writing. The installer refuses mismatched source files, existing integration files and paths escaping the checkout. Install dependencies in RAGFlow's Python environment. Rebuild the frontend using RAGFlow's normal `npm run build` from `web`, then restart the source installation. Its separate Go execution engine is outside this Python component's compatibility scope.

## Visual workflows

Add **FXMacroData** from the operator menu. Select an operation, then fill its generated argument fields. The default is the public USD release calendar. Connect its outputs to later nodes:

- `json`: the record/table projection.
- `response`: the complete original response, retaining units, dates, revision metadata and source fields.
- `formalized_content`: RAGFlow reference chunks for generated answers, with an FXMacroData link.
- `source_url`: the canonical public source URL, without credentials or campaign parameters.

## Agent tools

In an Agent's tool picker, select **FXMacroData** and choose the desired operation. The agent receives that operation's full input schema and supplies its arguments at runtime. Add more FXMacroData tool instances for other operations—for example catalogue discovery, indicator history and release calendar for an economic briefing. The corresponding reference chunks enter RAGFlow's normal citation pipeline.

## Connect your subscription

To connect a subscription, the deployment operator supplies `FXMACRODATA_API_KEY` through the process secret/environment configuration and enables **Deployment credential** on the selected node. Only the boolean access mode is saved in the workflow. A node cannot read arbitrary environment variables, and no key is stored in its settings, model arguments or exports. A deployment credential authorizes users able to execute that node; use a separate deployment when credentials must be isolated by tenant.

Requests use documented query-parameter authentication over HTTPS. Redirects are disabled and diagnostics are sanitized. Website links use static attribution parameters; data requests do not. There are no tracking calls.

Missing values and publication times remain missing. Forecast labels and source distinctions are retained. FX reference rates are not executable quotes. Event streaming is a finite capture bounded by duration and count; choose a host execution timeout compatible with that capture.

See `CAPABILITIES.md`, `PUBLIC_FILES.json` and `UPSTREAM_FILES.json` for operation coverage, package contents and the matching upstream source.
