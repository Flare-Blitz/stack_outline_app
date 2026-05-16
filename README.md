# Project Description

This is Pokemon Champions, a site for building Pokemon teams
Using this application, you will be able to select a trainer,
and modify the trainer's item list and team setup.


# Stack Outline App

Barebones project outline for:
- Python 3
- Flask backend
- Relational DB (SQLite by default)
- SQLAlchemy ORM
- HTML5/CSS3 frontend with Bootstrap and Jinja2 templates
- Git version control

## Project Structure

```
stack_outline_app/
  app/
    __init__.py
    extensions.py
    models.py
    routes.py
    static/css/styles.css
    templates/base.html
    templates/index.html
  config.py
  run.py
  requirements.txt
  .env.example
  .gitignore
```

## Quick Start

1. Create and activate a virtual environment.
   ```
   python -m venv venv   
   venv\Scripts\activate 
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Insert data.
   ```bash
   python seed.py
   ```

3. Run the app:
   ```bash
   python run.py
   ```
4. Open http://127.0.0.1:5000

# Database Seyup

The database is setup by running python seed.py in the previous Quick Start section,
referencing models.py for the table setup.


# Usage

You start on the index page, from there you can click on a user to go to the profile page
From the profile page, you can:
- Click on one of the teams to open the editTeam page
- Click on the Add Held Item button to go to the item list page
- Click the discard button on the item list to remove the item from the user
From the edit team page, you can:
- Select a combination of team slot, pokemon, and item
- When you hit submit, that team slot is replaced with the selected pokemon and item.
From the Item List page, you can:
- Click on an item to add it to the trainer's collection

## Multi-Table CRUD

### Create

- When a pokemon is added to an empty team slot, a Team row is inserted
- When an item is added to a trainer, the Trainer_HeldItem table is updated with the new relationship

### Read

- Just about every page displays SQL data

### Update

- When you replace an existing pokemon in the Team table, an Update statement is used
- When an item is discarded from a user, All instances of that item in the Teams section for that Trainer are updated to none

### Delete

- When you discard an item, the row is deleted from the Trainer_HeldItem table

## Relationship Management

There are many one to many, and many-to-many relationships being shown.
Examples:
- The profile page displays all items belonging to a user
- The profile page displays all pokemon associated with a user

## Transaction Logic

When an item is removed from a trainer, first the item is removed from the Trainer_HeldItem table,
Then after the item was successfully removed, the Teams table is queried for all instances of that trainer
and held item, and the held-item is updated to null. Afterwards, the changes are commited.

## Data Validation

There are parts when data is checked, such as when an item is being added to a trainer,
it is first checked to make sure the trainer doesn't already own that item before
inserting a row into the database.

## Summary Dashboard

The Index page has 3 statistics:
1) The total number of trainers
2) The total number of Pokemon Species in the database
3) The average base stat total (sum all stats and divide by the number of stats) of all pokemon species


