
# gunicorn


# run gunicorn server
[group: 'gunicorn']
gunicorn-run:
    uv run gunicorn "$FLASK_APP"
