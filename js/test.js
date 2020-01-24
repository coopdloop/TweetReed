function testy(handle, c){
	
	var url = `http://localhost:1337/handle?h=${handle}&c=${c}`;
		//var tweetco = url.substring(url.length-1,url.length);
	var req = new XMLHttpRequest();
	req.open("GET", url, true);

	req.onload = function (e) {
  		if (req.readyState === 4) {
    		if (req.status === 200) {
    			var data=JSON.parse(req.response);
    			console.log(data);
    			buildBlocks(data,c);
    		} else {
      			console.error(req.statusText);
    		}
  		}
	}

	req.send();
	
}	
function buildBlocks(data, tweetco){

var data2 =[];
	for (var count=0; count < tweetco; count++){
		var handle = data[count]["handle"]
		var createdAt = data[count]["created_at"]
		var text = data[count]["text"]
		var author = data[count]["author"]

		data2[count] = document.getElementsByClassName('media content-section')[0].cloneNode(true);
		document.getElementsByClassName("col-md-8")[0].append(data2[count]);
		data2[count].children[0].children[0].children[0].innerText=handle;
		data2[count].children[0].children[0].children[1].innerText=createdAt;
		data2[count].children[0].children[1].innerText=text;
		data2[count].children[0].children[0].children[2].innerText=author;
		data2[count].hidden=false;
		
	};
}
