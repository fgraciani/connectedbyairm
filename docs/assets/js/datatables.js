	$(document).ready( function () {
		$('#example').DataTable({
		"ordering": true,
		"info":     true,
		"columnDefs": [
		  { "width": "180px", "targets": 1 }
		]
		} );
	} );