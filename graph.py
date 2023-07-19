from neo4j import Auth, GraphDatabase

#establishing connection to local dbms (to default dbms)
graph_db=GraphDatabase.driver(uri='bolt://localhost:7687',auth=('neo4j','Legis123'))
#establishing a session
session=graph_db.session()

#execute queries
def main():
    inp = input('Insert the name of the student: ')
    q1 = '''MATCH (s1:Student {name: $inp})-[r]->(s:Student) 
            RETURN s.name AS name, type(r) AS relationship'''
    name = session.run(q1, inp = inp)

    for edge in name:
        n = edge.get('name')
        r = edge.get('relationship')
        print(n + ', ' + r)
        print('')

main()
