from schema import Schema, Optional

config_schema = Schema(
    {
        "sources": [
            {
                "type": str,
                "url": str,
                Optional("config"): object,
            }
        ],
        "elastic": {
            "url": str,
            "username": str,
            "password": str,
            Optional("cert_location"): str,
            "index": str,
        },
    },
    ignore_extra_keys=True,
)

config_file = "config.yaml"

default_config = {"sources": []}


def validate(config: dict):
    config_schema.validate(config)
