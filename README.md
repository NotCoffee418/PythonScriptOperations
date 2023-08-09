# PythonScriptOperations

[![PyPI](https://img.shields.io/pypi/v/pythonscriptoperations?style=for-the-badge)](https://pypi.org/project/pythonscriptoperations/)

## What is it?
`PythonScriptOperations` is a library for Python console applications to quickly set up a console application interface. Developers can utilize it to swiftly access specific portions of their codebase by registering operations.

It is the brother to [CSharpScriptOperations](https://github.com/NotCoffee418/CSharpScriptOperations), a similar library for C# console applications.

## Quick Start

1. **Import the pip package**:
    ```python
    from pythonscriptoperations import register_operation, start_listening, start_listening_async
    ```
2. **Create a function or async function and register it**:
    ```python
    def add_numbers():
        result = 2 + 2
        print(f"2 + 2 = {result}")

    register_operations(add_numbers, "Print the result of 2+2")
    ```

3. **Start listening for operations**:
    ```python
    start_listening()
    ```

## What does it look like?

This is an example taken from the `demo.py`.
```
Available operations:
0. Exit
1. Addition: 5 + 7
2. Subtraction: 12 - 4
3. Multiplication (async): 6 * 3
4. Division: 36 / 6

Select an operation ('help' for list of operations)
1

Running operation: Addition: 5 + 7
12

Done
```

## Detailed Instructions

### 1. Install the pip package

Install the pip package using:
```bash
pip install pythonscriptoperations
```
Then, simply `import pythonscriptoperations` wherever you need it.

### 2. Register your operations

Operations are simple Python functions (or async functions) dedicated to specific tasks.  
To provide a description, simply pass it when registering the function:

```python
def example_function():
    print("This is an example.")

async def example_async_function():
    print("This will be awaited")
    await asyncio.sleep(1000)

register_operations(example_function, "An example operation")
register_operations(example_async_function, "An example async operation")
```

### 3. Start listening

Start the listener to display available operations and accept user input:

```python
start_listening()
```

If you need the console to be non-blocking, you can use the async version:
```python
start_listening_async()
```

### 4. Try it out

When you run your script, you should see a list of operations with numbers next to them. To execute an operation, simply input its number.

### Example

For a complete working example, refer to the `demo.py` in the repository.