from collections import deque, defaultdict

def course_schedule(num_courses, prerequisites):
    # Build graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    for pre, course in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1
    
    # Queue for courses with no prerequisites
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []
    
    while queue:
        course = queue.popleft()
        order.append(course)
        
        # Decrease in-degree of neighbors
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if topological ordering is possible
    if len(order) == num_courses:
        return order  # valid sequence
    else:
        return []  # cycle detected, no valid schedule


# Example: 4 courses (0,1,2,3), prerequisites list
num_courses = 4
prerequisites = [(0, 1), (1, 2), (2, 3)]  # 0 -> 1 -> 2 -> 3

print("Course sequence:", course_schedule(num_courses, prerequisites))
