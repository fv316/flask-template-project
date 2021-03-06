# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask_script import Manager
from flask import render_template
from project import create_app

# in case we run the test command choose the "TestConfig"
import sys
#arg_dict = dict((i, v) for i, v in enumerate(sys.argv))
#config = "config.TestConfig" if arg_dict.get(1, None) == "test" else None
app = create_app(None)
manager = Manager(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def main():
    import project.commands as cmd
    manager.add_command("worker", cmd.WorkerCommand())
    manager.add_command("test", cmd.TestCommand())
    manager.add_command("routes", cmd.ListRoutesCommand())
    manager.add_command("create-user", cmd.CreateUserCommand())
    manager.add_command("delete-user", cmd.DeleteUserCommand())
    manager.add_command("create-db", cmd.CreateDBCommand())
    manager.run()

if __name__ == '__main__':
    main()


__version__ = '0.0.0.1'
__author__ = "Francisco Correia"
__email__ = "fvc@hotmail.co.uk"
