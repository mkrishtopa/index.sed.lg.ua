function newWindow (filename, w, h) {
	window.open(filename,'','width='+w+', height='+h, toolbar=0, status=0);
}

function search_check(text) {
	var str=text.value;
	var len = str.length;
	var a = str.split("");
	if(a[a.length-1]==" ") {
		alert('Поиск ведётся только по одному слову!');
		text.value = str.substring(0,len-1);
	}
}

function checkifagree() {
	name = document.submitinfo.Name.value;
	email = document.submitinfo.From.value;
	agreed = document.submitinfo.agree.checked;
	if (name!="" & email!="" & agreed!=false) {
		return true;
	}
	else {
		alert('Заполните корректно форму отправки заявки!');
		return false;
	}
}
