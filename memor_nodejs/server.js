console.log("hello world");

const express = require('express');
const multer = require('multer'); //파일 업로드 시 사용하는
const path = require('path');
const fs = require('fs');
const url = require('url');
const mime = require('mime');
// const {spawn} = require('child_process');
// const { PythonShell } = require('python-shell');

const app = express();

app.set("views", __dirname + "/views");
app.set("view engine", 'ejs');


app.use(express.json());
app.use(express.urlencoded({extended: true })); //이거 json에서 다중객체 읽기 가능하도록. 
app.use(express.static('images'));







// var users = {
//   developer: {
//     id: 1,
//     name: "seoyeon"
//   },
//   client: [
//     {
//       id: 1,
//       name: 'alice',
//       text: 'hi, this is test sample',
//       title: 'test sample'
//     },
//     {
//       id: 2,
//       name: 'cat',
//       text: 'hi, this is test sample',
//       title: 'test sample'
//     }]
// }


// let options={
//   mode:'binary',
//   pythonOptions: ['-u']
// };

// PythonShell.runString('./test.py', null, function (err,msg) {
//   if (err) throw err;
//   console.log(msg);
// });

//pythonshell 안되면,,. 안드로이드랑 라즈베리 서버를 따로 운영해야 할 것 같다
//라즈베리에서 이미지 받아오는 포트--> 필요없음. 유민이가 py코드에서 컴퓨터 폴더에 저장하도록 만듬. 
//, 서버에 저장된 이미지를 안드로이드에 올리는 포트 하나 -> 이 포트에서 이미지 폴더 경로 연결해야함 

//파일 경로는 uploadedFiles, 파일 이름은 랜덤으로 설정
var upload = multer({ dest: 'uploadedFiles/'});



var users = [
  { id: 1, name: 'dog', text: 'hi, this is test sample', title: 'test sample' },
  { id: 2, name: 'cat', text: 'hi, this is test sample', title: 'test sample' }
]

//포트에서 날라온 데이터들을 임시적으로 담는 객체 변수
var temp;

// 웹 test용
app.get('/', (req, res) => {
  console.log('get listen');
  res.render("test.ejs");
});

// //안드로이드 기본 홈 화면
// app.get('/home', (req, res) => {
//    console.log('get listen');
//    res.json(users)
// });

//라즈베리에서 이미지 데이터(비트맵데이터? 이미지 객체?)를 받는 포트. 소켓연결 필요
//이미지 한개 받는
// app.post('/uploadFile', upload.single('attachment'), (req, res)=>{
//   temp = {file: req.file, files: null}
//   res.render('confirm.ejs',temp);
//   console.log("single upload\n"+JSON.stringify(temp.file));
//   // temp = null;
// });


// //이미지 여러개를 받는 
// app.post('/uploadFiles', upload.array('attachments'), (req,res) => {
//   temp = { file: null, files: req.file }
//   res.render('confirm.ejs',temp);
//   console.log("array upload\n"+JSON.stringify(temp.files[0]));
//   // temp = null;
// });


// 이미지 분류





// 파일 다운됨: 파일 하나 전송
app.get('/download', function(req, res){
  console.log("loaing");

  var file = __dirname + '/images/2021-05-25_20_24_36.PNG';

  // var filename = path.basename(file);
  // var mimetype = mime.getType(file);
  // console.log("1. file type: "+mimetype);

  // res.setHeader('Content-disposition', 'attachment; filename=' + filename);
  // res.setHeader('Content-type', mimetype);

  var filestream = fs.createReadStream(file,{flags:'r'});

  console.log(filestream);
  console.log("3. filestream type: "+mime.getType(filestream));

  filestream.pipe(res);
});

//파일 여러개 (작업중)
// app.get('/download/2021-05-25_20_24_36.PNG', function(req, res){
//   console.log("loaing");
//   var file = [];
//   for(var i = 0; i<4;i++){
//     var file = __dirname + '/images/2021-05-25_20_24_36.PNG';

//     var filestream = fs.createReadStream(file,{flags:'r'});

//     console.log(filestream);
//     console.log("3. filestream type: "+mime.getType(filestream));

//     filestream.pipe(res);
//   }
  
// });

//안드로이드에서 새로운 데이터(문자)를 보낼 때 받는
app.post('/data', (req, res) => {
   console.log('post listen');
   console.log("id: "+req.body.id + "\nname : "+req.body.name+"\ntitle: "+req.body.title+"\n");
   console.log(req);
   temp = {
     id: req.body.id,
     name: req.body.name,
     text: req.body.text,
     title: req.body.title
   }
   users.push(temp);
   console.log(users);
   //  res.json("running");
   res.json(temp);

   temp = null;
});

app.use((request, response, next) => {
  response.status(404).send("Page not found :");
});

app.listen(8080, ()=> {
  var dir = './uploadedFiles';
  if(!fs.existsSync(dir)) fs.mkdirSync(dir);
});


