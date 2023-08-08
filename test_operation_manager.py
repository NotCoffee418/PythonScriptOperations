import asyncio
import unittest
from operation_manager import list_operations, reset_operations, register_operations


class TestOperations(unittest.TestCase):

    def test_sync_function(self):
        def sync_func():
            return "sync result"
        register_operations(sync_func, "Sync function")
        op = list_operations()[-1]  # Get the last registered operation
        self.assertEqual(op.func(), "sync result")

    def test_async_function(self):
        async def async_func():
            return "async result"
        register_operations(async_func, "Async function")
        op = list_operations()[-1]  # Get the last registered operation
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(op.func())
        self.assertEqual(result, "async result")

    def test_sorting(self):
        # Clearing any previously registered operations
        reset_operations()

        def func1():
            pass

        async def func2():
            pass

        def func3():
            pass

        register_operations(func1, "Func 1", 2)
        register_operations(func2, "Async Func 2", 3)
        register_operations(func3, "Func 3", 1)

        ops = list_operations()
        # Highest priority
        self.assertEqual(ops[0].description, "Async Func 2")
        # Second highest priority
        self.assertEqual(ops[1].description, "Func 1")
        self.assertEqual(ops[2].description, "Func 3")  # Lowest priority


if __name__ == "__main__":
    unittest.main()
