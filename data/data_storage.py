from flaskApp.models import db, SteelPrice


def store_data(price, date, region):
    try:
        steel_price = SteelPrice(price=price, date=date, region=region)
        db.session.add(steel_price)
        db.session.commit()
        print("Data stored successfully.")
    except Exception as e:
        db.session.rollback()
        print(f"Failed to store data: {e}")


def fetch_all_data():
    return SteelPrice.query.all()


def fetch_data_by_region(region):
    return SteelPrice.query.filter_by(region=region).all()


def fetch_data_by_date_range(start_date, end_date):
    return SteelPrice.query.filter(SteelPrice.date.between(start_date, end_date)).all()