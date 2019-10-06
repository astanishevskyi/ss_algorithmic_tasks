import unittest
from tasks import task_108, task_331_a, task_331_b
class Test_tasks(unittest.TestCase):

    def test_task_108(self):
        self.assertEqual(task_108(2), 4)  
        self.assertEqual(task_108(100), 128)              
        self.assertEqual(task_108("ddd"),'Type integer')
    def test_task_331_a(self):
        self.assertEqual(task_331_a(3), [1, 1, 1])  
        self.assertEqual(task_331_a(-1), 'n must be bigger than 0')              
        self.assertEqual(task_331_a(7),'There is no x, y, z')

    def test_task_331_b(self):
        self.assertEqual(task_331_b(7), [])  
        self.assertEqual(task_331_b(10), [[0, 1, 3], [0, 3, 1], [1, 0, 3], [1, 3, 0], [3, 0, 1], [3, 1, 0]])              
        self.assertEqual(task_331_b("sss"), 'Type integer')
       

if __name__=="__main__":
    unittest.main()