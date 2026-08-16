from pydantic import Field


def add(
    a: int = Field(description="The first number to add"),
    b: int = Field(description="The second number to add"),
) -> int:
    """Add two numbers together.

    This tool performs basic arithmetic addition of two integers.

    When to use:
    - Adding two numbers together
    - Basic mathematical operations

    Examples:
    >>> add(2, 3)
    5
    >>> add(-1, 5)
    4
    """
    return a + b
