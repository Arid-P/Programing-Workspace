from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask import Flask, render_template, request, redirect, url_for, flash

from backend.crud.auth_crud import login_user
from backend.crud.advocate_crud import get_advocate_by_id, register_advocate
from backend.crud.client_crud import register_client
from backend.main import Assignment, start_backend_system

app = Flask(__name__, 
            template_folder="gui/templates", 
            static_folder="gui/static")
app.secret_key = "diary_secret_key"

def start_backend ():
    start_backend_system() 
    global assign
    assign = Assignment()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    uid = request.form.get('user_id')
    phone = request.form.get('phone')
    
    user, error = login_user(uid, phone) # type: ignore
    
    if user:
        session['user_id'] = uid
        # Determine type by prefix
        session['user_type'] = 'client' if uid.startswith('Cl') else 'advocate' # type: ignore
        
        if session['user_type'] == 'advocate':
            return redirect(url_for('advocate_dashboard'))
        return redirect(url_for('client_dashboard'))
    
    flash(error or "Invalid Credentials")
    return redirect(url_for('index'))

@app.route('/advocate')
def advocate_dashboard():
    if 'user_id' not in session or session['user_type'] != 'advocate':
        return redirect(url_for('index'))
    
    # Fetch the actual advocate object to display their name
    advocate = get_advocate_by_id(session['user_id'])
    return render_template('advocate_dashboard.html', advocate=advocate)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    # If the user just clicked the link, show them the form
    if request.method == 'GET':
        return render_template('signup.html')
    
    # If they submitted the form (POST)
    data = request.form.to_dict()
    
    # Logic to decide which backend function to call
    if data.get('user_type') == 'advocate':
        # Your backend/crud/advocate_crud.py function
        uid, error = register_advocate(data)
    else:
        # Your backend/crud/client_crud.py function
        uid, error = register_client(data)
        
    if error:
        flash(error) # This sends the error message back to the signup page
        return redirect(url_for('register'))
    
    # Success! Send them to login and show their new ID
    flash(f"Account created! Your ID is: {uid}. Please login.")
    return redirect(url_for('index'))

@app.route('/case/add', methods=['POST'])
def add_existing_case():
    data = request.form.to_dict()

    data['role'] = 'adv'
    global assign
    success, error = assign.verify_and_assign_case(data)
    
    if not success:
        flash(f"Error: {error}")
    else:
        flash("Case successfully added to your diary!")
    return redirect(url_for('advocate_dashboard'))

@app.route('/case/create', methods=['POST'])
def create_new_case():
    data = request.form.to_dict()
    adv_id = session.get('user_id')
    
    global assign
    case_id, error = assign.create_and_assign_new_case(adv_id, data)
    
    if error:
        flash(error)
    else:
        flash(f"Case {case_id} created and assigned to you.")
    return redirect(url_for('advocate_dashboard'))

if __name__ == "__main__":
    start_backend()
    print("--- Attempting to start Flask Server ---")
    app.run(use_reloader=False)