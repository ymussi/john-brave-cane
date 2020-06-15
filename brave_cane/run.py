from brave_cane.app import create_app, create_graphql

app = create_app()
graphql = create_graphql(app)

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    debug = True
    app.run(host, port, debug)
    graphql.run(host, port, debug)
