def init_lazy_user_object(lazy_user_object):
    if hasattr(lazy_user_object, '_wrapped') and hasattr(lazy_user_object, '_setup'):
        if lazy_user_object._wrapped.__class__ == object:
            lazy_user_object._setup()
            lazy_user_object = lazy_user_object._wrapped

    return lazy_user_object
