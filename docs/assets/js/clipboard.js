		var btns = document.querySelectorAll('a');
		var clipboard = new ClipboardJS(btns);
		clipboard.on('success', function(e) {
			console.log(e);
		});
		clipboard.on('error', function(e) {
			console.log(e);
		});