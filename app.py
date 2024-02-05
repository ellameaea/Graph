from flask import Flask, render_template, request
from collections import deque

app = Flask(__name__)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, source, target):
        self.vertices[source].append(target)
        self.vertices[target].append(source)

    def shortest_path_bfs(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return None

        queue = deque([(start, [start])])

        while queue:
            current_station, path = queue.popleft()

            if current_station == end:
                return ' -> '.join(path)

            for neighbor in self.vertices[current_station]:
                if neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))

        return None

graph = Graph()

stations = ["North Avenue", "Quezon Avenue", "Kamuning", "Cubao", "Santolan-Anapolis", "Ortigas", "Shaw Blvd.", "Boni", "Guadalupe", "Buendia", "Ayala", "Magallanes", "Taft",
"Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore", "Betty Go-Belmonte", "Cubao", "Anonas", "Katipunan", "Santolan", "Marikina", "Antipolo",
"Baclaran", "EDSA", "Libertad", "Gil Puyat", "Vito Cruz", "Quirino Ave.", "Pedro Gil", "UN", "Central Terminal", "Carriedo",
"Doroteo Jose", "Bambang", "Tayuman", "Bluementrit", "Abad Santos", "R. Papa", "5th Ave.", "Monumento", "Malvar", "Balintawak", "Roosevelt", "North Ave."]

for station in stations:
    graph.add_vertex(station)

edges = [("North Avenue", "Quezon Avenue"), ("Quezon Avenue", "Kamuning"), ("Kamuning", "Cubao"),
         ("Cubao", "Santolan-Anapolis"), ("Santolan-Anapolis", "Ortigas"), ("Ortigas", "Shaw Blvd."), ("Shaw Blvd.", "Boni"),
         ("Boni", "Guadalupe"), ("Guadalupe", "Buendia"), ("Buendia", "Ayala"), ("Ayala", "Magallanes"), ("Magallanes", "Taft"), ("Taft", "EDSA"),
         ("Recto", "Legarda"), ("Legarda", "Pureza"), ("Pureza", "V. Mapa"), ("V. Mapa", "J. Ruiz"), ("J. Ruiz", "Gilmore"),
         ("Gilmore", "Betty Go-Belmonte"), ("Betty Go-Belmonte", "Cubao"), ("Cubao", "Anonas"),
         ("Anonas", "Katipunan"), ("Katipunan", "Santolan"), ("Santolan", "Marikina"), ("Marikina", "Antipolo"), ("Baclaran", "EDSA"), ("EDSA", "Libertad"), ("Libertad", "Gil Puyat"),
         ("Gil Puyat", "Quirino Ave."), ("Quirino Ave.", "Pedro Gil"), ("Pedro Gil", "UN"), ("UN", "Central Terminal"), ("Central Terminal", "Carriedo"),
         ("Carriedo", "Doroteo Jose"), ("Doroteo Jose", "Bambang"), ("Doroteo Jose", "Recto"), ("Bambang", "Tayuman"), ("Tayuman", "Bluementrit"), ("Bluementrit", "Abad Santos"),
         ("Abad Santos", "R. Papa"), ("R. Papa", "5th Ave."), ("5th Ave.", "Monumento"), ("Monumento", "Balintawak"), ("Balintawak", "Roosevelt")]

for edge in edges:
    graph.add_edge(edge[0], edge[1])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shortestpath', methods=['POST'])
def shortest_path():
    start_station = request.form['start']
    end_station = request.form['end']
    shortest_path = graph.shortest_path_bfs(start_station, end_station)

    if shortest_path:
        return render_template('index.html', start_station=start_station, end_station=end_station, shortest_path=shortest_path)
    else:
        return render_template('index.html', start_station=start_station, end_station=end_station, shortest_path='None. Make sure to input correct stations!')

if __name__ == '__main__':
    app.run(debug=True)
