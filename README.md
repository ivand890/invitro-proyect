# Product Review Feedback Microservice

## Overview
A backend microservice built with FastAPI (Python) that accepts user-submitted product reviews and returns AI-generated feedback.

### Features
- **POST /review/feedback**: Accepts a product review and returns:
  - Sentiment (positive, negative, neutral)
  - Readability score
  - Suggestions for improvement
- Modular, clean architecture (routing, services, AI logic)
- Unit and integration tests
- Dockerized for easy local development
- CI with GitHub Actions

## Setup & Run

### Prerequisites
- Docker & docker-compose installed

### Local Development
```sh
docker-compose up --build
```
The API will be available at [http://localhost:8000/docs](http://localhost:8000/docs)


### Run Tests
```sh
docker-compose run --rm --env PYTHONPATH=. app pytest
```

### Lint & Format
Run lint and formatting checks:
```sh
docker-compose run --rm app flake8 app tests
docker-compose run --rm app black --check app tests
```


## Project Structure
```
app/
  main.py            # FastAPI app
  routers/
    review.py        # API endpoint
  services/
    feedback_service.py # Business logic
  ai_logic/          # Simulated AI logic
    sentiment.py
    readability.py
    suggestions.py

 tests/              # Unit and integration tests
```


## AI Tools Used
This project was developed using **GitHub Copilot** for code generation, structure, and test writing. Copilot accelerated development by suggesting boilerplate and test cases, allowing me to focus on clean architecture and extensibility. Docstrings were also suggested by Copilot, improving code clarity and maintainability.

## Extending with Real AI
The `app/ai_logic/` modules are designed for easy replacement with real AI models or external API calls in the future.

---

Feel free to reach out with any questions!
