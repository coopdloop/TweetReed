var url = "http://localhost:1337/handle?h=realDonaldTrump&c=4";
var req = new XMLHttpRequest();
req.open("GET", url, true);
req.send();
req.responseText;
console.log(req.responsetext);

req.responseText

JSON.parse(req.response)[0]["author"]