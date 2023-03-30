import yaml
import flask
import urllib

app = flask.Flask(__name__)


@app.route("/")
def index():
    """defines flask"""
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)


CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}
class Person(object):
    """person object"""
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    """function for printing nametag"""
    print(format_string.format(person=person))


def fetch_website(urllib_version, url):
    """function will fetch the webiste"""
    # Import the requested version (2 or 3) of urllib
    exec(f"import urllib{urllib_version} as urllib", globals())
    # Fetch and print the requested URL

    try:
        http = urllib.PoolManager()
        r = http.request('GET', url)
    except:
        print('Exception')


def load_yaml(filename):
    """function for loading the yaml file"""
    stream = open(filename, encoding='utf-8')
    deserialized_data = yaml.load(stream, Loader=yaml.Loader) #deserializing data
    return deserialized_data
    
def authenticate(PASSWORD):
    """function for auth"""
    # Assert that the PASSWORD is correct
    assert PASSWORD == "Iloveyou", "Invalid PASSWORD!"
    print("Successfully authenticated!")

if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability: use string={person.__init__.__globals__[CONFIG][API_KEY]}")
    print("2. Code injection vulnerability: use string=;print('Own code executed') #")
    print("3. Yaml deserialization vulnerability: use string=file.yaml")
    print("4. Use of assert statements vulnerability: run program with -O argument")
    CHOICE = input("Select vulnerability: ")
    if CHOICE == "1": 
        NEW_PERSON = Person("Vickie")
        print_nametag(input("Please format your nametag: "), NEW_PERSON)
    elif CHOICE == "2":
        urlib_version = input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif CHOICE == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif CHOICE == "4":
        PASSWORD = input("Enter master PASSWORD: ")
        authenticate(PASSWORD)
