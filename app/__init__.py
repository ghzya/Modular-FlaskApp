from flask import Flask

def create_app():
    app = Flask(__name__)

    # Initialize flask extention here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    @app.route("/test/")
    def test_page():
        return "<h1>Testing the Flask Applicarion Factory Pattern</h1>"
    
    return app