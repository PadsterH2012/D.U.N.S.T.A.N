# DUNSTAN Project Models Summary

This document provides a summary of the models and their respective fields used in the DUNSTAN project. Each model is defined in a specific location within the project directory structure.

Character Model
Fields:

id: Integer, Primary Key
name: String, Indexed
sex: String, Indexed
age: String, Indexed
traits: Text
behaviors: Text
background_summary: Text
book_title: String, Indexed (nullable)
author: String, Indexed (nullable)
dialogue_examples: Text (nullable)
genre: String, Indexed (nullable)
Locations:

project-root/web/app/models.py
project-root/rpg-content-api/api/models.py
project-root/content_creator/extractor/models.py
project-root/shared/models/models.py (added to share models across containers)
Quest Model
Fields:

id: Integer, Primary Key
name: String, Indexed
storyline_summary: Text
expected_gameplay_duration: String
book_title: String, Indexed (nullable)
author: String, Indexed (nullable)
genre: String, Indexed (nullable)
Locations:

project-root/web/app/models.py
project-root/rpg-content-api/api/models.py
project-root/shared/models/models.py (added to share models across containers)
Player Model
Fields:

id: Integer, Primary Key
username: String, Indexed
email: String, Indexed
password: String
Locations:

project-root/web/app/models.py
project-root/shared/models/models.py (added to share models across containers)
Game Model
Fields:

id: Integer, Primary Key
name: String, Indexed
description: Text
creator_id: Integer, Foreign Key referencing Player.id
created_at: DateTime
Locations:

project-root/web/app/models.py
project-root/shared/models/models.py (added to share models across containers)
Setting Model
Fields:

id: Integer, Primary Key
key: String, Indexed
value: Text
Locations:

project-root/web/app/models.py
project-root/shared/models/models.py (added to share models across containers)
PlayerGame Model
Fields:

player_id: Integer, Foreign Key referencing Player.id, Primary Key
game_id: Integer, Foreign Key referencing Game.id, Primary Key
Locations:

project-root/web/app/models.py
project-root/shared/models/models.py (added to share models across containers)
Notes
The Character model is indeed used across multiple containers to ensure consistency in character data management.
Each model is defined using SQLAlchemy and is utilized for various operations like data storage, retrieval, and manipulation.
Ensure the models are synchronized across different containers to maintain data integrity and consistency.
Updated models.py in Shared Directory
To ensure consistency, all model definitions should now be maintained in project-root/shared/models/models.py.
