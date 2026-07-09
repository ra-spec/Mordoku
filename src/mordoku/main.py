"""Main module for Mordoku."""


def hello(name: str = "World") -> str:
    """Greet someone.
    
    Args:
        name: The name to greet.
        
    Returns:
        A greeting message.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(hello())
