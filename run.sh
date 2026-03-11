#!/bin/bash

source .venv/bin/activate
uvicorn src.manage:app --host 0.0.0.0 --port 5099 --log-level debug --reload
deactivate
