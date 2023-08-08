from typing import Union, Callable, Optional, List
import asyncio
import types


class RegisteredOperation:
    # Static counter to keep track of order
    _counter = 0

    def __init__(self, func: Union[Callable, types.CoroutineType], description: str, priority: Optional[int] = None, asyncness: bool = False):
        if not hasattr(func, "__call__"):
            raise ValueError(f"{func} is not a function or async function.")

        if not isinstance(description, str):
            raise ValueError(
                "Description must be provided and should be a string.")

        self.func = func
        self.description = description
        self.priority = 0 if priority is None else priority
        self.asyncness = asyncness

        # Increment the static counter and assign order
        RegisteredOperation._counter += 1
        self.order = RegisteredOperation._counter


# List to hold registered operations
registered_operations = []


def register_operation(func: Union[Callable, types.CoroutineType], description: str, priority: Optional[int] = None):
    asyncness = asyncio.iscoroutinefunction(func)
    operation = RegisteredOperation(func, description, priority, asyncness)
    registered_operations.append(operation)


def reset_operations():
    registered_operations.clear()


def list_operations() -> List[RegisteredOperation]:
    # Sort based on priority first (higher values first), and then by order (ascending)
    sorted_operations = sorted(
        registered_operations,
        key=lambda op: (op.priority == 0, -op.priority, op.order)
    )
    return sorted_operations
