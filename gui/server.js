const express = require("express")
const bodyparser = require("body-parser")
const cors = require("cors")
const path = require("path")
const favicon = require("serve-favicon")
const dateFormat = require('dateformat');
const fs = require("fs")

var app = express()

var corsOptions = {
    origin: ['https://localhost:80', 'http://localhost:80', 'https://1cc0d8af.ngrok.io/', 'http://1cc0d8af.ngrok.io/'],
    optionsSuccessStatus: 200 // some legacy browsers (IE11, various SmartTVs) choke on 204
}

var port = 80           // For ngrok (access via the internet)    [/Users/Maxi/ngrok/ -> ./ngrok http(s) 80]
app.listen(port)
console.log(`Listening on port: ${port}`)

// CONFIGURE SERVER (pathes):
app.use(bodyparser.json())
app.use(bodyparser.urlencoded({extended: true}))
app.use(cors())
var d = dateFormat(new Date(), "dd-mm-yyyy").toString()
app.use(path.join("../data/" + d + "/01_de.json"), express.static(path.join("../data/" + d + "/01_de.json")))
app.use("/styles.css", express.static(__dirname + '/styles.css'))
app.use("/app.js", express.static(__dirname + '/app.js'))
app.use(favicon(path.join(__dirname + "/favicon.ico")))

app.get('/', cors(corsOptions), function (req, res, next) {
    console.log("NEW Request: /")
    res.sendFile(path.join(__dirname + "/index.html"))
  });

app.get('/index.html', cors(corsOptions), function (req, res, next) {
    console.log("NEW Request: /index.html")
    res.sendFile(path.join(__dirname + "/index.html"))
  });

app.get('/favicon.ico', cors(corsOptions), function (req, res, next) {
    console.log("NEW Request: /favicon.ico")
    res.sendFile(path.join(__dirname + "/favicon.ico"))
});

app.get('/current-data', cors(corsOptions) , (req, res, next) => {
    // var d = dateFormat(new Date(), "dd-mm-yyyy").toString()
    // var d = new Date().toISOString().replace(/T..*/, ' ');
    console.log("NEW Request: /current-data")
    console.log(d)
    var data_obj = {}
    // fs.readFile(path.join("../data/" + d + "/01_de.json"), 'utf8', function (err, data) {
    //   if (err) throw err;
    //   data_obj = JSON.parse(data);
    // });
    var data_obj = JSON.parse(fs.readFileSync(path.join("../data/" + d + "/01_de.json"), 'utf-8'))
    // console.log(data_obj)
    res.json(data_obj)
})