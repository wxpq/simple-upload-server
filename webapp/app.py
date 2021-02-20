
from flask import Flask, request, render_template, send_from_directory
from urllib.request import pathname2url, url2pathname
import urllib
import os, glob, sys

app = Flask("Flask Upload Server")
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 3000


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return docu()

@app.route('/upload/<filename>', methods=["POST"])
def uploadfile(filename):
    file_ = urllib.parse.unquote(filename)
    return str(request.headers)

    # bytes_left = int(request.headers.get('content-length'))
    # with open(os.path.join("cdn", filename), 'wb') as upload:
    #     chunk_size = 1024
    #     while bytes_left > 0:
    #         chunk = request.stream.read(chunk_size)
    #         upload.write(chunk)
    #         bytes_left -= len(chunk)
    #     return "wget https://jack1100up.herokuapp.com/cdn/{}\n\n".format(pathname2url(file_))

    # file.save(os.path.join("cdn", file.filename))

@app.route('/cdn/<path:codeword>')
def download_file(codeword):
    file = url2pathname(codeword)
    return send_from_directory("cdn", file, as_attachment=True)

@app.route('/all')
def get_list():
    return "<br>".join([
    "<b><u>All uploads</u></b>",
    *["wget <a href='https://jack1100up.herokuapp.com/cdn/{0}'>https://jack1100up.herokuapp.com/cdn/{0}</a>\n\n".format(pathname2url(file)) for file in os.listdir("cdn")]
    ])

def docu():
    return "<br>".join([
    "Welcome to Personal Mini Cloud.",
    "========================================================================================",
    "Usage:",
    "curl -F file=@FILE_PATH  https://jack1100up.herokuapp.com",
    "",
    "Replace FILE_PATH with absolute path of the file to be uploaded to the cloud."
    "","",
    "<a href='https://jack1100up.herokuapp.com/all'>List all uploads</a>",
    ""
    ])

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
