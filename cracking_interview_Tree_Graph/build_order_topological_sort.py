# projects is a,b,c,d,e,f
# dependencies is: (a,d), (f,b), (b,d), (f,a), (d,c)
def createGraph(projects, dependencies):
    project_graph = {}
    for project in projects:
        # because one node can be depends on more than one node and I'll create a list.
        project_graph[project] = []
    # next we need to added dependencies to value of project in to dictionary
    for pairs in dependencies:
        project_graph[pairs[0]].extend(pairs[1])
    return project_graph


def get_project_with_dependencies(graph):
    # first crating an empty set
    project_with_dependencies = set()
    for project in graph:
        project_with_dependencies = project_with_dependencies.union(
            set(graph[project]))
    return project_with_dependencies


def get_project_with_out_dependencies(project_with_dp, graph):
    # creating empty set
    project_with_out_dependencies = set()
    for project in graph:
        if not project in project_with_dp:
            project_with_out_dependencies.add(project)
    return project_with_out_dependencies


def find_build_order(projects, dependencies):
    build_order = []
    project_graph = createGraph(projects, dependencies)
    while project_graph:
        with_dependencies = get_project_with_dependencies(project_graph)
        with_out_dependencies = get_project_with_out_dependencies(
            with_dependencies, project_graph)
        if len(with_out_dependencies) == 0 and project_graph:
            raise ValueError("There is a cycle in Build order")
        for independent in with_out_dependencies:
            build_order.append(independent)
            del project_graph[independent]
    return build_order


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

my_graph = createGraph(projects, dependencies)
print(my_graph)

with_dependencies = get_project_with_dependencies(my_graph)
print(with_dependencies)

with_out_dependencies = get_project_with_out_dependencies(
    dependencies, my_graph)
print(with_out_dependencies)


print(find_build_order(projects, dependencies))
