# ECM Community Platform

A community platform for discovering and ranking Energy Conservation Measures (ECMs) by building type, climate zone, and HVAC system. Built with Python and Streamlit.

---

## Features

- **Top-5 ECM Recommendations** — Describe your building (type, location, HVAC systems, NABERS-aligned operational data) and get ranked ECM suggestions via LLM.
- **Natural Language Search** — Query the ECM library with free-form questions.
- **ECM Browser** — Filter and sort all ECMs by building type, vote score, and keyword.
- **Community Voting** — Thumbs up/down on every ECM with required reasoning for downvotes.
- **Admin Dashboard** — Paginated view of all votes (password-protected).

---

## Prerequisites

- Python 3.10 or higher
- [An OpenRouter API key](https://openrouter.ai/keys) (free tier available)

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/FilhoRicardo/ecm-community-platform
cd ecm-community-platform

# 2. Install dependencies
pip install -e ".[dev]"   # includes all runtime deps + pytest

# 3. Configure environment
cp .env.example .env
# Edit .env and set OPENROUTER_API_KEY

# 4. Run the app
streamlit run app.py
```

The app will be available at `http://localhost:8501`.

---

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `OPENROUTER_API_KEY` | Yes | API key from [openrouter.ai/keys](https://openrouter.ai/keys). Used for LLM-based ECM ranking. |
| `ADMIN_PASSWORD` | No | Password protecting the Admin page and Settings changes. If unset, Settings is freely accessible and Admin is disabled. |
| `ECM_DATA_DIR` | No | Directory for `votes.db`. Defaults to the project root. Set to a persistent path when running multiple environments (dev/staging). |

---

## Project Structure

```
ecm-community-platform/
├── app.py            # Streamlit UI, page routing, all page functions
├── db_utils.py       # SQLite persistence (votes, ECM metadata, migrations)
├── ecm_utils.py      # ECM loading from .md files, path-traversal guards
├── llm_utils.py      # OpenRouter API client, keyword scoring, rate limiting
├── ecms/             # Community ECM content (organized by building typology)
│   ├── office_zero_energy/
│   ├── grocery/
│   └── ...
├── tests/            # pytest suite (36 tests, all passing)
├── .env.example      # Template for local configuration
├── setup.sh          # One-time setup helper script
└── pyproject.toml    # Package metadata and dependency declarations
```

---

## ECM Content Format

ECMs are Markdown files in `ecms/<building_slug>/`. Each file is parsed as:

- **Title**: First `# Heading` in the file
- **Content**: Full Markdown body
- **ID**: `<building_slug>:<filename.md>` (e.g. `office_zero_energy:ECM_Daylight_Harvesting_Controls_Office.md`)

The ECM browser loads all `.md` files recursively under `ecms/`. There is no CMS — content is managed via git.

---

## Running Tests

```bash
pip install -e ".[dev]"
pytest -v
```

---

## Deployment Notes

### Single-process (Streamlit native)

```bash
streamlit run app.py
```

### Multi-process (gunicorn / waitress)

Streamlit is not WSGI-native. Use the `--server.headless` flag and a reverse proxy:

```bash
streamlit run app.py --server.headless true --server.port 8501
```

**Rate limiting** (`llm_utils.py`): The rate limiter is **per-process**. Under multi-worker WSGI (e.g. `gunicorn --workers 4`), each worker maintains its own counter. For production multi-instance deployments, consider replacing the in-process rate limiter with a shared Redis counter.

**Database** (`db_utils.py`): `votes.db` uses SQLite with WAL mode. For multi-instance deployments, use a shared network path (NFS) or migrate to PostgreSQL.

**Security headers**: Streamlit does not set `X-Frame-Options`, `Content-Security-Policy`, or `X-Content-Type-Options` by default. For production, add these via a reverse proxy (nginx, Caddy) or a custom Streamlit component.

---

## License

MIT — Ricardo Filho
