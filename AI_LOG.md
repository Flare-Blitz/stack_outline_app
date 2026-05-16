# AI Usage:

- Tool: GitHub Copilot
  Date: 2026-05-09
  Prompt: "I want to create a database that will store the data I will be using throughout this project. How can I create a database that will be apparent to someone who it running my application based on the git repository?"
  AI Output: Explained that Flask-SQLAlchemy is already configured, recommended storing the SQLite DB in `instance/`, creating a seed/init script or CLI command, and documenting the setup in README.
  My Modification: Revied files, no changes made

- Tool: GitHub Copilot
  Date: 2026-05-09
  Prompt: "Assuming I do option 1, will the data constantly be updated in the Git Repo as I alter the table and add rows/columns?"
  AI Output: Clarified that `instance/` is ignored by git, so the local SQLite file will not be tracked or updated in the repository.
  My Modification: No changes made

- Tool: GitHub Copilot
  Date: 2026-05-09
  Prompt: "I would want them to be able to demo the application, how can I include a database with sample data in the repo so they can see my application?"
  AI Output: Recommended a seed script as the best approach, explained how to create `seed.py`, and compared it with including a pre-populated DB file in git.
  My Modification: Discussed options with the user; no changes were made to the repo yet.

- Tool: GitHub Copilot
  Date: 2026-05-09
  Prompt: "I like option 1. Although, I don't understand what the role of the models.py file is. Explain it to me and what it may look like after I add my database?"
  AI Output: Explained that `models.py` defines tables as Python classes, described class-to-table and attribute-to-column mapping, and gave example model classes for Pokemon and Team.
  My Modification: No file edits were made; clarified how models connect to the DB.

- Tool: GitHub Copilot
  Date: 2026-05-09
  Prompt: "Using the attatched image of the database (This is the model used in Project 2), add classes to the file models.py to create the necessary tables for the application"
  AI Output: Added full SQLAlchemy model classes to `app/models.py` matching the provided schema, including species, abilities, moves, trainers, items, instances, and team tables.
  My Modification: Updated `app/models.py` with the new table classes.
    Verified that each table has the appropriate entries and modified/inserted columns when different.

- Tool: GitHub Copilot
  Date: 2026-05-10
  Prompt: "Based on the TODO comments left in the seed.py file, add sample entries to the database."
  AI Output: Created comprehensive seed data for Pokemon database including 58 abilities, 150+ moves, 50+ Pokemon species (all final evolutions), 26 items (including mega stones), 12 trainers with realistic usernames, 100+ Pokemon instances (2 per species), and team data.
  My Modification: Updated seed.py with complete database seeding functionality.

- Tool: GitHub Copilot
  Date: 2026-05-10
  Prompt: "There were some problems with your script. First, some of the pokemon were not final evolutions. Second, the trainer names didn't sound like the names of users who would be using this application. Third, you only created an instance for some of the pokemon, instead of 2 instances for every pokemon species created."
  AI Output: Fixed the seed script by replacing non-final evolutions with final forms, changed trainer names to realistic usernames (e.g., "jacob_stream", "sarah_p92"), and added 2 instances per Pokemon species with varied EVs, natures, and moves.
  My Modification: Corrected seed.py data to ensure accuracy and completeness.

- Tool: GitHub Copilot
  Date: 2026-05-10
  Prompt: "This looks good, but it needs some modifications. First, we need some variant forms, including mega evolutions, regional forms, and transformations (such as palafin normal and hero). Any variants should include the version without variants."
  AI Output: Added variant Pokemon species (mega evolutions like Mega Venusaur, regional forms like Alolan Raichu, transformations like Palafin Hero Form) to the Pokemon data, along with corresponding abilities, moves, and instances.
  My Modification: Extended seed.py to include variant forms while maintaining base forms.

- Tool: GitHub Copilot
  Date: 2026-05-10
  Prompt: "If a pokemon only learns 1 ability, such as how Palafin only learns Zero to Hero, or how Mega Charizard Y only learns Drought, then they should only have 1 ability. Pokemon that aren't a base form should not have their own instance, as the instance will be based off of the base form. Also, Palafin zero form is the pokemon's base form."
  AI Output: Fixed ability assignments for single-ability Pokemon (removed duplicate abilities for Palafin and Mega Charizard Y), corrected is_base_form flag for Palafin Zero (set to True), and removed instances for non-base forms (variants) since instances should only exist for base forms.
  My Modification: Corrected seed.py to properly handle abilities and base form instances.

  Tool: Google Gemini
  Date: 2026-05-15
  Prompt: "If I have a Trainer table and Item table in Flask, with a helper table in between, where they each have a trainers and items variable, how can I query all items that are not owned by a specific trainer?"
  AI Output: Provided an example where a subquery is generated and used to filter the item list by querying the items
  that already exist
  My Modification: Modified the class names, and changed the query type to accomodate for my existing variables.
