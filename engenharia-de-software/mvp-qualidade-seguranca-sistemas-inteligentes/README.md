# MVP — Quality & Security of Intelligent Systems: Diabetes Prediction API

Capstone project for the Quality & Security of Intelligent Systems module of the PUC-Rio "Ciência de Dados e Analytics" postgraduate program. A full-stack application that serves a diabetes-risk classification model behind a documented REST API, with automated tests and a simple web front-end for interacting with it.

## Architecture

- **`api/`** — Flask + Flask-OpenAPI3 REST API.
  - `model/` — SQLAlchemy models and ML pipeline glue (loading, preprocessing, evaluation).
  - `schemas/` — Pydantic request/response schemas, exposed as interactive OpenAPI docs (Swagger/Redoc/RapiDoc).
  - `MachineLearning/` — the ML side of the project: training notebook/script, trained models (KNN, Logistic Regression, Random Forest), scaler and pipeline artifacts, and held-out test data.
  - `test_api.py`, `test_modelos.py` — automated tests (pytest/nose2) covering the API endpoints and the model pipeline.
- **`front/`** — vanilla HTML/CSS/JS client served by the API, for adding, viewing, and predicting diabetes risk for patients.

## Running it

```bash
cd api
pip install -r requirements.txt
python app.py
```

The API redirects `/` to the front-end (`/front/index.html`) and exposes interactive docs at `/docs`.

Run the test suite with:

```bash
pytest
```

## Tech stack

Python, Flask, Flask-OpenAPI3, SQLAlchemy, Pydantic, scikit-learn, pandas, pytest — vanilla HTML/CSS/JS front-end.
