# import modules
from flask import Flask
from flask_restful import Resource, Api
import markdown
import os




# create an instance of Flask
app = Flask(__name__)


api = Api(app)


# route index page that used as main page
@app.route('/')
def index():
    
    """
        demonstrate README doc on the main page
    """
    
    # open the README
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as open_markdown:

        # read the content from README file        
        file_content = open_markdown.read()

        # return README on html
        return markdown.markdown(file_content)



