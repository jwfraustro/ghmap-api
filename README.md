# ghmap-api

Project to allow community contributions to GHMap

## Installation

### Using pip

```bash
pip install -r requirements.txt
pip install -e .
```

### Using conda

```bash
conda env create -f environment.yml
conda activate ghmap_api
```


### Using Docker

```bash
docker-compose up
```


## Usage

Start the development server:

```bash
./start.sh
```

Or manually:

```bash
uvicorn ghmap_api.main:app --reload
```

The API will be available at http://localhost:8000

API documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

Run tests:

```bash
pytest
```

Format code:

```bash
black ghmap_api
```

Lint code:

```bash
ruff ghmap_api
```

## License

This project is licensed under the MIT License.


## Author

Joshua Fraustro (jwfraustro@gmail.com)