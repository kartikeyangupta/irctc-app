from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
from app import db

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Set your classes here.

class User(Base):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'),
        nullable=False)
        
    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
    
    def __repr__(self):
        return '<User %r>' % self.name

class Role(Base):
    __tablename__ = 'Role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    
        
    def __init__(self, name=None, password=None):
        self.name = name
    
    def __repr__(self):
        return '<Role %r>' % self.name

class Coach(Base):
    __tablename__ = 'Coach'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    
        
    def __init__(self, name=None, password=None):
        self.name = name
    
    def __repr__(self):
        return '<Coach %r>' % self.name

class Train(Base):
    __tablename__ = 'Train'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    
        
    def __init__(self, name=None, password=None):
        self.name = name
    
    def __repr__(self):
        return '<Train %r>' % self.name

class TrainCoach(Base):
    __tablename__ = 'TrainCoach'

    id = db.Column(db.Integer, primary_key=True)
    train_id = db.Column(db.Integer, db.ForeignKey('train.id'),
        nullable=False)
    coach_id = db.Column(db.Integer, db.ForeignKey('coach.id'),
        nullable=False)
    
        
    def __init__(self, name=None, password=None):
        self.name = name
    
    def __repr__(self):
        return '<TrainCoach %r>' % self.id

class Booking(Base):
    __tablename__ = 'TrainCoach'

    id = db.Column(db.Integer, primary_key=True)
    train_coach_id = db.Column(db.Integer, db.ForeignKey('traincoach.id'),
        nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    password = db.Column(db.Integer, nullable=False)
        
    def __init__(self, name=None, password=None):
        self.name = name
    
    def __repr__(self):
        return '<Booking %r>' % self.id

# Create tables.
Base.metadata.create_all(bind=engine)