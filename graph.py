from neo4j import Auth, GraphDatabase
#establishing connection to local dbms (to default dbms)
graph_db=GraphDatabase.driver(uri='bolt://localhost:7687',auth=('neo4j','Legis123'))

#establishing a session
session=graph_db.session()

#execute queries
inp = input('Insert the name of the student: ')
q1 = 'MATCH (s1:Student {name: "' + str(inp) + '"})-->(s2:Student) RETURN s2.name' #concatenate strings because f'{}' does not work
q2 = 'MATCH (s1:Student {name: "' + str(inp) + '"})-[r]->(s2:Student) RETURN type(r)'
name = session.run(q1)
rel = session.run(q2)
for vertex in rel:
    print(vertex)
    for edge in name:
        print(edge)
    print('')



