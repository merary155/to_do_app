import unittest
from to_do import ToDoList

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo = ToDoList()

    def test_add_task(self):
        # ここでタスクを直接追加するメソッドを作る
        self.todo.tasks.append("テストタスク")
        self.assertIn("テストタスク", self.todo.tasks)

if __name__ == "__main__":
    unittest.main()
