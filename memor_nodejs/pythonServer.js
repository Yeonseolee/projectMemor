console.log("hello world");

const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

// const {spawn} = require('child_process');
// const { PythonShell } = require('python-shell');

const app = express();

app.set("views", __dirname + "/views");
app.set("view engine, 'ejs");


app.use(express.json());
app.use(express.urlencoded({extended: true })); 
