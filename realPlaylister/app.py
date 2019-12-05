from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb+srv://peaches:peaches17@cluster0-zmgrg.mongodb.net/test?retryWrites=true&w=majority")
database = client.Playlister
collection = database.Videos

youtube = 'https://youtube.com/embed/'

@app.route('/')
def playlists_index():
    videos = collection.find({})
    return render_template('index.html', videos=videos)

@app.route('/playlists/new')
def playlists_new():
    """Create a new playlist."""
    return render_template('playlists_new.html')

@app.route('/', methods=['POST'])
def playlists_add():
    """Create a new playlist."""
    video_ids = request.form.get('video_ids').split()
    print(video_ids)
    if (len(video_ids) < 1):
        video_ids = ['VwWV4JelEzY', 'VwWV4JelEzY']
    video = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'video_url': video_ids
    }
    collection.insert_one(video)
    videos = list(collection.find({}))
    return render_template('index.html', videos=videos)

@app.route('/playlists/<playlist_id>')
def playlists_show(playlist_id):
    """Show a single playlist."""
    playlist = collection.find({'_id':ObjectId(playlist_id)})
    urls = []
    for url in playlist[0]['video_url']:
        urls.append(youtube + url)
    return render_template('playlist_show.html', playlist=playlist, urls=urls)

@app.route('/updated', methods=['POST'])
def playlists_updated():
    """Create a new playlist."""
    video_ids = request.form.get('video_ids').split()
    if (len(video_ids) < 1):
        video_ids = ['VwWV4JelEzY', 'VwWV4JelEzY']
    video = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'video_url': video_ids
    }
    playlist_id = request.form.get('objid')
    print(playlist_id)
    collection.replace_one({'_id':ObjectId(playlist_id)}, video)
    videos = list(collection.find({}))
    return render_template('index.html', videos=videos)

@app.route('/update', methods=['POST'])
def playlists_update():
    """showing update html"""
    playlist_id = request.form.get('update_vid_id')
    print(playlist_id)
    playlist = collection.find({'_id':ObjectId(playlist_id)})
    return render_template('playlists_update.html', playlist=playlist, id=playlist_id)
    
@app.route('/deleted', methods=['POST'])
def playlists_delete():
    """Deleting playlist and going home"""
    playlist_id = request.form.get('vid_id')
    collection.delete_one({'_id':ObjectId(playlist_id)})
    videos = collection.find({})
    return render_template('index.html', videos=videos)


if __name__ == '__main__':
    app.run(debug=True)