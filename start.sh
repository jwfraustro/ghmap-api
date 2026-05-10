#!/bin/bash

# Start script for ghmap-api

uvicorn ghmap_api.main:app --host "" --port ${PORT:-8000}