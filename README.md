# Product Review Feedback Microservice

## Overview
A backend microservice built with FastAPI (Python) that accepts user-submitted product reviews and returns AI-generated feedback. The service is modular, testable, and ready for extension with real AI models.

## Features
- **POST /v1/review/feedback**: Accepts a product review and returns:
  - Sentiment ("positive", "negative", "neutral")
  - Readability score (Flesch Reading Ease approximation)
  - Suggestions for improvement
- OpenAPI docs at `/docs`
- Modular, clean architecture (routing, services, AI logic)
- API versioning for future enhancements
- Unit and integration tests (pytest)
- Code coverage enforced in CI (min 85%)
- Linting (flake8) and formatting (black) checks
- Dockerized for easy local development
- CI/CD with GitHub Actions (build, test, lint, push image)

## API Usage

### Endpoint
`POST /v1/review/feedback`

#### Request Body
```json
{
  "review": "string"
}
```

#### Response
```json
{
  "sentiment": "positive",
  "readability_score": 72.5,
  "suggestions": ["Add more details to your review."]
}
```

See [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API documentation.

## Setup & Run

### Prerequisites
- Docker & docker-compose installed

### Local Development
```sh
docker compose up --build
```
The API will be available at [http://localhost:8000/docs](http://localhost:8000/docs)

### Run Tests
```sh
docker compose run --rm --env PYTHONPATH=. app pytest
```

### Run Code Coverage
```sh
docker compose run --rm --env PYTHONPATH=. app pytest --cov=app --cov-fail-under=85
```

### Lint & Format
```sh
docker compose run --rm --env PYTHONPATH=. app flake8 app/
docker compose run --rm --env PYTHONPATH=. app black --check app/
```

## Project Structure
```
app/
  main.py                # FastAPI app entrypoint
  config.py              # App configuration
  routers/
    __init__.py
    v1/
      review.py          # API endpoint for review feedback
  services/
    feedback_service.py  # Business logic for feedback
  models/
    ai/
      interfaces.py      # ReviewAnalyzer interface
      mock/
        __init__.py      # Mock AI implementation
        sentiment.py     # Rule-based sentiment analysis
        readability.py   # Readability score logic
        suggestions.py   # Suggestions logic
tests/
  test_api.py            # API integration tests
  test_feedback_service.py # Unit tests for feedback logic
Dockerfile
docker-compose.yml
requirements.txt
```

## Development & Testing
- All code is formatted with **black** and checked with **flake8**.
- Tests and coverage are run with **pytest** and **pytest-cov**.
- CI workflow: build, test, coverage, lint, and push Docker image to GitHub Container Registry.

## AI Logic
The AI logic is currently rule-based and located in `app/models/ai/mock/`. It is designed for easy replacement with real AI models or external API calls in the future. The interface is defined in `app/models/ai/interfaces.py`.

## Credits
This project was developed using **GitHub Copilot** for code generation, and test writing. Copilot accelerated development by suggesting boilerplate and test cases, allowing focus on clean architecture and extensibility.

---

Feel free to reach out with any questions! [@ivand890](https://github.com/ivand890)
