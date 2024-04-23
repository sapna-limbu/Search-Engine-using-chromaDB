from flask import Flask, render_template, request
import chromadb

path = "C:/Users/RATNADEEP/Desktop/backend/SSENG/chroma"

chroma_client = chromadb.PersistentClient(path=path)
collection = chroma_client.get_collection(
        name="my_collection3"
        # metadata={"hnsw:space": "cosine"} # l2 is the default
    )



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get("input_text")
        results = collection.query(
            query_texts = [query],
            n_results=5,
        )
   
        return render_template('index.html', query=query, results=results)

        

if __name__ == "__main__":
    app.run(debug=True)