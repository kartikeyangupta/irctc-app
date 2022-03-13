from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
from app import db

engine = create_engine('sqlite:///database.db', echo=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush = False,
#                                          bind = engine))
Base = declarative_base()
# Base.query = db_session.query_property()

# Set your classes here.


class Role(Base):
    __tablename__ = 'Role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % self.name


class User(Base):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('Role.id'),
                        nullable=False)

    def __init__(self, name=None, password=None, isAdmin=False):
        self.name = name
        self.password = password
        self.role_id = 1
        if isAdmin == True:
            self.role_id = 2

    def __repr__(self):
        return '<User %r>' % self.name


class Coach(Base):
    __tablename__ = 'Coach'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Coach %r>' % self.name


class Train(Base):
    __tablename__ = 'Train'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Train %r>' % self.name


class TrainCoach(Base):
    __tablename__ = 'TrainCoach'

    id = db.Column(db.Integer, primary_key=True)
    train_id = db.Column(db.Integer, db.ForeignKey('Train.id'),
                         nullable=False)
    coach_id = db.Column(db.Integer, db.ForeignKey('Coach.id'),
                         nullable=False)

    def __init__(self, train_id=None, coach_id=None):
        self.train_id = train_id
        self.coach_id = coach_id

    def __repr__(self):
        return '<TrainCoach %r>' % self.id


class Booking(Base):
    __tablename__ = 'Booking'

    id = db.Column(db.Integer, primary_key=True)
    train_coach_id = db.Column(db.Integer, db.ForeignKey('TrainCoach.id'),
                               nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'),
                        nullable=False)
    seat_number = db.Column(db.Integer, nullable=False)

    def __init__(self, train_coach_id=None, user_id=None, seat_number=None):
        self.train_coach_id = train_coach_id
        self.user_id = user_id
        self.seat_number = seat_number

    def __repr__(self):
        return '<Booking %r>' % self.id


# Create tables.
Base.metadata.create_all(bind=engine)
