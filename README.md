# Rich Kuku Hub

## Preview Options

### 1. Static preview with Live Server

For quick HTML/CSS checks on `index.html`:

1. Install the **Live Server** extension in VS Code.
2. Open `templates/index.html`.
3. Right-click the file and choose **Open with Live Server**.

> Note: `menu.html` and `checkout.html` use Flask template tags like `{{ url_for('static', filename='...') }}`. Those pages need the Flask app to render correctly.

### 2. Full app preview with Flask

To run the full site with `/menu` and `/checkout` routes:

1. Open a terminal in the project root.
2. Install dependencies if needed:
   ```powershell
   pip install flask requests
   ```
3. Start the Flask app:
   ```powershell
   python -m flask run
   ```
4. Open the browser at:
   ```text
   http://127.0.0.1:5000/
   ```

### 3. Use the VS Code task

A VS Code task is provided to launch the Flask app directly.

- Open the Command Palette: `Ctrl+Shift+P`
- Run: **Tasks: Run Task**
- Select: **Run Flask App**

## File notes

- Static files like CSS, JavaScript, and images are served from the project root via Flask's static folder.
- Do not host locally unless you want to. The app will run only when you explicitly start Flask.
