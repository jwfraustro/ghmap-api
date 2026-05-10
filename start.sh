#!/bin/bash

# Start script for ghmap-api

uvicorn ghmap_api.main:app --reload --host 0.0.0.0 --port 8000