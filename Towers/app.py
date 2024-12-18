from flask import Flask, render_template, request, jsonify
from tower_puzzle import TowerPuzzle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_puzzle():
    data = request.json
    initial_towers = data.get('initialTowers')
    initial_towers = data.get('goalTowers')
    algorithm = data.get('algorithm', 'a_star')  # Default to A* search
    
    try:
        print(f'{initial_towers= }')
        print(f'{goal_towers= }')
        tp = TowerPuzzle(initial_towers, goal_towers)
        if algorithm == 'bfs':
            moves = tp.bfs()
        elif algorithm == 'greedy':
            moves = tp.greedy()
        else:
            moves = tp.a_star()
        
        return jsonify({"success": True, "moves": moves})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
