from app import app

if __name__ == '__main__':
    # Run without the reloader to keep a single stable process for tests
    app.run(debug=False, port=5000)
