# Project: DUNSTAN
### Dynamic Universal Narrative System for Tabletop Adventure Navigation

## Aim
This project aims to create an application that leverages LLMs to become a Game Master for any type of RPG, providing an option to import and digest rules for gameplay. The system will offer open-ended play with the ability to maintain game flow and realism through saved gameplay and history.

## Components

### Web Application (Flask)
- **URL**: [http://localhost:5000](http://localhost:5000)
- Manages the main user interface and interactions.
- **Folder/File Locations**:
  - `project-root/web/Dockerfile`
  - `project-root/web/app/__init__.py`
  - `project-root/web/run.py`
  - `project-root/web/app/upload_routes.py`
- **Responsibilities**:
  - Serves HTML pages to the user.
  - Handles user authentication and authorization using Flask-Login.
  - Provides routes for various user interactions like uploading files, viewing results, etc.
  - Forwards uploaded PDF files to the content-creator container for processing.
  - Displays the extracted and processed data received from the content-creator.
- **Key Files**:
  - `Dockerfile`: Defines the environment for the web service.
  - `__init__.py`: Initializes the Flask app, SQLAlchemy, Bcrypt, and LoginManager.
  - `run.py`: Runs the Flask app.
  - `upload_routes.py`: Handles the upload route and forwards files to the content-creator.
- **Ports**: Exposes port 5000 for web access.
- **Dependencies**: Depends on db and content-creator for its operations.

### Database (DB) Container
- **Purpose**: Provides persistent storage for the application data.
- **Description**:
  - Database: PostgreSQL.
- **Folder/File Locations**:
  - `project-root/db/Dockerfile`
  - `project-root/db/init.sql`
- **Responsibilities**:
  - Stores user information, game details, character data, and quest details.
  - Provides a relational database for SQLAlchemy to interact with.
- **Key Files**:
  - `Dockerfile`: Defines the environment for the PostgreSQL database.
  - `init.sql`: Initializes the database schema with required tables.
- **Ports**: Exposes port 5432 for database connections.
- **Dependencies**: None, but must be healthy before other containers dependent on it can start.

### Content Creator Container
- **Purpose**: Processes PDF files to extract character and quest information.
- **Description**:
  - Framework: Flask for API routes.
- **Folder/File Locations**:
  - `project-root/content_creator/Dockerfile`
  - `project-root/content_creator/__init__.py`
  - `project-root/content_creator/run.py`
  - `project-root/content_creator/extractor/upload_routes.py`
- **Responsibilities**:
  - Receives PDF files from the web container.
  - Uses AI/ML models to extract and process text from PDF files.
  - Extracts character details, quest information, and other relevant data.
  - Communicates with external services (e.g., Ollama) for processing tasks.
  - Returns the processed data back to the web container.
- **Key Files**:
  - `Dockerfile`: Defines the environment for the content creator service.
  - `run.py`: Runs the Flask app and registers API routes.
  - `upload_routes.py`: Handles the file upload and processing logic.
- **Ports**: Exposes port 8001 for API access.
- **Dependencies**: Depends on db for accessing configuration settings.

### RPG Content API Container
- **Purpose**: Provides an API for interacting with RPG content.
- **Description**:
  - Framework: Flask for API routes.
- **Folder/File Locations**:
  - `project-root/rpg-content-api/Dockerfile`
  - `project-root/rpg-content-api/run.py`
  - `project-root/rpg-content-api/api/models.py`
- **Responsibilities**:
  - Manages RPG content like characters and quests.
  - Provides endpoints to query and manage RPG data.
  - Integrates with the content-creator to process and store data.
- **Key Files**:
  - `Dockerfile`: Defines the environment for the RPG content API service.
  - `run.py`: Runs the Flask app and registers API routes.
  - `models.py`: Defines the SQLAlchemy models for characters and quests.
- **Ports**: Exposes port 8000 for API access.
- **Dependencies**: Depends on db for storing and retrieving data, and optionally on content-creator for data processing.

## Overall Architecture Flow
- **Web Container**: Serves as the front-end interface for users to interact with the application. It handles file uploads and forwards them to the content-creator.
- **Content Creator Container**: Receives the uploaded PDF files, processes them to extract relevant data, and returns this data to the web container.
- **RPG Content API Container**: Provides an API to manage and retrieve RPG-related content like characters and quests. It interacts with the content-creator for processing and the db for data storage.
- **DB Container**: Stores all the application data, including user information, game details, characters, and quests. It serves as the central storage accessed by all other containers.

This architecture ensures a clear separation of concerns, with each container handling a specific aspect of the application's functionality, thereby enhancing maintainability and scalability.