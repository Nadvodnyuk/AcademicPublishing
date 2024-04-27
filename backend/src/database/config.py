
TORTOISE_ORM = {
    "connections": {"default": f"postgres://postgres:231703@localhost:5432/paper_python"},
    "apps": {
        "models": {
            "models": [
                "src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}

SECRETKEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"