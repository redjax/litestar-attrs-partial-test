import uvicorn

import attrs
from typing import Dict, List, Any, Optional, Union


@attrs.define()
class UvicornCustomServer(object):
    app: str = attrs.field(default="example:app")
    host: str = attrs.field(default="0.0.0.0")
    port: int = attrs.field(default=8120)
    reload: bool = attrs.field(default=False)
    log_level: str = attrs.field(default="debug")

    def run_server(self):
        uvicorn.run(
            app=self.app,
            host=self.host,
            port=self.port,
            reload=self.reload,
            log_level=self.log_level,
            # log_config=self.log_config,
        )


dev_conf = {
    "app": "example:app",
    "host": "0.0.0.0",
    "port": 8120,
    "reload": True,
    "log_level": "debug",
}


def main(_server: UvicornCustomServer = UvicornCustomServer()):
    # log.debug(f"Server: {_server}")
    _server.run_server()


if __name__ == "__main__":
    dev_server = UvicornCustomServer(**dev_conf)

    main(dev_server)
