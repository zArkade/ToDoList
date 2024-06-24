import unittest
import sys
from pathlib import Path

#sem essa linha, nao encontra o diretorio src
sys.path.append(str(Path(__file__).resolve().parent.parent / 'src'))

from src.gerenciadorTask import add_task, list_tasks, mark_task_completed, remove_task, tasks

class TestGerenciadorTask(unittest.TestCase):
    def setUp(self):
        #limpar a lista de tarefa antes de cada teste
        tasks.clear()
    
    def test_add_task(self):
        add_task("Teste")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Teste")
        self.assertFalse(tasks[0]["completed"])

    def test_mark_task_completed(self):
        add_task("Teste")
        mark_task_completed(0)
        self.assertTrue(tasks[0]["completed"])

    def test_remove_task(self):
        add_task("Teste")
        remove_task(0)
        self.assertEqual(len(tasks), 0)

if __name__ == '__main__':
    unittest.main()