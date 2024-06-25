# Dynamic Universal Narrative System for Tabletop Adventure Navigation (D-U-N-S-T-A-N)

## Overview

This project aims to create an application that leverages LLMs to become a Game Master for any type of RPG, providing an option to import and digest rules for gameplay. The system will offer open-ended play with the ability to maintain game flow and realism through saved gameplay and history.

## Components

- **Web Application (Flask)**: [http://localhost:5000](http://localhost:5000)
  - Manages the main user interface and interactions.
- **Database (PostgreSQL)**: Stores game data, player data, rules, and state information.
- **RPG-Content-API**: [http://localhost:8000](http://localhost:8000)
  - Extracts and provides data from PDF rulebooks and other resources.
  - **Characters Endpoint**: [http://localhost:8000/api/characters](http://localhost:8000/api/characters)
  - **Quests Endpoint**: [http://localhost:8000/api/quests](http://localhost:8000/api/quests)
- **AI Agents**: Handles different aspects of the game logic.
  - **AI_Agent_StoryTeller**: Describes scenes and progresses the narrative.
  - **AI_Agent_PlayerInteractor**: Manages player interactions.
  - **AI_Agent_PlayerCharacter**: Manages player stats and inventory.
  - **AI_Agent_Combat**: Manages combat scenarios.
  - **AI_Agent_OverSeer**: Ensures game rules are followed.
  - **AI_Agent_CampaignManager**: Manages overarching quests and campaigns.
  - **AI_Agent_SideQuest**: Handles minor quests and encounters.
  - **AI_Agent_NPCManager**: Creates and manages dynamic NPCs.
  - **AI_Agent_Validator**: Ensures content and actions adhere to game rules.
- **Rule Extraction**: Processes and ingests rules from PDFs and updates the database.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Project

1. Clone the repository.
2. Navigate to the project root directory.
3. Run `docker-compose up --build` to build and start all containers.

### Directory Structure

- `web/`: Flask web application.
  - `Dockerfile`
  - `app/`
    - `__init__.py`
    - `routes.py`
    - `templates/`
  - `requirements.txt`
- `rpg-content-api/`: API for reading and extracting data from PDFs.
  - `Dockerfile`
  - `api/`
    - `__init__.py`
    - `endpoints.py`
    - `pdf_processing.py`
  - `requirements.txt`
- `ai-agents/`: AI agents handling game logic.
  - `Dockerfile`
  - `agents/`
    - `__init__.py`
    - `storyteller.py`
    - `player_interactor.py`
  - `requirements.txt`
- `rule-extraction/`: Rule extraction and ingestion.
  - `Dockerfile`
  - `extractor/`
    - `__init__.py`
    - `rule_parser.py`
  - `requirements.txt`
- `docker-compose.yml`: Docker Compose configuration.
- `README.md`: Project overview and setup instructions.

### API Endpoints

#### RPG-Content-API

- **Characters Endpoint**: [http://localhost:8000/api/characters](http://localhost:8000/api/characters)
  - Returns a list of characters.
- **Quests Endpoint**: [http://localhost:8000/api/quests](http://localhost:8000/api/quests)
  - Returns a list of quests.

### Example API Requests

curl http://localhost:8000/api/characters
curl http://localhost:8000/api/quests

Using a Web Browser:
Open http://localhost:8000/api/characters
Open http://localhost:8000/api/quests