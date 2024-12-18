document.getElementById('towerForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    
    const initialTowers = JSON.parse(document.getElementById('initialTowers').value);
    const goalTowers = JSON.parse(document.getElementById('goalTowers').value);
    const algorithm = document.getElementById('algorithm').value;
    
    const response = await fetch('/solve', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ initialTowers, goalTowers, algorithm })
    });
    
    const data = await response.json();
    if (data.success) {
        document.getElementById('results').textContent = `Moves: ${JSON.stringify(data.moves, null, 2)}`;
    } else {
        document.getElementById('results').textContent = `Error: ${data.error}`;
    }
});
