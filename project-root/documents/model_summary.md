# DUNSTAN Project Models Summary

This document provides a summary of the models and their respective fields used in the DUNSTAN project. Each model is defined in a specific location within the project directory structure.

## Character Model

### Fields
- **id**: Integer, Primary Key
- **name**: String, Indexed
- **sex**: String, Indexed
- **age**: String, Indexed
- **traits**: Text
- **behaviors**: Text
- **background_summary**: Text
- **book_title**: String, Indexed (nullable)
- **author**: String, Indexed (nullable)
- **dialogue_examples**: Text (nullable)
- **genre**: String, Indexed (nullable)

### Locations
- `project-root/web/app/models.py`
- `project-root/rpg-content-api/api/models.py`
- `project-root/content_creator/extractor/models.py`

## Quest Model

### Fields
- **id**: Integer, Primary Key
- **name**: String, Indexed
- **storyline_summary**: Text
- **expected_gameplay_duration**: String
- **book_title**: String, Indexed (nullable)
- **author**: String, Indexed (nullable)
- **genre**: String, Indexed (nullable)

### Locations
- `project-root/web/app/models.py`
- `project-root/rpg-content-api/api/models.py`

## Player Model

### Fields
- **id**: Integer, Primary Key
- **username**: String, Indexed
- **email**: String, Indexed
- **password**: String

### Locations
- `project-root/web/app/models.py`

## Game Model

### Fields
- **id**: Integer, Primary Key
- **name**: String, Indexed
- **description**: Text
- **creator_id**: Integer, Foreign Key referencing Player.id
- **created_at**: DateTime

### Locations
- `project-root/web/app/models.py`

## Setting Model

### Fields
- **id**: Integer, Primary Key
- **key**: String, Indexed
- **value**: Text

### Locations
- `project-root/web/app/models.py`

## PlayerGame Model

### Fields
- **id**: Integer, Primary Key
- **player_id**: Integer, Foreign Key referencing Player.id
- **game_id**: Integer, Foreign Key referencing Game.id

### Locations
- `project-root/web/app/models.py`

## Notes

- The Character model is used across multiple containers to ensure consistency in character data management.
- Each model is defined using SQLAlchemy and is utilized for various operations like data storage, retrieval, and manipulation.
- Ensure the models are synchronized across different containers to maintain data integrity and consistency.
