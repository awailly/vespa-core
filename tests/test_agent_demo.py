import unittest
import sys
import os

DOSSIER_COURRANT = os.path.dirname(os.path.abspath(__file__))
DOSSIER_PARENT = os.path.dirname(DOSSIER_COURRANT)
sys.path.append(DOSSIER_PARENT)

from vespa.node import Node
from vespa.agent import Agent
from vespa.agent_demo import Agent_Demo


class TestInit(unittest.TestCase):
    def test_instance_node(self):
        v = Agent_Demo('testnode', "127.0.0.1", 1337, None, run=False)
        self.assertTrue(isinstance(v, Agent))
        self.assertTrue(isinstance(v, Node))

if __name__ == '__main__':
    unittest.main()
