from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    images = [
        {'url': 'https://example.com/image1.jpg', 'title': 'Image 1'},
        {'url': 'https://example.com/image2.jpg', 'title': 'Image 2'},
        {'url': 'https://example.com/image3.jpg', 'title': 'Image 3'},
    ]
    return render_template('gallery.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
