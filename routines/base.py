import os
import logging
from typing import Any
import anthropic

logger = logging.getLogger(__name__)

MODEL = "claude-opus-4-7"


def run_agent(
    system_prompt: str,
    user_prompt: str,
    tools: list[dict],
    handlers: dict[str, Any],
    max_tokens: int = 8096,
) -> str:
    """Run a Claude Opus 4.7 agentic loop until end_turn."""
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    messages = [{"role": "user", "content": user_prompt}]
    final_text = ""

    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            system=system_prompt,
            tools=tools,
            messages=messages,
        )
        logger.info(f"Claude response: stop_reason={response.stop_reason}, tokens={response.usage}")

        tool_uses = []
        for block in response.content:
            if hasattr(block, "text"):
                final_text = block.text
            elif block.type == "tool_use":
                tool_uses.append(block)

        if response.stop_reason == "end_turn" or not tool_uses:
            break

        tool_results = []
        for block in tool_uses:
            handler = handlers.get(block.name)
            if handler:
                try:
                    result = handler(**block.input)
                except Exception as e:
                    result = f"Tool error ({block.name}): {e}"
            else:
                result = f"Unknown tool: {block.name}"

            logger.debug(f"Tool {block.name} -> {str(result)[:200]}")
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": str(result),
            })

        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})

    return final_text
