from ddtrace import config, patch_all

# Override service name, default 'flask'
# config.flask['service_name'] = 'brave_cane'
config.flask['analytics_enabled'] = True

patch_all(flask=True)

from brave_cane.app import create_app

app = create_app()

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    debug = True
    app.run(host, port, debug)
