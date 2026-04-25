# shoutout rosetta code for this method

# import necessary bits and bobs
import collections
import random

# define constants (honestly not needed SO much but it's how rosetta code lines it up with the mathematical definition of the algorithm)
INF = float('inf')
NIL = 0

# graph class - from here on out all comments are from rosetta code and they explain it rlly well!
class HKGraph:
    """
    Implementation of the Hopcroft-Karp algorithm for finding maximum matching
    in a bipartite graph.

    Assumes vertices in the left partition (U) are numbered 1 to m,
    and vertices in the right partition (V) are numbered 1 to n.
    The NIL node is represented by 0.
    """

    def __init__(self, m, n):
        self.m = m  # Number of vertices on the left side (U)
        self.n = n  # Number of vertices on the right side (V)

        # Adjacency list: adj[u] contains list of neighbors of u in V
        # Initialize with empty lists for vertices 1 to m
        self.adj = [[] for _ in range(m + 1)]

        # Matching pairs:
        # pair_u[u] stores the vertex v in V matched with u in U (or NIL if unmatched)
        self.pair_u = [NIL] * (m + 1)
        # pair_v[v] stores the vertex u in U matched with v in V (or NIL if unmatched)
        self.pair_v = [NIL] * (n + 1)

        # dist[u] stores the distance (level) of vertex u in U during BFS
        # Initialized within the hopcroft_karp_algorithm or bfs method
        self.dist = [INF] * (m + 1)

    def add_edge(self, u, v):
        """
        Adds a directed edge from vertex u (left partition) to vertex v (right partition).
        """
        # Ensure vertices are within the valid range
        if 1 <= u <= self.m and 1 <= v <= self.n:
            self.adj[u].append(v)  # Add v to u's adjacency list
        else:
            # Optionally print a warning for edges added outside the defined range
            # This check is now also done in the main section when adding edges.
            print(f"Warning: Attempted to add edge ({u}, {v}) outside graph bounds [1..{self.m}], [1..{self.n}]")
            pass

    def bfs(self) -> bool:
        """
        Performs Breadth-First Search (BFS) to find layers in the graph; checks if there exists an augmenting path starting from a free vertex in U 
        + returns true if an augmenting path might exist (dist[NIL] is finite)
        """
        queue = collections.deque()  # Use deque for efficient queue operations

        # Initialize distances for vertices in U
        for u in range(1, self.m + 1):
            if self.pair_u[u] == NIL:
                # If u is a free vertex, its distance is 0, add to queue
                self.dist[u] = 0
                queue.append(u)
            else:
                # Otherwise, set distance to infinity initially
                self.dist[u] = INF

        # Distance to the NIL node represents the length of the shortest augmenting path
        self.dist[NIL] = INF

        while queue:
            u = queue.popleft()  # Dequeue a vertex from U

            # If the path through u can potentially lead to a shorter augmenting path
            if self.dist[u] < self.dist[NIL]:
                # Explore neighbors v of u in V
                for v in self.adj[u]:
                    matched_u = self.pair_v[v]  # Get the vertex u' matched with v
                    # If the matched vertex u' hasn't been visited yet (its distance is INF)
                    if self.dist[matched_u] == INF:
                        # Set the distance of u' based on u
                        self.dist[matched_u] = self.dist[u] + 1
                        # Enqueue u' to explore further
                        queue.append(matched_u)

        # If dist[NIL] is still INF, no augmenting path was found originating
        # from the initial free vertices. Otherwise, augmenting paths might exist.
        return self.dist[NIL] != INF

    def dfs(self, u: int) -> bool:
        """
        Performs Depth-First Search (DFS) starting from vertex u in U
        to find and augment along a shortest path identified by BFS.

        Args:
            u (int): The current vertex in U being visited (or NIL).

        Returns:
            bool: True if an augmenting path was found and used starting from u,
                  False otherwise.
        """
        if u != NIL:
            # Explore neighbors v of u in V
            for v in self.adj[u]:
                matched_u = self.pair_v[v]  # Get the vertex u' matched with v
                # Check if the edge (u, v) leads to a vertex u'
                # such that the path u -> v -> u' is part of a shortest augmenting path
                if self.dist[matched_u] == self.dist[u] + 1:
                    # Recursively call DFS on u'
                    if self.dfs(matched_u):
                        # If an augmenting path is found starting from u',
                        # update the matching: match v with u, and u with v
                        self.pair_v[v] = u
                        self.pair_u[u] = v
                        print("matching u=",u,"to v=",v)
                        return True  # Augmentation successful

            # If no augmenting path was found starting from u through any neighbor v,
            # mark u as visited in this DFS phase by setting its distance to INF
            self.dist[u] = INF
            return False  # Augmentation failed for this path

        # Base case: If u is NIL, it means we have reached the end of an alternating path
        # originating from a free vertex in U and ending at a free vertex in V (represented by NIL).
        return True

    def hopcroft_karp_algorithm(self) -> int:
        """
        Executes the Hopcroft-Karp algorithm to find the maximum matching.

        Returns:
            int: The size of the maximum matching found.
        """
        # Initialize matching pairs to NIL (unmatched)
        self.pair_u = [NIL] * (self.m + 1)
        self.pair_v = [NIL] * (self.n + 1)

        matching_size = 0  # Initialize the size of the matching

        # Keep finding augmenting paths using BFS and DFS until no more exist
        while self.bfs():
            # For every free vertex u in U
            for u in range(1, self.m + 1):
                # If u is free and an augmenting path starting from u is found via DFS
                if self.pair_u[u] == NIL and self.dfs(u):
                    # Increment the matching size
                    matching_size += 1

        return matching_size, self.pair_u, self.pair_v

