#!/usr/bin/env bash
# Setup script — copies .env.example to .env and verifies Python dependencies.
# Run once after cloning:  bash setup.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -f "$SCRIPT_DIR/.env" ]; then
    if [ -f "$SCRIPT_DIR/.env.example" ]; then
        cp "$SCRIPT_DIR/.env.example" "$SCRIPT_DIR/.env"
        echo "✓ Created .env from .env.example"
        echo "  → Edit .env and set OPENROUTER_API_KEY (and ADMIN_PASSWORD for admin access)"
    else
        echo "✗ .env.example not found — cannot create .env"
        exit 1
    fi
else
    echo "✓ .env already exists"
fi

# Verify Python dependencies
if command -v python3 &>/dev/null; then
    echo "Checking Python dependencies..."
    python3 -c "import streamlit; import pandas; import requests; import dotenv; import markdown" 2>/dev/null \
        && echo "✓ All dependencies are installed" \
        || echo "✗ Missing dependencies — run: pip install -r requirements.txt"
else
    echo "⚠ python3 not found — cannot verify dependencies"
fi

echo ""
echo "Setup complete. Start the app with: streamlit run app.py"
