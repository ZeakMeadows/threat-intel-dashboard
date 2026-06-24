from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

def init_db():
    conn = sqlite3.connect('threat_intel.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS iocs
                 (id INTEGER PRIMARY KEY, 
                  value TEXT NOT NULL,
                  type TEXT NOT NULL,
                  source TEXT,
                  confidence INTEGER,
                  first_seen TEXT,
                  last_seen TEXT,
                  notes TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/iocs', methods=['GET', 'POST'])
def iocs():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'value' not in data or 'type' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
        
        conn = sqlite3.connect('threat_intel.db')
        c = conn.cursor()
        c.execute('''INSERT INTO iocs (value, type, source, confidence, first_seen, notes)
                       VALUES (?, ?, ?, ?, ?, ?)''',
                  (data['value'], data['type'], data.get('source', 'manual'),
                   data.get('confidence', 50), datetime.now().isoformat(),
                   data.get('notes', '')))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'}), 201
    
    conn = sqlite3.connect('threat_intel.db')
    c = conn.cursor()
    c.execute('SELECT * FROM iocs ORDER BY first_seen DESC LIMIT 100')
    rows = c.fetchall()
    conn.close()
    
    iocs_list = []
    for row in rows:
        iocs_list.append({
            'id': row[0],
            'value': row[1],
            'type': row[2],
            'source': row[3],
            'confidence': row[4],
            'first_seen': row[5],
            'notes': row[6]
        })
    return jsonify(iocs_list)

@app.route('/api/stats')
def stats():
    conn = sqlite3.connect('threat_intel.db')
    c = conn.cursor()
    
    c.execute('SELECT type, COUNT(*) FROM iocs GROUP BY type')
    type_counts = dict(c.fetchall())
    
    c.execute('SELECT source, COUNT(*) FROM iocs GROUP BY source')
    source_counts = dict(c.fetchall())
    
    conn.close()
    
    return jsonify({
        'total_iocs': sum(type_counts.values()),
        'by_type': type_counts,
        'by_source': source_counts
    })

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
