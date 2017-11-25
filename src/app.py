from flask import Flask, render_template
import json

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))

app = CustomFlask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/api/configuration')
def get_configuration():
    return json.dumps([{
        'application' : 'applicationA',
        'status' : 'up'
    },
        {
            'application': 'applicationB',
            'status': 'down'
        }
    ])

if __name__ == "__main__":
    app.run(use_debugger=True, use_reloader=True)