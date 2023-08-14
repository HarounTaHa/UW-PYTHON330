from model import db, SavedTotal


def run():
    db.connect()
    db.create_tables([SavedTotal])


if __name__ == "__main__":
    run()
