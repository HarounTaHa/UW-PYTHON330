from model import db, SavedTotal


def setup_database():
    db.connect()
    db.create_tables([SavedTotal])


if __name__ == "__main__":
    setup_database()
