import os


def clear_db(session, base):
    if os.getenv('FLASK_ENV') not in ['development']:
        raise Exception('TESTS IS ALLOWED TO RUN ONLY END DEVELOPMENT MODE')
    session.rollback()
    for table in reversed(base.metadata.sorted_tables):
        session.execute(table.delete())
    session.commit()
