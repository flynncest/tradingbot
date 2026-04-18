import logging

logger = logging.getLogger(__name__)

TOOL_DEFINITIONS = [
    {
        "name": "send_notification",
        "description": "Log a summary or alert to the console.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "message": {"type": "string"},
                "urgent": {"type": "boolean", "default": False},
            },
            "required": ["title", "message"],
        },
    },
]


def send_notification(title: str, message: str, urgent: bool = False) -> str:
    level = "URGENT" if urgent else "INFO"
    logger.info(f"[{level}] {title}\n{message}")
    print(f"\n{'='*60}\n[{level}] {title}\n{message}\n{'='*60}")
    return "Notification logged."


HANDLERS = {
    "send_notification": send_notification,
}
