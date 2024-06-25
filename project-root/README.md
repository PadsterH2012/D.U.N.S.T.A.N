# Dynamic Universal Narrative System for Tabletop Adventure Navigation (D-U-N-S-T-A-N)

## Overview

This project aims to create an application that leverages LLMs to become a Game Master for any type of RPG, providing an option to import and digest rules for gameplay. The system will offer open-ended play with the ability to maintain game flow and realism through saved gameplay and history.

## Components

- **Web Application (Flask)**
- **Database (PostgreSQL)**
- **RPG-Content-API**
- **AI Agents**
- **Rule Extraction**

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Project

1. Clone the repository.
2. Navigate to the project root directory.
3. Run `docker-compose up --build` to build and start all containers.

## Directory Structure

- `web/`: Flask web application.
- `rpg-content-api/`: API for reading and extracting data from PDFs.
- `ai-agents/`: AI agents handling game logic.
- `rule-extraction/`: Rule extraction and ingestion.
- `docker-compose.yml`: Docker Compose configuration.
- `README.md`: Project overview and setup instructions.

## License

This project is licensed under the MIT License.
