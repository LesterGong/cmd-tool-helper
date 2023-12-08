from flask import Flask, render_template, request, redirect, url_for
from request_and_execute import construct_and_request, execute


app = Flask(__name__)

# Temporary storage for demonstration purposes. In a real-world scenario, you might use a database.
inputs = {
    "requirements": "",
    "answer": "",
    "execution": ""
}


@app.route('/', methods=['GET', 'POST'])  # Define the route for the index page that accepts both GET and POST requests.
def index():
    if request.method == 'POST':  # Check if the current request is a POST request.
        if 'confirm' in request.form:  # Check if 'confirm' was clicked.
            # Update the requirements in the inputs dictionary with the data received from the form.
            inputs['requirements'] = request.form['requirements']
            inputs['answer'] = construct_and_request(inputs['requirements'])
            inputs['execution'] = execute(inputs['answer'])
            # Redirect to the GET method to display the updated inputs, preventing form resubmission issues.
            return redirect(url_for('index'))
        elif 'cancel' in request.form:  # Check if 'cancel' was clicked.
            # Clear the inputs for requirements.
            inputs['requirements'] = ""
            # Redirect to the index page to reset the form.
            return redirect(url_for('index'))

    # Render the form with inputs. Pass the inputs dictionary to the template.
    return render_template('index.html', inputs=inputs)


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application with debug mode on.
