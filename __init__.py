from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB':"my_blog"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"


db = MongoEngine(app)


if __name__ == '__main__':
    app.run()


def register_blueprints(app):
    # imports
    from blog.views import posts
    from blog.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)
