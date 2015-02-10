#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from datetime import datetime
from flask import Flask, render_template, jsonify, redirect, url_for, request
from Bio import SeqIO
import subprocess


ALLOWED_EXTENSIONS = set(['fasta', 'gbk'])

app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template("index.html")

from Bio.Seq import Seq
@app.route('/', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            now = datetime.now()
            filename = os.path.join(app.config['UPLOAD_FOLDER'], "%s.%s" % (now.strftime("%Y-%m-%d-%H-%M"), file.filename.rsplit('.', 1)[1]))
            file.save(filename)
            sq = filename
            position = -1
            for seq_record in SeqIO.parse(sq, "fasta"):
                x = request.form['search_item']
                seq = Seq(x)
                seq_rev = seq.reverse_complement()
                data = seq_record.seq
                position = data.find(x)
                position_rev = data.find(seq_rev)
            return render_template('result.html', position=position, position_rev=position_rev)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    app.run(debug=True)

