Original Functional Dependencies:

Pokemon Species Table:
Name, Variant -> Everything Else
    Note: These are not the primary key in the database, because the Name could potentially be changed later, such as across languages

Pokemon Instance Table:
InstanceID -> Everything Else

Trainer Table:
Trainer_ID -> Everything
Name -> Everything (Changable, so not used as primary key)

Held Item Table:
Item_ID -> Everything
Name -> Description, Add_Date

Team Table:
Trainer_ID, Team_Slot, Party_slot -> Pokemon_ID, Item_ID, Last_Updated

Ability_List Table:
Ability_ID -> Name, Description, AddDate

MoveList Table:
Move_ID -> Everything

Anomoly Identification:

    Update Anomalies:
        I couldn't find any update anomalies.
        However, hypothetically, if a pokemon has a lot of variants with the same stats, and one game updates those stats,
        There could be one variant that they forgot to update. However, since it is possible for different variants
        to have different stats, I don't consider this an update anomoly

    Insert Anomalies:
        A pokemon type cannot be added without a corresponding pokemon.
        A pokemon nature cannot be added without a corresponding pokemon instance.

    Delete Anomalies:
        If you remove all pokemon species of a given type, you will lose that type in the database
        If you remove all pokemon instances of a specific pokemon nature, you will lose that nature in the database


Decomposition steps:
    A nature table and a type table have been added. 
    Now, PokemonSpecies references type IDs, and PokemonInstance references nature IDs
