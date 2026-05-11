from .extensions import db
from datetime import date


class PokemonSpecies(db.Model):
    """Base Pokemon species table with stats and type information."""
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    variant = db.Column(db.String(50))
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    special_attack = db.Column(db.Integer, nullable=False)
    special_defense = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    type_1 = db.Column(db.String(10))
    type_2 = db.Column(db.String(10))
    is_base_form = db.Column(db.Boolean, default=True)
    add_date = db.Column(db.Date, default=date.today)
    abilities = db.relationship('AbilityList', secondary='pokemon_ability', backref='pokemon_species')
    moves = db.relationship('MoveList', secondary='pokemon_move', backref='pokemon_species')
    instances = db.relationship('PokemonInstance', backref='species', lazy=True)
    
    def __repr__(self):
        return f"<PokemonSpecies {self.name}>"


class AbilityList(db.Model):
    """List of available Pokemon abilities."""
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    add_date = db.Column(db.Date, default=date.today)
    pokemon_species = db.relationship('PokemonSpecies', secondary='pokemon_ability', backref='abilities')
    
    def __repr__(self):
        return f"<AbilityList {self.name}>"


class Pokemon_Ability(db.Model):
    """Many-to-many relationship between Pokemon species and abilities."""
    __tablename__ = 'pokemon_ability'
    species_id = db.Column(db.String(20), db.ForeignKey('pokemon_species.id'), primary_key=True)
    ability_id = db.Column(db.String(20), db.ForeignKey('ability_list.id'), primary_key=True)
    add_date = db.Column(db.Date, default=date.today)
    
    def __repr__(self):
        return f"<Pokemon_Ability {self.species_id} - {self.ability_id}>"


class MoveList(db.Model):
    """List of available Pokemon moves with stats."""
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    power = db.Column(db.Integer)
    accuracy = db.Column(db.Float)
    type = db.Column(db.String(20))
    priority = db.Column(db.Integer)
    description = db.Column(db.String(255))
    power_points = db.Column(db.Integer)
    add_date = db.Column(db.Date, default=date.today)
    pokemon_species = db.relationship('PokemonSpecies', secondary='pokemon_move', backref='moves')
    
    def __repr__(self):
        return f"<MoveList {self.name}>"


class Pokemon_Move(db.Model):
    """Many-to-many relationship between Pokemon species and moves."""
    __tablename__ = 'pokemon_move'
    species_id = db.Column(db.String(20), db.ForeignKey('pokemon_species.id'), primary_key=True)
    move_id = db.Column(db.String(20), db.ForeignKey('move_list.id'), primary_key=True)
    add_date = db.Column(db.Date, default=date.today)
    
    def __repr__(self):
        return f"<Pokemon_Move {self.species_id} - {self.move_id}>"


class Trainer(db.Model):
    """Trainer profile information."""
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    victory_points = db.Column(db.Integer, default=0)
    battle_tickets = db.Column(db.Integer, default=0)
    join_date = db.Column(db.Date, default=date.today)
    held_items = db.relationship('HeldItem', secondary='trainer_held_item', backref='trainers')
    pokemon_instances = db.relationship('PokemonInstance', backref='trainer', lazy=True)
    teams = db.relationship('Team', backref='trainer', lazy=True)
    
    def __repr__(self):
        return f"<Trainer {self.name}>"


class HeldItem(db.Model):
    """List of items that Pokemon can hold."""
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    add_date = db.Column(db.Date, default=date.today)
    trainers = db.relationship('Trainer', secondary='trainer_held_item', backref='held_items')
    
    def __repr__(self):
        return f"<HeldItem {self.name}>"


class Trainer_HeldItem(db.Model):
    """Many-to-many relationship between trainers and held items."""
    trainer_id = db.Column(db.String(20), db.ForeignKey('trainer.id'), primary_key=True)
    item_id = db.Column(db.String(20), db.ForeignKey('held_item.id'), primary_key=True)
    obtain_date = db.Column(db.Date, default=date.today)
    
    def __repr__(self):
        return f"<Trainer_HeldItem {self.trainer_id} - {self.item_id}>"


class PokemonInstance(db.Model):
    """Individual Pokemon instances owned by trainers with specific EVs, nature, and moves."""
    id = db.Column(db.String(20), primary_key=True)
    species_id = db.Column(db.String(20), db.ForeignKey('pokemon_species.id'), nullable=False)
    trainer_id = db.Column(db.String(20), db.ForeignKey('trainer.id'))
    hp_ev = db.Column(db.Integer, default=0)
    attack_ev = db.Column(db.Integer, default=0)
    defense_ev = db.Column(db.Integer, default=0)
    special_attack_ev = db.Column(db.Integer, default=0)
    special_defense_ev = db.Column(db.Integer, default=0)
    speed_ev = db.Column(db.Integer, default=0)
    nature = db.Column(db.String(50))
    ability_id = db.Column(db.String(50), db.ForeignKey('ability_list.id'))
    move_1 = db.Column(db.String(50), db.ForeignKey('move_list.id'))
    move_2 = db.Column(db.String(50), db.ForeignKey('move_list.id'))
    move_3 = db.Column(db.String(50), db.ForeignKey('move_list.id'))
    move_4 = db.Column(db.String(50), db.ForeignKey('move_list.id'))
    source = db.Column(db.String(20))
    species = db.relationship('PokemonSpecies', backref='pokemon_instances')
    trainer = db.relationship('Trainer', backref='pokemon_instances')
    
    def __repr__(self):
        return f"<PokemonInstance {self.instance_id}>"


class Team(db.Model):
    """Trainer's battle teams containing up to 6 Pokemon with held items."""
    id = db.Column(db.String(20), primary_key=True)
    trainer_id = db.Column(db.String(20), db.ForeignKey('trainer.id'), nullable=False)
    team_slot = db.Column(db.String(1), nullable=False)
    party_slot = db.Column(db.Integer)
    pokemon_id = db.Column(db.String(20), db.ForeignKey('pokemon_instance.id'))
    item_id = db.Column(db.String(20), db.ForeignKey('held_item.id'))
    last_updated = db.Column(db.Date, default=date.today)
    trainer = db.relationship('Trainer', backref='teams')
    pokemon = db.relationship('PokemonInstance', backref='teams')
    item = db.relationship('HeldItem', backref='teams')
    
    def __repr__(self):
        return f"<Team {self.trainer_id} - Slot {self.team_slot}>"
