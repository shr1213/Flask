import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, System,SysDate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, System=System, SysDate=SysDate)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
