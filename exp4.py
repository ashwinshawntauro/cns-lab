class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]

    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

    def print_solution(self,dist):
        print("Vertex Distance: ")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}\n")
        
    def bellman(self,src):
        dist=[float("Inf")]*self.V
        dist[src]=0
        for _ in range(self.V-1):
            for u,v,w in self.graph:
                if dist[u]!=float("Inf") and dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w
        for u,v,w in self.graph:       
            if dist[u]!=float("Inf") and dist[u]+w<dist[v]:
                print("Graph contains negative values")
                return
        self.print_solution(dist)

def main():
    V=int(input("Enter the number of vertices: "))
    E=int(input("Enter the number of edges: "))
    g=Graph(V)
    print("Enter the paht in form [sorce destination weight]: ")
    for _ in range(E):
        u,v,w=map(int,input().split())
        g.add_edge(u,v,w)
    src=int(input("Enter the source path: "))
    g.bellman(src)

if __name__=="__main__":
    main()