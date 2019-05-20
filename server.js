var express = require('express');
var app = express();
app.listen(3000, function () {
  console.log('server running on port 3000');
})

app.use(express.static('public'))


app.get('/get_bait', bait_caller);
function bait_caller(req, res) {
    console.log('get request')
  // using spawn instead of exec, prefer a stream over a buffer
  // to avoid maxBuffer issue
  var spawn = require('child_process').spawn;
  var process = spawn('python', ['./get_bait.py']);
  process.stdout.setEncoding('utf8');
  process.stdout.on('data', function (data) {
    res.send(data.toString());
  });
}