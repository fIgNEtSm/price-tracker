from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://price_tracker_postgresql_user:yA04ULdjNEwDWd2fPpuVAvDKvMkBL9XN@dpg-cueg54lds78s73ae06s0-a.singapore-postgres.render.com/price_tracker_postgresql'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

class PriceTracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(120), nullable=False)

def add_tracking(url, price, email):
    new_entry = PriceTracker(url=url, price=price, email=email)
    db.session.add(new_entry)
    db.session.commit()

def tracking_exists(url, email):
    return PriceTracker.query.filter_by(url=url, email=email).first() is not None

def get_all():
    trackers = PriceTracker.query.all()
    return [{"id": tracker.id, "email": tracker.email, "price": tracker.price, "url": tracker.url} for tracker in trackers]
