"""libranet_flask.formatter."""

import logging
import textwrap
from typing import Any, cast

from colorlog import ColoredFormatter


class HttpFormatter(logging.Formatter):
    """HTTP-Formatter."""

    def format_headers(self, d: dict) -> str:
        """Format HTTP headers as a string."""
        return "\n".join(f"{k}: {v}" for k, v in d.items())

    def formatMessage(self, record: logging.LogRecord) -> str:  # noqa: N802
        """Format the log message with HTTP request/response details."""
        if hasattr(record, "req") and hasattr(record, "res"):
            req = cast("Any", record.req)
            res = cast("Any", record.res)
            message_extra = record.message
            message_extra += textwrap.dedent("""
                ---------------- request ----------------
                {req.method} {req.url}
                {req_headers}

                Body:
                {req.body}
                \n
                ---------------- response ----------------
                {resp.status_code} {resp.reason} {resp.url}
                {resp_headers}

                {resp.text}
            """).format(
                req=req,
                resp=res,
                req_headers=self.format_headers(req.headers),
                resp_headers=self.format_headers(res.headers),
            )

            record.message = message_extra
        else:
            # breakpoint()
            pass
        return super().formatMessage(record)


class ColorHttpFormatter(HttpFormatter, ColoredFormatter):
    """Colorized HTTP-Formatter."""
