import Pyro4

@Pyro4.expose
class Chain(object):
    def __init__(self, name, current_server):
        self.name = name
        self.current_serverName = current_server
        self.current_server = None
    
    def process(self, matrix_data):
        if self.current_server is None:
            self.current_server = Pyro4.core.Proxy("PYRONAME:example.chainTopology." + self.current_serverName)
        
        if self.name in matrix_data:
            print("Back at %s; the chain is closed!" % self.name)
            return ["complete at " + self.name]
        else:
            print("%s forwarding the message to the object %s" % (self.name, self.current_serverName))
            
            A = [[1, 2], [3, 4]]
            B = [[5, 6], [7, 8]]
            res = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        res[i][j] += A[i][k] * B[k][j]
            
            matrix_data.append(self.name)
            matrix_data.append(res)
            
            result = self.current_server.process(matrix_data)
            result.insert(0, "passed on from " + self.name)
            return result