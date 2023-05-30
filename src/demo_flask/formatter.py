"""demo_flask.formatter."""

import logging
import textwrap

from colorlog import ColoredFormatter


class HttpFormatter(logging.Formatter):
    """HTTP-Formatter."""

    def format_headers(self, d):
        return '\n'.join(f'{k}: {v}' for k, v in d.items())

    def formatMessage(self, record):
        # result = super().formatMessage(record)

        if hasattr(record, "req"):
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
                req=record.req ,
                resp=record.res,
                req_headers=self.format_headers(record.req.headers),
                resp_headers=self.format_headers(record.res.headers),
            )

            record.message = message_extra
        else: 
            # breakpoint()
            pass
        result = super().formatMessage(record)
        return result


class ColorHttpFormatter(HttpFormatter,ColoredFormatter):
    """Colorized HTTP-Formatter."""