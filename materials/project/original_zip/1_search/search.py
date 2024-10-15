# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    """
    0. Data sturcture: We have known that state is stored as tuple,
    also need one stack for path travelled, a list to record visited node.
       Helper function: An expand function, a function to generate valid move.
    1. First visit the start point, and store it in the stack
    2. Recursion: Pop one, mark it as visited, and for each of its unvisited child, expand it.
    3. End when you find the goal.
    """
    visited = set()
    _stack = util.Stack()
    _stack.push((problem.getStartState(), []))
    while not _stack.isEmpty(): 
        # When you pop, the node should be regarded as visited
        state, actions = _stack.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            visited.add(state)
            for succ, act, _ in problem.getSuccessors(state):
                new_path = actions + [act]
                _stack.push((succ, new_path))
    return []
                
    
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    visited = set()
    _queue = util.Queue()
    _queue.push((problem.getStartState(), []))
    while not _queue.isEmpty(): 
        # When you pop, the node should be regarded as visited
        state, actions = _queue.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            visited.add(state)
            for succ, act, _ in problem.getSuccessors(state):
                new_path = actions + [act]
                _queue.push((succ, new_path))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    visited = set()
    _pq = util.PriorityQueue()  # As util.py shows, pq is a min-heap
    _pq.push((problem.getStartState(), [], 0), 0)

    while not _pq.isEmpty():
        frontier, actions, property = _pq.pop()
        if problem.isGoalState(frontier):
            return actions
        if frontier not in visited:
            visited.add(frontier)
            for succ, act, cost in problem.getSuccessors(frontier):
                _pq.push((succ, actions + [act], property + cost), property + cost)
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    visited = set()
    _pq = util.PriorityQueue()
    _pq.push(
        (problem.getStartState(), [], 0), 
        0 + heuristic(problem.getStartState(), problem)
    )
    while not _pq.isEmpty():
        frontier, actions, cost_sofar = _pq.pop()
        if problem.isGoalState(frontier):
            return actions
        if frontier not in visited:
            visited.add(frontier)
            for succ, act, cost in problem.getSuccessors(frontier):
                new_heu_total_cost = cost_sofar + cost + heuristic(succ, problem)
                new_actions = actions + [act]
                _pq.push((succ, new_actions, cost_sofar + cost), new_heu_total_cost)
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
