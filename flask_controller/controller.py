from abc import ABC


def route(rule, **options):
    """Decorator for defining routes of FlaskController classes.

    Acts in the same way ass @app.route.
    Can be used for a class to set a base route too.

    Args:
        path (str): The path of the newly defined route
        options: refer to flasks docs for those, all of them can be used
    """
    def decorator(f):
        f._route = (rule, options)
        return f

    return decorator


class FlaskController(ABC):
    """Baseclass for the Controller Classes.

    Extend tis class and use it in conjunction with the route decoractor
    to define routes for your flask app.
    Use the register method to add your defined routes to a flask app.
    """

    def __init__(self):
        super(FlaskController, self).__init__()

    def register(self, app):
        """Adds the routes of a Controller to a Flask instance.
        
        Args:
            app (Flask)
        """
        members = dir(self)
        routes = []
        for member in members:
            if hasattr(getattr(self, member), "_route"):
                if member is not "__class__":
                    routes.append(member)
        self._register_routes(routes, app)

    def _register_routes(self, routes, app):
        for route in routes:
            func = getattr(self, route)
            real_route = self._generate_route(func._route[0])
            options = func._route[1]
            app.add_url_rule(real_route, route + real_route,  func, **options)

    def _generate_route(self, route):
        base_route = ""

        if hasattr(self, "_route"):
            base_route = self._route[0]

        return base_route + route
