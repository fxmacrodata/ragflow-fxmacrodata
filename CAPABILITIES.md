# FXMacroData operation coverage

One native visual component and an Agent tool form support all 72 operations. Each configured Agent instance exposes the selected operation with its complete input schema.

The adapter preserves the full public response alongside its record projection. Dates, units, source metadata and unavailable values remain as supplied. REST access is limited by the user's dataset entitlement; public USD catalogue, recent history and calendars can be used anonymously. Streaming returns finite captures.

This table describes the included public discovery snapshot: 23 REST operations and 49 hosted MCP tools. New service operations require a refreshed package.

| Operation | Public interface | Native surface |
|---|---|---|
| `health` | GET /v1/health | Operation selector: `health` |
| `ping` | GET /v1/ping | Operation selector: `ping` |
| `forex` | GET /v1/forex/{base}/{quote} | Operation selector: `forex` |
| `intraday_reference_rates` | GET /v1/fx/intraday-reference-rates/{base}/{quote} | Operation selector: `intraday_reference_rates` |
| `fx_sources` | GET /v1/fx/sources | Operation selector: `fx_sources` |
| `fx_source_universe` | GET /v1/fx/source-universe | Operation selector: `fx_source_universe` |
| `data_catalogue` | GET /v1/data_catalogue/{currency} | Operation selector: `data_catalogue` |
| `release_calendar` | GET /v1/calendar/{currency} | Operation selector: `release_calendar` |
| `market_sessions` | GET /v1/market_sessions | Operation selector: `market_sessions` |
| `rate_differentials` | GET /v1/rate_differentials/{base}/{quote} | Operation selector: `rate_differentials` |
| `curves` | GET /v1/curves/{currency} | Operation selector: `curves` |
| `financial_prices` | GET /v1/financial_prices/{currency} | Operation selector: `financial_prices` |
| `press_releases` | GET /v1/press-releases/{currency} | Operation selector: `press_releases` |
| `risk_sentiment` | GET /v1/risk_sentiment | Operation selector: `risk_sentiment` |
| `factors` | GET /v1/factors/{currency}/{factor} | Operation selector: `factors` |
| `event_predictions` | GET /v1/predictions/{currency}/{indicator} | Operation selector: `event_predictions` |
| `latest_announcements` | GET /v1/announcements/{currency}/latest | Operation selector: `latest_announcements` |
| `indicator_history` | GET /v1/announcements/{currency}/{indicator} | Operation selector: `indicator_history` |
| `cot` | GET /v1/cot/{currency} | Operation selector: `cot` |
| `latest_commodities` | GET /v1/commodities/latest | Operation selector: `latest_commodities` |
| `commodities` | GET /v1/commodities/{indicator} | Operation selector: `commodities` |
| `announcement_changes` | GET /v1/announcements/changes | Operation selector: `announcement_changes` |
| `stream_events` | GET /v1/stream/events | Operation selector: `stream_events` |
| `mcp_ping` | MCP tools/call | Operation selector: `mcp_ping` |
| `mcp_mcp_capabilities` | MCP tools/call | Operation selector: `mcp_mcp_capabilities` |
| `mcp_mcp_auth_guide` | MCP tools/call | Operation selector: `mcp_mcp_auth_guide` |
| `mcp_subscribe_for_mcp_access` | MCP tools/call | Operation selector: `mcp_subscribe_for_mcp_access` |
| `mcp_data_catalogue` | MCP tools/call | Operation selector: `mcp_data_catalogue` |
| `mcp_risk_sentiment` | MCP tools/call | Operation selector: `mcp_risk_sentiment` |
| `mcp_macro_news` | MCP tools/call | Operation selector: `mcp_macro_news` |
| `mcp_release_calendar` | MCP tools/call | Operation selector: `mcp_release_calendar` |
| `mcp_release_calendar_visual_artifact` | MCP tools/call | Operation selector: `mcp_release_calendar_visual_artifact` |
| `mcp_event_predictions` | MCP tools/call | Operation selector: `mcp_event_predictions` |
| `mcp_latest_announcements` | MCP tools/call | Operation selector: `mcp_latest_announcements` |
| `mcp_announcement_changes` | MCP tools/call | Operation selector: `mcp_announcement_changes` |
| `mcp_press_releases` | MCP tools/call | Operation selector: `mcp_press_releases` |
| `mcp_macro_factor` | MCP tools/call | Operation selector: `mcp_macro_factor` |
| `mcp_fx_reference_sources` | MCP tools/call | Operation selector: `mcp_fx_reference_sources` |
| `mcp_fx_reference_universe` | MCP tools/call | Operation selector: `mcp_fx_reference_universe` |
| `mcp_fx_intraday_reference_rates` | MCP tools/call | Operation selector: `mcp_fx_intraday_reference_rates` |
| `mcp_rate_curve` | MCP tools/call | Operation selector: `mcp_rate_curve` |
| `mcp_rate_differentials` | MCP tools/call | Operation selector: `mcp_rate_differentials` |
| `mcp_latest_commodities` | MCP tools/call | Operation selector: `mcp_latest_commodities` |
| `mcp_forex` | MCP tools/call | Operation selector: `mcp_forex` |
| `mcp_seasonality` | MCP tools/call | Operation selector: `mcp_seasonality` |
| `mcp_indicator_query` | MCP tools/call | Operation selector: `mcp_indicator_query` |
| `mcp_plot_visual_artifact` | MCP tools/call | Operation selector: `mcp_plot_visual_artifact` |
| `mcp_indicator_visual_artifact` | MCP tools/call | Operation selector: `mcp_indicator_visual_artifact` |
| `mcp_forex_visual_artifact` | MCP tools/call | Operation selector: `mcp_forex_visual_artifact` |
| `mcp_commodities_visual_artifact` | MCP tools/call | Operation selector: `mcp_commodities_visual_artifact` |
| `mcp_cot_visual_artifact` | MCP tools/call | Operation selector: `mcp_cot_visual_artifact` |
| `mcp_policy_rate_differential_visual_artifact` | MCP tools/call | Operation selector: `mcp_policy_rate_differential_visual_artifact` |
| `mcp_macro_briefing_task` | MCP tools/call | Operation selector: `mcp_macro_briefing_task` |
| `mcp_indicator_intel_task` | MCP tools/call | Operation selector: `mcp_indicator_intel_task` |
| `mcp_pair_intel_task` | MCP tools/call | Operation selector: `mcp_pair_intel_task` |
| `mcp_macro_heatmap_task` | MCP tools/call | Operation selector: `mcp_macro_heatmap_task` |
| `mcp_policy_scenario_modeler_task` | MCP tools/call | Operation selector: `mcp_policy_scenario_modeler_task` |
| `mcp_macro_war_room_task` | MCP tools/call | Operation selector: `mcp_macro_war_room_task` |
| `mcp_event_impact_replay_task` | MCP tools/call | Operation selector: `mcp_event_impact_replay_task` |
| `mcp_quant_scenario_lab_task` | MCP tools/call | Operation selector: `mcp_quant_scenario_lab_task` |
| `mcp_known_at_time_task` | MCP tools/call | Operation selector: `mcp_known_at_time_task` |
| `mcp_macro_regime_classifier_task` | MCP tools/call | Operation selector: `mcp_macro_regime_classifier_task` |
| `mcp_release_risk_score_task` | MCP tools/call | Operation selector: `mcp_release_risk_score_task` |
| `mcp_portfolio_risk_engine_task` | MCP tools/call | Operation selector: `mcp_portfolio_risk_engine_task` |
| `mcp_fx_trade_setup_task` | MCP tools/call | Operation selector: `mcp_fx_trade_setup_task` |
| `mcp_fx_backtest_task` | MCP tools/call | Operation selector: `mcp_fx_backtest_task` |
| `mcp_macro_research_pack_task` | MCP tools/call | Operation selector: `mcp_macro_research_pack_task` |
| `mcp_market_sessions` | MCP tools/call | Operation selector: `mcp_market_sessions` |
| `mcp_cot_data` | MCP tools/call | Operation selector: `mcp_cot_data` |
| `mcp_commodities` | MCP tools/call | Operation selector: `mcp_commodities` |
| `mcp_financial_prices` | MCP tools/call | Operation selector: `mcp_financial_prices` |
| `mcp_official_dataset_family` | MCP tools/call | Operation selector: `mcp_official_dataset_family` |

[FXMacroData API reference](https://fxmacrodata.com/documentation/reference?utm_source=github&utm_medium=referral&utm_campaign=ragflow-fxmacrodata&utm_content=docs)
