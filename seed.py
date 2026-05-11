from app import create_app, db
from app.models import (
    PokemonSpecies, AbilityList, Pokemon_Ability, MoveList, Pokemon_Move,
    Trainer, HeldItem, Trainer_HeldItem, PokemonInstance, Team
)
from datetime import date, timedelta

app = create_app()

def seed_database():
    with app.app_context():
        db.drop_all()  # Drop existing tables for a clean slate
        db.create_all()  # Create tables if they don't exist

        # ===== ABILITIES =====
        abilities_data = [
            ("A1", "Overgrow", "Boosts Grass-type moves when HP is low"),
            ("A2", "Blaze", "Boosts Fire-type moves when HP is low"),
            ("A3", "Torrent", "Boosts Water-type moves when HP is low"),
            ("A4", "Rivalry", "Deals more damage to same gender Pokemon"),
            ("A5", "Static", "May paralyze on contact"),
            ("A6", "Piggyback", "Takes on appearance of Pokemon it battles"),
            ("A7", "Intimidate", "Lowers opponent's Attack on switch-in"),
            ("A8", "Pressure", "Opponent's moves use 2 PP instead of 1"),
            ("A9", "Adaptability", "Powers up moves of the same type"),
            ("A10", "Dry Skin", "Takes damage in sun, heals in rain"),
            ("A11", "Compound Eyes", "Increases accuracy of moves"),
            ("A12", "Simple", "Doubles stat changes"),
            ("A13", "Shed Skin", "May heal status conditions each turn"),
            ("A14", "Thick Fat", "Resists Fire and Ice-type moves"),
            ("A15", "Water Absorb", "Heals HP when hit by Water-type moves"),
            ("A16", "Effect Spore", "May poison, paralyze or sleep on contact"),
            ("A17", "Flash Fire", "Immune to Fire moves and gains their power"),
            ("A18", "Motor Drive", "Immune to Electric moves and gains Speed"),
            ("A19", "Sturdy", "Immune to OHKO moves and paralysis"),
            ("A20", "Analysis", "Boosts Special Attack when moving after opponent"),
            ("A21", "Synchronize", "Passes status conditions to opponent"),
            ("A22", "Clear Body", "Prevents stat reduction"),
            ("A23", "Natural Cure", "Heals status on switch-out"),
            ("A24", "Lightning Rod", "Draws in Electric moves and boosts Special Attack"),
            ("A25", "Serene Grace", "Moves have a 60% chance to have a secondary effect"),
            ("A26", "Swift Swim", "Doubles Speed in rain"),
            ("A27", "Chlorophyll", "Doubles Speed in sun"),
            ("A28", "Illuminate", "Increases wild Pokemon encounter rate"),
            ("A29", "Trace", "Copies opponent's ability"),
            ("A30", "Huge Power", "Doubles Attack"),
            ("A31", "Poison Point", "May poison on contact"),
            ("A32", "Inner Focus", "Protects from flinching"),
            ("A33", "Magnet Pull", "Traps Steel-type Pokemon"),
            ("A34", "Soundproof", "Immune to sound-based moves"),
            ("A35", "Rain Dish", "Heals HP in rain"),
            ("A36", "Sand Stream", "Creates sandstorm on switch-in"),
            ("A37", "Pressure", "Opponent's moves use 2 PP instead of 1"),
            ("A38", "Thick Fat", "Resists Fire and Ice-type moves"),
            ("A39", "Early Bird", "Wakes up quickly from sleep"),
            ("A40", "Flame Body", "May burn on contact"),
            ("A41", "Run Away", "Allows escape from any wild Pokemon"),
            ("A42", "Keen Eye", "Prevents accuracy reduction"),
            ("A43", "Hyper Cutter", "Prevents Attack reduction"),
            ("A44", "Pickup", "May pick up items after battle"),
            ("A45", "Truant", "Skips every other turn"),
            ("A46", "Hustle", "Boosts Attack but lowers accuracy"),
            ("A47", "Cute Charm", "May infatuate on contact"),
            ("A48", "Plus", "Boosts Special Attack when with minus Pokemon"),
            ("A49", "Minus", "Boosts Special Attack when with plus Pokemon"),
            ("A50", "Forecast", "Changes type based on weather"),
            ("A51", "Marvel Scale", "Boosts Defense when afflicted with status"),
            ("A52", "Liquid Ooze", "Damages Pokemon that drain HP"),
            ("A53", "Limber", "Immune to paralysis"),
            ("A54", "Cloud Nine", "Negates weather effects"),
            ("A55", "Sniper", "Boosts damage of critical hits"),
            ("A56", "Infiltrator", "Bypasses opponent's barrier moves"),
            ("A57", "Competitive", "Boosts Special Attack when stat is lowered"),
            ("A58", "Moxie", "Boosts Attack after knocking out opponent"),
        ]
        
        for ability_id, name, desc in abilities_data:
            ability = AbilityList(id=ability_id, name=name, description=desc)
            db.session.add(ability)
        
        db.session.commit()
        print(f"✓ Added {len(abilities_data)} abilities")

        # ===== MOVES =====
        moves_data = [
            ("M1", "Tackle", 40, 1.0, "Normal", 0, "Physical attack with basic power", 20),
            ("M2", "Ember", 40, 1.0, "Fire", 0, "Shoots flames at opponent, may burn", 20),
            ("M3", "Water Gun", 40, 1.0, "Water", 0, "Sprays water, may lower accuracy", 20),
            ("M4", "Vine Whip", 45, 1.0, "Grass", 0, "Whips with vines", 20),
            ("M5", "Thunder Bolt", 90, 1.0, "Electric", 0, "Electric attack, may paralyze", 20),
            ("M6", "Hydro Pump", 110, 0.8, "Water", 0, "Powerful water attack", 20),
            ("M7", "Fire Blast", 110, 0.85, "Fire", 0, "Powerful fire attack, may burn", 20),
            ("M8", "Blizzard", 110, 0.7, "Ice", 0, "Freezing attack, may freeze", 20),
            ("M9", "Hurricane", 110, 0.7, "Flying", 0, "Whirlwind attack, may confuse", 20),
            ("M10", "Earthquake", 100, 1.0, "Ground", 0, "Causes tremor, hits all around", 20),
            ("M11", "Close Combat", 120, 1.0, "Fighting", 0, "Lowers Defense and Special Defense", 20),
            ("M12", "Stone Edge", 100, 0.8, "Rock", 0, "High critical hit ratio", 20),
            ("M13", "Iron Head", 80, 1.0, "Steel", 0, "May flinch opponent", 20),
            ("M14", "Waterfall", 80, 1.0, "Water", 0, "Physical water attack, may paralyze", 20),
            ("M15", "Psychic", 90, 1.0, "Psychic", 0, "May lower Special Defense", 20),
            ("M16", "Shadow Ball", 80, 1.0, "Ghost", 0, "May lower Special Defense", 20),
            ("M17", "Dark Pulse", 80, 1.0, "Dark", 0, "May flinch opponent", 20),
            ("M18", "Aura Sphere", 90, 1.0, "Fighting", 0, "Never misses, physical attack", 20),
            ("M19", "Dragon Pulse", 85, 1.0, "Dragon", 0, "Dragon attack from distance", 20),
            ("M20", "Surf", 90, 1.0, "Water", 0, "Hits all adjacent Pokemon", 20),
            ("M21", "Hammer Arm", 100, 1.0, "Fighting", 0, "Lowers Speed of user", 20),
            ("M22", "Superpower", 120, 1.0, "Fighting", 0, "Lowers user's Attack and Defense", 20),
            ("M23", "Focus Blast", 120, 0.7, "Fighting", 0, "May lower Special Defense", 20),
            ("M24", "Vacuum Wave", 40, 1.0, "Fighting", 1, "High priority move", 20),
            ("M25", "Quick Attack", 40, 1.0, "Normal", 1, "Strikes first always", 20),
            ("M26", "Mach Punch", 40, 1.0, "Fighting", 1, "Strikes first always", 20),
            ("M27", "Aqua Jet", 60, 1.0, "Water", 1, "Strikes first always", 20),
            ("M28", "Ice Shard", 40, 1.0, "Ice", 1, "Strikes first always", 20),
            ("M29", "Extreme Speed", 80, 1.0, "Normal", 2, "Always goes first with priority", 20),
            ("M30", "Trick Room", 0, 1.0, "Psychic", 0, "Reverses Speed order", 20),
            ("M31", "Reflect", 0, 1.0, "Psychic", 0, "Halves Physical damage taken", 20),
            ("M32", "Light Screen", 0, 1.0, "Psychic", 0, "Halves Special damage taken", 20),
            ("M33", "Stealth Rock", 0, 1.0, "Rock", 0, "Damages Pokemon on switch-in", 20),
            ("M34", "Toxic Spikes", 0, 1.0, "Poison", 0, "Poisons Pokemon on switch-in", 20),
            ("M35", "Spikes", 0, 1.0, "Ground", 0, "Damages Pokemon on switch-in", 20),
            ("M36", "Leech Seed", 0, 0.9, "Grass", 0, "Seeds opponent, drains HP", 20),
            ("M37", "Toxic", 0, 0.9, "Poison", 0, "Badly poisons opponent", 20),
            ("M38", "Thunder Wave", 0, 0.9, "Electric", 0, "Paralyzes opponent", 20),
            ("M39", "Willowisp", 0, 0.85, "Fire", 0, "Burns opponent", 20),
            ("M40", "Recover", 0, 1.0, "Normal", 0, "Heals 50% HP", 20),
            ("M41", "Synthesis", 0, 1.0, "Grass", 0, "Heals 50% HP, more in sun", 20),
            ("M42", "Morning Sun", 0, 1.0, "Normal", 0, "Heals 50% HP, more in sun", 20),
            ("M43", "Curse", 0, 1.0, "Ghost", 0, "Lowers Speed, raises Attack and Defense", 20),
            ("M44", "Dragon Dance", 0, 1.0, "Dragon", 0, "Raises Attack and Speed", 20),
            ("M45", "Bulk Up", 0, 1.0, "Fighting", 0, "Raises Attack and Defense", 20),
            ("M46", "Calm Mind", 0, 1.0, "Psychic", 0, "Raises Special Attack and Defense", 20),
            ("M47", "Swords Dance", 0, 1.0, "Normal", 0, "Doubles Attack", 20),
            ("M48", "Nasty Plot", 0, 1.0, "Dark", 0, "Doubles Special Attack", 20),
            ("M49", "Amnesia", 0, 1.0, "Psychic", 0, "Doubles Special Defense", 20),
            ("M50", "Iron Defense", 0, 1.0, "Steel", 0, "Doubles Defense", 20),
            ("M51", "Protect", 0, 1.0, "Normal", 4, "Blocks all damage this turn", 20),
            ("M52", "Substitute", 0, 1.0, "Normal", 0, "Takes 25% HP to create substitute", 20),
            ("M53", "U-turn", 70, 1.0, "Bug", 0, "Switches out after attacking", 20),
            ("M54", "Volt Switch", 70, 1.0, "Electric", 0, "Switches out after attacking", 20),
            ("M55", "Flip Turn", 60, 1.0, "Water", 0, "Switches out after attacking", 20),
            ("M56", "Dragon Claw", 80, 1.0, "Dragon", 0, "Physical dragon attack", 20),
            ("M57", "Sludge Bomb", 90, 1.0, "Poison", 0, "Special poison attack", 20),
            ("M58", "Giga Drain", 75, 1.0, "Grass", 0, "Heals half damage dealt", 20),
            ("M59", "Sleep Powder", 0, 0.75, "Grass", 0, "Puts opponent to sleep", 20),
            ("M60", "Spore", 0, 1.0, "Grass", 0, "Puts opponent to sleep", 20),
            ("M61", "Scald", 80, 1.0, "Water", 0, "May burn opponent", 20),
            ("M62", "Ice Beam", 90, 1.0, "Ice", 0, "May freeze opponent", 20),
            ("M63", "Frost Breath", 60, 0.9, "Ice", 0, "Always critical hit", 20),
            ("M64", "Icicle Crash", 85, 0.9, "Ice", 0, "May flinch opponent", 20),
            ("M65", "Sheer Cold", 0, 0.3, "Ice", 0, "One-hit KO move", 20),
            ("M66", "Freeze-Dry", 70, 1.0, "Ice", 0, "Super effective on Water", 20),
            ("M67", "Signal Beam", 75, 1.0, "Bug", 0, "May confuse opponent", 20),
            ("M68", "Bug Buzz", 90, 1.0, "Bug", 0, "May lower Special Defense", 20),
            ("M69", "Megahorn", 120, 0.85, "Bug", 0, "Physical bug attack", 20),
            ("M70", "Pollen Powder", 75, 0.75, "Grass", 0, "Poisons opponent", 20),
            ("M71", "Stun Spore", 0, 0.75, "Grass", 0, "Paralyzes opponent", 20),
            ("M72", "Powder Snow", 40, 1.0, "Ice", 0, "May freeze opponent", 20),
            ("M73", "Avalanche", 60, 1.0, "Ice", 0, "Power doubled if hit this turn", 20),
            ("M74", "Aqua Ring", 0, 1.0, "Water", 0, "Heals 1/8 HP each turn", 20),
            ("M75", "Rain Dance", 0, 1.0, "Water", 0, "Summons rain", 20),
            ("M76", "Sunny Day", 0, 1.0, "Fire", 0, "Summons sun", 20),
            ("M77", "Sandstorm", 0, 1.0, "Rock", 0, "Summons sandstorm", 20),
            ("M78", "Hail", 0, 1.0, "Ice", 0, "Summons hail", 20),
            ("M79", "Tailwind", 0, 1.0, "Flying", 0, "Raises Speed of team", 20),
            ("M80", "Trick", 0, 1.0, "Psychic", 0, "Swaps held items", 20),
            ("M81", "Switcheroo", 0, 1.0, "Dark", 0, "Swaps held items", 20),
            ("M82", "Ally Switch", 0, 1.0, "Psychic", 2, "Switches with ally", 20),
            ("M83", "Heal Bell", 0, 1.0, "Normal", 0, "Heals status of team", 20),
            ("M84", "Refresh", 0, 1.0, "Normal", 0, "Heals status of user", 20),
            ("M85", "Defog", 0, 1.0, "Flying", 0, "Removes hazards and boosts", 20),
            ("M86", "Rapid Spin", 50, 1.0, "Normal", 0, "Removes hazards and boosts Speed", 20),
            ("M87", "Dragon Rage", 40, 1.0, "Dragon", 0, "Always deals 40 damage", 20),
            ("M88", "Dragon Darts", 50, 1.0, "Dragon", 0, "Hits twice", 20),
            ("M89", "Outrage", 120, 1.0, "Dragon", 0, "Locks into move, confuses user", 20),
            ("M90", "Draco Meteor", 130, 0.9, "Dragon", 0, "Lowers user's Special Attack", 20),
            ("M91", "Power Whip", 120, 0.85, "Grass", 0, "Physical grass attack", 20),
            ("M92", "Leech Life", 80, 1.0, "Bug", 0, "Drains 50% damage dealt", 20),
            ("M93", "X-Scissor", 80, 1.0, "Bug", 0, "Physical bug attack", 20),
            ("M94", "First Impression", 90, 1.0, "Bug", 2, "Priority bug attack", 20),
            ("M95", "Brave Bird", 120, 1.0, "Flying", 0, "Physical attack with recoil", 20),
            ("M96", "Meteor Mash", 90, 0.9, "Steel", 0, "May raise Attack", 20),
            ("M97", "Iron Tail", 100, 0.75, "Steel", 0, "May lower Defense", 20),
            ("M98", "Flash Cannon", 80, 1.0, "Steel", 0, "May lower Special Defense", 20),
            ("M99", "Power Gem", 80, 1.0, "Rock", 0, "Special rock attack", 20),
            ("M100", "Ancient Power", 60, 1.0, "Rock", 0, "May raise all stats", 20),
            ("M101", "Power Up Punch", 40, 1.0, "Fighting", 0, "Raises Attack after hit", 20),
            ("M102", "Drain Punch", 75, 1.0, "Fighting", 0, "Heals 50% damage dealt", 20),
            ("M103", "Liquid Swirl", 90, 1.0, "Water", 0, "May reduce opponent's Special Defense", 20),
            ("M104", "Aurora Beam", 65, 1.0, "Ice", 0, "May lower Attack", 20),
            ("M105", "Ether", 0, 1.0, "Psychic", 0, "Restores PP to a move", 20),
            ("M106", "Teleport", 0, 1.0, "Psychic", 0, "User escapes battle", 20),
            ("M107", "Horn Leech", 75, 1.0, "Grass", 0, "Drains 50% damage dealt", 20),
            ("M108", "Leaf Storm", 130, 0.9, "Grass", 0, "Lowers user's Special Attack", 20),
            ("M109", "Energy Ball", 90, 1.0, "Grass", 0, "May lower Special Defense", 20),
            ("M110", "Seed Bomb", 80, 1.0, "Grass", 0, "Physical grass attack", 20),
            ("M111", "Solar Beam", 120, 1.0, "Grass", 0, "Charges then attacks", 20),
            ("M112", "Solar Blade", 125, 1.0, "Grass", 0, "Charges then attacks", 20),
            ("M113", "Moonlight", 0, 1.0, "Fairy", 0, "Heals 50% HP, more in sun", 20),
            ("M114", "Starlight", 0, 1.0, "Fairy", 0, "Heals 50% HP, more at night", 20),
            ("M115", "Cosmic Power", 0, 1.0, "Psychic", 0, "Raises Special Attack and Defense", 20),
            ("M116", "Power Spot", 0, 1.0, "Psychic", 0, "Boosts team's Special Attack", 20),
            ("M117", "Follow Me", 0, 1.0, "Normal", 3, "Draws attacks to user", 20),
            ("M118", "Spotlight", 0, 1.0, "Normal", 3, "Draws attacks to target", 20),
            ("M119", "Aromatic Mist", 0, 1.0, "Fairy", 0, "Boosts ally's Special Defense", 20),
            ("M120", "Play Rough", 90, 0.9, "Fairy", 0, "May lower Attack", 20),
            ("M121", "Moonblast", 95, 1.0, "Fairy", 0, "May lower Special Attack", 20),
            ("M122", "Dazzling Gleam", 80, 1.0, "Fairy", 0, "Hits all adjacent Pokemon", 20),
            ("M123", "Knock Off", 65, 1.0, "Dark", 0, "Removes held items", 20),
            ("M124", "Sucker Punch", 70, 1.0, "Dark", 1, "Only works if opponent attacks", 20),
            ("M125", "Pursuit", 40, 1.0, "Dark", 0, "Doubled if opponent switches", 20),
            ("M126", "Shadow Sneak", 40, 1.0, "Ghost", 1, "Priority ghost attack", 20),
            ("M127", "Destiny Bond", 0, 1.0, "Ghost", 0, "Faints both if hit next turn", 20),
            ("M128", "Perish Song", 0, 1.0, "Normal", 0, "All Pokemon faint after 3 turns", 20),
            ("M129", "Explosion", 250, 1.0, "Normal", 0, "User faints", 20),
            ("M130", "Selfdestruct", 200, 1.0, "Normal", 0, "User faints", 20),
            ("M131", "Memento", 0, 1.0, "Dark", 0, "User faints, lowers opponent stats", 20),
            ("M132", "Healing Wish", 0, 1.0, "Psychic", 0, "User faints, heals next Pokemon", 20),
            ("M133", "Lunar Dance", 0, 1.0, "Psychic", 0, "User faints, heals next Pokemon", 20),
            ("M134", "Teleport", 0, 1.0, "Psychic", 0, "User escapes battle", 20),
            ("M135", "Horn Drill", 0, 0.3, "Normal", 0, "One-hit KO move", 20),
            ("M136", "Wood Hammer", 120, 1.0, "Grass", 0, "Physical attack with recoil", 20),
            ("M137", "High Horsepower", 95, 0.95, "Ground", 0, "Physical ground attack", 20),
            ("M138", "Heavy Slam", 80, 1.0, "Steel", 0, "Heavier user does more damage", 20),
            ("M139", "Gunk Shot", 120, 0.8, "Poison", 0, "Physical poison attack", 20),
            ("M140", "Close Combat", 120, 1.0, "Fighting", 0, "Powerful fighting move", 20),
            ("M141", "Crunch", 80, 1.0, "Dark", 0, "May lower Defense", 20),
            ("M142", "Aqua Tail", 90, 0.9, "Water", 0, "Physical water attack", 20),
            ("M143", "Stone Edge", 100, 0.8, "Rock", 0, "Physical rock attack", 20),
            ("M144", "Earthquake", 100, 1.0, "Ground", 0, "Physical ground attack", 20),
            ("M145", "Dive", 80, 1.0, "Water", 0, "Dives and attacks next turn", 20),
            ("M146", "Aerial Ace", 60, 1.0, "Flying", 0, "Always hits", 20),
            ("M147", "Wing Attack", 60, 1.0, "Flying", 0, "Basic flying attack", 20),
            ("M148", "Peck", 35, 1.0, "Flying", 0, "Basic peck attack", 20),
            ("M149", "Night Slash", 70, 1.0, "Dark", 0, "High critical hit ratio", 20),
            ("M150", "Cross Poison", 70, 1.0, "Poison", 0, "May poison opponent", 20),
        ]
        
        for move_data in moves_data:
            move = MoveList(
                id=move_data[0], name=move_data[1], power=move_data[2],
                accuracy=move_data[3], type=move_data[4], priority=move_data[5],
                description=move_data[6], power_points=move_data[7]
            )
            db.session.add(move)
        
        db.session.commit()
        print(f"✓ Added {len(moves_data)} moves")

        # ===== POKEMON SPECIES (50 FINAL EVOLUTIONS + VARIANTS) =====
        pokemon_data = [
            # Base forms
            ("3", "Venusaur", None, 80, 82, 83, 100, 100, 80, "Grass", "Poison", True),
            ("6", "Charizard", None, 78, 84, 78, 109, 85, 100, "Fire", "Flying", True),
            ("9", "Blastoise", None, 79, 83, 100, 83, 83, 78, "Water", None, True),
            ("26", "Raichu", None, 60, 90, 55, 90, 80, 110, "Electric", None, True),
            ("59", "Arcanine", None, 90, 110, 80, 100, 80, 95, "Fire", None, True),
            ("208", "Steelix", None, 75, 85, 200, 55, 65, 30, "Steel", "Ground", True),
            ("149", "Dragonite", None, 91, 134, 95, 100, 100, 80, "Dragon", "Flying", True),
            ("134", "Vaporeon", None, 130, 65, 60, 110, 95, 65, "Water", None, True),
            ("135", "Jolteon", None, 65, 65, 60, 110, 95, 130, "Electric", None, True),
            ("136", "Flareon", None, 65, 130, 60, 95, 110, 65, "Fire", None, True),
            ("196", "Espeon", None, 65, 65, 60, 130, 95, 110, "Psychic", None, True),
            ("197", "Umbreon", None, 95, 65, 110, 60, 130, 65, "Dark", None, True),
            ("144", "Articuno", None, 90, 85, 100, 95, 125, 85, "Ice", "Flying", True),
            ("145", "Zapdos", None, 90, 100, 90, 125, 90, 100, "Electric", "Flying", True),
            ("146", "Moltres", None, 90, 100, 90, 125, 85, 90, "Fire", "Flying", True),
            ("150", "Mewtwo", None, 106, 110, 90, 154, 90, 130, "Psychic", None, True),
            ("248", "Tyranitar", None, 100, 134, 110, 95, 100, 61, "Rock", "Dark", True),
            ("249", "Lugia", None, 106, 90, 130, 90, 154, 110, "Psychic", "Flying", True),
            ("250", "Ho-Oh", None, 106, 130, 90, 110, 154, 90, "Fire", "Flying", True),
            ("384", "Rayquaza", None, 105, 150, 90, 150, 90, 95, "Dragon", "Flying", True),
            ("445", "Garchomp", None, 108, 130, 95, 80, 85, 102, "Dragon", "Ground", True),
            ("483", "Dialga", None, 100, 120, 120, 150, 100, 90, "Steel", "Dragon", True),
            ("484", "Palkia", None, 100, 120, 100, 150, 120, 100, "Water", "Dragon", True),
            ("485", "Heatran", None, 91, 90, 106, 130, 106, 77, "Fire", "Steel", True),
            ("487", "Giratina", None, 150, 100, 120, 100, 120, 90, "Ghost", "Dragon", True),
            ("488", "Cresselia", None, 120, 70, 120, 80, 130, 60, "Psychic", None, True),
            ("643", "Reshiram", None, 100, 120, 100, 150, 120, 90, "Dragon", "Fire", True),
            ("644", "Zekrom", None, 100, 150, 120, 120, 100, 90, "Dragon", "Electric", True),
            ("645", "Tornadus", None, 101, 122, 90, 121, 80, 111, "Flying", None, True),
            ("647", "Keldeo", None, 91, 72, 90, 108, 90, 101, "Water", "Fighting", True),
            ("681", "Aegislash", None, 60, 50, 140, 50, 140, 60, "Steel", "Ghost", True),
            ("689", "Trevenant", None, 61, 90, 76, 65, 82, 56, "Ghost", "Grass", True),
            ("703", "Carbink", None, 50, 50, 132, 50, 132, 50, "Rock", "Fairy", True),
            ("718", "Zygarde", None, 108, 121, 95, 91, 95, 99, "Dragon", "Ground", True),
            ("735", "Gumshoos", None, 72, 107, 60, 55, 60, 45, "Normal", None, True),
            ("776", "Turtonator", None, 60, 84, 135, 74, 80, 36, "Fire", "Dragon", True),
            ("784", "Kommo-o", None, 75, 110, 125, 100, 105, 85, "Dragon", "Fighting", True),
            ("785", "Tapu Koko", None, 70, 115, 85, 130, 95, 130, "Electric", "Fairy", True),
            ("786", "Tapu Lele", None, 70, 85, 95, 130, 115, 95, "Psychic", "Fairy", True),
            ("787", "Tapu Bulu", None, 70, 130, 115, 85, 95, 75, "Grass", "Fairy", True),
            ("788", "Tapu Fini", None, 70, 75, 115, 100, 130, 75, "Water", "Fairy", True),
            ("800", "Necrozma", None, 73, 107, 89, 137, 71, 129, "Psychic", None, True),
            ("812", "Urshifu", None, 119, 130, 100, 63, 60, 97, "Fighting", None, True),
            ("816", "Sobble", None, 50, 40, 40, 70, 50, 70, "Water", None, True),
            ("823", "Corviknight", None, 98, 87, 105, 53, 85, 67, "Flying", "Steel", True),
            ("834", "Drednaw", None, 100, 134, 100, 55, 68, 48, "Water", "Rock", True),
            ("858", "Hatterene", None, 57, 60, 95, 136, 103, 72, "Psychic", "Fairy", True),
            ("879", "Cptain", None, 80, 90, 100, 70, 90, 75, "Psychic", None, True),
            ("887", "Dragapult", None, 88, 120, 75, 100, 75, 142, "Dragon", "Ghost", True),
            ("898", "Calyrex", None, 80, 85, 95, 85, 95, 80, "Psychic", "Grass", True),
            ("905", "Enamorus", None, 74, 115, 70, 135, 80, 115, "Flying", "Fairy", True),
            
            # Mega Evolutions (not base forms)
            ("3M", "Venusaur", "Mega", 80, 100, 123, 122, 120, 80, "Grass", "Poison", False),
            ("6X", "Charizard", "Mega X", 78, 130, 111, 130, 85, 100, "Fire", "Dragon", False),
            ("6Y", "Charizard", "Mega Y", 78, 104, 78, 159, 115, 100, "Fire", "Flying", False),
            ("9M", "Blastoise", "Mega", 79, 103, 120, 135, 115, 78, "Water", None, False),
            ("248M", "Tyranitar", "Mega", 100, 164, 150, 95, 120, 71, "Rock", "Dark", False),
            ("445M", "Garchomp", "Mega", 108, 170, 115, 120, 95, 92, "Dragon", "Ground", False),
            
            # Regional Forms (considered base forms)
            ("26A", "Raichu", "Alolan", 60, 85, 50, 95, 85, 110, "Electric", "Psychic", True),
            
            # Transformations (not base forms)
            ("964", "Palafin", "Zero Form", 100, 70, 72, 53, 62, 100, "Water", None, True),
            ("964H", "Palafin", "Hero Form", 100, 160, 97, 106, 87, 100, "Water", None, False),
        ]
        
        for poke_id, name, variant, hp, att, defense, sp_att, sp_def, speed, type1, type2, is_base in pokemon_data:
            pokemon = PokemonSpecies(
                id=poke_id, name=name, variant=variant, hp=hp, attack=att,
                defense=defense, special_attack=sp_att, special_defense=sp_def,
                speed=speed, type_1=type1, type_2=type2, is_base_form=is_base
            )
            db.session.add(pokemon)
        
        db.session.commit()
        print(f"✓ Added {len(pokemon_data)} Pokemon species (all final evolutions)")

        # ===== POKEMON_ABILITY LINKS =====
        pokemon_ability_links = [
            ("3", "A1"), ("3", "A29"), 
            ("6", "A2"), ("6", "A7"),
            ("9", "A3"), ("9", "A6"),
            ("26", "A5"), ("26", "A11"),
            ("59", "A7"), ("59", "A40"),
            ("208", "A19"), ("208", "A38"),
            ("149", "A9"), ("149", "A39"),
            ("134", "A15"), ("134", "A35"),
            ("135", "A18"), ("135", "A42"),
            ("136", "A17"), ("136", "A40"),
            ("196", "A29"), ("196", "A13"),
            ("197", "A23"), ("197", "A13"),
            ("144", "A51"), ("144", "A12"),
            ("145", "A51"), ("145", "A42"),
            ("146", "A51"), ("146", "A40"),
            ("150", "A25"), ("150", "A29"),
            ("248", "A7"), ("248", "A48"),
            ("249", "A51"), ("249", "A39"),
            ("250", "A51"), ("250", "A40"),
            ("384", "A9"), ("384", "A39"),
            ("445", "A56"), ("445", "A57"),
            ("483", "A22"), ("483", "A38"),
            ("484", "A22"), ("484", "A39"),
            ("485", "A17"), ("485", "A40"),
            ("487", "A25"), ("487", "A29"),
            ("488", "A30"), ("488", "A39"),
            ("643", "A40"), ("643", "A39"),
            ("644", "A42"),
            ("645", "A48"), ("645", "A49"),
            ("647", "A9"), ("647", "A39"),
            ("681", "A56"), ("681", "A57"),
            ("689", "A23"), ("689", "A29"),
            ("703", "A22"), ("703", "A38"),
            ("718", "A9"), ("718", "A39"),
            ("735", "A41"), ("735", "A44"),
            ("776", "A2"), ("776", "A40"),
            ("784", "A51"), ("784", "A39"),
            ("785", "A42"), ("785", "A48"),
            ("786", "A25"), ("786", "A29"),
            ("787", "A26"), ("787", "A27"),
            ("788", "A15"), ("788", "A35"),
            ("800", "A56"), ("800", "A29"),
            ("812", "A56"), ("812", "A57"),
            ("816", "A3"), ("816", "A6"),
            ("823", "A42"), ("823", "A19"),
            ("834", "A7"), ("834", "A44"),
            ("858", "A25"), ("858", "A29"),
            ("879", "A29"), ("879", "A55"),
            ("887", "A9"), ("887", "A39"),
            ("898", "A29"), ("898", "A25"),
            ("905", "A48"), ("905", "A49"),
            # Mega Evolutions
            ("3M", "A1"), ("3M", "A29"),
            ("6X", "A2"), ("6X", "A58"),
            ("6Y", "A58"),
            ("9M", "A3"), ("9M", "A58"),
            ("248M", "A7"), ("248M", "A58"),
            ("445M", "A56"), ("445M", "A58"),
            # Regional Forms
            ("26A", "A29"), ("26A", "A13"),
            # Transformations
            ("964", "A58"),
            ("964H", "A58"),
        ]
        
        for species_id, ability_id in pokemon_ability_links:
            link = Pokemon_Ability(species_id=species_id, ability_id=ability_id)
            db.session.add(link)
        
        db.session.commit()
        print(f"✓ Added {len(pokemon_ability_links)} Pokemon-Ability links")

        # ===== POKEMON_MOVE LINKS (base forms only) =====
        pokemon_move_links = [
            ("3", "M4"), ("3", "M58"), ("3", "M44"), ("3", "M111"),
            ("6", "M2"), ("6", "M7"), ("6", "M56"), ("6", "M89"),
            ("9", "M3"), ("9", "M20"), ("9", "M62"), ("9", "M14"),
            ("26", "M5"), ("26", "M25"), ("26", "M38"), ("26", "M75"),
            ("59", "M2"), ("59", "M7"), ("59", "M96"), ("59", "M25"),
            ("208", "M144"), ("208", "M138"), ("208", "M143"), ("208", "M13"),
            ("149", "M89"), ("149", "M43"), ("149", "M44"), ("149", "M19"),
            ("134", "M3"), ("134", "M20"), ("134", "M55"), ("134", "M8"),
            ("135", "M5"), ("135", "M75"), ("135", "M27"), ("135", "M38"),
            ("136", "M2"), ("136", "M7"), ("136", "M39"), ("136", "M25"),
            ("196", "M15"), ("196", "M46"), ("196", "M26"), ("196", "M47"),
            ("197", "M144"), ("197", "M123"), ("197", "M141"), ("197", "M43"),
            ("150", "M15"), ("150", "M19"), ("150", "M43"), ("150", "M26"),
            ("248", "M144"), ("248", "M57"), ("248", "M143"), ("248", "M43"),
            ("249", "M20"), ("249", "M15"), ("249", "M90"), ("249", "M43"),
            ("250", "M7"), ("250", "M20"), ("250", "M90"), ("250", "M43"),
            ("384", "M89"), ("384", "M19"), ("384", "M90"), ("384", "M44"),
            ("445", "M144"), ("445", "M89"), ("445", "M44"), ("445", "M45"),
            ("483", "M144"), ("483", "M90"), ("483", "M43"), ("483", "M13"),
            ("484", "M20"), ("484", "M90"), ("484", "M43"), ("484", "M19"),
            ("485", "M7"), ("485", "M144"), ("485", "M13"), ("485", "M96"),
            ("487", "M17"), ("487", "M43"), ("487", "M19"), ("487", "M26"),
            ("488", "M46"), ("488", "M49"), ("488", "M41"), ("488", "M30"),
            ("643", "M89"), ("643", "M19"), ("643", "M7"), ("643", "M44"),
            ("644", "M89"), ("644", "M19"), ("644", "M5"), ("644", "M44"),
            ("645", "M95"), ("645", "M44"), ("645", "M26"), ("645", "M53"),
            ("647", "M18"), ("647", "M20"), ("647", "M44"), ("647", "M11"),
            ("681", "M13"), ("681", "M43"), ("681", "M143"), ("681", "M26"),
            ("689", "M17"), ("689", "M43"), ("689", "M58"), ("689", "M29"),
            ("703", "M143"), ("703", "M120"), ("703", "M43"), ("703", "M46"),
            ("718", "M89"), ("718", "M90"), ("718", "M144"), ("718", "M44"),
            ("735", "M141"), ("735", "M101"), ("735", "M86"), ("735", "M123"),
            ("776", "M7"), ("776", "M19"), ("776", "M96"), ("776", "M26"),
            ("784", "M11"), ("784", "M89"), ("784", "M19"), ("784", "M44"),
            ("785", "M5"), ("785", "M120"), ("785", "M26"), ("785", "M47"),
            ("786", "M15"), ("786", "M120"), ("786", "M26"), ("786", "M46"),
            ("787", "M91"), ("787", "M58"), ("787", "M44"), ("787", "M45"),
            ("788", "M20"), ("788", "M120"), ("788", "M26"), ("788", "M46"),
            ("800", "M15"), ("800", "M19"), ("800", "M43"), ("800", "M26"),
            ("812", "M11"), ("812", "M21"), ("812", "M26"), ("812", "M45"),
            ("816", "M3"), ("816", "M20"), ("816", "M62"), ("816", "M14"),
            ("823", "M95"), ("823", "M144"), ("823", "M143"), ("823", "M25"),
            ("834", "M14"), ("834", "M143"), ("834", "M20"), ("834", "M97"),
            ("858", "M15"), ("858", "M120"), ("858", "M26"), ("858", "M46"),
            ("879", "M15"), ("879", "M19"), ("879", "M43"), ("879", "M26"),
            ("887", "M89"), ("887", "M90"), ("887", "M19"), ("887", "M44"),
            ("898", "M15"), ("898", "M44"), ("898", "M41"), ("898", "M26"),
            ("905", "M95"), ("905", "M44"), ("905", "M26"), ("905", "M120"),
            # Mega Evolutions
            ("3M", "M4"), ("3M", "M58"), ("3M", "M44"), ("3M", "M111"),
            ("6X", "M2"), ("6X", "M56"), ("6X", "M89"), ("6X", "M44"),
            ("6Y", "M2"), ("6Y", "M7"), ("6Y", "M89"), ("6Y", "M44"),
            ("9M", "M3"), ("9M", "M20"), ("9M", "M62"), ("9M", "M14"),
            ("248M", "M144"), ("248M", "M57"), ("248M", "M143"), ("248M", "M43"),
            ("445M", "M144"), ("445M", "M89"), ("445M", "M44"), ("445M", "M45"),
            # Regional Forms
            ("26A", "M5"), ("26A", "M25"), ("26A", "M38"), ("26A", "M75"),
            # Transformations
            ("964", "M3"), ("964", "M20"), ("964", "M55"), ("964", "M8"),
            ("964H", "M3"), ("964H", "M20"), ("964H", "M55"), ("964H", "M8"),
        ]
        
        for species_id, move_id in pokemon_move_links:
            link = Pokemon_Move(species_id=species_id, move_id=move_id)
            db.session.add(link)
        
        db.session.commit()
        print(f"✓ Added {len(pokemon_move_links)} Pokemon-Move links")

        # ===== HELD ITEMS =====
        items_data = [
            ("I1", "Life Orb", "Increases move power by 30%, user takes recoil damage"),
            ("I2", "Choice Scarf", "Increases Speed by 50%, user locked into first move"),
            ("I3", "Choice Band", "Increases Attack by 50%, user locked into first move"),
            ("I4", "Choice Specs", "Increases Special Attack by 50%, user locked into first move"),
            ("I5", "Assault Vest", "Increases Special Defense by 50%, user cannot use status moves"),
            ("I6", "Weakness Policy", "Doubles Attack and Special Attack when hit by super effective move"),
            ("I7", "Focus Sash", "Survives with 1 HP if hit when at full health"),
            ("I8", "Rocky Helmet", "Damages Pokemon that make contact"),
            ("I9", "Rough Skin", "Damages Pokemon that make contact"),
            ("I10", "Leftovers", "Heals 12.5% HP at the end of each turn"),
            ("I11", "Air Balloon", "Negates Ground-type moves, popped on contact"),
            ("I12", "Eviolite", "Increases Defense and Special Defense of not fully evolved Pokemon"),
            ("I13", "Flame Orb", "Burns the holder, used strategically with abilities"),
            ("I14", "Toxic Orb", "Badly poisons the holder, used with abilities"),
            ("I15", "Figy Berry", "Heals when HP is low, may confuse"),
            ("I16", "Occa Berry", "Resists Fire-type damage"),
            ("I17", "Passho Berry", "Resists Water-type damage"),
            ("I18", "Rindo Berry", "Resists Electric-type damage"),
            ("I19", "Yache Berry", "Resists Ice-type damage"),
            ("I20", "Charti Berry", "Resists Rock-type damage"),
            ("I21", "Venusaurite", "Mega Stone for Venusaur"),
            ("I22", "Charizardite X", "Mega Stone for Charizard X"),
            ("I23", "Charizardite Y", "Mega Stone for Charizard Y"),
            ("I24", "Blastoisinite", "Mega Stone for Blastoise"),
            ("I25", "Tyranitarite", "Mega Stone for Tyranitar"),
            ("I26", "Garchompite", "Mega Stone for Garchomp"),
        ]
        
        for item_id, name, desc in items_data:
            item = HeldItem(id=item_id, name=name, description=desc)
            db.session.add(item)
        
        db.session.commit()
        print(f"✓ Added {len(items_data)} held items")

        # ===== TRAINERS (Realistic user names) =====
        trainers_data = [
            ("T1", "jacob_stream", 5000, 250),
            ("T2", "sarah_p92", 3000, 150),
            ("T3", "mike_gaming", 3500, 175),
            ("T4", "emma_collector", 3200, 160),
            ("T5", "alex_pro", 4500, 225),
            ("T6", "jordan_battles", 4600, 230),
            ("T7", "casey_competitive", 4400, 220),
            ("T8", "taylor_master", 5000, 250),
            ("T9", "chris_player", 2500, 125),
            ("T10", "morgan_trainer", 2700, 135),
            ("T11", "riley_fan", 3000, 150),
            ("T12", "sam_elite", 4800, 240),
        ]
        
        for trainer_id, name, vp, bt in trainers_data:
            trainer = Trainer(id=trainer_id, name=name, victory_points=vp, battle_tickets=bt)
            db.session.add(trainer)
        
        db.session.commit()
        print(f"✓ Added {len(trainers_data)} trainers")

        # ===== TRAINER_HELDITEM LINKS =====
        trainer_item_links = [
            ("T1", "I1", date.today() - timedelta(days=30)),
            ("T1", "I2", date.today() - timedelta(days=25)),
            ("T1", "I10", date.today() - timedelta(days=20)),
            ("T2", "I3", date.today() - timedelta(days=28)),
            ("T2", "I10", date.today() - timedelta(days=15)),
            ("T3", "I4", date.today() - timedelta(days=32)),
            ("T3", "I5", date.today() - timedelta(days=18)),
            ("T4", "I2", date.today() - timedelta(days=22)),
            ("T4", "I7", date.today() - timedelta(days=10)),
            ("T5", "I1", date.today() - timedelta(days=40)),
            ("T5", "I10", date.today() - timedelta(days=35)),
            ("T6", "I3", date.today() - timedelta(days=38)),
            ("T6", "I8", date.today() - timedelta(days=12)),
            ("T7", "I4", date.today() - timedelta(days=35)),
            ("T7", "I11", date.today() - timedelta(days=8)),
            ("T8", "I1", date.today() - timedelta(days=45)),
            ("T8", "I10", date.today() - timedelta(days=40)),
            ("T9", "I2", date.today() - timedelta(days=20)),
            ("T9", "I7", date.today() - timedelta(days=5)),
            ("T10", "I3", date.today() - timedelta(days=18)),
            ("T10", "I10", date.today() - timedelta(days=10)),
            ("T11", "I1", date.today() - timedelta(days=15)),
            ("T11", "I4", date.today() - timedelta(days=9)),
            ("T12", "I1", date.today() - timedelta(days=50)),
            ("T12", "I10", date.today() - timedelta(days=45)),
        ]
        
        for trainer_id, item_id, obtain_date in trainer_item_links:
            link = Trainer_HeldItem(trainer_id=trainer_id, item_id=item_id, obtain_date=obtain_date)
            db.session.add(link)
        
        db.session.commit()
        print(f"✓ Added {len(trainer_item_links)} Trainer-HeldItem links")

        # ===== POKEMON INSTANCES (2 for EVERY pokemon species) =====
        natures = ["Adamant", "Modest", "Timid", "Jolly", "Calm", "Bold", "Careful", "Quiet"]
        
        pokemon_instances_data = [
            # Venusaur - 2 instances
            ("PI1", "3", "T1", 11, 11, 11, 11, 11, 11, "Calm", "A1", "M4", "M58", "M44", "M111"),
            ("PI2", "3", "T2", 22, 0, 11, 11, 22, 0, "Modest", "A29", "M58", "M44", "M111", "M59"),
            
            # Charizard
            ("PI3", "6", "T3", 0, 22, 11, 0, 11, 22, "Jolly", "A2", "M2", "M7", "M96", "M89"),
            ("PI4", "6", "T4", 11, 11, 0, 22, 11, 11, "Timid", "A7", "M7", "M96", "M89", "M26"),
            
            # Blastoise
            ("PI5", "9", "T5", 11, 0, 22, 11, 11, 11, "Calm", "A3", "M3", "M20", "M62", "M14"),
            ("PI6", "9", "T6", 22, 11, 11, 0, 11, 11, "Modest", "A6", "M20", "M62", "M14", "M39"),
            
            # Raichu
            ("PI7", "26", "T7", 0, 11, 11, 11, 22, 11, "Timid", "A5", "M5", "M25", "M38", "M75"),
            ("PI8", "26", "T8", 11, 22, 0, 11, 11, 11, "Jolly", "A11", "M25", "M38", "M75", "M53"),
            
            # Arcanine
            ("PI9", "59", "T9", 0, 22, 11, 11, 11, 11, "Adamant", "A7", "M2", "M7", "M96", "M25"),
            ("PI10", "59", "T10", 11, 11, 22, 0, 11, 11, "Modest", "A40", "M7", "M96", "M25", "M26"),
            
            # Steelix
            ("PI11", "208", "T11", 11, 11, 22, 0, 11, 11, "Careful", "A19", "M144", "M138", "M143", "M13"),
            ("PI12", "208", "T12", 0, 22, 11, 11, 11, 11, "Adamant", "A38", "M138", "M143", "M13", "M96"),
            
            # Dragonite
            ("PI13", "149", "T1", 11, 22, 11, 0, 11, 11, "Adamant", "A9", "M89", "M43", "M44", "M19"),
            ("PI14", "149", "T2", 11, 11, 0, 11, 22, 11, "Modest", "A39", "M19", "M44", "M89", "M26"),
            
            # Vaporeon
            ("PI15", "134", "T3", 22, 0, 11, 11, 11, 11, "Calm", "A15", "M3", "M20", "M55", "M62"),
            ("PI16", "134", "T4", 11, 11, 11, 22, 0, 11, "Bold", "A35", "M20", "M55", "M62", "M39"),
            
            # Jolteon
            ("PI17", "135", "T5", 0, 11, 11, 11, 11, 22, "Timid", "A5", "M5", "M75", "M27", "M38"),
            ("PI18", "135", "T6", 11, 11, 22, 11, 0, 11, "Jolly", "A11", "M75", "M27", "M38", "M53"),
            
            # Flareon
            ("PI19", "136", "T7", 0, 22, 11, 11, 11, 11, "Adamant", "A2", "M2", "M7", "M39", "M25"),
            ("PI20", "136", "T8", 11, 11, 0, 22, 11, 11, "Modest", "A40", "M7", "M39", "M25", "M26"),
            
            # Espeon
            ("PI21", "196", "T9", 11, 0, 11, 22, 11, 11, "Modest", "A29", "M15", "M46", "M26", "M47"),
            ("PI22", "196", "T10", 11, 11, 22, 11, 0, 11, "Bold", "A13", "M46", "M26", "M47", "M39"),
            
            # Umbreon
            ("PI23", "197", "T11", 11, 11, 22, 0, 11, 11, "Careful", "A23", "M144", "M123", "M141", "M43"),
            ("PI24", "197", "T12", 0, 11, 11, 11, 22, 11, "Calm", "A13", "M123", "M141", "M43", "M26"),
            
            # Articuno
            ("PI25", "144", "T1", 11, 11, 11, 11, 22, 0, "Calm", "A51", "M8", "M62", "M95", "M47"),
            ("PI26", "144", "T2", 0, 11, 22, 11, 11, 11, "Bold", "A12", "M62", "M95", "M47", "M39"),
            
            # Zapdos
            ("PI27", "145", "T3", 11, 0, 11, 22, 11, 11, "Modest", "A51", "M5", "M75", "M26", "M47"),
            ("PI28", "145", "T4", 11, 11, 0, 11, 22, 11, "Timid", "A42", "M75", "M26", "M47", "M39"),
            
            # Moltres
            ("PI29", "146", "T5", 11, 22, 11, 0, 11, 11, "Adamant", "A51", "M7", "M76", "M26", "M47"),
            ("PI30", "146", "T6", 0, 11, 11, 11, 22, 11, "Modest", "A40", "M76", "M26", "M47", "M39"),
            
            # Mewtwo
            ("PI31", "150", "T7", 11, 0, 11, 22, 11, 11, "Modest", "A25", "M15", "M19", "M43", "M26"),
            ("PI32", "150", "T8", 11, 11, 0, 11, 22, 11, "Timid", "A29", "M19", "M43", "M26", "M39"),
            
            # Tyranitar
            ("PI33", "248", "T9", 11, 22, 11, 0, 11, 11, "Adamant", "A7", "M144", "M57", "M143", "M43"),
            ("PI34", "248", "T10", 0, 11, 11, 22, 11, 11, "Modest", "A48", "M57", "M143", "M43", "M39"),
            
            # Lugia
            ("PI35", "249", "T11", 11, 0, 22, 11, 11, 11, "Calm", "A51", "M20", "M15", "M90", "M43"),
            ("PI36", "249", "T12", 11, 11, 11, 22, 0, 11, "Bold", "A39", "M15", "M90", "M43", "M39"),
            
            # Ho-Oh
            ("PI37", "250", "T1", 11, 22, 11, 0, 11, 11, "Adamant", "A51", "M7", "M20", "M90", "M43"),
            ("PI38", "250", "T2", 0, 11, 11, 22, 11, 11, "Modest", "A40", "M20", "M90", "M43", "M39"),
            
            # Rayquaza
            ("PI39", "384", "T3", 11, 22, 0, 11, 11, 11, "Jolly", "A9", "M89", "M19", "M90", "M44"),
            ("PI40", "384", "T4", 11, 11, 11, 22, 0, 11, "Modest", "A39", "M19", "M90", "M44", "M39"),
            
            # Garchomp
            ("PI41", "445", "T5", 11, 22, 11, 0, 11, 11, "Adamant", "A56", "M144", "M89", "M44", "M45"),
            ("PI42", "445", "T6", 0, 11, 11, 22, 11, 11, "Modest", "A57", "M89", "M44", "M45", "M39"),
            
            # Dialga
            ("PI43", "483", "T7", 11, 11, 22, 11, 0, 11, "Calm", "A22", "M144", "M90", "M43", "M13"),
            ("PI44", "483", "T8", 11, 22, 11, 0, 11, 11, "Adamant", "A38", "M90", "M43", "M13", "M96"),
            
            # Palkia
            ("PI45", "484", "T9", 11, 0, 11, 22, 11, 11, "Modest", "A22", "M20", "M90", "M43", "M19"),
            ("PI46", "484", "T10", 11, 11, 0, 11, 22, 11, "Timid", "A39", "M90", "M43", "M19", "M39"),
            
            # Heatran
            ("PI47", "485", "T11", 11, 11, 22, 11, 0, 11, "Calm", "A17", "M7", "M144", "M13", "M96"),
            ("PI48", "485", "T12", 0, 11, 11, 22, 11, 11, "Modest", "A40", "M144", "M13", "M96", "M39"),
            
            # Giratina
            ("PI49", "487", "T1", 11, 11, 11, 0, 22, 11, "Careful", "A25", "M17", "M43", "M19", "M26"),
            ("PI50", "487", "T2", 0, 11, 22, 11, 11, 11, "Bold", "A29", "M43", "M19", "M26", "M39"),
            
            # Cresselia
            ("PI51", "488", "T3", 11, 0, 11, 11, 22, 11, "Calm", "A30", "M46", "M49", "M41", "M30"),
            ("PI52", "488", "T4", 11, 11, 22, 11, 0, 11, "Bold", "A39", "M49", "M41", "M30", "M39"),
            
            # Reshiram
            ("PI53", "643", "T5", 11, 11, 0, 22, 11, 11, "Modest", "A40", "M89", "M19", "M7", "M44"),
            ("PI54", "643", "T6", 0, 22, 11, 11, 11, 11, "Adamant", "A39", "M19", "M7", "M44", "M45"),
            
            # Zekrom
            ("PI55", "644", "T7", 11, 22, 11, 0, 11, 11, "Adamant", "A42", "M89", "M19", "M5", "M44"),
            ("PI56", "644", "T8", 11, 11, 0, 22, 11, 11, "Modest", "A42", "M19", "M5", "M44", "M39"),
            
            # Tornadus
            ("PI57", "645", "T9", 0, 11, 11, 11, 11, 22, "Jolly", "A48", "M95", "M44", "M26", "M53"),
            ("PI58", "645", "T10", 11, 11, 22, 11, 0, 11, "Bold", "A49", "M44", "M26", "M53", "M39"),
            
            # Keldeo
            ("PI59", "647", "T11", 11, 11, 11, 22, 0, 11, "Modest", "A9", "M18", "M20", "M44", "M11"),
            ("PI60", "647", "T12", 0, 11, 22, 11, 11, 11, "Adamant", "A39", "M20", "M44", "M11", "M45"),
            
            # Aegislash
            ("PI61", "681", "T1", 11, 0, 22, 11, 11, 11, "Calm", "A56", "M13", "M43", "M143", "M26"),
            ("PI62", "681", "T2", 11, 11, 11, 0, 22, 11, "Quiet", "A57", "M43", "M143", "M26", "M39"),
            
            # Trevenant
            ("PI63", "689", "T3", 11, 22, 11, 0, 11, 11, "Adamant", "A23", "M17", "M43", "M58", "M29"),
            ("PI64", "689", "T4", 0, 11, 11, 22, 11, 11, "Modest", "A29", "M43", "M58", "M29", "M39"),
            
            # Carbink
            ("PI65", "703", "T5", 11, 11, 22, 0, 11, 11, "Calm", "A22", "M143", "M120", "M43", "M46"),
            ("PI66", "703", "T6", 0, 11, 11, 11, 22, 11, "Quiet", "A38", "M120", "M43", "M46", "M39"),
            
            # Zygarde
            ("PI67", "718", "T7", 11, 22, 11, 0, 11, 11, "Adamant", "A9", "M89", "M90", "M144", "M44"),
            ("PI68", "718", "T8", 11, 11, 0, 22, 11, 11, "Modest", "A39", "M90", "M144", "M44", "M39"),
            
            # Gumshoos
            ("PI69", "735", "T9", 0, 22, 11, 11, 11, 11, "Adamant", "A41", "M141", "M101", "M86", "M123"),
            ("PI70", "735", "T10", 11, 11, 22, 0, 11, 11, "Modest", "A44", "M101", "M86", "M123", "M39"),
            
            # Turtonator
            ("PI71", "776", "T11", 11, 11, 0, 22, 11, 11, "Modest", "A2", "M7", "M19", "M96", "M26"),
            ("PI72", "776", "T12", 11, 22, 11, 0, 11, 11, "Adamant", "A40", "M19", "M96", "M26", "M45"),
            
            # Kommo-o
            ("PI73", "784", "T1", 11, 22, 11, 0, 11, 11, "Adamant", "A51", "M11", "M89", "M19", "M44"),
            ("PI74", "784", "T2", 0, 11, 11, 22, 11, 11, "Modest", "A39", "M89", "M19", "M44", "M39"),
            
            # Tapu Koko
            ("PI75", "785", "T3", 0, 11, 11, 11, 11, 22, "Timid", "A42", "M5", "M120", "M26", "M47"),
            ("PI76", "785", "T4", 11, 22, 11, 0, 11, 11, "Jolly", "A48", "M120", "M26", "M47", "M45"),
            
            # Tapu Lele
            ("PI77", "786", "T5", 11, 0, 11, 22, 11, 11, "Modest", "A25", "M15", "M120", "M26", "M46"),
            ("PI78", "786", "T6", 11, 11, 0, 11, 22, 11, "Timid", "A29", "M120", "M26", "M46", "M39"),
            
            # Tapu Bulu
            ("PI79", "787", "T7", 11, 22, 11, 0, 11, 11, "Adamant", "A26", "M91", "M58", "M44", "M45"),
            ("PI80", "787", "T8", 0, 11, 11, 22, 11, 11, "Modest", "A27", "M58", "M44", "M45", "M39"),
            
            # Tapu Fini
            ("PI81", "788", "T9", 11, 0, 11, 11, 22, 11, "Calm", "A15", "M20", "M120", "M26", "M46"),
            ("PI82", "788", "T10", 11, 11, 22, 11, 0, 11, "Bold", "A35", "M120", "M26", "M46", "M39"),
            
            # Necrozma
            ("PI83", "800", "T11", 11, 11, 0, 22, 11, 11, "Modest", "A56", "M15", "M19", "M43", "M26"),
            ("PI84", "800", "T12", 0, 11, 22, 11, 11, 11, "Timid", "A29", "M19", "M43", "M26", "M39"),
            
            # Urshifu
            ("PI85", "812", "T1", 11, 22, 11, 0, 11, 11, "Adamant", "A56", "M11", "M21", "M26", "M45"),
            ("PI86", "812", "T2", 0, 11, 11, 22, 11, 11, "Modest", "A57", "M21", "M26", "M45", "M39"),
            
            # Sobble
            ("PI87", "816", "T3", 11, 0, 11, 11, 22, 11, "Modest", "A3", "M3", "M20", "M62", "M14"),
            ("PI88", "816", "T4", 11, 11, 0, 11, 22, 11, "Timid", "A6", "M20", "M62", "M14", "M39"),
            
            # Corviknight
            ("PI89", "823", "T5", 0, 11, 22, 11, 11, 11, "Bold", "A42", "M95", "M144", "M143", "M25"),
            ("PI90", "823", "T6", 11, 11, 11, 0, 22, 11, "Quiet", "A19", "M144", "M143", "M25", "M39"),
            
            # Drednaw
            ("PI91", "834", "T7", 11, 22, 11, 0, 11, 11, "Adamant", "A7", "M14", "M143", "M20", "M97"),
            ("PI92", "834", "T8", 0, 11, 11, 22, 11, 11, "Modest", "A44", "M143", "M20", "M97", "M39"),
            
            # Hatterene
            ("PI93", "858", "T9", 11, 0, 11, 22, 11, 11, "Modest", "A25", "M15", "M120", "M26", "M46"),
            ("PI94", "858", "T10", 11, 11, 0, 11, 22, 11, "Timid", "A29", "M120", "M26", "M46", "M39"),
            
            # Cptain
            ("PI95", "879", "T11", 11, 11, 11, 22, 0, 11, "Modest", "A29", "M15", "M19", "M43", "M26"),
            ("PI96", "879", "T12", 0, 11, 22, 11, 11, 11, "Timid", "A55", "M19", "M43", "M26", "M39"),
            
            # Dragapult
            ("PI97", "887", "T1", 0, 11, 11, 11, 11, 22, "Timid", "A9", "M89", "M90", "M19", "M44"),
            ("PI98", "887", "T2", 11, 22, 11, 0, 11, 11, "Adamant", "A39", "M90", "M19", "M44", "M45"),
            
            # Calyrex
            ("PI99", "898", "T3", 11, 0, 11, 22, 11, 11, "Modest", "A29", "M15", "M44", "M41", "M26"),
            ("PI100", "898", "T4", 11, 11, 0, 11, 22, 11, "Timid", "A25", "M44", "M41", "M26", "M39"),
            
            # Enamorus
            ("PI101", "905", "T5", 0, 11, 11, 11, 11, 22, "Timid", "A48", "M95", "M44", "M26", "M120"),
            ("PI102", "905", "T6", 11, 22, 11, 0, 11, 11, "Adamant", "A49", "M44", "M26", "M120", "M45"),
            
            # Palafin (base form only)
            ("PI103", "964", "T7", 11, 0, 11, 11, 22, 11, "Modest", "A58", "M3", "M20", "M55", "M8"),
            ("PI104", "964", "T8", 11, 11, 0, 11, 22, 11, "Timid", "A58", "M20", "M55", "M8", "M39"),
        ]
        
        for inst_id, species_id, trainer_id, hp_ev, att_ev, def_ev, sp_att_ev, sp_def_ev, spd_ev, nature, ability_id, move1, move2, move3, move4 in pokemon_instances_data:
            instance = PokemonInstance(
                id=inst_id, species_id=species_id, trainer_id=trainer_id,
                hp_ev=hp_ev, attack_ev=att_ev, defense_ev=def_ev,
                special_attack_ev=sp_att_ev, special_defense_ev=sp_def_ev, speed_ev=spd_ev,
                nature=nature, ability_id=ability_id,
                move_1=move1, move_2=move2, move_3=move3, move_4=move4,
                source="Pokemon Sword"
            )
            db.session.add(instance)
        
        db.session.commit()
        print(f"✓ Added {len(pokemon_instances_data)} Pokemon instances (2 per species)")

        # ===== TEAMS (1+ per trainer with 6 Pokemon each) =====
        teams_data = [
            ("TE1", "T1", "A", None, "PI1", "I1", date.today() - timedelta(days=7)),
            ("TE2", "T1", "A", None, "PI3", "I2", date.today() - timedelta(days=7)),
            ("TE3", "T1", "A", None, "PI5", "I10", date.today() - timedelta(days=7)),
            ("TE4", "T1", "A", None, "PI7", "I1", date.today() - timedelta(days=7)),
            ("TE5", "T1", "A", None, "PI9", "I2", date.today() - timedelta(days=7)),
            ("TE6", "T1", "A", None, "PI11", "I10", date.today() - timedelta(days=7)),
            
            ("TE7", "T2", "A", None, "PI2", "I3", date.today() - timedelta(days=14)),
            ("TE8", "T2", "A", None, "PI4", "I10", date.today() - timedelta(days=14)),
            ("TE9", "T2", "A", None, "PI6", "I3", date.today() - timedelta(days=14)),
            ("TE10", "T2", "A", None, "PI8", "I10", date.today() - timedelta(days=14)),
            ("TE11", "T2", "A", None, "PI10", "I7", date.today() - timedelta(days=14)),
            ("TE12", "T2", "A", None, "PI12", "I3", date.today() - timedelta(days=14)),
            
            ("TE13", "T3", "A", None, "PI13", "I4", date.today() - timedelta(days=5)),
            ("TE14", "T3", "A", None, "PI15", "I5", date.today() - timedelta(days=5)),
            ("TE15", "T3", "A", None, "PI17", "I4", date.today() - timedelta(days=5)),
            ("TE16", "T3", "A", None, "PI19", "I5", date.today() - timedelta(days=5)),
            ("TE17", "T3", "A", None, "PI21", "I4", date.today() - timedelta(days=5)),
            ("TE18", "T3", "A", None, "PI23", "I5", date.today() - timedelta(days=5)),
            
            ("TE19", "T4", "A", None, "PI14", "I2", date.today() - timedelta(days=10)),
            ("TE20", "T4", "A", None, "PI16", "I7", date.today() - timedelta(days=10)),
            ("TE21", "T4", "A", None, "PI18", "I2", date.today() - timedelta(days=10)),
            ("TE22", "T4", "A", None, "PI20", "I7", date.today() - timedelta(days=10)),
            ("TE23", "T4", "A", None, "PI22", "I2", date.today() - timedelta(days=10)),
            ("TE24", "T4", "A", None, "PI24", "I7", date.today() - timedelta(days=10)),
            
            ("TE25", "T5", "A", None, "PI25", "I1", date.today() - timedelta(days=3)),
            ("TE26", "T5", "A", None, "PI27", "I10", date.today() - timedelta(days=3)),
            ("TE27", "T5", "A", None, "PI29", "I1", date.today() - timedelta(days=3)),
            ("TE28", "T5", "A", None, "PI31", "I10", date.today() - timedelta(days=3)),
            ("TE29", "T5", "A", None, "PI33", "I1", date.today() - timedelta(days=3)),
            ("TE30", "T5", "A", None, "PI35", "I10", date.today() - timedelta(days=3)),
            
            # Teams with Palafin (base form only)
            ("TE31", "T6", "B", None, "PI103", "I10", date.today() - timedelta(days=2)),  # Palafin Zero
            ("TE32", "T6", "B", None, "PI104", "I10", date.today() - timedelta(days=2)),  # Palafin Zero
            ("TE33", "T6", "B", None, "PI37", "I1", date.today() - timedelta(days=2)),
            ("TE34", "T6", "B", None, "PI39", "I10", date.today() - timedelta(days=2)),
            ("TE35", "T6", "B", None, "PI41", "I1", date.today() - timedelta(days=2)),
            ("TE36", "T6", "B", None, "PI43", "I10", date.today() - timedelta(days=2)),
            
            ("TE37", "T7", "B", None, "PI45", "I1", date.today() - timedelta(days=1)),
            ("TE38", "T7", "B", None, "PI47", "I10", date.today() - timedelta(days=1)),
            ("TE39", "T7", "B", None, "PI49", "I1", date.today() - timedelta(days=1)),
            ("TE40", "T7", "B", None, "PI51", "I10", date.today() - timedelta(days=1)),
            ("TE41", "T7", "B", None, "PI53", "I1", date.today() - timedelta(days=1)),
            ("TE42", "T7", "B", None, "PI55", "I10", date.today() - timedelta(days=1)),
        ]
        
        for team_id, trainer_id, team_slot, party_slot, pokemon_id, item_id, last_updated in teams_data:
            team = Team(
                id=team_id, trainer_id=trainer_id, team_slot=team_slot,
                party_slot=party_slot, pokemon_id=pokemon_id, item_id=item_id,
                last_updated=last_updated
            )
            db.session.add(team)
        
        db.session.commit()
        print(f"✓ Added {len(teams_data)} teams")

        print("\n✅ Database seeded successfully!")
        print(f"   • {len(abilities_data)} abilities")
        print(f"   • {len(moves_data)} moves")
        print(f"   • {len(pokemon_data)} Pokemon species (all final evolutions)")
        print(f"   • {len(pokemon_ability_links)} Pokemon-Ability links")
        print(f"   • {len(pokemon_move_links)} Pokemon-Move links")
        print(f"   • {len(items_data)} held items")
        print(f"   • {len(trainers_data)} trainers")
        print(f"   • {len(trainer_item_links)} Trainer-HeldItem links")
        print(f"   • {len(pokemon_instances_data)} Pokemon instances")
        print(f"   • {len(teams_data)} teams")

if __name__ == "__main__":
    seed_database()



    