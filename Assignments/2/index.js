const btn1 = document.getElementById('btn1');
const btn2 = document.getElementById('btn2');



const QArrays = [];
/*
btn1.addEventListener('click',
  function getQuestions(event) {
    event.preventDefault();
    const query = document.getElementById('query');
    QArrays.push(query.value);
    query.value = '';
    alert("Question successfully Submitted!");
  })

btn2.addEventListener('click',
  function showQuestions(event) {
    event.preventDefault();
    let text = "<ul style=\"text-align:center;\">";
    let fLen = QArrays.length;
    for (let i = 0; i < fLen; i++) {
      text += "<li>" + QArrays[i] + "</li>";
    }
    text += "</ul>";
    document.getElementById("demo").innerHTML = text;
  })
*/
var apigClientFactory = require('aws-api-gateway-client').default;
var apigClient = apigClientFactory.newClient();
btn1.addEventListener('click',
  function getQuestions(event) {
    event.preventDefault();
    //let url = 
  })

btn2.addEventListener('click',
  function showQuestions(event) {
    event.preventDefault();
    apigClient.answersGet();
  })
