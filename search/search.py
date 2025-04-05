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

Code Written by: Michael E Newbold #747638
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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start State: " + str(problem.getStartState()))
    print("Is the start state ( " + str(problem.getStartState()) + " ) a goal?: " + str(problem.isGoalState(problem.getStartState())))
    
    # Demonstrate how successor function works
    print("Successor function of initial start state ( " + str(problem.getStartState()) + " ) yields a tuple with 3 pieces:")
    print("\t(nextState, actionFromCurrStateToNextState, costToGetFromCurrStateToNextState)")
    for statePortion in problem.getSuccessors(problem.getStartState()):
        print("\t" + str(statePortion))
    """
    "*** YOUR CODE HERE ***"
    #Initialization
    from game import Directions

    fringe = util.Stack() # Stack Initialization
    # In order for this to be a proper stack you can only interact with it as a .append() or .pop()
    # {If we are using straight Py list}

    fringe.push((problem.getStartState(), []))  # Adds the start state and a list which will be the path

    # Needs to be filled with the directions maybe? Instead of the nodes themselves.
    explored = [] # Explored nodes, starts as empty, will end up with all explored nodes.

    while not fringe.isEmpty():
        node, path = fringe.pop() # Gets the next node to look at
        # path is an updated way to get to the given node, which is always what should be returned

        if problem.isGoalState(node): #
            return path # Path is what the program is wanting, as it wants the route to the correct node.

        if node not in explored: # DFS does not want to revisit states.
            explored.append(node) # Adds the node to the explored list

            # Expand the nodes successors, and push them to the stack.
            # Might have an issue with successor needing to be renamed to nextState
            for successor, actionFromCurrStateToNextState, _ in problem.getSuccessors(node):
                if successor not in explored: # DFS does not want to revisit states.
                    new_path = path + [actionFromCurrStateToNextState] # Updates the path to the new successor
                    fringe.push((successor, new_path)) # Sends the path with the successor into the fringe.
    # Fringe is empty, meaning they have explored every node and not found the correct one.
    return [] # Added list to return correct datatype.


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # Initialization
    from game import Directions

    fringe = util.Queue()  # Stack Initialization
    # In order for this to be a proper stack you can only interact with it as a .append() or .pop()
    # {If we are using straight Py list}

    fringe.push((problem.getStartState(), []))  # Adds the start state and a list which will be the path

    # Needs to be filled with the directions maybe? Instead of the nodes themselves.
    explored = []  # Explored nodes, starts as empty, will end up with all explored nodes.

    while not fringe.isEmpty():
        node, path = fringe.pop()  # Gets the next node to look at
        # path is an updated way to get to the given node, which is always what should be returned

        if problem.isGoalState(node):  #
            return path  # Path is what the program is wanting, as it wants the route to the correct node.

        if node not in explored:  # DFS does not want to revisit states.
            explored.append(node)  # Adds the node to the explored list

            # Expand the nodes successors, and push them to the stack.
            # Might have an issue with successor needing to be renamed to nextState
            for successor, actionFromCurrStateToNextState, _ in problem.getSuccessors(node):
                if successor not in explored:  # DFS does not want to revisit states.
                    new_path = path + [actionFromCurrStateToNextState]  # Updates the path to the new successor
                    fringe.push((successor, new_path))  # Sends the path with the successor into the fringe.
    # Fringe is empty, meaning they have explored every node and not found the correct one.
    return []  # Added list to return correct datatype.

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # Initialization
    from game import Directions

    fringe = util.PriorityQueue()  # Stack Initialization
    # In order for this to be a proper stack you can only interact with it as a .append() or .pop()
    # {If we are using straight Py list}

    fringe.push((problem.getStartState(), [], 0), 0)  # Adds the start state and a list which will be the path
    # Added a third position to hold the Cost of the first item, and a second item to hold the priority level

    # Needs to be filled with the directions maybe? Instead of the nodes themselves.
    explored = []  # Explored nodes, starts as empty, will end up with all explored nodes.

    while not fringe.isEmpty():
        node, path, cost = fringe.pop()  # Gets the next node to look at
        # path is an updated way to get to the given node, which is always what should be returned

        if problem.isGoalState(node):  #
            return path  # Path is what the program is wanting, as it wants the route to the correct node.

        if node not in explored:  # DFS does not want to revisit states.
            explored.append(node)  # Adds the node to the explored list

            # Expand the nodes successors, and push them to the stack.
            # Might have an issue with successor needing to be renamed to nextState
            for successor, actionFromCurrStateToNextState, stepCost in problem.getSuccessors(node):
                if successor not in explored:  # DFS does not want to revisit states.
                    new_path = path + [actionFromCurrStateToNextState]  # Updates the path to the new successor
                    new_cost = cost + stepCost
                    fringe.push((successor, new_path, new_cost), new_cost)  # Sends the path with the successor into the fringe.
    # Fringe is empty, meaning they have explored every node and not found the correct one.
    return []  # Added list to return correct datatype.

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # Initialization
    from game import Directions

    fringe = util.PriorityQueue()  # Stack Initialization
    # In order for this to be a proper stack you can only interact with it as a .append() or .pop()
    # {If we are using straight Py list}

    startState = problem.getStartState() # Need to store start state separately now, since we need to use it twice

    fringe.push((startState, [], 0), 0)  # Adds the start state and a list which will be the path
    # Added a third position to hold the Cost of the first item, and a second item to hold the priority level

    heuristic(startState, problem) # f(n) = g(n) + h(n)
    # Holds the data that will be used by the heursitic calculations

    # Needs to be filled with the directions maybe? Instead of the nodes themselves.
    explored = []  # Explored nodes, starts as empty, will end up with all explored nodes.

    while not fringe.isEmpty():
        node, path, cost = fringe.pop()  # Gets the next node to look at
        # path is an updated way to get to the given node, which is always what should be returned

        if problem.isGoalState(node):  #
            return path  # Path is what the program is wanting, as it wants the route to the correct node.

        if node not in explored:  # DFS does not want to revisit states.
            explored.append(node)  # Adds the node to the explored list

            # Expand the nodes successors, and push them to the stack.
            # Might have an issue with successor needing to be renamed to nextState
            for successor, actionFromCurrStateToNextState, stepCost in problem.getSuccessors(node):
                if successor not in explored:  # DFS does not want to revisit states.
                    new_path = path + [actionFromCurrStateToNextState]  # Updates the path to the new successor
                    new_cost = cost + stepCost # Updates the cost to kick to next nodes
                    priority = new_cost + heuristic(successor, problem) # Gets the priority value that each item should get (f(n) = g(n) + h(n))
                    fringe.push((successor, new_path, new_cost), priority)  # Sends the path with the successor into the fringe.
    # Fringe is empty, meaning they have explored every node and not found the correct one.
    return []  # Added list to return correct datatype.


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
