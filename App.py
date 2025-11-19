import os
from dotenv import load_dotenv
load_dotenv()
from app import Luzvioleta

app = Luzvioleta()

if __name__ == "__main__":
    app.run(debug=True)
    