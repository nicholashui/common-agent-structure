# Build Central LLM API Usage & Cost Dashboard App

## Project Name Suggestion
**LLMUsageHub** or **MultiLLM Dashboard** or **API Cost Central** or **LLM Spend Tracker**

## 1. Project Overview
Create a **web application** that provides a **single central view** for tracking usage, costs, balances, spending, and token consumption across **all** of the user's LLM API accounts.

The user currently has accounts with:  
- x.ai (Grok API)  
- Poe  
- MiniMax  
- Kimi (Moonshot AI)  
- OpenRouter  
...and many others.

The app should let the user add their API keys once and see **everything aggregated in one beautiful dashboard** — total monthly spend, remaining credits, per-provider breakdowns, charts, trends, alerts, etc.

**Reference / Inspiration**:
Inspired by **[cc-switch](https://github.com/farion1231/cc-switch)** (the popular desktop tool for managing LLM providers for Claude Code / Codex / Gemini CLI). This web app is **purely focused on usage/cost analytics** across direct personal API keys, serving as a usage-only companion to cc-switch but as a web application.

## 2. Core Goals
- One unified place to monitor **all** LLM spending and usage.
- Secure, local-only storage of API keys (never sent to any server).
- Automatic or on-demand fetching of usage/billing data.
- Historical tracking + visualizations.
- Extremely extensible — easy to add new providers.
- Beautiful, modern UI similar to cc-switch.

## 3. Key Features (Must-Have)

### Provider Management
- Add / edit / remove accounts with: name, provider type (preset), API key, base URL (for custom endpoints), notes.
- Pre-built **presets** for as many providers as possible (see section 4).
- Support multiple accounts per provider.
- One-click “Refresh All” and individual refresh buttons.

### Usage & Balance Fetching
- Prefer **official APIs** where available (e.g. `/usage`, `/billing`, `/balance`, `/v1/token_plan/remains`, etc.).
- Fallback options:
  - Manual entry of current usage/balance.
  - Web dashboard scraping (using Playwright if needed, last resort).
- Background auto-refresh (configurable interval) + manual refresh.
- Store full history snapshots in local DB.

### Dashboard UI
- **Overview page**:
  - Total estimated USD spend (today / this month / all time).
  - Total remaining credits/balance (normalized where possible).
  - Number of active providers + quick status.
- **Provider cards** (grid or list):
  - Name + logo (if available).
  - Current balance / remaining credits.
  - Spend this month + trend indicator.
  - Last updated timestamp.
- **Charts**:
  - Spending trend (line chart — daily/weekly).
  - Cost breakdown by provider (pie).
  - Token usage by model (bar).
  - Usage heatmap or calendar view.
- **Detailed tables**:
  - Per-provider usage history.
  - Model-level breakdown.
- **Alerts**:
  - Low balance warnings (configurable thresholds).
  - High daily spend notifications.

### Cost Calculation
- Built-in pricing tables for major models (input/output tokens → USD).
- Allow user to override pricing per model.
- Show estimated USD even when provider only reports tokens.

### Data Persistence & Export
- Local **SQLite** database for all historical usage snapshots.
- Export full data as CSV or JSON.

### Security & UX
- API keys stored **encrypted** locally (Fernet symmetric encryption).
- Dark/light theme (default dark, matching modern AI tools).
- Browser-based UI accessible from localhost.
- Fully offline-first after initial setup.
- Responsive, clean, professional UI.

### Nice-to-Have (Phase 2)
- AI-powered insights (“You spent 68% on Kimi this month — consider switching heavy tasks to Groq”).
- Import/export configuration (including possible cc-switch import).
- Per-model cost forecasting.
- Optional proxy/router mode (like LiteLLM or cc-switch) so the app can also log usage from actual API calls.

## 4. Supported Providers (List as Many as Possible)
The app must ship with **pre-built presets** (fetch logic + pricing) for **as many providers as possible**. Start with user-mentioned ones, then expand.

**High Priority (User’s Current Providers)**
- xAI (Grok API) — console.x.ai usage / billing endpoints
- Poe.com — usage/points_history and current_balance endpoints
- OpenRouter — account usage API
- MiniMax — token plan remains and usage endpoints
- Kimi (Moonshot AI) — platform.moonshot.ai usage/balance API

**Other Major Providers (Include Full Presets)**
- OpenAI
- Anthropic (Claude)
- Google Gemini / Vertex AI
- Groq
- Mistral AI
- Together.ai
- Fireworks.ai
- DeepSeek
- SiliconFlow
- Zhipu AI (GLM / ChatGLM)
- Baichuan
- StepFun
- Alibaba (DashScope / Qwen)
- Baidu (ERNIE)
- Tencent (Hunyuan)
- iFlytek (Spark)
- 01.AI
- Cohere
- Perplexity
- Replicate
- Hugging Face Inference Endpoints
- Novita.ai
- Lepton AI
- Azure OpenAI
- AWS Bedrock (if possible via API or manual)
- Any custom OpenAI-compatible endpoint (user can add base URL + key)

For providers without public usage APIs, still include presets with:
- Manual balance entry
- Notes on how to copy-paste from their dashboard

## 5. Technical Stack

### Backend
- **Framework**: Python 3.11+ with FastAPI
- **API**: OpenAPI 3.1 (auto-generated from FastAPI, browsable at /docs)
- **Database**: SQLite with SQLAlchemy ORM
- **HTTP Client**: httpx (async)
- **Security**: API keys encrypted at rest using cryptography Fernet
- **Background Tasks**: FastAPI BackgroundTasks + APScheduler

### API Design (OpenAPI)
- RESTful endpoints for all CRUD operations
- Automatic OpenAPI schema generation
- Interactive API docs via Swagger UI at /docs
- ReDoc alternative at /redoc

### Frontend
- **Framework**: React 18 + TypeScript
- **Build Tool**: Vite
- **Styling**: TailwindCSS + shadcn/ui
- **Charts**: Recharts
- **State Management**: Zustand
- **HTTP Client**: Axios or fetch API

### Architecture
- **Web App** (not desktop) — runs locally in browser
- Backend runs as a local server (localhost:8000)
- Frontend served by FastAPI static files or separate Vite dev server
- 100% local — no cloud sync unless explicitly added later

## 6. Development Phases (Suggested)
1. Project setup (FastAPI backend + React frontend + SQLite).
2. Provider management + secure key storage.
3. Core usage fetcher system (abstract interface).
4. Implement 5–6 high-priority providers (xAI, Poe, OpenRouter, MiniMax, Kimi, OpenAI).
5. Dashboard UI + charts.
6. Add remaining providers + pricing tables.
7. Background refresh, alerts, export, polish.
8. Testing + documentation.

## 7. Deliverables
- Complete source code with excellent comments and README.
- Clear instructions on **how to add a new provider** (new Python module + pricing config).
- Setup scripts for running locally with FastAPI + React.
- Sample data / test mode.
- License: MIT (or whatever user prefers).

This spec should give the coding agent everything needed to build a production-ready, beautiful, and highly useful central usage dashboard. Feel free to ask the user for clarification on specific provider APIs or preferred tech choices.

**Ready to code!** 🚀
