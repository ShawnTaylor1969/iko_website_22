class DatabaseRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_to_local = {'Configuration',}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_to_local:
            return 'local'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_to_local:
            return 'local'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_to_local or
            obj2._meta.app_label in self.route_to_local
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name in self.route_to_local:
            return 'local'
        return None