# MAIN METHOD hi codes doing comments again
if __name__ == "__main__":
    # size of sets is to set up graph and make sure all edges added are valid - we can make this just measure the size of input arrays instead!
    number_of_authors = 10
    number_of_artists = 10
    # example graphs below - realistically these will import from the output of the validation and edge making, for now they're just here to test everything works
    edges_data = [
        #a
        (1, 1), (1, 3), (1, 4),
        #b
        (2, 1), (2, 2), (2, 8),
        #c
        (3, 1), (3, 3),
        #d
        (4, 3), (4, 4),
        #e
        (5, 3), (5, 4),
        #f
        (6, 2), (6, 5), (6, 7),
        #g
        (7, 5), (7, 6), (7, 10),
        #h
        (8, 5), (8, 6), (8, 7), (8, 8), (8, 10),
        #i
        (9, 9),
        #j
        (10, 4), (10, 9)
    ]
    # edges_data = [
    #     (1,1), (1,2),
    #     (2,1), (2,2),
    #     (3,3), (3,4),
    #     (4,3), (4,4),
    #     (5,6), (5,5), (5,7),
    #     (6,5), (6,6)
    # ]

    # shuffle things about here
    print("ORIGINAL LIST:")
    print(hardcoded_edges)
    random.shuffle(hardcoded_edges)
    print("SHUFFLED LIST:")
    print(hardcoded_edges)

    # define graph size and then make it
    v1 = number_of_authors
    v2 = number_of_artists
    e = len(edges_data)
    g = HKGraph(v1, v2)
    print(f"Graph dimensions: m={v1}, n={v2}, edges={e}")

    # add edges one by one, checking they're within the correct range
    for u, v in edges_data:
        print(f"  Adding edge: ({u}, {v})")
        if 1 <= u <= v1 and 1 <= v <= v2:
            g.add_edge(u, v)
        else:
            print(f"Warning: Skipping invalid hard-coded edge ({u}, {v}) - indices out of range [1..{v1}] or [1..{v2}]")

    # run the algorithm (this gives the size, list output printed from inside but i should change that)
    max_matching_size, pitches_to_artists, artists_to_pitches = g.hopcroft_karp_algorithm()

    matches = []
    unmatched_pitches = []
    unmatched_artists = []
    for i in range(1,len(pitches_to_artists)):
        if pitches_to_artists[i] == 0:
            unmatched_pitches.append(i)
        else:
            matches.append((i,pitches_to_artists[i]))
    for i in range(1,len(artists_to_pitches)):
        if artists_to_pitches[i] == 0:
            unmatched_artists.append(i)
        # already should be in matches

    print("matches: ", matches)
    print("unmatched_pitches: ", unmatched_pitches)
    print("unmatched_artists: ", unmatched_artists)

    # Print the result
    print(f"\nMaximum matching size is {max_matching_size}")
