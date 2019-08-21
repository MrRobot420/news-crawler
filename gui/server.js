const express = require("express")
const bodyparser = require("body-parser")
const cors = require("cors")
const path = require("path")
const favicon = require("serve-favicon")


var app = express()

var corsOptions = {
    origin: 'http://localhost:5000',
    optionsSuccessStatus: 200 // some legacy browsers (IE11, various SmartTVs) choke on 204
}
app.listen(5000)
console.log("Listening on port: 5000")

app.use(bodyparser.json())
app.use(bodyparser.urlencoded({extended: true}))
app.use(cors())
app.use("/styles.css", express.static(__dirname + '/styles.css'));
app.use(favicon(path.join(__dirname + "/favicon.ico")))

app.get('/styles.css', cors(corsOptions), (req, res, next) => {
    console.log("NEW Request: /styles.css")
    res.sendFile(path.join(__dirname * "/styles.css"))
})

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