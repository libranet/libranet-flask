
# uvicorn


# run uvicorn server
[group: 'uvicorn']
uvicorn-run:
    uv run uvicorn --factory "${FLASK_APP%()}"
