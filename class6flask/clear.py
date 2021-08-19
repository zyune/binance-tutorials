from flask.ext.cache importCache
from yourapp import app, your_cache_config
cache =Cache()
def main():
    cache.init_app(app, config=your_cache_config)
with app.app_context():
        cache.clear()
if __name__ =='__main__':
    main()